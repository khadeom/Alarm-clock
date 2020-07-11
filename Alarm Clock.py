#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import winsound, time, os, platform

def Alarm():
    print('Alarm Clock'.center(os.get_terminal_size().columns))
    print('Enter Time :', end = '')
    hour, minute = map(int,input().split())
    ampm = input('am or pm :')
    
    if ampm.lower() == 'pm':
        hour += 12
    
    while True:
        if (hour == datetime.datetime.now().hour and
           minute == datetime.datetime.now().minute):
            print('Wake up')
            for i in range(5):                # Number of repeats
                for j in range(9):            # Number of beeps
                    winsound.MessageBeep(-1)  # Sound played  -1 for default window sound
                time.sleep(2)
            break
Alarm()


# In[ ]:




