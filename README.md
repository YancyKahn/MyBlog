# 基于Django 的博客＋视频网站

### 部署：
环境要求：　python3.6 + Django2 + Mysql

1. 在项目根目录下运行：　pip3 install -r requirements.txt  安装必要mod

2. 数据库迁移
    ```
    python3 manage.py makemigrations
    python3 manage.py mmigrate
    ```

3. 创建超级用户

    ```
    python3 manage.py cratesuperuser
    ```
4. 运行服务

    ```
    python3 manage.py runserver
    ```
5. 打开浏览器输入127.0.0.1：8000打开网站
