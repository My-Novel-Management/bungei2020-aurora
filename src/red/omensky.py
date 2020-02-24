# -*- coding: utf-8 -*-
"""Episode: 予兆
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
def sc_comewinter(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("冬の到来",
            camera=w.nocht,
            area=w.Tampere,
            stage=w.on_street,
            day=w.in_winterday, time=w.at_afternoon,
            )

def sc_desperation(w: World):
    return w.scene("自暴自棄",
            )

def sc_missingher(w: World):
    return w.scene("彼女はもういない",
            )

## episode
def ep_omen(w: World):
    return w.episode("崩壊の予兆",
            ## NOTE
            sc_comewinter(w),
            sc_desperation(w),
            sc_missingher(w),
            )
