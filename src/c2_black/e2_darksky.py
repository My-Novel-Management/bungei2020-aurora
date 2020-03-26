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
            nocht.be("翌朝まだ日が昇って間もない白闇の静寂の中で、$Sはバイクの背に荷物を積み、出発した", "&"),
            _.do("ジョギングをしているトレーニングシャツの男性や新聞配達のバイクとすれ違う",
                "杖を突いて歩いていく老婦は日課の礼拝に向かうところだろう", "彼女は気づかなかったようだが時々$eruccoの教会で姿を見かける"),
            _.do("信号が赤に変わり、交差点でブレーキを掛けた",
                "荷台に詰んだキャンプ用のテントやら器具の重みで軽く左右に揺られる",
                "信号待ちをしている間に端末をライダースジャケットのポケットから取り出し、彼女に家を出たことを知らせた",
                "向こうはそろそろ昼頃だからちょうど良いだろう"),
            w.eventPoint("自動運転バス", "信号無視をしていくのを見かける"),
            _.do("右側の道から試験中の自動運転バスがゆるゆると左折の合図を出して進んでくる",
                "しかしその間にもバスの進行方向の信号は色を変え、赤になってしまった",
                "バスは停まる気配を見せず、赤信号でも構わずに曲がって$Sの前を通り過ぎて反対車線へと入って行った"),
            _.think("実用化までは程遠いな、と感じながら見送ると、$asahiから返信が入る"),
            asahi.voice("車の免許は持っていないのかしら"),
            nocht.do("挨拶もなく単刀直入な問いかけに『$w_japaneseは情緒を大切にするんじゃないのか』と訊いていた$mousaにイエスと返したことを少しだけ後悔している"),
            nocht.think("――できれば取りたいと思ってるけど仕事が忙しくてなかなかそういった時間が取れないままなんだ",
                "君は持っているの？"),
            asahi.voice("趣味で車に乗りたい人じゃなければほとんど$autocarで事足りるから、誰も取らないわ",
                "昔は身分証代わりに誰もが免許を持つよう指導されていたみたいだけど"),
            nocht.think("――自動運転がそこまで進んでいるなんて流石に$w_japanだね", "けどバイクの旅も良いものだよ",
                "過ぎ去る景色の中を走っていると自分が風にでもなったかのような気分になれる"),
            _.do("送信しておいて、端末を仕舞う",
                "ペダルに足を掛け、地面を蹴りつけて再び走り出した", "目指すは北部のラップランドだ",
                "上手くいけばこんな時期からオーロラを見つけられるだろう"),
            _.do("ただヘルメット越しに見上げた空模様はどんよりとグレィな雲が横たわり、出かける前に確認した天気予報も曇りから雨というものだった"),
            nocht.talk("あ……"),
            _.do("嫌だな、という予感はすぐ小さな水滴で包まれ、アスファルトの上を雨が叩き始める",
                "対抗車は強烈なライトを照らし、その眩しさに$Sは思わず目を閉じた"),
            w.comment("このパートの最後で事故った風に装う"),
            camera=w.nocht,
            area=w.Tampere,
            stage=w.on_bike,
            day=w.in_shorttrip, time=w.at_midmorning,
            )

def sc_godisexists(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    shopper, worker = W(w.shopper), W(w.worker)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("神はいるか",
            w.comment("シーンに違和感を抱かせつつ、いきなり休憩シーンに飛ばすこと"),
            inside.look("黄色い天板にオレンジのライトが光っていた", "&"),
            nocht.be("その縁から滴る雨水を睨めつけて、$Sはバイクに寄り掛かる"),
            shopper.come(),
            _.talk("旅行の予定だったんでしょう？", "散々ですな"),
            shopper.look("セルフのスタンドだったが、併設されているパン屋の店員がやってきて焼き過ぎて油で汚れた鉄くずみたいなパンを手に「食べますか？」と$CSに訊いた"),
            nocht.talk("$Rovaniemiまで行ってオーロラでも見ようと思ってるんですけど、望み薄っぽいですよね",
                "本当に貰ってもいいんですか？"),
            nocht.do("朝食用につい今し方$piirakatを買ったところだけれど、おまけにくれると言う"),
            shopper.talk("まだ去年始めたばかりでなかなか上手くはならなくてね"),
            _.do("彼はビニル袋にそれを入れて$CSに渡すと、苦笑してグレィの鼻髭を指で擦った",
                "歳の頃は五十から六十といったところだろう", "目は小さく、髪は丁寧に短く刈り込まれ、ぬいぐるみのクマを思わせる風貌だ"),
            nocht.talk("パンを焼く前は何を？"),
            _.think("自分の将来について今まであまり考えてこなかった",
                "それはどこまでも生き続けられるとは思えないからだ"),
            shopper.talk("エンジニアです", "主に携帯端末向けのアプリを開発していました"),
            nocht.talk("ああ", "$meもそっち側ですよ",
                "今はゲームソフトを作ってます"),
            _.think("いつかはこの仕事を辞め、別の何かを見つけるのだろうか",
                "人生なんていつ何が起こって終わってしまうか分からないのに、ずっと先のことまで計画を立てて生きようという気にはなれない",
                "それを一度$asahiに言うと、彼女は「プランＡだけしかない人生はハイリスク」だと一蹴した"),
            shopper.talk("最近のゲームは３Ｄは当たり前で、画質やらオンラインやらの機能も求められるから大変でしょ？"),
            nocht.talk("そういうのはツールやらプラグインやら便利なものがいっぱい出てきて、全部自作してた頃に比べれば楽なんじゃないですかね",
                "それよりは画面構成のセンスだとか、遊び方の工夫とか、より本質的なものの方が重要になってきてる気がします"),
            shopper.talk("綺麗な画面で誤魔化してた時代は終わりって訳ですか", "$meなんかはＦＰＳやＴＰＳは苦手なんで、レトロなインベーダーとか、",
                "ああいった分かりやすいのが好きですよ"),
            nocht.do("自分もそうだと答え、$Sは貰ったばかりの焦げパンに齧りつく","&"),
            _.think("表面こそ炭でコーティングされていたが中身はしっかりとライ麦のパンの味わいだ"),
            _.talk("これ、大丈夫ですよ"),
            shopper.talk("そう言ってもらえると力が出ますわ",
                "ただ娘に言わせるともっと柔らかくて甘い菓子パンを焼いてくれってね", "自然な味はノーサンキューなんですよ、今の子たち"),
            _.do("一瞬父親らしい顔を見せた彼は客に呼ばれ、小走りに行ってしまう"),
            nocht.do("雨はまだ止む気配がない",
                "湿った音をさせてトラックが側道を走り抜けていくのを何台見送ったか数えようとしたところで、$Sの端末が鳴った",
                "$asahiだ"),
            asahi.voice("秋の天気のようね"),
            nocht.think("確かにこの国の秋の気候は安定しない", "けれど酷い雨だと送ったことに対しての返答にしては違和感がある",
                "その意味するところを尋ねると、彼女は更にこんな返信を送ってきた"),
            asahi.voice("こちらではね、女心と秋の空という格言があるの",
                "それはどちらも変わりやすいものの喩えで、天候に関しては諦めるしかないという意味だったの", "ごめんなさい"),
            nocht.think("――君が謝ることはないさ",
                "ただこちらの季節のことをよく知っているなと勘違いしただけだよ",
                "それより天候じゃなくて女心に関して、変わってしまった場合にも同様に考えた方が良いのだろうか？"),
            _.think("送ってしまってから胃袋の上辺りを小さな後悔が撫でていったが、もうそろそろ少しくらい、という気がなかった訳でもない"),
            asahi.voice("天候と女心の違いは何か分かる？", "それが分かっているなら答えは簡単よ"),
            nocht.think("答えは後で送るとメッセージを書いて、$Sはバイクのスタンドを外した",
                "パン屋の方を見れば店主の男性が客を捕まえて何やら話し込んでいる",
                "パンのお礼を言うのは諦め、エンジンを掛けた"),
            _.do("あまり車の通りはなく、雨が続く中にゆるりと滑り出すように入っていく",
                "右手には鋭い葉を茂らせたアカマツが壁となって並び、威圧感いっぱいに$Sを見下ろしていた",
                "この国はどこに行くにも緑が多い", "自然豊かで良いと言われるもののそれは自然の厳しさとイコールでもあると$Sは思っている"),
            _.do("ちょうどガソリンスタンドから一キロほど先に進んだところで、大型の重機が三台、道を完全に塞ぐ形で置かれていた"),
            worker.be(),
            nocht.talk("あの、何してるんでしょうか"),
            worker.talk("ん？　見て分かんねえか？"),
            _.do("カラースティックを手にした作業員の男性は道路の中央に置いた看板をそれで指し示す",
                    "この先は落石により通行止めだと書かれていて、迂回路はないという注意書きも貼り付けられていた"),
            nocht.talk("ラップランドの方に行きたいんですが、どの辺りまで戻ればいいですかね？"),
            worker.talk("さあな", "それこそ一週間ばかり掛かりそうだから電車でも使った方が早いんじゃないかね"),
            _.do("男性はそれだけ言うと興味なさそうに重機に腰掛けている別の作業員に好きな女のタイプについて語り始めた"),
            nocht.do("$Sは端末を取り出し、それで別の経路を確認する",
                    "けれどどこも通行不可能と表示され、一旦元の市内まで戻るしかないらしいことが分かっただけだった"),
            nocht.talk("仕方ないか"),
            _.do("時間的にオーロラ観測は諦め、別のプランを考えるしかない",
                    "$Sはアクセルをふかし、Ｕターンして小雨の中に走り出した"),
            stage=w.on_gasstand,
            )

def sc_talkangel(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("天使の話",
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
            ).omit()

## episode
def ep_darksky(w: World):
    return w.episode("2-2.暗い空",
            sc_hischildhood(w),
            sc_godisexists(w),
            sc_talkangel(w),
            ## NOTE
            ##  - バイクでキャンプ場へと向かう
            ##  - 途中休憩を取る。彼女はノクトが小さい頃から不思議な体験をしていることについて、興味を持っていた
            note="キャンプ場を目指してバイクで走っていた。途中で休憩を取り、$asahiの生活について少し深く知ろうと質問をする")
