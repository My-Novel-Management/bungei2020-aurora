# -*- coding: utf-8 -*-
"""Episode: 約束
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
def sc_aboutaurora(w: World):
    return w.scene("オーロラについて",
            )

def sc_asahilife(w: World):
    return w.scene("彼女の暮らし",
            )

def sc_promiseher(w: World):
    return w.scene("彼女にオーロラを見る約束をした",
            )

## episode
def ep_promise(w: World):
    return w.episode("約束",
            ## NOTE
            sc_aboutaurora(w),
            sc_asahilife(w),
            sc_promiseher(w),
            )
