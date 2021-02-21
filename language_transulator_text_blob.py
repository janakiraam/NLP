# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 21:22:04 2021

@author: I340968
"""

from textblob import TextBlob
word = TextBlob('வணக்கம்')
wordl = word.translate(from_lang='ta',to='en')
print(wordl)

word = TextBlob('Hello')
wordl = word.translate(from_lang='en',to='ta')
print(wordl)