# -*- coding: utf-8 -*-
"""Episode: 3-2.ネット障害
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
def sc_overnight(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    mousa, irene, adonis = W(w.mousa), W(w.irene), W(w.adonis)
    return w.scene("泊まり込み",
            nocht.be("この日から最後の追い上げで泊まり込んでの作業が始まった"),
            _.do("誰もが文句を言いつつも、毛布を抱いてパーテーションで作った仮眠室で眠る"),
            mousa.come(),
            mousa.talk("あれで寝ると腰痛くなるんだ"),
            nocht.talk("横になって寝られるだけマシだろ"),
            irene.come(),
            irene.talk("喋ってないでさっさと手を動かして",
                "もう半月切ってるんだから"),
            nocht.talk("はいはい"),
            _.do("作業をする"),
            camera=w.nocht,
            stage=w.on_office_int,
            day=w.in_modifyfirst, time=w.at_afternoon,
            )

def sc_lastmodify(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    mousa, irene, adonis = W(w.mousa), W(w.irene), W(w.adonis)
    return w.scene("最後の修正作業",
            nocht.be("修正作業"),
            _.do("作業は大詰めを迎えていた"),
            _.do("デモプレイで見つかったバグを徹底的に潰していく",
                "CG班、システム班、関係なく、みんながデバッグに追われていた"),
            _.do("$Sは黙々と作業をしながら、彼女のことを考えていた"),
            _.think("今までその可能性に思い当たらなかったが、ひょっとしたら彼女の私生活で大きな変化があったのかも知れないということだ",
                "大切な家族が亡くなったり、事故にあったり、何か事件に巻き込まれたり",
                "そういう可能性を考え始めると、自分のつまらない物言いに対して彼女が愛想をつかしてしまった訳ではないかも知れないと思えてくる"),
            _.do("駄目だと思いつつも、久しぶりに彼女にメッセージを送る",
                "帰ってこない。でもそれは届いている",
                "まだつながっているんだと思えて、力が湧き上がってきた"),
            mousa.come(),
            mousa.talk("そっちはどうだ？"),
            nocht.talk("ああ、ここの変数を書き換えたら終わりだ"),
            nocht.do("コミットする"),
            _.do("サーバに上げて確認が終われば、再度ゲームをビルドし直して、チェックが始まる"),
            irene.talk("ビルドが終わるまで、少し休みましょうか"),
            nocht.do("$ireneの手には差し入れの$pullaだ"),
            nocht.do("みんながコーヒーを求めて席を立つ"),
            mousa.talk("あれ？"),
            nocht.talk("どうした？"),
            mousa.talk("いや、なんかサーバが止まってるな。とりあえず社内サーバは動いてるからそっちで大丈夫だろうけど"),
            day=w.in_modifylast, time=w.at_night,
            )

def sc_stop_ending(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    mousa, irene, adonis = W(w.mousa), W(w.irene), W(w.adonis)
    return w.scene("エンディングまで届かない",
            nocht.be("ゲームを進めていた"),
            _.do("ヘッドフォンをして集中していたが、何だか騒がしいな、とは思っている"),
            _.do("ラスボスを何とか撃破して、やっとエンディングが始まる"),
            _.do("画面にはバケモノになりはてた主人公が、その身を崩壊させていく",
                "そこに女神が降りてくる",
                "彼女により戦士の魂が救済されるという流れになっている、シナリオ上では"),
            _.do("その女神の姿は$Sの想像上の$asahiだった",
                "彼女の科学者然とした思考と、そこに時折垣間見える優しさ、情",
                "そういったものを何とか表現したつもりだった",
                "光のエフェクトが強すぎてよく見えないが、デザイナの演出案だから仕方ない"),
            _.talk("ん？"),
            _.do("画面がずっと光ったまま静止している"),
            _.think("バグか？　と思うが、自分以外にも同じ状況が発生しているらしい"),
            mousa.talk("なんだよ！"),
            nocht.do("$mousaが、声を上げた"),
            stage=w.on_office_int,
            day=w.in_lastday, time=w.at_morning,
            )

## episode
def ep_network_fault(w: World):
    return w.episode("3-2.ネット障害",
            sc_overnight(w),
            sc_lastmodify(w),
            sc_stop_ending(w),
            ## NOTE
            ##  - ゲームのマスタアップに向けて泊まり込みが続いていた
            ##  - しかしエンディングの確認をしている最中に障害が発生する
            note="大規模なネット障害が発生し、出来上がったゲームを登録できない事態になる。そんな中、$nochtは$asahiからのメッセージを受信した")
