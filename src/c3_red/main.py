# -*- coding: utf-8 -*-
"""Chapter: 3.ワインレッド
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.c3_red.e1_omensky import ep_omen
from src.c3_red.e2_netfault import ep_network_fault
from src.c3_red.e3_redsky import ep_red_sky

## defines
W = Writer
_ = W.getWho()


## main
def ch_red(w: World):
    return w.chapter("3.ワインレッドの帯",
            ep_omen(w),
            ep_network_fault(w),
            ep_red_sky(w),
            ## NOTE
            ##  - 彼女との連絡が途絶え、失意の中でゲームのマスタアップに向けて作業をする
            ##  - 作業も大詰めになったところで突然大規模なネット障害が発生する
            ##  - 彼女からメッセージが届き、外に出てみると空は真っ赤なオーロラが出現していた
            ##  冬になる
            ##  だが彼女と連絡が取れなくなり、自暴自棄になっていた
            ##  何度も死ぬ。でも死ねない。またやり直す
            ##  そしてある日、アサヒから連絡が来る
            ##  彼女はこの世界の滅びが近いと教えてくれる
            ##  さよなら、だと
            ##  ノクトはアサヒが日本ではなく、本当は空にいると気づいて飛び出す
            ##  叫ぶ。声の限り。彼女に届けと。空に。
            ##  その時、空には真っ赤なオーロラが開いた
            note="$asahiと連絡が途絶え、傷心の中、いよいよゲームのマスターアップの日を迎える。だがその最中、世界中でネット回線の異常が発生し、空にはオーロラが出現する")
