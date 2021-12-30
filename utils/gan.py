# encoding=utf-8
"""
@author: xiao nian
@contact: xiaonian030@163.com
@time: 2021-12-30 14:30
"""
import os
from ppgan.apps.wav2lip_predictor import Wav2LipPredictor
from ppgan.apps.first_order_predictor import FirstOrderPredictor

# 热加载
wav2lip_predictor = Wav2LipPredictor(static=False,
                                     face_enhancement=True)


def wav2lip(input_video, input_audio, output):
    wav2lip_predictor.run(input_video, input_audio, output)
    return output


def driver(source_image, driving_video, output_path):
    output, filename = os.path.split(output_path)
    first_order_predictor = FirstOrderPredictor(output=output,
                                                filename=filename,
                                                face_enhancement=True,
                                                ratio=0.4,
                                                relative=True,
                                                image_size=512,
                                                adapt_scale=True)
    first_order_predictor.run(source_image, driving_video)
    return os.path.join(output, filename)
