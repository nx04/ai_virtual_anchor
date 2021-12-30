# encoding=utf-8
"""
@author: xiao nian
@contact: xiaonian030@163.com
@time: 2021-12-30 11:30
"""
from PaddleTools.GAN import FOM
from config.config import MODEL_CONFIG

if __name__ == '__main__':
    cvh = FOM(MODEL_CONFIG['driver']['input_image'],
              MODEL_CONFIG['driver']['input_video'],
              MODEL_CONFIG['driver']['output_video'])

    print('已成功创建虚拟人，文件保存在{}'.format(cvh))

