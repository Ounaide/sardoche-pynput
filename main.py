# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:25:37 2022

@author: Ounaide
"""

from pynput.keyboard import Controller, Listener, Key
from keyboard import add_abbreviation, unhook_all


k=Controller()

d = {
     "buy_mr":"마방템 사",
     "buy_antiheal":"치감 사",
     "buy_armor":"방템 사",
     "i_need_reset":"집가야해",
     "wait_for_me_please":"나 기다려줘",
     "Im_strong":"나 엄청 쌤",
     "go_drake":"용 ㄱㄱ",
     "lets_end":"끝내자",
     "go_baron":"바론 ㄱㄱ",
     "lets_group":"모이자",
     "careful":"조심해",
     "winnable":"이길수있어",
     "my_bad":"미안",
     "nice":"나이스"
     }

def on_press(key):
    if key == Key.esc:
        unhook_all()
        l.stop()

def ab():
    for exp in d.keys():
        add_abbreviation(exp,d[exp],match_suffix=True,timeout=0.5)
    
if __name__=="__main__":
    ab()
    
    with Listener(on_press=on_press) as l:
        l.join()
