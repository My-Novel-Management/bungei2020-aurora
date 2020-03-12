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
    robber, shopper = W(w.robber), W(w.shopper)
    oldlady = W(w.oldlady)
    sky = W(w.sky)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("神に感謝する",
            w.comment("冒頭は空の描写。特に色調に何か違和感を持たせる"),
            w.comment("ミッドサマーを終えて、まだその余韻が残る街中"),
            w.comment("舞台が日本ではない、ということを端的に分からせる＝看板の文字など"),
            w.comment("日本と逆で、右側通行、左ハンドルが主流"),
            sky.look("夏の空。雲がほとんどなく、一匹の鳥もいない"),
            w.eventStart("電子世界"),
            w.eventPoint("電子世界", "オブジェクトの数が減らされている"),
            w.comment("タンペレは湖畔工業都市。北欧の夏と分かるように"),
            nocht.come("自転車に乗っている"),
            outside.look("＜街の様子＞"),
            _.look("半裸のおじさんが歩いたりしていて、実に夏っぽい"),
            nocht.think("風を感じつつつ"),
            nocht.do("空を見上げて、オーロラの季節が待ち遠しい"),
            nocht.do("お金を下ろそうとコンビニに入る"),
            robber.be(),
            shopper.be(),
            oldlady.be(),
            robber.talk("おい！　さっさとしろ！"),
            robber.look("目出し帽を被り、手にライフルを持った大柄な男"),
            oldlady.do("人質に取られている"),
            nocht.do("人生に絶望した強盗が、ライフルを手に老婆を人質にとって金を取ろうとしている"),
            nocht.do("それを見て、神に祈り、駆け出して強盗に襲いかかる"),
            _.do("もみ合いになり、銃声が響いた"),
            w.comment("ここで$nochtの人となりを多少とも分かってもらう。何故そんな無謀をするのか、と疑問も持たせる"),
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
