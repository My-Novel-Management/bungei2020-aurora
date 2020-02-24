# -*- coding: utf-8 -*-
"""Episode: 暗い空
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
def sc_nearwinter(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("冬が近づく",
            camera=w.nocht,
            area=w.Tampere,
            stage=w.on_street,
            day=w.in_autumnday, time=w.at_afternoon,
            )

def sc_hischildhood(w: World):
    return w.scene("小さい頃の話",
            )

def sc_godisexists(w: World):
    return w.scene("神はいるか",
            )

## episode
def ep_darksky(w: World):
    return w.episode("暗い空",
            ## NOTE
            sc_nearwinter(w),
            sc_hischildhood(w),
            sc_godisexists(w),
            )
