# -*- coding: utf-8 -*-
"""Episode: ゲーム
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
def sc_gameworld(w: World):
    return w.scene("ゲームの世界",
            )

def sc_hismind(w: World):
    return w.scene("本当に作りたいもの",
            )

def sc_launch(w: World):
    return w.scene("ゲーム発売を迎えて",
            )

## episode
def ep_game(w: World):
    return w.episode("ゲーム",
            ## NOTE
            sc_gameworld(w),
            sc_hismind(w),
            sc_launch(w),
            )
