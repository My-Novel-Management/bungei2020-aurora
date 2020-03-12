# -*- coding: utf-8 -*-
"""Episode: 2-2.暗い空
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
def sc_hischildhood(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("小さい頃の話",
            w.comment("この道中では特に$nochtの小さい頃の話に焦点を当てる。ここで不思議なことが起こっているのだと知らせる"),
            w.comment("向かう先は$Rovaniemi。バスで１１時間２５分程度"),
            nocht.be("バイクに荷物を積み、走っている"),
            _.explain("キャンプ用品を積み込んでいるので結構大きな荷物がある"),
            _.do("北部のラップランド地方を目指していた"),
            _.do("オーロラ観測をするならラップランドだ"),
            _.do("$asahiはオーロラをまだ見たことがないという",
                "そこで是非カメラで収めて彼女にも見せてあげようという心づもりだった"),
            _.do("ただ空模様はよくなく、天気予報も曇りだった"),
            w.comment("このパートの最後で事故った風に装う"),
            camera=w.nocht,
            stage=w.on_bike,
            day=w.in_shorttrip, time=w.at_midmorning,
            )

def sc_godisexists(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    shopper = W(w.shopper)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("神はいるか",
            w.comment("シーンに違和感を抱かせつつ、いきなり休憩シーンに飛ばすこと"),
            inside.look("ガソリンスタンドの様子を"),
            shopper.be(),
            shopper.look("簡単な店員の描写"),
            nocht.be("途中で店に立ち寄り休憩する"),
            _.do("コンビニ付きのガソリンスタンドで休む"),
            outside.look("森が広がる", "あまり人はいない", "ときどき道路を車が抜けていく"),
            nocht.do("端末を手に、片手にはパンで、$asahiとやり取りをする"),
            asahi.voice("そういえば以前、死にそうになったことがあると言っていたけど"),
            nocht.talk("ああ、そうだよ",
                "そして何度も助けられたんだ",
                "$asahiは神を信じるかい？"),
            asahi.voice("神という存在がいるかどうかを議論するつもりはないわ",
                "それでも、少なくともあなたは神を信じるべき立場でしょう？"),
            nocht.talk("$asahiにはないだろうか",
                "小さい頃から、何か大きな存在に自分が見守られている、と感じることが"),
            asahi.voice("何度も助けられているというのが、その神の仕業だとでも？"),
            nocht.talk("そこまでは言わないけれど、そういうことを感じたりしないか、という話"),
            asahi.voice("そうね。偶然七七という揃いの番号を見たり、たまたま購入した金額が揃っていたり、そういうのは何か大きな意志が働いているように感じるかも知れないわ",
                "でもそれはエンジェルナンバーと呼ばれる、ただの確証バイアスよ",
                "人間はね、自分に関係ある数字はよく覚えていて、それ以外のどうでもいい数字も同じように目撃しているはずなのに、よく見る数字のことだけを記憶として留めておくの",
                "奇跡の多く、偶然や運命と感じる物事の多くは、そういった捻じ曲げられた主観によるものなのよ"),
            nocht.do("彼女はどうやら神の存在よりも、$Sが本当にただ運良く生き延びているだけだと主張したいようだった"),
            nocht.talk("そろそろ出る", "また途中の休憩で続きを話そう"),
            nocht.do("ガソリンを給油したバイクで走り出す",
                "車もほとんど通らず、どこまでも真っ直ぐに道が伸びていた"),
            stage=w.on_conveni,
            )

## episode
def ep_darksky(w: World):
    return w.episode("2-2.暗い空",
            sc_hischildhood(w),
            sc_godisexists(w),
            ## NOTE
            ##  - バイクでキャンプ場へと向かう
            ##  - 途中休憩を取る。彼女はノクトが小さい頃から不思議な体験をしていることについて、興味を持っていた
            note="キャンプ場を目指してバイクで走っていた。途中で休憩を取り、$asahiの生活について少し深く知ろうと質問をする")
