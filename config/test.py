# encoding=utf-8
"""
@author: xiao nian
@contact: xiaonian030@163.com
@time: 2021-12-30 11:15
"""

# http 配置
HTTP_CONFIG = {
    'host': '0.0.0.0',
    'port': 55001,
    'workers': 2
}

MODEL_CONFIG = {
    "driver": {
      'input_image': './data/input/test.png',
      'input_video': './data/input/zimeng.mp4',
      'output_video': './data/input/test.mp4'
    },
    "tts": {
      'speed': 1.0,
      'pitch': 1.0,
      'energy': 1.0
    },
    "save": {
      'video': './data/output/video/',
      'audio': './data/output/audio/'
    }
}
