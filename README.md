# 🥢 中国美食地图

一个交互式中国美食地图网站，点击各省份即可查看当地特色美食。

## 🌟 功能特点

- 🗺️ 交互式中国地图
- 🍜 34 个省份美食展示
- 📱 响应式设计，支持手机和电脑
- 🎨 精美 UI 设计
- 🔍 点击省份查看美食详情

## 🚀 快速发布

### 方式一：GitHub Pages（推荐 - 免费）

1. 在 GitHub 创建新仓库（例如：`china-food-map`）
2. 在本地执行以下命令：

```bash
cd /home/admin/.openclaw/workspace/china-food-map

# 关联远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/你的用户名/china-food-map.git

# 推送到 GitHub
git push -u origin main
```

3. 在 GitHub 仓库页面：
   - 进入 **Settings** → **Pages**
   - Source 选择 **main branch**
   - 点击 **Save**
   
4. 几分钟后，你的网站就会在 `https://你的用户名.github.io/china-food-map/` 上线！

---

### 方式二：Vercel（推荐 - 免费）

1. 访问 [vercel.com](https://vercel.com)
2. 用 GitHub 账号登录
3. 点击 **Add New Project**
4. 导入你的 `china-food-map` 仓库
5. 点击 **Deploy**

**或使用 CLI：**
```bash
npm install -g vercel
cd /home/admin/.openclaw/workspace/china-food-map
vercel --prod
```

---

### 方式三：Netlify（免费）

1. 访问 [netlify.com](https://netlify.com)
2. 拖拽 `china-food-map` 文件夹到部署区域
3. 或连接 GitHub 仓库自动部署

---

### 方式四：本地预览

```bash
cd /home/admin/.openclaw/workspace/china-food-map
python3 -m http.server 8080
```

然后在浏览器访问：`http://localhost:8080`

---

## 📁 文件结构

```
china-food-map/
└── index.html    # 主页面（包含所有 HTML/CSS/JS）
```

## 🎨 自定义

### 添加更多美食

编辑 `index.html` 中的 `provinceFoods` 对象：

```javascript
beijing: {
    name: "北京",
    foods: [
        { name: "北京烤鸭", emoji: "🦆", desc: "皮脆肉嫩" },
        // 添加更多美食...
    ]
}
```

### 更换图片

目前使用 emoji 展示，如需使用真实图片：

1. 在 `images/` 文件夹添加图片
2. 修改 `food-image` 部分的 HTML：
```html
<img src="images/北京烤鸭.jpg" alt="北京烤鸭" class="food-image">
```

## 📊 已包含省份

- **华北**：北京、天津、河北、山西、内蒙古
- **东北**：辽宁、吉林、黑龙江
- **华东**：上海、江苏、浙江、安徽、福建、江西、山东
- **华中**：河南、湖北、湖南
- **华南**：广东、广西、海南
- **西南**：重庆、四川、贵州、云南、西藏
- **西北**：陕西、甘肃、青海、宁夏、新疆

## 📝 说明

- 地图为简化版示意图
- 美食数据可根据需要扩展
- 使用 emoji 代替图片，加载快速

## 📄 许可证

MIT License - 可自由使用和修改

---

**享受中国美食之旅！** 🍜🥟🦀
