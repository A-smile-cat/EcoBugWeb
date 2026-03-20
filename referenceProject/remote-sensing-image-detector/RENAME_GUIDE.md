# 项目重命名说明

当前项目文件夹名称: `1 website-001`

## 推荐的新名称

根据项目功能，建议重命名为以下之一：

### 选项 1: `remote-sensing-image-detector` （推荐）
- **含义**: 遥感影像检测器
- **优点**: 英文命名，符合项目主题，专业性强

### 选项 2: `rs-image-processor`
- **含义**: 遥感影像处理器
- **优点**: 简短，突出处理功能

### 选项 3: `flask-rs-detection`
- **含义**: Flask遥感检测系统
- **优点**: 突出技术栈

### 选项 4: `pipeline-defect-detector`
- **含义**: 管道缺陷检测器
- **优点**: 符合HTML标题中的"智能管道缺陷检测系统"

## 重命名步骤

### 方法 1: 使用文件管理器（推荐）
1. 关闭所有正在使用此文件夹的程序（IDE、终端等）
2. 在文件管理器中导航到 `D:\wnew\`
3. 右键点击 `1 website-001` 文件夹
4. 选择"重命名"
5. 输入新名称（推荐: `remote-sensing-image-detector`）
6. 按 Enter 确认

### 方法 2: 使用命令行
1. 关闭所有正在使用此文件夹的程序
2. 打开命令提示符或PowerShell
3. 运行以下命令：

```cmd
cd D:\wnew
ren "1 website-001" "remote-sensing-image-detector"
```

### 方法 3: 使用Git（如果使用版本控制）
```bash
cd D:\wnew
git mv "1 website-001" "remote-sensing-image-detector"
```

## 重命名后的操作

重命名后，需要更新以下内容：

### 1. 更新工作目录
如果你在其他工具中引用了这个路径，需要更新：
- IDE 项目配置
- 脚本中的路径
- 快捷方式

### 2. 更新 Git 仓库（如果使用）
```bash
cd D:\wnew\remote-sensing-image-detector
git add .
git commit -m "chore: 重命名项目文件夹"
```

### 3. 更新虚拟环境路径（如果使用）
如果创建了虚拟环境，可能需要重新创建：
```bash
cd D:\wnew\remote-sensing-image-detector
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
```

## 验证

重命名后，验证项目是否正常：

1. **检查路径**
   ```bash
   cd D:\wnew\remote-sensing-image-detector
   ```

2. **运行测试**
   ```bash
   python test_setup.py
   ```

3. **启动应用**
   ```bash
   python manager.py
   ```

4. **访问应用**
   打开浏览器访问: http://127.0.0.1:5000/

## 注意事项

- ⚠️ 重命名前确保关闭所有使用该文件夹的程序
- ⚠️ 如果项目已推送到远程仓库，重命名可能需要更新远程URL
- ⚠️ 虚拟环境的路径是硬编码的，重命名后可能需要重新创建

## 推荐

**我推荐使用 `remote-sensing-image-detector` 这个名称**，因为：
1. 清晰描述了项目功能
2. 符合英文命名规范
3. 适合作为Git仓库名称
4. 专业且易于理解
