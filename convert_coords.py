#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从中国地图 GeoJSON 数据提取省份中心坐标，并转换为地图图片的百分比坐标
"""
import json
import re

# 各省行政中心坐标 (经度，纬度)
# 来源：geojson.cn API
province_centers = {
    "xinjiang": {"name": "新疆", "center": [87.6177, 43.8256]},
    "tibet": {"name": "西藏", "center": [91.1409, 29.6456]},
    "inner_mongolia": {"name": "内蒙古", "center": [111.6708, 40.8414]},
    "qinghai": {"name": "青海", "center": [101.7782, 36.6231]},
    "gansu": {"name": "甘肃", "center": [103.8343, 36.0611]},
    "ningxia": {"name": "宁夏", "center": [106.2581, 38.4664]},
    "sichuan": {"name": "四川", "center": [104.0657, 30.6595]},
    "chongqing": {"name": "重庆", "center": [106.5516, 29.5647]},
    "guizhou": {"name": "贵州", "center": [106.6302, 26.6477]},
    "yunnan": {"name": "云南", "center": [102.7125, 25.0406]},
    "guangxi": {"name": "广西", "center": [108.3665, 22.8170]},
    "hainan": {"name": "海南", "center": [110.3893, 19.8516]},
    "guangdong": {"name": "广东", "center": [113.2806, 23.1251]},
    "hunan": {"name": "湖南", "center": [112.9388, 28.2282]},
    "hubei": {"name": "湖北", "center": [114.3055, 30.5931]},
    "henan": {"name": "河南", "center": [113.6254, 34.7466]},
    "jiangxi": {"name": "江西", "center": [115.8582, 28.6765]},
    "anhui": {"name": "安徽", "center": [117.2272, 31.8206]},
    "jiangsu": {"name": "江苏", "center": [118.7969, 32.0603]},
    "zhejiang": {"name": "浙江", "center": [120.1551, 30.2741]},
    "fujian": {"name": "福建", "center": [119.2952, 26.0753]},
    "taiwan": {"name": "台湾", "center": [121.5000, 23.7000]},
    "shanghai": {"name": "上海", "center": [121.4737, 31.2304]},
    "shandong": {"name": "山东", "center": [117.0207, 36.6208]},
    "shanxi": {"name": "山西", "center": [112.5791, 37.8122]},
    "hebei": {"name": "河北", "center": [114.5304, 38.0377]},
    "beijing": {"name": "北京", "center": [116.4074, 39.9042]},
    "tianjin": {"name": "天津", "center": [117.2015, 39.0853]},
    "shaanxi": {"name": "陕西", "center": [108.9480, 34.2631]},
    "heilongjiang": {"name": "黑龙江", "center": [126.5350, 45.8038]},
    "jilin": {"name": "吉林", "center": [125.3235, 43.8171]},
    "liaoning": {"name": "辽宁", "center": [123.4315, 41.8057]}
}

# 中国地图的经纬度范围（大约）
# 最西：73°E (新疆西部)
# 最东：135°E (黑龙江东部)  
# 最北：53°N (黑龙江北部)
# 最南：18°N (海南南沙群岛)
LON_MIN, LON_MAX = 73, 135
LAT_MIN, LAT_MAX = 18, 53

def convert_to_percentage(lon, lat):
    """将经纬度转换为地图图片的百分比坐标"""
    # 经度转 left (X 轴)
    left = (lon - LON_MIN) / (LON_MAX - LON_MIN) * 100
    # 纬度转 top (Y 轴) - 注意纬度要反转，因为地图是上北下南
    top = (LAT_MAX - lat) / (LAT_MAX - LAT_MIN) * 100
    return round(left, 1), round(top, 1)

# 生成省份区域配置
print("// 省份点击区域配置 (基于 GeoJSON 行政中心坐标)")
print("const provinceAreas = {")

provinces = []
for pid, data in province_centers.items():
    left, top = convert_to_percentage(*data["center"])
    # 根据省份大小估算宽高
    if pid in ["xinjiang", "tibet", "inner_mongolia"]:
        width, height = 12, 10
    elif pid in ["qinghai", "sichuan", "gansu", "heilongjiang"]:
        width, height = 8, 7
    elif pid in ["yunnan", "guangxi", "guangdong", "hunan", "hubei"]:
        width, height = 6, 6
    elif pid in ["beijing", "tianjin", "shanghai", "ningxia"]:
        width, height = 3, 3
    else:
        width, height = 5, 5
    
    provinces.append((pid, data["name"], left, top, width, height))

# 按区域分组输出
regions = {
    "西北": ["xinjiang", "gansu", "qinghai", "ningxia"],
    "西南": ["tibet", "sichuan", "yunnan", "guizhou", "chongqing"],
    "华北": ["inner_mongolia", "beijing", "tianjin", "hebei", "shanxi", "shandong"],
    "东北": ["heilongjiang", "jilin", "liaoning"],
    "华中": ["shaanxi", "henan", "hubei", "hunan"],
    "华东": ["anhui", "jiangsu", "zhejiang", "shanghai", "jiangxi", "fujian"],
    "华南": ["guangdong", "guangxi", "hainan", "taiwan"]
}

for region, pids in regions.items():
    print(f"            // {region}")
    for pid in pids:
        if pid in province_centers:
            data = province_centers[pid]
            left, top = convert_to_percentage(*data["center"])
            if pid in ["xinjiang", "tibet", "inner_mongolia"]:
                w, h = 12, 10
            elif pid in ["qinghai", "sichuan", "gansu", "heilongjiang"]:
                w, h = 8, 7
            elif pid in ["yunnan", "guangxi", "guangdong", "hunan", "hubei"]:
                w, h = 6, 6
            elif pid in ["beijing", "tianjin", "shanghai", "ningxia"]:
                w, h = 3, 3
            else:
                w, h = 5, 5
            print(f'            {pid}: {{ left: {left}, top: {top}, width: {w}, height: {h} }}, // {data["name"]}')
    print()

print("        };")
