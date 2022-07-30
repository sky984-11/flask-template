'''
Description: db配置
Date: 2022-06-16 16:37:25
LastEditTime: 2022-07-31 06:42:31
FilePath: \undefinedd:\GitData\resource\python\flask项目模板\app\db.py
Author: liupeng
'''



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# app.config.from_object(TestingConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookshelf.db' 
#解决json格式数据显示乱码
app.config['JSON_AS_ASCII'] = False
#解决pool相关报错
app.config.update({
    'SQLALCHEMY_POOL_SIZE': None,
    'SQLALCHEMY_POOL_TIMEOUT': None
})

db = SQLAlchemy(app)
# 通过类Migrate创建migrate实例
migrate = Migrate(db)




class Quotes(db.Model):
    """名言表"""
    __tablename__ = 'quotes'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(10),  nullable=False)
    content = db.Column(db.String(255), nullable=False)
    bookclass = db.Column(db.String(20), nullable=False)


#创建表
db.create_all()

#删除表
# db.drop_all()


