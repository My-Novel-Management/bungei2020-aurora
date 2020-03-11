# -*- coding: utf-8 -*-
"""Episode: 3-3.赤い空
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
def sc_hermessage(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    irene, mousa = W(w.irene), W(w.mousa)
    return w.scene("彼女の最後のメッセージ",
            nocht.be("自分のデスクに向かっている"),
            mousa.be(),
            irene.be(),
            nocht.talk("一体どうなってる？"),
            nocht.do("画面ではエンディングで天使が降りてくるところで画面が止まり、動かない",
                "コンソールには意味不明の文字列が表示され、流れていく"),
            mousa.talk("よくわからんぞ", "急に障害だ", "こいつのバグって訳じゃない"),
            nocht.talk("さっぱりだ。そもそもこれは本当にバグなのか？"),
            nocht.do("すぐにSNSを確認する",
                "しかし繋がらない"),
            irene.talk("駄目。全然つながらない",
                "ちょっとサーバ会社に問い合わせてみるけど"),
            nocht.do("電話も繋がらない様子"),
            nocht.talk("物理的な断線の可能性もあります",
                "ちょっと見てくる"),
            nocht.do("部屋を出ていく"),
            _.do("と、そこで端末が鳴った",
                "妙だと思って見てみると、何の件名もない不審なメッセージ"),
            _.do("見るとそれは『さよなら』とだけ書かれていた",
                "すぐに彼女だと直感する"),
            nocht.talk("これは……君なのか？"),
            _.do("大きな地震、続いて遠くで雷鳴が轟いた"),
            _.go("飛び出す$S"),
            camera=w.nocht,
            stage=w.on_office_int,
            day=w.in_lastday, time=w.at_morning,
            )

def sc_redsky(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("真っ赤な空に",
            nocht.come("外に出てくる"),
            nocht.do("外の様子がおかしい。街の人間がいない"),
            nocht.talk("どうなってるんだ！"),
            _.explain("鳥が空中で止まっている",
                "車はブレーキをかけて傾いたまま",
                "全てが時を止めたように静止していた"),
            nocht.talk("何なんだ……"),
            _.do("見上げれば空はうっすらと赤く、そこにオーロラのような光の帯がゆらめている",
                "ただ$Sとそのオーロラだけが動いていた"),
            _.do("$Sは駆け出す",
                "どこかに彼女がいるんじゃないかと、どこかで見てくれているんじゃないかと、思って"),
            stage=w.on_street,
            )

def sc_crying(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("叫び",
            nocht.come("走っていた"),
            _.do("コンビニもスーパーも、バーも、全て人がいない、消えていく"),
            _.do("失意の中、教会へとやってきた$Sはドアを開けて中に入る"),
            _.talk("一体何が起こっているんだ？"),
            _.do("だがそこに神父はいない",
                "ただマリア像があるだけだ"),
            _.do("天井が、壁が、消えていく"),
            _.talk("なあ、$asahi、いるんだろ？",
                "君はどこかでこれを見ているんだろう？",
                "もうこの世界は終わりなのかも知れない",
                "けれどその前に、一つだけ君に伝えておかなければならないことがあるんだ"),
            _.do("$Sはずっと隠していた本当の気持ち、考えを、声にした"),
            _.talk("$meは、君を、愛している！"),
            stage=w.on_church,
            )

## episode
def ep_red_sky(w: World):
    return w.episode("3-3.赤い空",
            sc_hermessage(w),
            sc_redsky(w),
            sc_crying(w),
            ## NOTE
            ##  - 慌てて外に出たノクトが見たのは、静止する世界、消えゆく街、そして空には真っ赤なオーロラ
            ##  - 異常な世界を走り、自分以外が消えていく中で、そのオーロラの彼方に彼女を感じ、ノクトは叫ぶ
            note="彼女のメッセージに外に出た$nochtは、空に真っ赤なオーロラが現れ、街が消えていくのを目の当たりにする")
