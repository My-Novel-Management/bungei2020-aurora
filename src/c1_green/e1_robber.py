# -*- coding: utf-8 -*-
"""Episode: 1-1.コンビニ強盗
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
# NOTE
#   冒頭は人助けをして死ぬところから
def sc_thanksgod(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    robber, shopper = W(w.robber), W(w.shopper)
    oldlady = W(w.oldlady)
    sky = W(w.sky)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("神に感謝する",
            w.comment("冒頭は空の描写。特に色調に何か違和感を持たせる"),
            w.comment("ミッドサマーを終えて、まだその余韻が残る街中"),
            w.comment("舞台が日本ではない、ということを端的に分からせる＝看板の文字など"),
            w.comment("日本と逆で、右側通行、左ハンドルが主流"),
            nocht.be(),
            sky.look("見上げた空は雲が一つも浮かんでいない青一色で、そこを飛空する鳥も飛行機も、虫の一匹すら見つけられない",
                "僅かにグラデーションさせて塗り潰したＣＧのような整った配色に、短くした金髪を掻き上げて青年はペダルを漕ぐ"),
            w.eventStart("電子世界"),
            w.eventPoint("電子世界", "オブジェクトの数が減らされている"),
            w.comment("タンペレは湖畔工業都市。北欧の夏と分かるように"),
            nocht.do("遊歩道をロードバイクで軽快に走るのが心地良い",
                "右手にはゆったりと水を湛えた$w_tan_riverが夏の陽光を反射して煌めき、それを眺めながら芝生にビニールシートを敷いたカップルが仲良く愛を語らっている",
                "青年はポケットに入れていた端末が震えたことに気づき、一旦止まって確認した"),
            asahi.voice("$nocht、あなたが昨日アップしていたイラスト見たところだけど、いつもみたいに天使じゃないのね"),
            nocht.do("$asahiという名前は彼女の国の言葉で朝の太陽のことを表すと聞いて、彼女のアイコンには太陽マークを当てていた",
                "液晶に表示された彼女のアイコンと名前を見ながら$Sは少し考え、返信メッセージを作る"),
            _.think("――あの女神は気に入らなかった？", "特別な時は天使よりも女神を描くことにしているんだ"),
            asahi.voice("女神というより誰かモデルのいる女性を描いたみたいだったわ",
                "森の中のソファは幻想的だけど、ちょっと露出が多いのが気になった"),
            nocht.think("――胸は見せていないしローブの丈も膝くらいだから、特別に露出が多いとは思わなかったよ",
                "そもそも厚着をしている神様はあまり見ないから変だとは思わない"),
            asahi.voice("古い時代のものほど凝った衣装がなかっただけじゃないかしら",
                "性的な魅力でバズらせようというのはどうかと思うわ"),
            nocht.do("そういうつもりはなかったけれど「ごめん」と謝罪文を送り端末をポケットに仕舞うと、再びペダルを漕ぎ出した",
                "柵にもたれかかり川を見ている親子は大きな荷物を足元に置いていて、ミッドサマーの休暇にどこか海外にでも出かけていたことを思わせる",
                "$Sの会社では土日に僅かばかりの休みがあった程度で、ほぼ毎日変わらずにこの遊歩道を通り抜けている",
                "今日もまた化粧気のない腕組みが得意なチーフが、監視ドローンのように「進捗どう？」と声を掛けてくる様を思い起こし、",
                "ペダルが五グラムほど重く感じた"),
            w.eventStart("自動運転実験"),
            w.eventPoint("自動運転実験", "試験運転バスの話"),
            outside.look("橋を渡り、大通りを進む",
                "信号待ちで並ぶ車列の中には去年から試験運転中のＡＩ搭載バスが大人しく一番先頭でブレーキランプを点灯させている",
                "自動運転技術は個人的に眉唾の域を出ていないと感じているけれど、いざ実証実験が始まってしまうと可能性よりも金になるかどうかの問題なのだなと、",
                "サイドボディにラッピングされた『$w_cyber_eng』という社名を見ながら小さく首を振った"),
            nocht.do("交差点を渡り、車線の左側をするすると進んでいく",
                "途中で脇の路地に曲がり、やや下り坂になったところを一気に駆け下りる",
                "その先、右手側に大きな駐車場とスーパーマーケットが見えてくる",
                "入り口に立っている緑色の制服を着た警備員は$Sの姿を見つけると誘導棒を振って挨拶してくれた"),
            _.do("その前の歩道を半裸のおじさんがウォッカ片手に歩き、",
                "必死に手押し車を握って歩く老婦人がそのおじさんを追い抜いていく",
                "黒猫が鈴を鳴らして一段高いブロックに登れば、",
                "その前を黄色い蝶が悠然と羽ばたいて空へと上っていった"),
            nocht.think("街の息吹を感じる",
                "$Sは思わずスケッチブックを広げたくなったが、仕事に間に合わなくなるので気持ちをシャツの中に仕舞い込み、",
                "角を曲がった"),
            w.comment("ここで$nochtの人となりを多少とも分かってもらう。何故そんな無謀をするのか、と疑問も持たせる"),
            ## NOTE
            ##  フィンランドであることが分かるように
            ##  人助けして、死ぬ、ということがすぐ想像しやすいイベント
            ##  ノクトの人柄が分かるもの
            camera=w.nocht,
            area=w.Tampere,
            stage=w.on_park,
            day=w.in_summerday, time=w.at_afternoon,
            )

def sc_robber(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    robber, shopper = W(w.robber), W(w.shopper)
    oldlady = W(w.oldlady)
    sky = W(w.sky)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("強盗",
            nocht.come("会社に向かう前に財布に余裕が欲しかったのでコンビニを見つけ、その前にロードバイクを停めた"),
            robber.be(),
            shopper.be(),
            oldlady.be(),
            nocht.do("キャッシュレス化が進んでいるとはいえ、まだまだ現金が必要な場面が多い",
                "ガラス戸を押し開け、店内に入る",
                "$asahiの国ではあちこちにコンビニが建ち、それが全て二十四時間やっていて、誰もがスーパーやドラッグストア以上に利用していると聞く",
                "特別価格が安い訳ではないらしいがこの国のコンビニはとにかく割高で、余程の事情がない限りはソーダ水一本すら買わない",
                "精々がＡＴＭを利用するくらいだ"),
            inside.look("商品棚には歯ブラシやコップ、ロウソク、下着といった生活雑貨やスナック菓子、チョコレート、サルミアッキの缶等が並ぶほか、",
                "ソフトドリンクの冷蔵ケースにパッキングされた惣菜やサンドウィッチがレジ脇の棚に置かれているのが目に付く",
                "客は$S以外に腰の曲がったハンチング帽の老人と、レジ裏の棚を掃除しているお腹の大きな男性店員だけだ",
                "そこに黒い目出し帽を被り片手にライフル銃を持った大柄な男が入ってきていがらっぽい声で喚いた"),
            robber.talk("おい！　金を入れろ！"),
            _.do("男はバッグをカウンターに置き、銃口を店員に向ける"),
            shopper.talk("え、その"),
            _.do("店員の男性は何が起こったのか分からないようで何度も鞄と目出し帽を見ながら口をパクパクとさせている"),
            robber.talk("金だ", "早くしないと首が飛ぶぞ？"),
            _.do("苛立った様子でそう言うと一発放ち、天井の隅の監視カメラを破壊した", "&"),
            oldlady.do("その音と衝撃に老人は腰を抜かし、床に転がった", "気づいた強盗は銃口を店員からその老人へと向け「早く」と急かす"),
            nocht.do("$Sはシャツの下のロザリオを服の上から握り、小声で神に祈る",
                "いつもみたいに見守っていて下さい、と"),
            nocht.do("それから声を上げ、二リットルのボトルを手にして男に襲いかかった",
                "目出し帽は咄嗟に銃口を向かってくる$Sへと向けるが、彼が引き金を引くよりもその頭部にボトルの縁が衝突する方が早かった",
                "鈍い呻き声を上げ、巨漢が後ろのカウンターへと吹き飛ぶ", "だがそれと同時に銃声が鳴った"),
            nocht.think("――あ、れ？"),
            _.do("$Sは自分の左半身が歪んだのに気づき、それから体勢を大きく崩した"),
            stage=w.on_conveni,
            )

## episode
def ep_conveni_robber(w: World):
    return w.episode("1-1.コンビニ強盗",
            ## NOTE
            sc_thanksgod(w),
            sc_robber(w),
            note="仕事に向かう途中で、コンビニ強盗に遭遇し、$nochtはそれを取り押さえようとしてライフルで撃たれてしまった")
