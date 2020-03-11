# -*- coding: utf-8 -*-
"""Episode: 2-3.キャンプ場
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
def sc_longdrive(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("遠出",
            nocht.be("車でオーロラを見に出かけている"),
            nocht.do("フィンランドでは秋から冬にかけてはいつでもオーロラを見られる。ただ白夜がある十一月から二月が一番いい"),
            _.do("スマートフォンに地図を表示し、時折それを見ては行き先を確認する"),
            _.do("車にはキャンプ用品を詰んである"),
            _.do("休憩しながら$asahiとメッセージのやり取りをしている"),
            _.do("彼女の暮らす国の話を聞いていた"),
            asahi.voice("今の時期は外気汚染が酷くてね。埃でいっぱいだからみんな防護マスクをせずには外出できない"),
            nocht.do("聞いていた日本とは全然印象が違っていた"),
            nocht.talk("日本はもっと綺麗でゴミも落ちてないと聞いている"),
            asahi.voice("それは一部のレジャーランドだけじゃないかしら",
                "人間はどこでも、いつの時代でも、ゴミを道端に捨てる人は減らないわ",
                "だからロボットに掃除をさせることになるのよ"),
            nocht.talk("じゃあ君の会社が儲かる訳だ"),
            asahi.voice("儲けているのはうちじゃなくて、納入先よ",
                "$meたちは研究をしているだけ"),
            nocht.talk("それでも東京は車が自動で運転しているんだろう？"),
            asahi.voice("一部地域だけだし、それにタクシーとしてだから"),
            nocht.talk("それでもすごいさ。こっちじゃ考えられない。まだ五十年前のマニュアル車が現役で走っているんだから"),
            nocht.do("実際、レンタルできたのもかなり旧式のワゴンだ", "それでも問題ない",
                "動けばいい、というのが常識だった"),
            nocht.talk("じゃあドライブはしないのかい？"),
            asahi.voice("そんなことしてるの、カーレーサーくらいよ。趣味がなければ運転なんて必要ないもの"),
            nocht.think("ちょっとつまらない世界だと感じた"),
            camera=w.nocht,
            area=w.Tampere,
            stage=w.on_car_int,
            )

def sc_arrivedcamping(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("キャンプ場に到着",
            nocht.come("キャンプ場にやってくる"),
            _.do("テントを張り始める"),
            _.do("手慣れたもので、何度もイラストを描いたりする為に一人で出かけてはこうしてキャンプをしていた"),
            _.do("使い古された道具たちを並べる"),
            _.do("キャンプで楽しみにしているのが、普段はほとんど料理をしない$Sが自分で作るキャンプ飯だった"),
            _.do("チーズを足してインスタント麺で即席パスタを作る",
                "これがうまい"),
            _.do("端末で今日の天気予報を確認すると、あまり晴れそうにはなかった"),
            camera=w.nocht,
            stage=w.on_campsite,
            day=w.in_shorttrip, time=w.at_afternoon,
            )

def sc_asahitalk(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("アサヒと話す",
            w.comment("オーロラ観測では望遠鏡などは使わない。視野が狭くなるし１００キロ先なのであまり意味がない"),
            nocht.be("カメラの準備中"),
            nocht.do("端末にはアサヒとの文字の会話が流れていく"),
            asahi.voice("オーロラは日本でも見られるようだけれど、こっちで観測しようという人は研究者と物好きくらいなものよ"),
            nocht.talk("神秘的なものを、女性は好むんじゃないのかい？"),
            asahi.voice("確かにそういう向きはある",
                "でも$meはあまり興味を持たないわ"),
            nocht.talk("神や天使についても？"),
            asahi.voice("そういった存在を信じることは否定しない",
                "でも科学的じゃないわね"),
            nocht.talk("それは正しく科学者としての態度かも知れないが、なんというか、寂しいね"),
            asahi.voice("寂しいというのは感情の言葉よ",
                "感情は主観を生む",
                "でも、感情に頼れば判断を誤るわ"),
            nocht.talk("けど感情の判断が正しいってことだってあるだろう？"),
            _.do("組み立て終えると、熱いコーヒーを飲みながら一枚のイラストを描き始める"),
            asahi.voice("今度はどんな傾倒を描いているの？"),
            nocht.talk("アップするやつじゃないから、ごく普通の自然さ",
                "目に映ったものや、心が捉えたものだよ"),
            _.do("サンプルを送る"),
            asahi.voice("こういうの、もっと描けば良いのに"),
            nocht.think("彼女の印象がよかったことに驚く"),
            _.talk("どこが良いんだい？", "写真と同じじゃないか"),
            asahi.voice("こちらにはあなたの目に映る自然がもうないのよ",
                "普段目にしているのは金属やコンクリート、樹脂やガラス、作られた僅かな緑たちだけ"),
            nocht.talk("でもこれじゃあ、誰も喜ばない"),
            asahi.voice("今までの天使や女神は誰かが喜んでくれた？"),
            nocht.think("$asahiだけだったことを思い出す"),
            nocht.talk("それでも$meは自分の神を描きたいんだ"),
            time=w.at_afternoon,
            )

def sc_cannotlook(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    sky = W(w.sky)
    return w.scene("オーロラは見えず",
            nocht.be("夜になり起き出す"),
            _.do("外に出て"),
            _.do("空を見る"),
            sky.look("＜夜空の美しさ、ただし星はわずかで曇っている＞"),
            w.comment("フィンランドはどうやら摂氏でいいらしい"),
            nocht.do("見上げて、観測できそうにないなと思いつつ、それでも適当にカメラを向ける"),
            _.do("深夜ともなればマイナス二十度三十度になる",
                "防寒具に身を包みながら、手は既に震えている", "でもそれこそがオーロラ観測の醍醐味だった"),
            nocht.do("オーロラが見えるその瞬間を待ち、何度もテントと外を往復する"),
            _.do("端末ではずっと$asahiと対話を続けていたが、彼女はさっさと諦めた方が良いと言う"),
            _.explain("結局その日はオーロラを見ることはできなかった"),
            time=w.at_night,
            )

## episode
def ep_camping(w: World):
    return w.episode("2-3.キャンプ場",
            sc_arrivedcamping(w),
            sc_asahitalk(w),
            sc_cannotlook(w),
            ## NOTE
            ##  - キャンプ場にやってきて、オーロラ観測に備える
            ##  - 夜になるまで、準備をしながらアサヒと話す
            ##  - 夜、オーロラは見えない。見えたら、彼女に話す覚悟を決めていたのに
            note="キャンプ場に到着し、オーロラ観測に備える。しかし今までに見たことのない空模様と荒れる気候に、観測の可能性は断たれる")
