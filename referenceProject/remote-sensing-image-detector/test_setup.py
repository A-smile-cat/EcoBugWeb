# 大规模遥感影像分布式目标检测系统 - 测试脚本

import os
import sys
import matplotlib.pyplot as plt
from scipy import ndimage
import imageio
import numpy as np

def test_dependencies():
    """测试所有依赖是否正确安装"""
    print("=" * 60)
    print("测试依赖包...")
    print("=" * 60)

    dependencies = {
        'flask': 'Flask',
        'scipy': 'SciPy',
        'matplotlib': 'Matplotlib',
        'numpy': 'NumPy',
        'PIL': 'Pillow',
        'imageio': 'imageio',
        'werkzeug': 'Werkzeug'
    }

    failed = []
    for module, name in dependencies.items():
        try:
            __import__(module)
            print(f"✓ {name} - 已安装")
        except ImportError:
            print(f"✗ {name} - 未安装")
            failed.append(name)

    print()
    if failed:
        print(f"❌ 缺少依赖: {', '.join(failed)}")
        print("请运行: pip install -r requirements.txt")
        return False
    else:
        print("✅ 所有依赖已正确安装")
        return True

def test_directories():
    """测试必要的目录是否存在"""
    print("\n" + "=" * 60)
    print("测试目录结构...")
    print("=" * 60)

    directories = [
        'assets',
        'assets/css',
        'assets/js',
        'assets/imgs',
        'assets/imgs/upload',
        'assets/imgs/final',
        'templates'
    ]

    all_exist = True
    for directory in directories:
        exists = os.path.exists(directory)
        status = "✓" if exists else "✗"
        print(f"{status} {directory}/")
        if not exists:
            all_exist = False

    print()
    if all_exist:
        print("✅ 所有目录存在")
        return True
    else:
        print("⚠️  部分目录不存在，应用将自动创建")
        return True

def test_image_processing():
    """测试图像处理功能"""
    print("\n" + "=" * 60)
    print("测试图像处理功能...")
    print("=" * 60)

    # 检查是否有测试图像
    upload_dir = 'assets/imgs/upload'
    if not os.path.exists(upload_dir):
        print("⚠️  上传目录不存在，跳过图像处理测试")
        return True

    # 查找第一个图像文件
    image_files = [f for f in os.listdir(upload_dir)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    if not image_files:
        print("⚠️  没有找到测试图像，跳过图像处理测试")
        print("提示: 上传一个图像到 assets/imgs/upload/ 目录进行测试")
        return True

    test_image = image_files[0]
    print(f"使用测试图像: {test_image}")

    try:
        # 读取图像
        input_path = os.path.join(upload_dir, test_image)
        img = plt.imread(input_path)
        print(f"✓ 成功读取图像，形状: {img.shape}")

        # 旋转图像
        img_rotated = ndimage.rotate(img, 90)
        print(f"✓ 成功旋转图像，形状: {img_rotated.shape}")

        # 转换数据类型
        if img_rotated.dtype == np.float32 or img_rotated.dtype == np.float64:
            if img_rotated.max() <= 1.0:
                img_rotated = (img_rotated * 255).astype(np.uint8)

        # 测试保存（不实际保存）
        print("✓ 数据类型转换成功")
        print()
        print("✅ 图像处理功能正常")
        return True

    except Exception as e:
        print(f"❌ 图像处理测试失败: {str(e)}")
        return False

def test_config():
    """测试配置文件"""
    print("\n" + "=" * 60)
    print("测试配置...")
    print("=" * 60)

    try:
        from config import config
        print("✓ config.py 加载成功")

        dev_config = config.get('development')
        if dev_config:
            print(f"✓ 开发环境配置: DEBUG={dev_config.DEBUG}")
            print(f"  上传目录: {dev_config.UPLOAD_FOLDER}")
            print(f"  输出目录: {dev_config.OUTPUT_FOLDER}")
            print(f"  支持的格式: {', '.join(dev_config.ALLOWED_EXTENSIONS)}")

        print()
        print("✅ 配置正常")
        return True

    except Exception as e:
        print(f"⚠️  配置文件加载失败: {str(e)}")
        return True  # 配置文件是可选的

def main():
    """运行所有测试"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "遥感影像处理系统 - 环境检查工具" + " " * 16 + "║")
    print("╚" + "=" * 58 + "╝")
    print()

    results = []

    # 测试1: 依赖
    results.append(("依赖包", test_dependencies()))

    # 测试2: 目录
    results.append(("目录结构", test_directories()))

    # 测试3: 配置
    results.append(("配置文件", test_config()))

    # 测试4: 图像处理
    results.append(("图像处理", test_image_processing()))

    # 总结
    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)

    for name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{name}: {status}")

    print()

    failed_count = sum(1 for _, result in results if not result)

    if failed_count == 0:
        print("🎉 所有测试通过！系统可以正常运行。")
        print()
        print("启动命令: python manager.py")
        print("访问地址: http://127.0.0.1:5000/")
        return 0
    else:
        print(f"⚠️  {failed_count} 个测试失败，请检查上述错误信息。")
        return 1

if __name__ == '__main__':
    sys.exit(main())
