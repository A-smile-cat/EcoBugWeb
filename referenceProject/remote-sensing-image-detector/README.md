# 大规模遥感影像分布式目标检测系统

一个基于 Flask 的遥感影像处理和目标检测 Web 应用系统。

## 📋 项目简介

本项目是一个用于大规模遥感影像处理和分布式目标检测的 Web 应用程序。系统提供了图像上传、处理和展示功能，适用于遥感影像分析和智能检测场景。

## ✨ 功能特性

- **图像上传**: 支持用户上传遥感影像文件
- **图像处理**: 自动对上传的图像进行旋转处理（90度）
- **可视化展示**: 处理后的图像实时展示
- **外部集成**: 集成 AI Earth 平台链接，方便进一步分析
- **动态界面**: 包含动态背景效果和交互式按钮
- **安全验证**: 文件类型验证、大小限制、安全文件名处理
- **错误处理**: 完善的错误处理和日志记录
- **API接口**: 提供RESTful API接口

## 🛠️ 技术栈

### 后端
- **Flask 2.3.3**: Python Web 框架
- **SciPy 1.11.4**: 科学计算库，用于图像处理
- **NumPy 1.24.3**: 数值计算库
- **Pillow 10.1.0**: 图像处理库
- **imageio 2.31.6**: 图像读写库

### 前端
- **HTML5/CSS3**: 现代化的页面结构和样式
- **JavaScript**: 交互式功能实现
- **动态背景效果**: CSS 动画

## 📁 项目结构

```
website-001/
├── assets/                  # 静态资源目录
│   ├── css/                # 样式文件
│   │   ├── button.css      # 按钮样式
│   │   ├── button2.css     # 按钮2样式
│   │   ├── main.css        # 主样式
│   │   └── style.css       # 通用样式
│   ├── js/                 # JavaScript 文件
│   │   └── main.js         # 主脚本
│   └── imgs/               # 图像存储目录
│       ├── upload/         # 上传的原始图像
│       └── final/          # 处理后的图像
├── templates/              # HTML 模板目录
│   ├── index.html          # 主页模板
│   └── upload.html         # 上传结果展示页
├── deal.py                 # 图像处理模块
├── manager.py              # Flask 应用主程序 (新)
├── mangager.py             # Flask 应用主程序 (旧，已弃用)
├── config.py               # 配置文件 (新)
├── requirements.txt        # 依赖管理 (新)
└── README.md               # 项目说明文档
```

## 🚀 安装与运行

### 环境要求

- Python 3.8+
- pip (Python 包管理器)

### 安装依赖

1. **克隆或下载项目**
   ```bash
   cd D:\wnew\1\website-001
   ```

2. **创建虚拟环境（推荐）**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

### 运行步骤

1. **启动应用**
   ```bash
   python manager.py
   ```

2. **访问应用**

   打开浏览器访问: `http://127.0.0.1:5000/` 或 `http://localhost:5000/`

## 📖 使用指南

### 1. 主页访问
- 访问根路径 `/` 进入系统主页
- 主页展示系统信息和动态背景效果
- 点击"选择文件"按钮选择要处理的图像

### 2. 图像上传
- 支持的格式: PNG, JPG, JPEG, GIF, BMP, TIFF, WEBP
- 最大文件大小: 50MB
- 在主页点击文件选择按钮
- 选择要处理的遥感影像文件
- 点击"上传并处理"按钮提交

### 3. 图像处理
- 系统自动接收上传的图像
- 验证文件类型和大小
- 将图像保存到 `assets/imgs/upload/` 目录
- 自动进行 90 度旋转处理
- 处理后的图像保存到 `assets/imgs/final/` 目录
- 展示处理结果并提供下载链接

### 4. 查看结果
- 上传成功后自动跳转到结果页面
- 可查看处理后的图像
- 可下载处理后的图像
- 可返回首页继续上传

### 5. 外部平台
- 点击"AI Earth"按钮跳转到阿里云 AI Earth 平台
- 可进行更深入的遥感影像分析

## 🔧 核心功能说明

### 图像处理模块 (deal.py)

```python
def rotate(filename, upload_dir='assets/imgs/upload', output_dir='assets/imgs/final'):
    """
    对图像进行90度旋转处理

    - 使用 matplotlib.pyplot 读取图像
    - 使用 scipy.ndimage.rotate() 进行图像旋转
    - 使用 imageio.imwrite() 保存处理结果
    - 完善的错误处理和日志记录
    """
```

主要功能:
- ✅ 图像读取和验证
- ✅ 90度旋转处理
- ✅ 自动数据类型转换
- ✅ 错误处理和日志记录
- ✅ 获取图像信息工具函数

### Web 应用 (manager.py)

主要路由:
- `/`: 主页，展示系统界面
- `/upload`: 处理文件上传，支持 GET 和 POST 方法
- `/api/images`: API接口，列出所有处理过的图像

安全特性:
- ✅ 文件类型验证
- ✅ 文件大小限制（50MB）
- ✅ 安全文件名处理（secure_filename）
- ✅ CSRF保护（SECRET_KEY）
- ✅ 完善的错误处理
- ✅ 日志记录

配置:
- 静态文件目录: `assets`
- 上传目录: `assets/imgs/upload`
- 输出目录: `assets/imgs/final`
- 开发模式: DEBUG=True

## 🔒 安全特性

### 已实现
1. **文件类型验证**: 只允许上传指定格式的图像文件
2. **文件大小限制**: 最大50MB，防止大文件攻击
3. **安全文件名**: 使用 `secure_filename` 防止路径遍历攻击
4. **CSRF保护**: 使用 SECRET_KEY 保护表单提交
5. **错误处理**: 完善的异常捕获和日志记录
6. **输入验证**: 验证文件是否存在、是否为空

### 建议增强（生产环境）
- [ ] 添加用户认证系统
- [ ] 实现HTTPS
- [ ] 添加速率限制
- [ ] 文件内容验证（不仅仅是扩展名）
- [ ] 使用专业的WSGI服务器（Gunicorn/uWSGI）

## 📊 API 文档

### GET /api/images
获取所有处理过的图像列表

**响应示例:**
```json
{
  "images": [
    "image1.jpg",
    "image2.png"
  ]
}
```

### POST /upload
上传并处理图像

**请求:**
- Content-Type: `multipart/form-data`
- Body: `file` (文件字段)

**响应:**
- 成功: 重定向到结果页面
- 失败: Flash错误消息

## ⚠️ 注意事项

1. **文件上传目录**: 系统会自动创建必要的目录

2. **支持的图像格式**:
   - PNG
   - JPG/JPEG
   - GIF
   - BMP
   - TIFF
   - WEBP

3. **性能考虑**:
   - 当前为单机运行模式
   - 大规模影像处理建议使用分布式架构
   - 考虑添加任务队列（Celery）

4. **生产环境部署**:
   建议使用专业的WSGI服务器:
   ```bash
   # Gunicorn
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 manager:app

   # uWSGI
   pip install uwsgi
   uwsgi --http :5000 --wsgi-file manager.py --callable app
   ```

5. **日志**: 应用会输出详细的运行日志，便于调试

## 🔍 故障排除

### 常见问题

1. **端口被占用**
   ```
   错误: Address already in use
   解决: 修改 manager.py 中的 PORT 配置
   ```

2. **依赖安装失败**
   ```
   解决: 升级 pip
   python -m pip install --upgrade pip
   ```

3. **图像处理失败**
   ```
   检查:
   - 图像格式是否支持
   - 图像是否损坏
   - 查看日志输出的错误信息
   ```

4. **权限问题**
   ```
   确保 assets/imgs/upload 和 assets/imgs/final 目录有写入权限
   ```

## 🚧 扩展建议

- [ ] 添加用户认证系统
- [ ] 支持批量图像上传和处理
- [ ] 集成深度学习目标检测模型（YOLO、Faster R-CNN等）
- [ ] 添加分布式任务队列（Celery + Redis）
- [ ] 实现数据库存储处理记录（PostgreSQL/MongoDB）
- [ ] 添加更多图像处理算法（缩放、裁剪、滤波等）
- [ ] 实现图像预览和对比功能
- [ ] 添加处理进度显示
- [ ] 实现WebSocket实时通信
- [ ] 添加Docker容器化部署
- [ ] 集成前端框架（React/Vue）

## 📝 更新日志

### v2.0 (2026-03-20) - 重大更新
- ✅ 修复依赖问题（scipy.misc.imsave -> imageio）
- ✅ 添加完善的错误处理
- ✅ 添加文件类型和大小验证
- ✅ 添加安全文件名处理
- ✅ 添加日志系统
- ✅ 添加配置文件
- ✅ 添加 requirements.txt
- ✅ 改进HTML模板（Flash消息、更好的UI）
- ✅ 添加API接口
- ✅ 添加CSRF保护
- ✅ 改进项目文档

### v1.0 (2024-02) - 初始版本
- 基本的图像上传功能
- 图像旋转处理
- 简单的 Web 界面

## 🤝 技术支持

如遇问题，请检查:
1. Python 环境是否正确安装 (Python 3.8+)
2. 依赖包是否完整安装 (`pip install -r requirements.txt`)
3. 文件目录权限是否正确
4. 端口 5000 是否被占用
5. 查看应用日志输出

## 📄 许可证

本项目仅供学习和研究使用。

## 👥 贡献

欢迎提交 Issue 和 Pull Request！

---

**开发团队**: Remote Sensing Image Processing Team
**最后更新**: 2026-03-20
