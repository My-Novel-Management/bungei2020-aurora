# -*- coding: utf-8 -*-
"""Main story.
"""
## path setting
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
## public libs
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## assets
from storybuilder.assets import basic, accessory
## local files
from src.c1_green.main import ch_green
from src.c2_black.main import ch_black
from src.c3_red.main import ch_red
from src.c4_pink.main import ch_pink
## settings
from config import PERSONS, AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS

## define alias
W = Writer
_ = Writer.getWho()


################################################################
# 章構成
#   1.緑の章：二人のなれそめ関係性職業、謎
#   2.黒の章：予兆、ノクトの不思議な人生
#   3.赤の章：世界の変貌と崩壊
#   4.紫の章：真実
################################################################

################################################################
#
# Sample step:
# 1) Create the world
#       世界を作成する。
# 2) Create a new chapter
#       章の作成。
# 3) Create a episode
#       エピソード作成。
# 4) Create a new scene
#       シーン作成。物語のベース。ここに様々なActionを追加する。
# 5) Create a new stage
#       舞台作成。シーンに必須要素
# 6) Create a new day and time
#       日時作成。シーンのサブ要素
# 7) Add a scene plot
#       シーンプロットの作成。概要のないシーンは原則使えない
# 8) Add scene actions
#       シーンアクションの追加。
#
################################################################


## main
def create_world():
    """Create a world.
    """
    w = World("オーロラの色を教えて")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.setAssets(accessory.ASSET)
    w.buildDB(PERSONS,
            AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    w.setBaseDate(2018)
    w.setBaseArea("Finland")
    # set persons
    # set stages
    # set block
    # set outline
    w.setOutline("ゲームプログラマで趣味でＣＧをやっている男性は、小さい頃から不思議と何かに助けられ、命を失わずにいられた。ある日、彼のＣＧを好きと言ってくれる女性が現れ、ネットを通じて心を通い合わせるようになるが")
    return w

def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ## NOTE
            ##  1. ノクス：緑の空
            ##  2. ノクス：黒い空
            ##  3. ノクス：赤い空
            ##  4. アサヒ：紫の空
            ch_green(w),
            ch_black(w),
            ch_red(w),
            ch_pink(w),
            )

if __name__ == '__main__':
    import sys
    sys.exit(main())

