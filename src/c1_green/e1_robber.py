# -*- coding: utf-8 -*-
"""Episode: 1-1.コンビニ強盗
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
# NOTE
#   冒頭は人助けをして死ぬところから
def sc_thanksgod(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("神に感謝する",
            nocht.come("歩いている"),
            nocht.do("空を見上げ、そろそろオーロラの季節だと考える"),
            nocht.do("コンビニに入る"),
            nocht.do("人生に絶望した強盗が、ライフルを手に老婆を人質にとって金を取ろうとしている"),
            nocht.do("駆け出して襲いかかる"),
            _.do("もみ合いになり、銃声が響いた"),
            ## NOTE
            ##  フィンランドであることが分かるように
            ##  人助けして、死ぬ、ということがすぐ想像しやすいイベント
            ##  ノクトの人柄が分かるもの
            camera=w.nocht,
            area=w.Tampere,
            stage=w.on_office,
            day=w.in_summerday, time=w.at_afternoon,
            )

## episode
def ep_conveni_robber(w: World):
    return w.episode("1-1.コンビニ強盗",
            ## NOTE
            sc_thanksgod(w),
            note="仕事に向かう途中で、コンビニ強盗に遭遇し、$nochtはそれを取り押さえようとしてライフルで撃たれてしまった")
