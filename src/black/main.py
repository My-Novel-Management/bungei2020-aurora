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
from src.black.darksky import ep_darksky
from src.black.heartbreak import ep_heartbreak
from src.black.tvgame import ep_game

## defines
W = Writer
_ = W.getWho()


## main
def ch_black(w: World):
    return w.chapter("黒の章",
            ## NOTE
            ##  アサヒに会いたいと言ってしまう
            ##  だが返事は駄目だった
            ep_darksky(w),
            ep_game(w),
            ep_heartbreak(w),
            )
