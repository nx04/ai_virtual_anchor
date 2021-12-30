# encoding=utf-8
"""
@author: xiao nian
@contact: xiaonian030@163.com
@time: 2021-12-30 11:30
"""


def api_response(code, data, msg):
    return {
        "code": code,
        'msg': msg,
        'data': data
    }
