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
from src.c1_green.e1_robber import ep_conveni_robber
from src.c1_green.e2_praygod import ep_pray_god
from src.c1_green.e3_gamemaker import ep_gamemaker
from src.c1_green.e4_asahi import ep_asahi

## defines
W = Writer
_ = W.getWho()


## main
def ch_green(w: World):
    return w.chapter("１．天色の風",
            ep_conveni_robber(w),
            ep_pray_god(w),
            ep_gamemaker(w),
            ep_asahi(w),
            ## NOTE
            ##  - コンビニ強盗を取り押さえようとして撃たれるノクトだが、彼は幸運にも死なずに済んだ
            ##  - 小さい頃から何かと幸運に助けられ、生きてきたノクトは、神のような存在を感じていた
            ##  - インディーズのゲームメーカーに勤めるノクトは趣味でCGをSNSに上げていた
            ##  - CGがきっかけで出会ったアサヒに、ノクトは惹かれていく
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
            note="小さい頃から何かと無茶をして、それでも不思議と死ななかった$nochtは、ある日、彼の趣味のＣＧを褒めてくれる女性$asahiとＳＮＳを通じて出会う")
