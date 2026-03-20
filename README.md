# EcoBugWeb - Flask Web应用

> 生态昆虫主题的 Flask Web 应用

[![Flask](https://img.shields.io/badge/Flask-2.0+-green)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.7+-yellow)](https://www.python.org/)

---

## 📖 项目简介

EcoBugWeb 是一个基于 Flask 框架开发的生态昆虫主题 Web 应用，包含多个页面和功能模块，是学习 Flask Web 开发的完整示例项目。

### 核心功能

- ✅ **多页面路由**: 首页、昆虫展示、数据可视化等
- ✅ **模板系统**: Jinja2 模板渲染
- ✅ **静态资源**: CSS、JavaScript、图片
- ✅ **响应式布局**: Bootstrap 框架

---

## 🚀 快速开始

### 环境要求

```bash
Python >= 3.7
Flask >= 2.0
```

### 安装依赖

```bash
cd "0 EcoBugWeb"
pip install flask
```

### 运行项目

```bash
python main.py
# 访问 http://localhost:5000
```

---

## 📁 项目结构

```
0 EcoBugWeb/
├── main.py              # 主程序入口
├── static/              # 静态资源
│   ├── css/            # 样式文件
│   ├── js/             # JavaScript 文件
│   └── images/         # 图片资源
├── templates/           # HTML 模板
│   ├── index.html      # 首页
│   ├── insect.html     # 昆虫展示页
│   ├── datashow.html   # 数据展示页
│   ├── app-profile.html
│   ├── app-widget-card.html
│   ├── chart.html      # 图表页
│   ├── table.html      # 表格页
│   ├── datamap.html    # 地图页
│   └── images.html     # 图片页
└── referenceProject/    # 参考项目
    ├── Echarts-Demo-master/              # ECharts 图表示例项目
    └── remote-sensing-image-detector/    # 遥感图像检测项目
```

---

## 💡 路由说明

### 页面路由

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """首页"""
    return render_template('index.html')

@app.route('/insect')
def insect():
    """昆虫展示页"""
    return render_template('insect.html')

@app.route('/datashow')
def datashow():
    """数据展示页"""
    return render_template('datashow.html')

@app.route('/dashboard1')
def dashboard1():
    """仪表盘页"""
    return render_template('dashboard1.html')

@app.route('/chart')
def chart():
    """图表页"""
    return render_template('chart.html')

@app.route('/table')
def table():
    """表格页"""
    return render_template('table.html')

@app.route('/datamap')
def datamap():
    """地图页"""
    return render_template('datamap.html')

@app.route('/images')
def images():
    """图片页"""
    return render_template('images.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

---

## 🎯 模板示例

### index.html

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcoBugWeb - 生态昆虫</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <h1>欢迎来到 EcoBugWeb</h1>
        <nav>
            <a href="/">首页</a>
            <a href="/insect">昆虫</a>
            <a href="/datashow">数据</a>
            <a href="/chart">图表</a>
        </nav>
    </header>

    <main>
        <h2>生态昆虫多样性展示</h2>
        <p>探索昆虫世界的奇妙之处...</p>
    </main>

    <footer>
        <p>&copy; 2024 EcoBugWeb</p>
    </footer>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
```

### insect.html (带数据传递)

```python
@app.route('/insect')
def insect():
    """昆虫展示页"""
    insects = [
        {"name": "蝴蝶", "order": "鳞翅目", "image": "butterfly.jpg"},
        {"name": "蜜蜂", "order": "膜翅目", "image": "bee.jpg"},
        {"name": "蜻蜓", "order": "蜻蜓目", "image": "dragonfly.jpg"}
    ]
    return render_template('insect.html', insects=insects)
```

```html
<!-- insect.html -->
{% for insect in insects %}
<div class="insect-card">
    <img src="{{ url_for('static', filename='images/' + insect.image) }}"
         alt="{{ insect.name }}">
    <h3>{{ insect.name }}</h3>
    <p>目: {{ insect.order }}</p>
</div>
{% endfor %}
```

---

## 🔧 扩展功能

### 1. 添加数据库

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecobug.db'
db = SQLAlchemy(app)

class Insect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    order = db.Column(db.String(50))
    description = db.Column(db.Text)

# 路由
@app.route('/insects')
def insect_list():
    insects = Insect.query.all()
    return render_template('insects.html', insects=insects)
```

### 2. 添加表单

```python
from flask import request

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        # 搜索逻辑
        results = Insect.query.filter(Insect.name.contains(keyword)).all()
        return render_template('search_results.html', results=results)
    return render_template('search.html')
```

### 3. 添加 API

```python
from flask import jsonify

@app.route('/api/insects')
def api_insects():
    insects = Insect.query.all()
    data = [{
        'id': insect.id,
        'name': insect.name,
        'order': insect.order
    } for insect in insects]
    return jsonify(data)
```

---

## 📊 静态资源

### CSS 示例

```css
/* static/css/style.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f5f5f5;
}

header {
    background-color: #4CAF50;
    color: white;
    padding: 20px;
    text-align: center;
}

nav a {
    color: white;
    margin: 0 10px;
    text-decoration: none;
}

main {
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
}

.insect-card {
    border: 1px solid #ddd;
    padding: 15px;
    margin: 10px 0;
    border-radius: 5px;
}
```

### JavaScript 示例

```javascript
// static/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('EcoBugWeb 加载完成');

    // 示例: 简单的交互
    const cards = document.querySelectorAll('.insect-card');
    cards.forEach(card => {
        card.addEventListener('click', function() {
            alert('你点击了: ' + this.querySelector('h3').textContent);
        });
    });
});
```

---

## 🌟 开发建议

### 1. 使用蓝图 (Blueprint)

```python
from flask import Blueprint

insect_bp = Blueprint('insect', __name__)

@insect_bp.route('/insect')
def insect():
    return render_template('insect.html')

app.register_blueprint(insect_bp)
```

### 2. 添加错误处理

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

### 3. 用户认证

```python
from flask_login import LoginManager, login_required

login_manager = LoginManager(app)

@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')
```

---

## ❓ 常见问题

### Q1: 修改端口?

```python
app.run(host='0.0.0.0', port=8080)
```

### Q2: 开启调试模式?

```python
app.run(debug=True)
```

### Q3: 使用生产环境?

```bash
# 使用 Gunicorn
pip install gunicorn
gunicorn -w 4 main:app
```

---

## 📂 参考项目

本项目包含两个参考项目，用于学习和参考：

### 1. Echarts-Demo-master

ECharts 图表示例项目，提供丰富的图表展示功能。

**位置**: `referenceProject/Echarts-Demo-master/`

**主要内容**:
- ✅ ECharts 数据可视化示例
- ✅ 多种图表类型展示
- ✅ datashow.html 数据展示页面
- ✅ 完整的静态资源（CSS、JS、字体、图片）

**参考价值**:
- 学习 ECharts 图表集成
- 数据可视化最佳实践
- 前端资源组织方式

**使用方式**:
```bash
cd referenceProject/Echarts-Demo-master
# 直接打开 datashow.html 或使用本地服务器
```

---

### 2. remote-sensing-image-detector

遥感图像检测项目，基于 Flask 的图像处理应用。

**位置**: `referenceProject/remote-sensing-image-detector/`

**主要功能**:
- ✅ Flask Web 应用框架
- ✅ 图像处理和检测功能
- ✅ 模板系统应用
- ✅ 配置管理系统

**技术栈**:
- Python Flask
- 图像处理库
- 配置管理（config.py）
- 批处理脚本（start.bat, start.sh）

**参考价值**:
- Flask 项目结构设计
- 图像处理流程
- 配置文件管理
- 跨平台启动脚本

**快速开始**:
```bash
cd referenceProject/remote-sensing-image-detector
pip install -r requirements.txt
python manager.py
```

**详细文档**:
- [README.md](referenceProject/remote-sensing-image-detector/README.md) - 项目说明
- [QUICKSTART.md](referenceProject/remote-sensing-image-detector/QUICKSTART.md) - 快速开始指南
- [FILE_LIST.md](referenceProject/remote-sensing-image-detector/FILE_LIST.md) - 文件列表说明

---

## 📚 参考资料

- [Flask 官方文档](https://flask.palletsprojects.com/)
- [Jinja2 模板文档](https://jinja.palletsprojects.com/)
- [Flask 教程](https://flask.palletsprojects.com/en/2.3.x/tutorial/)
- [ECharts 官方文档](https://echarts.apache.org/)

---

## 📄 许可证

MIT License

---

**最后更新**: 2026-03-04
**状态**: ✅ 可运行
**优先级**: ⭐⭐⭐⭐ (推荐)
**端口**: 5000
**模板引擎**: Jinja2
