# -*- coding: utf-8 -*-
"""Episode: 4-2.停止と終わり
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
def sc_stop_project(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    yoshi = W(w.yoshi)
    return w.scene("プロジェクト停止",
            w.comment("会社にくるところから始めて、空の様子を描いておく。ちょっと奇妙だな、と"),
            asahi.be("じっとモニタを見てデータを集めている"),
            _.hear("空調の音"),
            _.do("$nochtに言われたように、自分でノートに絵を描いてみる",
                "だが彼のようには上手く描けない"),
            asahi.talk("何しているんだろう", "データに影響されるのはどうかしてるわ"),
            _.do("それでもモニタ上で明滅する点が、星の息吹のようで、見ているとそれが生命体にも思えてくる"),
            yoshi.come("慌てた様子で入ってきて"),
            asahi.talk("忘れ物ですか？"),
            yoshi.talk("急なことだが、今すぐ実験を中止してくれ"),
            asahi.talk("え？"),
            yoshi.talk("プロジェクトは中止だ",
                "データも全部破棄するよう要請があった"),
            asahi.talk("そんな。急に"),
            yoshi.talk("たぶんこの前の経営統合の破断の影響だろう",
                "ここの研究所を売り払うつもりなのかもしれん",
                "とにかくデータは破棄、全て削除だ"),
            yoshi.go("慌ただしく出ていく"),
            time=w.at_night,
            )

def sc_delete_and_message(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    yoshi = W(w.yoshi)
    return w.scene("削除とメッセージ",
            asahi.be("データ削除のプログラムを動かしている"),
            asahi.do("画面上ではひたすらメッセージが出て、データ削除が進んでいることを示している",
                "削除され、ただのゼロに戻るデータ",
                "蓄積もプログラムも全てが最終的にはなくなる",
                "デジタルは無情だ"),
            asahi.do("それと同時並行して、最後のシミュレーションプログラムを走らせる",
                "まだ、彼だけは消す決心がつかないでいた"),
            asahi.do("世界で彼だけの街が精巧に作られている"),
            ## NOTE
            ##  その日、世界は停止する
            day=w.in_stoplabo, time=w.at_midmorning,
            )

def sc_stop_del(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    yoshi = W(w.yoshi)
    god = W(w.god)
    return w.scene("削除の停止を",
            w.comment("ここでリンクする。$nochtのラストと$asahiのラストが重なり、二人の気持ちも重なる。しかしそれもまた誰かにとっては単なるデータでしかない、という結末"),
            asahi.be(),
            asahi.talk("$nocht？"),
            asahi.do("画面の中で必死に明滅する点があった",
                "それが彼だと分かり、$Sは慌ててそこを映像化する"),
            _.do("画面にポリゴンで表現された街の交差点と、一人の人間の男性が浮かび、ウインドウに彼が何を喋っているかが表示される"),
            nocht.voice("$asahi！　そこにいるんだろ？",
                "君が何者かは分からない。けど、ずっと$meを助けてくれていた",
                "その存在が君だって$meは分かっている",
                "だから答えてくれなくていい",
                "聞いてくれるだけでいい",
                "$meは、ずっと、君のことを、愛している！",
                "たとえこの世界が消え去っても、この体が消えても、この思いは消えない！", "それが愛なんだ！"),
            asahi.talk("$nocht……"),
            _.think("それはただのデータのはずだ",
                "分かっているし、何度も自分に言い聞かせてきたのに、どうしようもなく心が動く"),
            asahi.talk("ごめんなさい。$nocht",
                "$meは"),
            nocht.voice("$asahi！"),
            asahi.do("画面で何度も彼が叫ぶ",
                "自分の名を呼び、愛を伝える"),
            _.do("それを目にして、$Sは端末の割り込み操作を行う",
                "データの削除を止めるためだ"),
            asahi.talk("待ってて。今、助けるから",
                "今までのように$meがあなたを！"),
            _.do("しかしデータ削除プログラムは止まらない"),
            asahi.talk("なんで？　どうして？"),
            _.do("慌てて量子コンピュータをシャットダウンしようとするが立ち上がった瞬間、何かの切れる音がした"),
            god.voice("どうやら実験は失敗だったようだ"),
            asahi.hear("それはどこか別の世界から響く声のようだった"),
            _.voice("やはり感情を回路に組み込んだのが失敗の要因だろう",
                "感情など不要なのだ",
                "判断を誤らせる"),
            asahi.do("真っ暗になり、目の前からモニタも機器も消え、壁も天井も消える"),
            _.do("彼女の体が緑の光に分解されていく"),
            _.do("世界には緑色の光の帯が揺れた"),
            )

## episode
def ep_stop_and_end(w: World):
    return w.episode("4-2.停止と終わり",
            sc_stop_project(w),
            sc_delete_and_message(w),
            sc_stop_del(w),
            ## NOTE
            ##  - 上司に突然プロジェクトの終了とデータの全削除を言い渡される
            ##  - データ削除作業をしながらアサヒはノクトへの気持ちを断ち切れず、最後のメッセージを送る
            ##  - ノクトが自分の存在に気づいたことを確認し、削除を止めようとするが
            note="上司からプロジェクトの終了と全てのデータ削除を言い渡され、苦悩の中で彼女はある選択をする")
