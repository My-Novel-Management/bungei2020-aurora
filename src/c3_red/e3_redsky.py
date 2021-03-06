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
            nocht.be("#自分のデスクに向かっている"),
            mousa.be(),
            irene.be(),
            nocht.talk("またバグか？"),
            nocht.do("不機嫌に椅子でふんぞり返り眉を寄せている$mousaの大きな腹の前に並ぶ四台のモニタ全てが、$Sのものと同じように強烈に発光し、とても見られたものじゃなくなっていた"),
            mousa.talk("やっと今からエンディングだってところでこのザマだよ",
                "どいつか知らねえが何を間違えて打ち込んだらこんなことになるんだ？"),
            nocht.do("$mousaは完全にバグを疑っているようだが$Sはただのバグにしては状況そのものがおかしいと感じていた",
                "そもそも全てのモニタが同じように光ったままフリーズするなんてことはあり得ない",
                "オンライン対戦中ならまだしも、それぞれが別の場面の確認中だったはずだ"),
            nocht.talk("中断処理も受け付けない？"),
            mousa.talk("何やっても無駄だぜ", "そもそもそれ、既にコンセントも抜いてあるから", "さっぱりだ"),
            mousa.do("お手上げと口にして$Sは両掌を見せて目を閉じる",
                "モニタのプラグもコンセントも床で繋がりを失い、だらりと寝そべっている",
                "バッテリィのないモニタが光っているのはそれこそ雷でも落ちて過電流が流れているとしか思えない"),
            nocht.do("と、画面にコンソールが出現し、意味をなさない英数字の羅列が表示される", "それが滝のように流れ、作業中の誰もが不気味だと声を上げた"),
            nocht.talk("これはバグじゃない"),
            nocht.do("$Sは端末を手にし、すぐにＳＮＳを確認する",
                "しかし繋がらない", "ブラウザも回線を見つけられないと嘆いている"),
            nocht.talk("駄目だな", "全部繋がらない", "電話も……無理だ",
                "今日何かあるって言ってたか？"),
            mousa.talk("何があったらこんな大規模電波障害が起こるってんだ？"),
            nocht.think("確かに$mousaの言う通りだ",
                "なら一体目の前で起こっている現象をどう説明すれば良いだろう"),
            irene.talk("ねえ、このバグなに？"),
            _.do("$Sが困った様子でやってくる", "既にここ連日の疲労で目の隈が酷かったし、後ろにまとめている髪の一部が解けてしまっていたが、",
                "それを気にしている余裕はないようだ"),
            nocht.talk("分かりません",
                "ただプログラムの方じゃなく、どうも電子機器そのものの障害みたいで"),
            _.do("そう答え、何も繋がらない自分の端末を彼女に見せた",
                "$ireneは腕組みをして目を伏せると「で、解決策は？」といつもの口調で尋ねる"),
            mousa.talk("何もできねえんで、とりあえず待つしかないんじゃねえの？"),
            nocht.talk("$meも$mousaの言う通りだと思うんですが"),
            _.do("冷静に考えればそれ以外に解法は無さそうなのに、頭のどこかで警告音が鳴ってしまう"),
            nocht.talk("ちょっと外、見てきます"),
            irene.talk("$nocht？"),
            nocht.do("$ireneの疑問の声を背に、$Sは部屋を出る"),
            _.do("と、そこで端末が鳴った", "アラームでも掛けておいただろうかと液晶を見るとメッセージの受信通知だ",
                "画面をタップする",
                "メッセージは宛名も件名もなく、ただ『さよなら』とだけ書かれていた",
                "さよなら、というニホン語は別れの言葉だ"),
            nocht.talk("君なのか？"),
            _.do("大きく廊下が揺れ、続いて遠くで雷鳴が轟いた"),
            _.go("#飛び出す$S"),
            camera=w.nocht,
            stage=w.on_office_int,
            day=w.in_lastday, time=w.at_morning,
            )

def sc_redsky(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("真っ赤な空に",
            w.br(),
            nocht.come("慌てて外に駆け出た$Sは目に入ってきた異様な光景に思わず足も呼吸も止めてしまう"),
            nocht.talk("どうなってるんだ！"),
            _.explain("三十メートルほど先の交差点で車が衝突して車体後部が浮き上がったまま静止している",
                "それを見て驚いたり顔を背けたり、逃げ出そうとしている人たちの動きも止まったままだ",
                "信号は赤のまま変わらず、スーパーの駐車場では警備員と客が言い争いをしている雰囲気があるが声は聞こえない"),
            _.think("そう", "何よりも音がない"),
            _.talk("何なんだよ！"),
            _.do("路上には$Sの声だけが響き渡る"),
            _.explain("見上げれば鳥が宙で羽ばたいたまま写真で切り取ったようにその姿で留まり、",
                "電柱から落下する途中の雪もそれ以上落ちてこないで$Sの頭上一メートルほどで固まっている",
                "まるで時が止まっているかのよう"),
            nocht.talk("一体、何なんだ……"),
            _.do("呆れたように呟き、何度か呼吸をし、ようやく一歩、前に踏み出す"),
            _.do("旗は揺らめいたまま止まっているし、歩いている誰もそこから動き出さない",
                "声を掛けても返事はなく、その頬に触れると光の粒となって消えてしまう"),
            nocht.talk("え？"),
            _.do("それが何かのフラグだったのか、目に見えていた通行人が一気に光を放って姿を消し、",
                "続いて道路脇の建物も一つ一つが消えてしまう"),
            _.do("$Sはそれに慌てて後ろを振り返る"),
            _.talk("そんな……"),
            _.do("会社の入るビルが丸ごと消えていた",
                "そこにはただ真っ白な地平だけが残り、$Sが見ているうちにも次々と建物が小さな光を放っては姿を消していく",
                "まるで線で囲って描いたイラストを切り取るように、安易に、簡単に、街が消えていく"),
            _.talk("うわあぁぁぁ！"),
            _.do("$Sは思い切り声を上げ、駆け出した",
                "どこに行く宛もなく、それでも誰か、何か、まだこの世界のどこか生き残っているものを探したかったのだ"),
            _.do("その頭上、遙か百キロの彼方でぶわりと大きな光の帯がなびいた", "オーロラだ", "それも$Sが見たことのない、血のような真っ赤なオーロラだった"),
            stage=w.on_street,
            )

def sc_crying(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("叫び",
            nocht.come("#走っていた"),
            _.do("その血のオーロラが大地に降り注ぐほどに光の帯を伸ばしていた",
                "それを何度も振り返りながら$Sは走る",
                "息を荒くして、車も人もスーパーも花屋もカフェも信号に横断歩道、電柱、標識、花壇に青銅製のよく分からないオブジェ",
                "そういった見慣れたものが一切姿を消した、ただの真っ白な地平を、走っていた"),
            _.do("理由も事情も分からない",
                "ただ彼女が『さよなら』と寄越したメッセージが$Sにとって唯一の希望だった"),
            _.talk("まだ、間に合う"),
            _.do("そこは教会だった",
                "門や花壇、$erucco神父が手入れしていた植木たちは姿を消してしまっていたが、真っ白な三角の屋根の建物だけは辛うじてそこに変わらずに建っていてくれた",
                "木戸に手を当て、思い切り押す",
                "軋んだ音を立てて開いたそこは、窓から差し込む光が床に神と天使たちの姿をぼんやりと映している"),
            _.talk("神父？　いるか？"),
            _.do("だが返事はない",
                "マリア像の慈悲の瞳だけが無言で$Sを迎えてくれた"),
            _.do("再び地面が揺らぎ、壁が、天井が、テクスチャが剥がれ落ちるようにして消えていく",
                "もうこの虚構の世界は長くは持たないのだろう"),
            _.talk("なあ$asahi！", "君には聞こえているんだろ？"),
            _.do("$Sは覚悟を決め、呼び掛ける"),
            _.talk("$asahi",
                "そこにいるんだろ？",
                "$meは小さい頃からずっと、誰かが自分のことを見守っているその視線を感じていた",
                "その誰かを神という存在に結びつけ、$meは今日まで生きてきた",
                "いや、生かされてきた",
                "けどあの『さよなら』という言葉を見て分かったんだ",
                "やはりこの存在は君なんだって！"),
            _.do("再び揺らぐ",
                "立っていられなくなり$Sは右膝を突いたが、それでも視線を落とすことなく、抜けた天井から覗く巨大な赤い光のカーテンに向かって呼び掛ける"),
            _.talk("$asahi！",
                "聞いてくれ",
                "もうこの世界は終わりなのかも知れない",
                "けどその前に、一つだけ君に伝えておかなければならないことがあるんだ"),
            _.do("$Sはずっと隠していた本当の気持ちを、考えを、思い切り声にして吐き出した"),
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
