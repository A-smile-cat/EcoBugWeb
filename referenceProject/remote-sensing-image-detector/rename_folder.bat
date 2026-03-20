@echo off
REM 项目文件夹重命名脚本
REM 由于文件夹正在使用，此脚本需要在关闭所有相关程序后手动运行

echo ========================================
echo 项目文件夹重命名工具
echo ========================================
echo.
echo 当前文件夹名称: 1 website-001
echo 新文件夹名称: remote-sensing-image-detector
echo.
echo ⚠️  注意: 请确保已关闭所有使用该文件夹的程序！
echo.
pause

cd /d D:\wnew

if exist "1 website-001" (
    echo 正在重命名...
    ren "1 website-001" "remote-sensing-image-detector"
    if %errorlevel% equ 0 (
        echo.
        echo ✅ 重命名成功！
        echo 新路径: D:\wnew\remote-sensing-image-detector
        echo.
        echo 接下来请:
        echo 1. 更新IDE的项目路径
        echo 2. 重新打开终端并导航到新路径
        echo 3. 如有虚拟环境，建议重新创建
        echo.
    ) else (
        echo.
        echo ❌ 重命名失败
        echo 可能原因:
        echo - 文件夹正在被使用
        echo - 没有权限
        echo - 文件夹不存在
        echo.
        echo 请尝试:
        echo 1. 关闭所有使用该文件夹的程序
        echo 2. 以管理员身份运行此脚本
        echo 3. 手动在文件管理器中重命名
        echo.
    )
) else (
    echo.
    echo ⚠️  文件夹 "1 website-001" 不存在
    echo 可能已经重命名过了
    echo.
)

pause
