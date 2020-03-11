# -*- coding: utf-8 -*-
"""Episode: 1-2.神に祈る
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
def sc_praygod(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    erucco = W(w.erucco)
    return w.scene("神に祈る",
            nocht.come("朝もやを割って、教会に入ってくる$S"),
            erucco.talk("聞きましたよ。また危ないことに首を突っ込んだそうですね"),
            nocht.talk("人助けをした人間に、それはないだろう？"),
            erucco.talk("自分の命を粗末にする人間にはいつかしっぺ返しがきますから"),
            _.talk("それより、今日は？"),
            nocht.talk("時間がないのでお祈りだけで"),
            nocht.do("いつも小さな懺悔というか、愚痴を聞いてもらっていた"),
            nocht.do("神を前にひざまずく。祈る"),
            nocht.do("しばし心の中に、いつもの存在を思い浮かべる"),
            nocht.do("銃で撃たれた。けれど致命傷にはならなかった",
                "それを運が良かったという人もいるだろう",
                "けれど$Sは思うのだ",
                "自分は守られていると",
                "なぜならずっと小さな頃から、何度も死にそうになりながらも、今まだ生きている、生きていられるからだ"),
            erucco.talk("そういえば、どうなんです、その後、あの彼女とは？　もう会ったんですか？"),
            nocht.talk("東京まではなかなか足が伸ばせないさ",
                "それに、向こうがどう思っているか分からない"),
            erucco.talk("人助けには積極的なのに、自分の気持ちには臆病なんですね"),
            nocht.talk("そういうんじゃないよ。ただ彼女は、ちょっと特別なんだ"),
            stage=w.on_church_int,
            time=w.at_morning,
            )

def sc_mygirlfriend(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("彼の彼女",
            nocht.be("自転車に乗っている"),
            nocht.do("心地良い風を感じながら、街を走る",
                "角を勢い良く曲がり、知らない人間に挨拶をして驚かれる"),
            nocht.think("朝一でもらった彼女からの返信でテンションが上がっていた"),
            nocht.do("最初は一週間に一度くらいのやり取りだったものが、最近は日をおかずに返信が来るようになっていた",
                "いつもSNSに上げた趣味のグラフィックに関しての意見や、時折ちょっとした発言への疑問や意見、そんなものだったが、",
                "今朝は珍しく絵を褒めてくれていたので嬉しかった"),
            nocht.do("今朝のやり取りを思い返す"),
            nocht.talk("それじゃあ、例えばあれをプリントアウトしたら$asahiの部屋に飾ってくれるのか？"),
            asahi.voice("大きなものは困るけど、今住んでいるマンションは殺風景だから、ちょっとあると助かるかもね",
                "いつものような宗教画ではなくて、こういったごくありふれた風景画も書けるのね"),
            nocht.talk("あれも$meの思考の延長だよ",
                "雲の中に女神がいただろう？"),
            asahi.voice("ああいった何気ないくらいのものは良いのよ",
                "ほら、あなたが普段アップしているものって、こう、もっと神々しく目立っているでしょう？"),
            nocht.talk("そりゃあ絵の主題は目立たせなきゃ"),
            asahi.voice("何でも目立つことが一番、とは思わないことよ"),
            nocht.talk("$asahiはそういうのは嫌いかい？"),
            asahi.voice("好き嫌いではなくて、バランスの問題",
                "バランスというのを壊してまで何かを中心にするという醜悪さが苦手なだけよ"),
            nocht.explain("彼女とはいつもこんなやり取りをする",
                "それが楽しい",
                "やがてその中身、いや、女性として興味を持つようになるのも当然だった"),
            stage=w.on_street,
            )

## episode
def ep_pray_god(w: World):
    return w.episode("1-2.神に祈る",
            sc_praygod(w),
            sc_mygirlfriend(w),
            ## NOTE
            note="小さい頃から死にそうなところを幸運に救われていた。$nochtは何かある度に教会を訪れ、祈っていた")
