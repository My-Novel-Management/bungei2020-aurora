# -*- coding: utf-8 -*-
"""Episode: 離れていても
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## define alias
W = Writer
_ = W.getWho()


## scenes
def sc_programmer(w: World):
    return w.scene("プログラムな日々",
            )

def sc_bothdistance(w: World):
    return w.scene("二人の距離は",
            )

def sc_secretthought(w: World):
    return w.scene("秘めた想い",
            )

## episode
def ep_distance(w: World):
    return w.episode("離れていても",
            ## NOTE
            sc_programmer(w),
            sc_secretthought(w),
            sc_bothdistance(w),
            )
