# -*- coding: utf-8 -*-
"""Episode: 失恋
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
def sc_longdrive(w: World):
    return w.scene("遠出",
            )

def sc_lookingaurora(w: World):
    return w.scene("オーロラが見えたなら",
            )

def sc_confession(w: World):
    return w.scene("告白",
            )

## episode
def ep_heartbreak(w: World):
    return w.episode("失恋",
            ## NOTE
            sc_longdrive(w),
            sc_lookingaurora(w),
            sc_confession(w),
            )
