# -*- coding: utf-8 -*-
"""Episode: 2-1.小旅行
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
def sc_nearwinter(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    inside, outside = W(w.inside), W(w.outside)
    sky = W(w.sky)
    return w.scene("秋のある日",
            w.comment("秋の町中の空気感を"),
            nocht.be("外を歩いている"),
            _.do("街は徐々に秋めいて、そろそろオーロラが見られるなと思う"),
            sky.look("秋になりかけた空の映像。雲が流れていく"),
            outside.look("街を歩く人、車の様子"),
            w.eventPoint("電子世界", "オブジェクトが似たものが複数ある"),
            nocht.do("$asahiからのメッセージを受け取る"),
            _.explain("出会ってから半年ほどになるが、随分とフランクにやり取りするようになっていた"),
            camera=w.nocht,
            area=w.Tampere,
            stage=w.on_street,
            day=w.in_autumnday, time=w.at_midmorning,
            )

def sc_getshortvacation(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    mousa, irene, adonis = W(w.mousa), W(w.irene), W(w.adonis)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("小さな休暇を得る",
            w.comment("仕事の進捗具合が分かるように。ここではまだ慌ててる感じじゃないが、それでもずっと作業してきた、という風"),
            nocht.be("会社で仕事をしている"),
            inside.look("一旦プロトタイプができあがり、資料が山積みで、みんな疲れている風な"),
            irene.come(),
            irene.talk("どう、調子は？"),
            w.eventPoint("ゲーム制作", "新しいデザインの提案"),
            nocht.talk("これ見て下さいよ"),
            _.do("新しい敵のデザインだ",
                "今までのおどろおどろしさがなく、愛らしさがある"),
            irene.talk("かわいいけど、指示書にはなかったものよね"),
            nocht.talk("不気味なものしか登場しないんじゃ視覚的に飽きがくると思って"),
            irene.talk("確かにそうね。けど$adonisがまた怒るわよ"),
            nocht.talk("良いゲームにするためだと言ってやりますよ",
                "それに、こういう敵キャラがいてこそ、不気味さも際立つってもんですよ"),
            adonis.come(),
            adonis.talk("なんだこれは"),
            nocht.do("見つかった、という心境"),
            nocht.talk("趣味のCGだよ"),
            adonis.talk("また指示を無視して勝手なもの作ったんだろ？",
                "でも、こういうキャラが世界に存在するのは悪くないかも知れないな"),
            nocht.do("$ireneと目を合わせる"),
            adonis.talk("また少し書き直すよ", "もう三パターンほど作ってみてくれないか？"),
            nocht.talk("ああ、わかったよ"),
            _.do("珍しく自分の仕事が認められた気がして喜ぶ"),
            nocht.explain("そんな感じで仕事が進み、その日の午後、一旦$ireneに全員呼びつけられた"),
            irene.talk("実は$adonisとも話して、三日だけ、一斉休暇を出すことにしたわ",
                "流石にこれからの追い上げを考えたらここらで休んでおかないと持たないし"),
            nocht.do("みんな喜ぶ"),
            stage=w.on_office_int,
            time=w.at_afternoon,
            )

def sc_gototrip(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    mirei = W(w.mirei)
    inside = W(w.inside)
    return w.scene("旅行に行こう",
            nocht.be("バーにいた"),
            inside.look("店内の様子"),
            mirei.do("注文されたプレートとアルコールを持ってくる"),
            w.eventStart("$asahiにオーロラを見せる"),
            nocht.do("運ばれてきた食事を楽しみつつ、$asahiとメッセージのやり取りをする"),
            nocht.talk("そういえば$asahiはオーロラを見たことがないと言っていたね"),
            asahi.voice("日本で見える場所もあると聞いているけれど、特別それを観測する為に出かけようとは思わないわ",
                "研究をしている方がずっと楽しいもの"),
            nocht.talk("君は本当に仕事好きだね。日本人はみんなそうなのか？"),
            asahi.voice("あら、あなただって仕事が好きでしょ？"),
            nocht.talk("仕事よりも絵を書いたりCG創っている方がずっと有意義だよ",
                "それともあれで仕事になるだろうか？"),
            asahi.voice("どうでしょうね", "$meには美術の素養がないから"),
            nocht.talk("でも気に入ってくれたんだろう？"),
            asahi.voice("ええ、個人的には好きよ", "けどそれがお金になるかどうかは分からない",
                "専門家じゃないもの"),
            nocht.talk("金を出して買ってくれるのは専門家よりも一般のお客さんの方がずっと多いよ",
                "それこそ節税対策にするような高額な美術品でも描かない限りはね"),
            nocht.talk("そうだ",
                "折角休暇が出たんだからそれを利用して$asahiにオーロラを見せてあげるよ",
                "うん、それがいい"),
            _.do("すぐに食べ終えて、立ち上がる"),
            _.do("会計を済ませて、旅行の準備に取り掛かった"),
            stage=w.on_cafebar_int,
            time=w.at_evening,
            )

## episode
def ep_short_trip(w: World):
    return w.episode("2-1.小旅行",
            sc_nearwinter(w),
            sc_getshortvacation(w),
            sc_gototrip(w),
            ## NOTE
            ##  - 秋になるとオーロラが徐々に見える日が増える
            ##  - ゲーム開発に一段落つき、ノクトは数日休暇をもらえた
            ##  - アサヒにオーロラを見せるため、オーロラ観測の小旅行へと出かける
            note="秋になり、オーロラの季節が到来。開発に一段落つき、数日休みとなったので気分転換に観測小旅行へと出かけた")
