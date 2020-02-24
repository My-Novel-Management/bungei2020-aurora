# -*- coding: utf-8 -*-
"""Episode: 彼女の空
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
def sc_herworld(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("彼女の世界",
            ## NOTE
            ##  アサヒの世界の事情
            camera=w.asahi,
            area=w.Tokyo,
            stage=w.on_labo,
            day=w.in_stoplabo, time=w.at_afternoon,
            )

def sc_nocht(w: World):
    return w.scene("ノクト",
            ## NOTE
            ##  ノクトについて興味を持ち、観察
            ##  やがてコンタクトを取るようになった
            ##  しかしある日、残酷な宣告がなされる
            )

def sc_shutdown(w: World):
    return w.scene("シャットダウンする日",
            ## NOTE
            ##  その日、世界は停止する
            )

## episode
def ep_hersky(w: World):
    return w.episode("彼女の空",
            ## NOTE
            sc_herworld(w),
            sc_nocht(w),
            sc_shutdown(w),
            )
