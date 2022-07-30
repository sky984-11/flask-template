'''
Description: 运行文件
Date: 2022-06-16 16:42:52
LastEditTime: 2022-07-31 06:39:21
FilePath: \undefinedd:\GitData\resource\python\flask项目模板\app\run.py
Author: liupeng
'''

import sys

from db import app,db
from router import b1



if __name__ == '__main__':
    app.register_blueprint(b1)
    app.run(debug=True,host='0.0.0.0')