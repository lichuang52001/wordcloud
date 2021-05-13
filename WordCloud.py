# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:38:37 2021

@author: www.lichuang.me
"""


import jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def trans_ch(txt):
  words = jieba.lcut(txt)
  newtxt = ''.join(words)
  return newtxt

f = open('ciyun.txt','r',encoding = 'utf-8')     # import text
txt = f.read()
f.close
txt = trans_ch(txt)
mask = np.array(Image.open("airplane.png"))               # background airplane
# mask = np.array(Image.open("Hanzi.png"))               # background Hanzi

wordcloud = WordCloud(background_color="white",\
                      width = 1920,\
                      height = 1080,\
                      max_words = 200,\
                      max_font_size = 80,\
                      mask = mask,\
                      contour_width = 4,\
                      contour_color = 'steelblue',\
                      font_path =  "FZZKFW.ttf"    # save font file in the same folder
                      ).generate(txt)

wordcloud.to_file('wordcloud.eps')

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
# plt.savefig('file_name.eps')
