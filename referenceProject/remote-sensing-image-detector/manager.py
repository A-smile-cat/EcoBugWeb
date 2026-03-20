import os
import logging
from flask import Flask, request, send_from_directory, render_template, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
import deal

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 创建Flask应用
app = Flask(__name__)
app.static_folder = 'assets'
app.static_url_path = '/assets'

# 配置
app.config['UPLOAD_FOLDER'] = 'assets/imgs/upload'
app.config['OUTPUT_FOLDER'] = 'assets/imgs/final'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB 最大文件大小
app.config['SECRET_KEY'] = os.urandom(24).hex()  # 用于flash消息和CSRF保护

# 允许的文件扩展名
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'webp'}

def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def ensure_directories():
    """确保必要的目录存在"""
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    """主页"""
    logger.info("访问主页")
    return render_template('index.html', name='Flask')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    """处理文件上传"""
    if request.method == 'POST':
        # 检查是否有文件
        if 'file' not in request.files:
            flash('没有选择文件', 'error')
            logger.warning("上传请求中没有文件")
            return redirect(request.url)

        file = request.files['file']

        # 检查文件名
        if file.filename == '':
            flash('没有选择文件', 'error')
            logger.warning("上传的文件名为空")
            return redirect(request.url)

        # 验证文件类型
        if not allowed_file(file.filename):
            flash(f'不支持的文件类型。支持的格式: {", ".join(ALLOWED_EXTENSIONS)}', 'error')
            logger.warning(f"不支持的文件类型: {file.filename}")
            return redirect(request.url)

        try:
            # 确保目录存在
            ensure_directories()

            # 安全的文件名
            filename = secure_filename(file.filename)

            # 保存原始文件
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)
            logger.info(f"文件已保存: {upload_path}")

            # 处理图像
            if deal.rotate(filename, app.config['UPLOAD_FOLDER'], app.config['OUTPUT_FOLDER']):
                flash('文件上传并处理成功！', 'success')
                logger.info(f"图像处理成功: {filename}")
                return render_template('upload.html', name=filename)
            else:
                flash('图像处理失败，请检查文件格式', 'error')
                logger.error(f"图像处理失败: {filename}")
                return redirect(request.url)

        except Exception as e:
            flash(f'上传失败: {str(e)}', 'error')
            logger.error(f"文件上传失败: {str(e)}", exc_info=True)
            return redirect(request.url)

    # GET 请求
    return render_template('upload.html')

@app.route('/api/images')
def list_images():
    """API: 列出所有处理过的图像"""
    try:
        output_dir = app.config['OUTPUT_FOLDER']
        if not os.path.exists(output_dir):
            return jsonify({'images': []})

        images = [f for f in os.listdir(output_dir)
                  if os.path.isfile(os.path.join(output_dir, f)) and allowed_file(f)]
        return jsonify({'images': sorted(images)})
    except Exception as e:
        logger.error(f"获取图像列表失败: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.errorhandler(413)
def request_entity_too_large(error):
    """处理文件过大错误"""
    flash('文件太大，最大支持50MB', 'error')
    return redirect(request.url), 413

@app.errorhandler(404)
def page_not_found(error):
    """404错误处理"""
    logger.warning(f"404错误: {request.url}")
    return render_template('index.html', error='页面未找到'), 404

@app.errorhandler(500)
def internal_server_error(error):
    """500错误处理"""
    logger.error(f"500错误: {str(error)}")
    return render_template('index.html', error='服务器内部错误'), 500

if __name__ == '__main__':
    # 确保必要的目录存在
    ensure_directories()

    logger.info("启动Flask应用...")
    logger.info(f"上传目录: {app.config['UPLOAD_FOLDER']}")
    logger.info(f"输出目录: {app.config['OUTPUT_FOLDER']}")

    # 运行应用（开发模式）
    app.run(debug=True, host='0.0.0.0', port=5000)
