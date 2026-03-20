# ECharts 数据可视化大屏

> 基于 ECharts 的响应式数据可视化大屏项目

[![ECharts](https://img.shields.io/badge/ECharts-5.0+-red)](https://echarts.apache.org/)
[![jQuery](https://img.shields.io/badge/jQuery-3.0+-blue)](https://jquery.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📖 项目简介

这是一个完整的 ECharts 数据可视化大屏项目，实现了自适应布局、多种图表类型、中国地图数据展示等功能，适合作为数据大屏开发的参考模板。

### 核心功能

- ✅ **响应式布局**: 使用 rem 适配不同屏幕
- ✅ **多种图表**: 折线图、柱状图、饼图、地图等
- ✅ **中国地图**: 省份数据可视化
- ✅ **实时更新**: 模拟实时数据更新
- ✅ **自适应**: 自动适应窗口大小变化

---

## 🚀 快速开始

### 直接打开

```bash
# 方法 1: 直接在浏览器中打开
双击 datashow.html 文件

# 方法 2: 使用本地服务器 (推荐)
python -m http.server 8000
# 访问 http://localhost:8000/datashow.html
```

### 在线演示

访问: https://nichan-13.github.io/Echarts-Demo/

---

## 📁 项目结构

```
0 Echarts-pro2/
├── datashow.html        # 数据可视化大屏主页
├── ECharts使用步骤.html  # 使用教程
├── README.md           # 项目说明
├── _config.yml         # 配置文件
├── css/                # 样式文件
│   └── (CSS 文件)
├── js/                 # JavaScript 文件
│   ├── china.js        # 中国地图数据
│   ├── datashow.js     # 主逻辑
│   ├── echarts.min.js  # ECharts 库
│   ├── flexible.js     # rem 适配
│   └── jquery.js       # jQuery 库
├── font/               # 字体文件
└── images/             # 图片资源
```

---

## 💡 核心代码

### 1. HTML 结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>数据可视化大屏</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- 大屏容器 -->
    <div class="container">
        <!-- 标题 -->
        <header class="header">数据可视化大屏</header>

        <!-- 内容区域 -->
        <div class="content">
            <!-- 左侧 -->
            <div class="left-panel">
                <div id="chart1" class="chart"></div>
                <div id="chart2" class="chart"></div>
            </div>

            <!-- 中间 -->
            <div class="center-panel">
                <div id="mapChart" class="chart"></div>
            </div>

            <!-- 右侧 -->
            <div class="right-panel">
                <div id="chart3" class="chart"></div>
                <div id="chart4" class="chart"></div>
            </div>
        </div>
    </div>

    <!-- 引入 JS 文件 -->
    <script src="js/jquery.js"></script>
    <script src="js/echarts.min.js"></script>
    <script src="js/flexible.js"></script>
    <script src="js/china.js"></script>
    <script src="js/datashow.js"></script>
</body>
</html>
```

### 2. 响应式 CSS (使用 rem)

```css
/* 基准字体大小 */
html {
    font-size: 16px;
}

/* 使用 rem 单位 */
.container {
    width: 100rem;
    height: 56.25rem;  /* 16:9 比例 */
    margin: 0 auto;
}

.chart {
    width: 100%;
    height: 100%;
}

/* 媒体查询 */
@media screen and (max-width: 1024px) {
    html {
        font-size: 14px;
    }
}
```

### 3. ECharts 初始化

```javascript
// datashow.js

// 1. 初始化图表实例
var chart1 = echarts.init(document.getElementById('chart1'));

// 2. 配置项
var option1 = {
    title: {
        text: '示例图表'
    },
    tooltip: {},
    xAxis: {
        data: ['A', 'B', 'C', 'D', 'E']
    },
    yAxis: {},
    series: [{
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10]
    }]
};

// 3. 设置配置项
chart1.setOption(option1);

// 4. 响应式
window.addEventListener('resize', function() {
    chart1.resize();
});
```

### 4. 中国地图

```javascript
// 初始化地图
var mapChart = echarts.init(document.getElementById('mapChart'));

var mapOption = {
    title: {
        text: '中国地图数据展示',
        left: 'center'
    },
    tooltip: {
        trigger: 'item',
        formatter: '{b}<br/>{c}'
    },
    visualMap: {
        min: 0,
        max: 1000,
        text: ['高', '低'],
        realtime: false,
        calculable: true,
        inRange: {
            color: ['#lightskyblue', 'yellow', 'orangered']
        }
    },
    series: [{
        name: '数据',
        type: 'map',
        map: 'china',
        roam: true,  // 允许缩放和平移
        label: {
            show: true,
            fontSize: 10
        },
        data: [
            {name: '北京', value: 900},
            {name: '上海', value: 850},
            {name: '广东', value: 950},
            // ... 更多省份数据
        ]
    }]
};

mapChart.setOption(mapOption);
```

### 5. 实时数据更新

```javascript
// 定时更新数据
setInterval(function() {
    // 更新图表数据
    var newData = generateRandomData();

    chart1.setOption({
        series: [{
            data: newData
        }]
    });
}, 3000);  // 每3秒更新一次

// 生成随机数据
function generateRandomData() {
    var data = [];
    for (var i = 0; i < 5; i++) {
        data.push(Math.floor(Math.random() * 100));
    }
    return data;
}
```

---

## 🎯 图表类型

### 1. 折线图

```javascript
var lineOption = {
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [820, 932, 901, 934, 1290, 1330, 1320],
        type: 'line',
        smooth: true  // 平滑曲线
    }]
};
```

### 2. 柱状图

```javascript
var barOption = {
    xAxis: {
        type: 'category',
        data: ['A', 'B', 'C', 'D', 'E']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [120, 200, 150, 80, 70],
        type: 'bar',
        itemStyle: {
            color: '#5470c6'
        }
    }]
};
```

### 3. 饼图

```javascript
var pieOption = {
    series: [{
        name: '访问来源',
        type: 'pie',
        radius: '50%',
        data: [
            {value: 1048, name: '搜索引擎'},
            {value: 735, name: '直接访问'},
            {value: 580, name: '邮件营销'},
            {value: 484, name: '联盟广告'},
            {value: 300, name: '视频广告'}
        ],
        emphasis: {
            itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
        }
    }]
};
```

### 4. 仪表盘

```javascript
var gaugeOption = {
    series: [{
        type: 'gauge',
        startAngle: 180,
        endAngle: 0,
        min: 0,
        max: 100,
        splitNumber: 10,
        axisLine: {
            lineStyle: {
                width: 30,
                color: [
                    [0.3, '#67e0e3'],
                    [0.7, '#37a2da'],
                    [1, '#fd666d']
                ]
            }
        },
        pointer: {
            itemStyle: {
                color: 'auto'
            }
        },
        detail: {
            valueAnimation: true,
            formatter: '{value}%',
            color: 'auto'
        },
        data: [{
            value: 75,
            name: '完成率'
        }]
    }]
};
```

---

## 🔧 自定义开发

### 修改颜色主题

```javascript
// 自定义颜色调色板
var colorPalette = [
    '#5470c6', '#91cc75', '#fac858', '#ee6666',
    '#73c0de', '#3ba272', '#fc8452', '#9a60b4'
];

option = {
    color: colorPalette,
    // ... 其他配置
};
```

### 添加交互

```javascript
// 点击事件
chart1.on('click', function(params) {
    console.log(params.name);
    console.log(params.value);
    alert('点击了: ' + params.name);
});

// 鼠标悬停
chart1.on('mouseover', function(params) {
    console.log('悬停在: ' + params.name);
});
```

---

## 📱 响应式适配

### flexible.js 原理

```javascript
// flexible.js 简化版
(function() {
    function setRemUnit() {
        // 设计稿宽度 (假设 1920px)
        var designWidth = 1920;

        // 获取当前屏幕宽度
        var currentWidth = document.documentElement.clientWidth;

        // 计算比例
        var scale = currentWidth / designWidth;

        // 设置基准字体大小
        document.documentElement.style.fontSize = scale * 100 + 'px';
    }

    setRemUnit();

    // 监听窗口变化
    window.addEventListener('resize', setRemUnit);
})();
```

---

## ❓ 常见问题

### Q1: 图表不显示?

- ✅ 检查 DOM 元素是否加载完成
- ✅ 检查 ECharts 库是否正确引入
- ✅ 检查容器是否有宽高

### Q2: 地图不显示?

- ✅ 确保 china.js 已引入
- ✅ 检查 ECharts 版本兼容性

### Q3: 响应式不生效?

- ✅ 检查 flexible.js 是否加载
- ✅ 检查 CSS 是否使用 rem 单位

---

**最后更新**: 2026-03-04
**状态**: ✅ 可运行
**优先级**: ⭐⭐⭐⭐ (推荐)
