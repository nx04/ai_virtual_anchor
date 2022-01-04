# encoding=utf-8
"""
@author: xiao nian
@contact: xiaonian030@163.com
@time: 2021-12-30 11:30
"""
import os
from config.config import MODEL_CONFIG
from anchor_kit.tts import TTSExecutor
from anchor_kit.gan import wav2lip

if __name__ == '__main__':
    text = '今天的天气不错啊'
    TTS = TTSExecutor()
    wav_file = TTS.run(text=text, output='output.wav')  # 合成音频
    video = wav2lip(MODEL_CONFIG['driver']['output_video'], wav_file, 'output.mp4')  # 将音频合成到唇形视频
    os.remove(wav_file)  # 删除临时的音频文件
    print('视频生成完毕')
