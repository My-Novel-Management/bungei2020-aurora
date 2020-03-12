# -*- coding: utf-8 -*-
"""Episode: 3-1.予兆
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
def sc_comewinter(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("冬の到来",
            w.comment("季節が切り替わり、道端には雪のオブジェクトやスキン、テクスチャが溢れている。一気に冬に切り替わっている"),
            w.comment("フィンランドの初雪は朝９時の積雪が１ｃｍ以上。早いと$Rovaniemiで９月中旬とかに降ることも。基本は十月に入ってから"),
            nocht.be(),
            outside.look("街を行き交う人の服装も冬服に切り替わり、雪が舞っている"),
            w.comment("必死に$asahiにメッセージを送るが、虚しさだけが募る"),
            nocht.do("歩いている"),
            _.do("手にはスマホ。それで情報を見ている"),
            _.do("空から雪が落ちてくるのを写真にして彼女に送る"),
            _.talk("いつかは君もこっちに来ればいい。フィンランドの冬はね、そっちとは違う"),
            _.do("返信は来ない"),
            _.talk("クソッ"),
            _.do("道端の缶を蹴り上げる。それが遠くに飛んで、消えた"),
            camera=w.nocht,
            area=w.Tampere,
            stage=w.on_street,
            day=w.in_winterday, time=w.at_afternoon,
            )

def sc_working(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    mousa, irene = W(w.mousa), W(w.irene)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("仕事やるしかない",
            nocht.be("不機嫌に仕事をしている"),
            inside.look("マスターアップも近くなり、作業が立て込んでいる。誰もが言葉少なに黙々と仕事をしている様",
                "大量に散らかっている机など"),
            mousa.come(),
            mousa.talk("なんか最近機嫌悪くないか"),
            nocht.talk("食事がまずい所為かもな"),
            mousa.talk("$meもよ、医者からビール減らせって言われちまってさ"),
            _.do("だがその手にはノンアルコールビールの缶"),
            nocht.talk("また仕事中に飲んでんのか？　$ireneに怒られるぞ"),
            mousa.talk("いいんだよ。どうせいつかはみんな死ぬんだ"),
            nocht.talk("命を大切にって母ちゃんから教わらなかったか？"),
            mousa.talk("何番目の母ちゃんだ？"),
            nocht.think("$mousaは何度も両親が離婚再婚を繰り返していて、五人も母親がいるそうだ"),
            w.eventPoint("ネット障害", "やや遅かったり、とぎれとぎれだったりと何か変"),
            nocht.talk("それより、どうなってる、ネット対戦の方？"),
            mousa.talk("一応整備できたが……どうもな"),
            nocht.do("二人でローカルネットで対戦してみるが、ぎこちない"),
            _.talk("こりゃ駄目だな"),
            _.do("二人で苦笑"),
            stage=w.on_office_int,
            )

def sc_desperation(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    mousa, irene = W(w.mousa), W(w.irene)
    return w.scene("自暴自棄",
            w.comment("弱音を吐くところ。唯一、じっくりと他の人間と話すところだから、しっかり描写する"),
            nocht.be(),
            irene.be(),
            w.eventPoint("失恋", "$ireneに相談"),
            nocht.do("珍しく$ireneと飲みにきていた"),
            _.do("既に酔いが回り、ぐでぐでで愚痴る"),
            _.talk("なんで返事してくれないんだよ。こんなにも$meは好意を伝えているのにさ"),
            irene.talk("意外と女々しい男だったんだね、あんた"),
            nocht.talk("誰だってこうなりますよ。それだけ好きってことですからね"),
            irene.talk("個人のことはあまり関わらないようにしてるけど、仕事だけはしっかりしてくれよ"),
            nocht.talk("いないんすか？　$ireneは恋人はいないんすか！"),
            irene.talk("いるよ"),
            nocht.talk("自分が幸せだからそんな風に言えるんすよ"),
            irene.talk("相手がいたって幸せかどうかは分からんだろう",
                "そもそも結婚してくれって言われて困ってるんだ"),
            nocht.talk("結婚すればいいじゃないですか"),
            irene.talk("家庭を持つ気はない。あまり幸せな家庭でなかったものでな"),
            nocht.talk("$meなんか生まれた時からずっと孤独ですよ！", "孤児院だし、今だって孤独だ"),
            irene.talk("そうですか。で、いつになったら解放してくれるんだ？"),
            nocht.talk("もう一軒いきましょう"),
            irene.talk("勘弁してくれ"),
            stage=w.on_cafebar_int,
            )

def sc_missingher(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    irene = W(w.irene)
    return w.scene("彼女はもういない",
            nocht.be("タクシーから降りて一人で帰っている"),
            w.comment("$ireneに近所まで送ってもらった"),
            irene.be(),
            irene.talk("ちゃんと帰りなさいよ。明日は昼からでいいから"),
            nocht.talk("すみません"),
            irene.talk("いいのよ。じゃ、おやすみ"),
            irene.go("タクシーは行ってしまう"),
            nocht.do("泥酔している"),
            _.do("空を見上げれば綺麗な星空"),
            _.think("なぜ答えてくれないんだ"),
            _.talk("なんでなんだよ！"),
            _.explain("あの日以来、彼女との連絡は途絶えたまま、ずっと一方的にメールを送り続けている"),
            _.do("足元がもつれて道に転ぶ"),
            _.do("そこに車がやってくる"),
            _.do("強烈な光を見た"),
            w.comment("事故るが死なない"),
            stage=w.on_street,
            time=w.at_night,
            )

def sc_lonelypray(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    eru = W(w.erucco)
    return w.scene("寂しい祈り",
            eru.be(),
            nocht.come("入ってくる"),
            eru.talk("最近あまり来てませんでしたね"),
            nocht.talk("ああ、仕事が忙しくてね"),
            eru.talk("どうかしましたか？"),
            nocht.talk("神父はさ、女が突然連絡をしなくなったら何だと考える？"),
            eru.talk("普通は愛想をつかされたか、あなたが何かをしてしまって怒っているか、そんなところでしょうか"),
            nocht.talk("その可能性は考えた。でも違うんだ"),
            nocht.think("自暴自棄になり、何度も死のうとしたけれど、その度に不思議なことが起こった",
                "そこに何かを感じたのだ"),
            nocht.talk("なあ。神様はいると、神父はいつも言うよな"),
            eru.talk("信じるか信じないか、と言われれば、正直分かりません",
                "ただいないと断言するには心もとないし、何より、いつも彼の視線を感じるんです"),
            nocht.talk("それ、$meも感じてるやつだよ"),
            _.talk("生まれた日からずっと、ずっと感じてるやつだ！"),
            eru.talk("ならそれは、神と呼ぶかどうかは別として、あなたにとってとても大切な存在なのでは？"),
            nocht.talk("ああ、そうだよ。何か、勘違いしてたみたいだ。ありがとうな"),
            nocht.go(),
            stage=w.on_church_int,
            )
## episode
def ep_omen(w: World):
    return w.episode("3-1.予兆",
            sc_comewinter(w),
            sc_working(w),
            sc_desperation(w),
            sc_missingher(w),
            sc_lonelypray(w),
            ## NOTE
            ##  - 彼女と連絡が途絶えて傷心のノクト
            ##  - ゲームは発売日を間近に控えて制作が大詰めになっていた
            ##  - 返信がないのを分かりつつ、彼女にメッセージを送り続けるノクト
            note="$asahiと連絡が途絶えたまま、失意の中でマスタアップに向けて作業をする$nocht")
