# -*- coding: utf-8 -*-
"""Chapter: 2.暗灰色
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.c2_black.e1_shorttrip import ep_short_trip
from src.c2_black.e2_darksky import ep_darksky
from src.c2_black.e3_camping import ep_camping
from src.c2_black.e4_heartbreak import ep_heartbreak

## defines
W = Writer
_ = W.getWho()


## main
def ch_black(w: World):
    return w.chapter("2.暗灰色の森",
            ep_short_trip(w),
            ep_darksky(w),
            ep_camping(w),
            ep_heartbreak(w),
            ## NOTE
            ##  - 一旦開発が落ち着いたことで数日休暇が出て、オーロラ観測に小旅行に出かける
            ##  - 道中、今までは訊けなかった彼女に関することを、色々と尋ねる
            ##  - キャンプ地に到着し、観測に備える。しかしオーロラが見えるような気象ではなかった
            ##  - 思い切って彼女に思いを伝えるノクト。しかしそこで待っていた彼女の答えは
            ##  アサヒに会いたいと言ってしまう
            ##  だが返事は駄目だった
            note="秋になり、オーロラの季節が到来する。$nochtは日に日に高まる$asahiへの思いを遂に伝えるのだが")
