# -*- coding: utf-8 -*-
"""Chapter: ノクス
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.red.lastday import ep_lastday
from src.red.omensky import ep_omen

## defines
W = Writer
_ = W.getWho()


## main
def ch_red(w: World):
    return w.chapter("赤の章",
            ## NOTE
            ##  冬になる
            ##  だが彼女と連絡が取れなくなり、自暴自棄になっていた
            ##  何度も死ぬ。でも死ねない。またやり直す
            ##  そしてある日、アサヒから連絡が来る
            ##  彼女はこの世界の滅びが近いと教えてくれる
            ##  さよなら、だと
            ##  ノクトはアサヒが日本ではなく、本当は空にいると気づいて飛び出す
            ##  叫ぶ。声の限り。彼女に届けと。空に。
            ##  その時、空には真っ赤なオーロラが開いた
            ep_omen(w),
            ep_lastday(w),
            )
