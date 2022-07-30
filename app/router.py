'''
Description: 路由配置
Date: 2022-06-16 16:47:38
LastEditTime: 2022-07-31 06:40:29
FilePath: \undefinedd:\GitData\resource\python\flask项目模板\app\router.py
Author: liupeng
'''
from flask_cors import CORS
from flask import Blueprint
#实例
from routes.QuotesRoute import *


# 创建蓝图
b1 = Blueprint('b1', __name__)
 # 解决跨域问题
CORS(b1) 

#获取随机名言api
b1.route('/api/random/quotes', methods=['GET'])(RandomImage)

