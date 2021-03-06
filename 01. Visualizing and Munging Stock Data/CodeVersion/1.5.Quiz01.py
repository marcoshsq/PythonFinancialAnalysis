# -*- coding: utf-8 -*-
"""Quiz 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yK_4mAiYgM0V9CmcTTixV46jLHHpITJf

### Quiz 1
"""

Question 01 - Which of the following library has DataFrame object?
# answer: Pandas

Question 2 - Which of the following is the correct way to import a library, eg Pandas?
# answer: import pandas as pd

Question 3 - What is the method of DataFrame object to import a csv file?
# answer: from_csv()

Question 4 - Which of the following attributes of a DataFrame return a list of column names of this DataFrame?
# answer: columns

Question 5 - Which of the following can slice ‘Close’ from ‘2015-01-01’ to 
‘2016-12-31’ from data, which is a DataFrame object?
# answer: data.loc[‘2015-01-01’:’2016-12-31’, ‘Close’]

Question 6 - What is the method of DataFrame to plot a line chart?
# answer: plot()

Question 7 - Suppose you have a DataFrame - data,  which contains columns ‘Open’, ‘High’, 
‘Low’, ‘Close’, ‘Adj Close’ and ‘Volume’. What does data[[‘Open’, ‘Low’]] return?
# answer: Columns ‘Open’ and ‘Low’ 

Question 8 - Suppose you have a DataFrame ms , which contains the daily data 
of  ‘Open’, ‘High’, ‘Low’, ‘Close’, ‘Adj Close’ and ‘Volume’ of Microsoft's stock.

Which of the following syntax calculates the Price difference, 
(ie ‘Close’ of tomorrow – ‘Close’ of today)?
# answer: ms[‘Close’].shift(1) – ms[‘Close’].shift(1)

Question 9 - Suppose you have a DataFrame - ms , which contains the daily data
of  ‘Open’, ‘High’, ‘Low’, ‘Close’, ‘Adj Close’ and ‘Volumn’ of Microsoft's stock.
What is the method of DataFrame to calculate the 60 days moving average?
# answer: rolling(60).mean()  

Question 10 - Which of the following idea(s) is/are correct to the simple trading strategy that we introduced in the lecture video?

# answer: a) If fast signal is larger than slow signal, this indicates an upward trend at the current moment;
# b) Use longer moving average as slow signal and shorter moving average as fast signal.