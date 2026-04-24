# 大文件获取说明 / Large File Download Guide

本项目使用 Git LFS (Large File Storage) 存储大文件，或将大文件通过外部链接提供。

---

## 方式一：Git LFS（推荐）

如果已安装 Git LFS，大文件会自动跟随仓库一起下载。

### 安装 Git LFS

```bash
# Windows (使用 Git Bash 或 PowerShell)
git lfs install

# 或下载安装包：https://git-lfs.github.com/
```

### 验证状态

```bash
git lfs ls-files
```

---

## 方式二：手动下载

如果未使用 Git LFS，可以手动下载所需文件。

### 大文件列表（> 1MB）

| 文件路径 | 大小 | 来源 |
|---------|------|------|
| `static/assets1/picture/2.jpg` | 5.3M | 昆虫图片 |
| `static/bg1.jpg` | 2.9M | 背景图 |
| `static/bg.jpg` | 2.4M | 背景图 |
| `static/assets3/images/user-profile.jpg` | 1.8M | 用户头像 |
| `static/assets3/砚湖滨海湿地生态评估报告.pdf` | 1.1M | PDF 报告 |
| `static/assets3/images/lights.jpg` | 442K | 图片 |
| `static/assets1/picture/1.jpg` | 434K | 昆虫图片 |
| `static/assets2/js/echarts.min.js` | 728K | ECharts 库 |
| `static/assets3/js/lib/chart-js/Chart.bundle.js` | 453K | Chart.js |
| `static/assets3/js/lib/rangeSlider/moment-with-locales.js` | 417K | 日期库 |
| `referenceProject/Echarts-Demo-master/js/echarts.min.js` | 728K | ECharts 库 |
| `referenceProject/Echarts-Demo-master/images/map.png` | 303K | 地图图片 |
| `referenceProject/Echarts-Demo-master/images/bg.jpg` | 253K | 背景图 |
| `referenceProject/Echarts-Demo-master/font/DS-DIGIT.TTF` | 25K | 数字字体 |
| `static/assets3/fontAwesome/webfonts/fa-brands-400.svg` | 586K | FontAwesome |
| `static/assets3/fontAwesome/webfonts/fa-solid-900.svg` | 425K | FontAwesome |
| `static/assets3/fonts/fontawesome-webfont.svg` | 759K | FontAwesome |

### 参考项目图片（remote-sensing-image-detector）

| 文件路径 | 大小 | 用途 |
|---------|------|------|
| `assets/imgs/upload/图片1.png` | 511K | 测试图片 |
| `assets/imgs/final/图片1.png` | 354K | 结果图片 |
| `assets/imgs/upload/2404.jpg` | 182K | 遥感图像 |
| `assets/imgs/final/2404.jpg` | 129K | 检测结果 |
| `assets/imgs/upload/demo1.jpg` | 239K | 演示图片 |
| `assets/imgs/final/demo1.jpg` | 151K | 结果图片 |
| 其他 `02.png`, `232.jpg`, `233.jpg` 等 | ~50-150K | 测试数据 |

---

## 快速获取所有大文件

### 方法 A: 使用下载脚本

```bash
# 创建 download_large_files.sh 或 download_large_files.bat
```

### 方法 B: 从云盘下载（如果有）

如果有 OneDrive / 百度网盘等，请将所有 `static/` 和 `referenceProject/` 中的大文件打包上传，然后在此处更新链接。

---

## 文件说明

### 静态资源说明

- **图片文件**: 大部分为昆虫、生态相关的图片，是项目展示的核心素材
- **JS 库**: ECharts、jQuery、Chart.js 等前端库，可从 CDN 替代
- **字体文件**: FontAwesome 图标字体，可从 CDN 获取
- **PDF**: 生态评估报告，是项目示例数据

### 建议的 CDN 替代方案

如果你希望减小仓库体积，可以在 HTML 中使用 CDN 链接：

```html
<!-- ECharts -->
<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>

<!-- jQuery -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<!-- Chart.js -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<!-- FontAwesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<!-- Bootstrap -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
```

---

## 部署注意事项

1. **生产环境**: 建议使用 CDN 替代本地大文件，减少仓库体积
2. **离线环境**: 如果需要离线运行，请确保所有依赖文件都存在
3. **图片优化**: 上传到生产环境前，可以压缩图片以提升加载速度

---

最后更新: 2026-04-24