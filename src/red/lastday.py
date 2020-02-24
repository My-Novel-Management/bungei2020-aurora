# -*- coding: utf-8 -*-
"""Episode: 最後の日
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
def sc_worldincident(w: World):
    return w.scene("世界の異変",
            )

def sc_hermessage(w: World):
    return w.scene("彼女の最後のメッセージ",
            )

def sc_sheis(w: World):
    return w.scene("彼女は存在する",
            )

def sc_redsky(w: World):
    return w.scene("真っ赤な空に",
            )

## episode
def ep_lastday(w: World):
    return w.episode("最後の日",
            ## NOTE
            sc_worldincident(w),
            sc_hermessage(w),
            sc_sheis(w),
            sc_redsky(w),
            )
