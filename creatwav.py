#!/usr/bin/python
# -*- coding: utf-8 -*-
import wave
import numpy as np
import scipy.signal as signal

# 打开WAV文档
s = wave.open(r"wav/cartoon012.wav", "rb")

# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = s.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

# 读取波形数据
str_data = s.readframes(nframes)
s.close()

#将波形数据转换为数组
wave_data = np.fromstring(str_data, dtype=np.int8)
wave_data = wave_data.T * 2
print wave_data

time = np.arange(0, nframes) * (1.0 / framerate)

# 打开WAV文档
f = wave.open(r"wav/test.wav", "wb")

# 配置声道数、量化位数和取样频率
f.setnchannels(nchannels)
f.setsampwidth(sampwidth)
f.setframerate(framerate)
# 将wav_data转换为二进制数据写入文件
f.writeframes(wave_data.tostring())
f.close()

