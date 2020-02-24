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
from src.green.distance import ep_distance
from src.green.god_and_her import ep_god_and_her
from src.green.promise import ep_promise

## defines
W = Writer
_ = W.getWho()


## main
def ch_green(w: World):
    return w.chapter("緑の章",
            ## NOTE
            ##  空の話
            ##  オーロラの話
            ##  人助けをするノクト（実はここで一度死んでいる）
            ##  何故か神様が助けてくれるんだ
            ##  教会でお祈りと告白
            ##  仕事はSE、ゲームの世界で沢山人殺しをする遊具を作る
            ##  趣味でグラフィックを
            ##  それに興味を持ってくれたアサヒという日本人女性がいた
            ##  彼女は神を信じない。日本人はそういうものらしい
            ##  徐々にアサヒに惹かれていく
            ##  その彼女に、一緒にオーロラを見ようと約束をした
            ep_god_and_her(w),
            ep_distance(w),
            ep_promise(w),
            )
