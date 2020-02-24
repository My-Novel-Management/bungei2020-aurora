# -*- coding: utf-8 -*-
"""Episode: 神と彼女
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
def sc_thanksgod(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("神に感謝する",
            camera=w.nocht,
            area=w.Tampere,
            stage=w.on_office,
            day=w.in_winterday, time=w.at_afternoon,
            )

def sc_praygod(w: World):
    return w.scene("神に祈る",
            )

def sc_mygirlfriend(w: World):
    return w.scene("彼の彼女",
            )

## episode
def ep_god_and_her(w: World):
    return w.episode("神と彼女",
            ## NOTE
            sc_thanksgod(w),
            sc_praygod(w),
            sc_mygirlfriend(w),
            )
