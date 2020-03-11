# -*- coding: utf-8 -*-
"""Episode: 2-4.失恋
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
def sc_lookingaurora(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("オーロラが見えたなら",
            nocht.be("キャンプ場"),
            nocht.do("夜になり、いよいよオーロラ観測と身構える"),
            _.do("端末を手に$asahiからのメッセージを見る"),
            asahi.voice("もうオーロラは見えた？"),
            nocht.talk("まだオーロラは見えないよ"),
            nocht.explain("この季節にしては珍しく小さな嵐がやってきて、空を覆って星すら見えない"),
            _.think("これは駄目だろうか、と諦めがち",
                "それでも$Sは心に決めていた",
                "オーロラが見えたなら、彼女に伝えようと"),
            asahi.voice("一つ聞きたいことがあったんだけど"),
            nocht.talk("何だい？"),
            asahi.voice("あなたは神の存在をどう思っているのか、ということ"),
            nocht.talk("日本人は無宗教なんだったっけ。そうだな",
                "見えないけれど、ずっと傍にいて、見守ってくれている。そんな存在を$meたちは神と呼んでいる"),
            asahi.voice("キリストのようなものではなく？"),
            nocht.talk("聖書の中の話は学者にでも任せておけばいいと思ってるけど、たぶんこの存在をそう呼んでいる人がいたとしても、その思いの中身は同じなんだ",
                "$meらは自分たちの傍に神がいて、その存在を感じているから安心して生きていられる",
                "自分が生きている、その支えとなっているものだ"),
            asahi.voice("全く論理的じゃないけれど、そういうものかも知れないわね"),
            nocht.talk("$asahiにはいないのかい？　君の神様"),
            asahi.voice("さあね"),
            nocht.explain("結局天候が悪く、オーロラ観察はできないまま、明け方を迎える"),
            stage=w.on_campsite,
            time=w.at_night,
            )

def sc_confession(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("告白",
            nocht.be("テントに戻っている"),
            _.do("結局オーロラは観測できず、帰り支度をしつつ端末で$asahiとやり取りをしていた"),
            w.comment("フィンランドと日本の時差は７時間"),
            nocht.do("既に東京はお昼だ",
                "今日の昼食は何を食べるつもりと送る"),
            asahi.voice("昼食は食べないことが多いわ", "ドリンクやサプリで済ませるつもり",
                "食べすぎると頭の働きが悪くなるし"),
            nocht.talk("全く日本人というのは勤勉すぎるよ",
                "食は人生の楽しみの一つじゃないか",
                "まあイギリスに次いで食べ物がまずいと言われるフィンランド人の$meが言えたもんじゃないか"),
            nocht.do("持ってきたパンを齧る", "温めた酒を少し"),
            nocht.do("新しいイラストについての意見を聞く"),
            asahi.voice("確かに今までとは作風が変わったわ",
                "でもね、一言でいうと今までのあなたらしさが薄くなった気がする"),
            nocht.talk("じゃあ以前の天使の絵の方が好み？"),
            asahi.voice("そうじゃない。ただね、最初に感じた神々しさがなくなって、それが今はもっと生身の人間性を持っていると言っているの",
                "上手とか下手じゃなくて、ふわっとしてものから、より生身になったというか。難しいわね。とにかく科学的じゃないけど"),
            nocht.talk("珍しいね、君がそんな風に言うのは。でも嬉しいよ",
                "$meは君に会ってからずっと、君のことを頭に思いながら描いているから"),
            asahi.voice("それじゃあこれはあなたの中の$meということかしら"),
            nocht.do("そこには半裸の女性がオーロラの下で物憂げに犬を見下ろしているＣＧイラストがあった"),
            nocht.talk("そうだと思う。ただ自信はないんだ。いつも何かに突き動かされるように描いているだけだから"),
            asahi.voice("でも今$meのことを考えていると言ったわ"),
            nocht.talk("それは常に考えているということだ。$asahi、聞いて欲しい", "$meは君が好きだ"),
            asahi.voice("もうお酒が入っているの？"),
            nocht.talk("今日はまだ飲んでない",
                "これは真面目な話なんだ"),
            nocht.do("信じようとしない彼女に、必死にその思いを伝える"),
            nocht.talk("君に褒められたあの日、$meはやっと出会えたと思った",
                "それまではバカにされるばかりだった自分を、やっと認めてくれる人が現れたんだと",
                "でもそれは勘違いだったと分かった",
                "認めてくれる人じゃなく、自分と向き合ってくれる人を探していたんだって",
                "それが君なんだよ、$asahi",
                "いつか君の住む日本に行きたい",
                "それに君にもこっちにきてもらって、一緒にオーロラが見たい",
                "君と愛し合いたいんだ"),
            asahi.voice("自分が何を言っているか分かっているの？"),
            nocht.talk("分かってる。ずっと言いたかったことなんだ",
                "この気持ちに答えてくれないだろうか？"),
            asahi.voice("ごめんなさい。$meは……あなたとは会えない"),
            nocht.do("彼女からの通信は途絶えた"),
            _.do("それから何度連絡しても、返信は返ってこなかった"),
            stage=w.on_lodge_ext,
            day=w.in_confession, time=w.at_earlymorning,
            )

## episode
def ep_heartbreak(w: World):
    return w.episode("2-4.失恋",
            sc_lookingaurora(w),
            sc_confession(w),
            ## NOTE
            ##  - オーロラの観測ができなかったが、ノクトはアサヒに今までの思いを伝える
            ##  - 思い切ってノクトはアサヒに思いを伝えた
            ##  - しかし彼女からは「ごめんなさい」という返事がきて、それ以降連絡が途絶えてしまった
            note="結局オーロラは見られず、それでも諦められずに$nochtは$asahiに告白をする。しかしその答えは")
