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
from src.pink.hersky import ep_hersky

## defines
W = Writer
_ = W.getWho()


## main
def ch_pink(w: World):
    return w.chapter("紫の章",
            ## NOTE
            ##  場面が切り替わり、現代へ
            ##  その状況に陥る、少し前の話から
            ##  ラボの中で、アサヒが研究しているのは「量子コンピュータで模造した現実世界のシミュレーション」
            ##  それを用いた社会学研究データを集めていた
            ##  ある日、その生命体の中におかしな動きをするものを見つけた。自分の死を顧みないのだ
            ##  彼女はその個体に興味を持ち、やがてコンタクトをとるようになる
            ##  それがノクトだった
            ##  全てはシミュレーション中の出来事だ
            ##  しかし、アサヒにも最後宣告がくる
            ##  ラボを閉じると言われた
            ##  研究費を出していたところからの資金援助が打ち切られたのだ
            ##  別の競合他社の量子コンピュータが採用された
            ##  全てのデータを削除しなければならない
            ##  そこで、暴れているノクトを見つけた
            ##  彼は自分の存在に気づいていた
            ##  真っ赤なオーロラが襲う
            ##  消せない
            ##  彼の存在は、気持ちは、消せない。だがそんな彼女に、ある声が響いた
            ##  アサヒの世界もまた、別の量子シミュレーションだったのだ
            ep_hersky(w),
            )
