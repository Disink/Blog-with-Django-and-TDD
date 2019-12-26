# Blog-with-Django-and-TDD
## 目的
- 練習使用TDD建立一個基於Django的Blog

## 環境設定
### 安裝Firefox和Geckodriver
- curl下載geckodriver會發生錯誤
```
yum install -y firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar zxvf geckodriver-v0.26.0-linux64.tar.gz
ln -f /usr/local/geckodriver /usr/bin/geckodriver
geckodriver --version
```

### 安裝並建立Python virtualenv
```
yum install python3
pip3 install virtualenv

python3.6 -m venv blog
source /share/python/env/blog/bin/activate
```

### 安裝Djanog和Selenium
```
pip3 install "django==2.1"
pip3 install "selenium<4"
```

### 建立並運行Blog APP
```
django-admin.py startproject blog
python manage.py runserver
```

### 新增給專案用的檔案
- 忽略一些不需要上傳到Git的檔案
- 紀錄套件相依
```
echo "db.sqlite3" >> .gitignore
echo "geckodriver.log" >> .gitignore

echo "__pycache__" >> .gitignore
echo "superlists/__pycache__" >> .gitignore
echo "*.pyc" >> .gitignore

pip3 freeze > requirements.txt
```
