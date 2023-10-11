from voice_main import call_for_voice
from threading import *
from hand_main import call_for_gesture

t1=Thread(target=call_for_voice)
t2=Thread(target=call_for_gesture)
t1.start()
print('T1 started')
t2.start()
print('T2 started')

t1.join()
print('T1 ended')
t2.join()
print('T2 ended')