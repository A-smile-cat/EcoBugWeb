import os
import logging
import matplotlib.pyplot as plt
from scipy import ndimage
import imageio
import numpy as np

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def rotate(filename, upload_dir='assets/imgs/upload', output_dir='assets/imgs/final'):
    """
    对图像进行90度旋转处理

    Args:
        filename: 文件名
        upload_dir: 上传目录路径
        output_dir: 输出目录路径

    Returns:
        bool: 处理成功返回True，失败返回False
    """
    try:
        # 构建完整的输入路径
        input_path = os.path.join(upload_dir, filename)

        # 检查文件是否存在
        if not os.path.exists(input_path):
            logger.error(f"文件不存在: {input_path}")
            return False

        # 读取图像
        logger.info(f"正在读取图像: {input_path}")
        img = plt.imread(input_path)

        # 检查图像数据
        if img is None or img.size == 0:
            logger.error(f"无法读取图像数据: {input_path}")
            return False

        # 旋转图像90度
        logger.info(f"正在旋转图像...")
        img_rotated = ndimage.rotate(img, 90)

        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)

        # 构建输出路径
        output_path = os.path.join(output_dir, filename)

        # 保存旋转后的图像
        logger.info(f"正在保存图像: {output_path}")

        # 将图像数据转换为0-255范围
        if img_rotated.dtype == np.float32 or img_rotated.dtype == np.float64:
            if img_rotated.max() <= 1.0:
                img_rotated = (img_rotated * 255).astype(np.uint8)
            else:
                img_rotated = img_rotated.astype(np.uint8)

        imageio.imwrite(output_path, img_rotated)

        logger.info(f"图像处理完成: {output_path}")
        return True

    except Exception as e:
        logger.error(f"图像处理失败: {str(e)}", exc_info=True)
        return False

def get_image_info(filename, upload_dir='assets/imgs/upload'):
    """
    获取图像信息

    Args:
        filename: 文件名
        upload_dir: 上传目录路径

    Returns:
        dict: 包含图像信息的字典
    """
    try:
        input_path = os.path.join(upload_dir, filename)
        img = plt.imread(input_path)

        return {
            'filename': filename,
            'shape': img.shape,
            'dtype': img.dtype,
            'size': os.path.getsize(input_path)
        }
    except Exception as e:
        logger.error(f"获取图像信息失败: {str(e)}")
        return None

if __name__ == '__main__':
    # 测试代码
    test_file = '02.png'
    if rotate(test_file):
        print(f"图像 {test_file} 处理成功")
        info = get_image_info(test_file, 'assets/imgs/final')
        if info:
            print(f"处理后的图像信息: {info}")
    else:
        print(f"图像 {test_file} 处理失败")
