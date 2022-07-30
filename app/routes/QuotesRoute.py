'''
Description: 
Date: 2022-06-17 08:22:09
LastEditTime: 2022-06-17 16:38:36
FilePath: \app\routes\QuotesRoute.py
Author: liupeng
'''
# import sys
# sys.path.append("..") 

from public.thirdPartyApi.getQuotes import QuoteApi
from flask import jsonify



def RandomImage():
  """获取随机名言"""
  data = QuoteApi().randomQuotes()
  response = {
      'msg': {'author':data.author,'content':data.content}
    }
  return jsonify(response)