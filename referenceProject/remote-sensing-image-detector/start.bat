@echo off
REM 大规模遥感影像处理系统 - Windows 启动脚本
echo ========================================
echo 遥感影像处理系统启动脚本
echo ========================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] Python未安装或未添加到PATH
    echo 请从 https://www.python.org/downloads/ 下载并安装Python
    pause
    exit /b 1
)

echo [1/3] 检查Python版本...
python --version
echo.

REM 检查虚拟环境
if exist "venv\Scripts\activate.bat" (
    echo [2/3] 激活虚拟环境...
    call venv\Scripts\activate.bat
) else (
    echo [2/3] 未检测到虚拟环境，使用系统Python
)
echo.

REM 检查依赖
echo [3/3] 检查依赖包...
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo [警告] 依赖包未安装
    echo 正在安装依赖包...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [错误] 依赖安装失败
        pause
        exit /b 1
    )
    echo [成功] 依赖安装完成
) else (
    echo [成功] 依赖包已安装
)
echo.

REM 运行测试
echo ========================================
echo 运行环境检查...
echo ========================================
python test_setup.py
if %errorlevel% neq 0 (
    echo.
    echo [警告] 环境检查发现问题，是否继续启动？ (Y/N)
    set /p continue=
    if /i not "%continue%"=="Y" (
        exit /b 1
    )
)
echo.

REM 启动应用
echo ========================================
echo 启动Flask应用...
echo ========================================
echo 访问地址: http://127.0.0.1:5000/
echo 按 Ctrl+C 停止服务器
echo ========================================
echo.

python manager.py

pause
