#!/bin/bash
# 大规模遥感影像处理系统 - Linux/Mac 启动脚本

echo "========================================"
echo "遥感影像处理系统启动脚本"
echo "========================================"
echo ""

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "[错误] Python3未安装"
    echo "请安装Python3: https://www.python.org/downloads/"
    exit 1
fi

echo "[1/3] 检查Python版本..."
python3 --version
echo ""

# 检查虚拟环境
if [ -d "venv" ]; then
    echo "[2/3] 激活虚拟环境..."
    source venv/bin/activate
else
    echo "[2/3] 未检测到虚拟环境，使用系统Python"
fi
echo ""

# 检查依赖
echo "[3/3] 检查依赖包..."
if ! python3 -c "import flask" &> /dev/null; then
    echo "[警告] 依赖包未安装"
    echo "正在安装依赖包..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "[错误] 依赖安装失败"
        exit 1
    fi
    echo "[成功] 依赖安装完成"
else
    echo "[成功] 依赖包已安装"
fi
echo ""

# 运行测试
echo "========================================"
echo "运行环境检查..."
echo "========================================"
python3 test_setup.py
if [ $? -ne 0 ]; then
    echo ""
    read -p "[警告] 环境检查发现问题，是否继续启动？ (y/n) " continue
    if [ "$continue" != "y" ] && [ "$continue" != "Y" ]; then
        exit 1
    fi
fi
echo ""

# 启动应用
echo "========================================"
echo "启动Flask应用..."
echo "========================================"
echo "访问地址: http://127.0.0.1:5000/"
echo "按 Ctrl+C 停止服务器"
echo "========================================"
echo ""

python3 manager.py
