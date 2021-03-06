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
            w.comment("$nocht側は映像と音のみで、臭いや触感などの他の感覚については表記しないこと"),
            w.comment("季節が切り替わり、道端には雪のオブジェクトやスキン、テクスチャが溢れている。一気に冬に切り替わっている"),
            w.comment("フィンランドの初雪は朝９時の積雪が１ｃｍ以上。早いと$Rovaniemiで９月中旬とかに降ることも。基本は十月に入ってから"),
            w.symbol("　　　　１３"),
            nocht.be(),
            nocht.do("吐く息が白い"),
            _.do("それが消えゆくのを見つめながら$Sはいくつのレイヤでその繊細さを表現しようかと、ぼんやり考える"),
            outside.look("建物の傾斜した屋根には雪が帽子となり、裸になった街路樹から時折白い塊が落とされる",
                "その下を歩く人々もニット帽にマフラー、コートやダウンジャケットと冬服で、",
                "季節は完全に切り替わっていた"),
            w.comment("必死に$asahiにメッセージを送るが、虚しさだけが募る"),
            nocht.do("$Sも黒のダウンジャケットで肩を竦めるようにして歩いていたが、首筋を抜けていく風に何度も震える",
                "けれどそれは寒さが原因とは言い切れない"),
            _.do("ポケットに突っ込んでいた端末を取り出し、メッセージの確認をする",
                "仕事のメール以外は何もない", "ＳＮＳに放流したイラストにもリプライが付かなくなった",
                "それでも$Sはもう一度と、彼女に送る文面を考える"),
            nocht.think("――ん？"),
            _.do("空から落ちてきた雪片が端末の液晶を濡らしたのを見て、この景色を撮影して送ろうと決めた",
                "日本でも雪は降ると聞いているが彼女の暮らす街は自然がないそうだから、ひょっとすると珍しいと喜んでくれるかも知れない"),
            _.do("雪が珍しい、という感覚はなかった",
                "それは$Sが雪の国の住人であり、",
                "生まれた時からあまりにも見慣れすぎた光景だからだ",
                "もし仮にこの街で暮らす人間だけしか存在しなかったとすれば、人類にとって雪とはありふれたものの一つにしかならなかっただろう"),
            _.do("空に向け、端末のレンズを光らせる"),
            _.think("――いつかは君もこっちに来て、この雪景色と冬の寒さを体験すると良い",
                "フィンランドの冬は日本のそれとかなり違うから"),
            _.do("添付した文面は、彼女にどう伝わるだろうか"),
            _.do("一分ほど立ち止まり、何度か返信を確認したがリアクションはない"),
            _.talk("クソッ"),
            _.do("道端に転がっていた缶に八つ当たりし、$Sは足早に横断歩道を渡る",
                "転がった缶はアスファルトの上に出て、走り抜ける車のタイヤに蹴られて何度か跳ね、消えた"),
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
            w.symbol("　　　　１４"),
            nocht.be("#不機嫌に仕事をしている"),
            nocht.do("モニタに映ったＣＧの怪物の長い手足をマウスで引っ張って縮める",
                "長すぎてアクションの邪魔だからとデバッグ作業で文句が出たのだ",
                "一番最初のデザインに近くなったそれを見て、$Sはテーブルで赤鼻を膨らませて笑い声を上げている$adonisに内心で毒づいた"),
            mousa.come(),
            nocht.do("来月にゲームの発売を控え、プログラマの大半が会社で寝泊まりをするようになり、それぞれが目尻に皺を寄せて作業に勤しんでいる",
                "そんな状況下でディレクター一人が気楽そうにしているのは何とも心地の悪いものだ",
                "隣にやってきた$mousaがメモを置いて無言で立ち去る", "そこにはチャットに書き込むとすぐ警告を受けるスラングがいくつか書き連ねられ、",
                "おまけに男性の股間と思しきイラストに一輪の花を咲かせてあった"),
            nocht.think("小さく口元を歪め、作業に戻る"),
            _.do("修正指示のメモを見て、敵キャラクタのデザインを変更していく",
                "$adonisの心変わりはいつも突然で言い出すと止まらないので仕方なく従うのだけれど、",
                "何故一度絶賛した$Sのデザインを「これじゃあゲームの世界観に合わない」と言って切り捨てるのか、流石に理解に苦しむ",
                "そもそも理解しようという考えが間違っているのかも知れない"),
            _.do("彼の指示通りに頭を不必要に大きくしたり、体中にトゲを生やしたりして見た目のバランスを欠いた怪物たちは、",
                "プレイヤーである神の戦士の矢を受けて汚い悲鳴を上げながら絶命するだろう",
                "そんな彼らにも何かしらの個性をと思って特徴的な柄のスキンを当てたり、突起を増やしたり、時には人間臭い表情を描き込んだりする",
                "だがそれらは無意味だと$adonisは切って捨てるのだ",
                "ゲームの世界に欲しいのはただ快感と感動だけだ、というのが$Sと相容れない彼の持論だった"),
            _.do("手足の長くなったものを元の長さに修正し、ほっと一息つく",
                "三分ほど前に$adonisの鼻に掛かった声は遠くなり、部屋を出ていった",
                "$Sは思い切り伸びをするとデータを保存し、$ireneにチェックを頼む"),
            inside.look("顔を上げれば誰もがモニタに齧りつくような姿勢で集中している",
                "マスターアップが近づくほど全員の精気のない顔が黒光りしたモニタに反射して見えるようになり、",
                "さながらお化け屋敷のような有様になる",
                "机の上にはいつも以上に資料やファイルが積み上がり、それが崩れては誰かの足の上に落ちる"),
            mousa.talk("ほらよ"),
            _.do("ダン、と音を立てて机に紙コップが置かれる", "$mousaだ",
                "勢いで中のコーヒーが零れることなど気にしない"),
            nocht.talk("ありがとう"),
            mousa.talk("次のプロジェクトの時は担当を$adonisから別の奴に変えてもらいてえよな"),
            mousa.do("隣の椅子を引き寄せて座ると、彼はソフトドリンクの缶を手に$CSに笑いかける"),
            nocht.talk("変わってもっと酷いのが来たら洒落にならないから難しいところだ"),
            mousa.talk("闇の先にもっと深い闇があるってか", "確かに世の中、悪いことには底がねえな"),
            mousa.do("コーヒーを一口に飲み干すと、$Sは$CSのモニタを覗き込んで太い眉を顰める"),
            mousa.talk("なあ、そいつも敵か？"),
            nocht.do("画面には黒髪の女性のＣＧモデルが映っていた",
                "瞳は濃い茶色で、肌は白っぽい", "小さな目鼻の、東洋人を思わせる顔立ちだ"),
            nocht.talk("いや"),
            mousa.talk("じゃあ味方？"),
            nocht.think("それにも苦笑して首を振り「ゲームのキャラじゃないんだ」と溜息をつく"),
            mousa.do("その返答に「アーウ」と勝手に納得したように頷くと、彼は缶を口につけて喉を鳴らした"),
            nocht.talk("おいそれ、アルコールか？"),
            mousa.talk("ノンアルだ", "医者からさんざんビール減らせって言われてるからな"),
            nocht.talk("また仕事中に飲んでんのか？　$ireneに怒られるぞ"),
            mousa.talk("いいんだよ。どうせいつかはみんな死ぬ"),
            nocht.think("確かにそうかも知れないが、$mousaは稀に驚くような正論を口にするから驚く"),
            nocht.talk("命を大切にって母ちゃんから教わらなかったか？"),
            mousa.talk("何番目の母ちゃんだ？"),
            nocht.think("$mousaは何度も両親が離婚再婚を繰り返していて、五人も母親がいるそうだ"),
            w.eventPoint("ネット障害", "やや遅かったり、とぎれとぎれだったりと何か変"),
            mousa.talk("それよりちょっとネット対戦を開いてみてくれねえか？"),
            nocht.talk("ああ、いいよ"),
            _.do("彼女のＣＧモデルの画面を一旦閉じ、ネット対戦モデルのゲームサンプルを起動する",
                    "近年のゲームはどれもオンラインを通じて同じゲームを持つ人間と対戦したり協力したりできるような遊び方も求められていて、",
                    "それは$Sたちのようなインディーズゲームメーカーですら抗えない流行になりつつあった"),
            nocht.talk("それで、何が問題……あ、これか"),
            _.do("彼から聞くよりも早くそれは画面に現れていた"),
            mousa.talk("さっきから繋がんなくてな", "対戦サーバがいかれちまってるのか？"),
            nocht.do("ずっと『接続できません』という表示が点滅している",
                    "有線の問題かと思ったがブラウザでの閲覧は問題ない",
                    "端末の無線も時折電波が弱くなるものの、利用に支障が出るほどでもない"),
            nocht.talk("プログラムの方の問題は？"),
            mousa.talk("一応調べてみたがそれらしいバグは見当たらんな"),
            nocht.talk("Ｐ２Ｐは？"),
            mousa.talk("そっちに切り替えてやってみるか"),
            nocht.do("端末同士の対戦モードに切り替え、再度試してみる",
                    "画面はエラーも出ず、一応$mousaの端末も認識しているようだが、", "動かしてみると何ともぎこちない"),
            nocht.talk("やっぱりプログラムの方の問題じゃないか？"),
            mousa.talk("参ったぜ", "今日も泊まりかよ"),
            nocht.do("二人で苦笑を合わせ、とりあえず何か腹に入れようと席を立った"),
            stage=w.on_office_int,
            )

def sc_desperation(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    mousa, irene = W(w.mousa), W(w.irene)
    return w.scene("自暴自棄",
            w.symbol("　　　　１５"),
            w.comment("弱音を吐くところ。唯一、じっくりと他の人間と話すところだから、しっかり描写する"),
            nocht.be(),
            irene.be(),
            w.eventPoint("失恋", "$ireneに相談"),
            nocht.do("結局その日は泊まり込みでネット対戦プログラムの方のバグを探したがそれらしい箇所は見つからず、",
                "明け方になって試してみるとそれまでがおかしなくらいにスムーズに対戦が行えて、ただのネットかサーバの不具合でもあったのだろうという結論に落ち着いた"),
            nocht.talk("で、こんなところまで$meを引っ張り出して仕事の話ですか？"),
            nocht.do("$Sは$ireneに連れられ、彼女の行きつけのバーにやってきた"),
            _.explain("古めかしい木戸を潜ると薄暗くて狭い店内に、カウンターとテーブル席が四つ、詰め込まれているのが分かる",
                "店員は眼鏡をしたグレィの髭面の男性のみで、客が自分でカウンターまで料理を取りに行っていた"),
            irene.talk("仕事の話なら会社で済ませておくわよ"),
            _.do("溜息がちにそう答えると、彼女はカウンターに座るよう$CSに促す"),
            nocht.talk("じゃあプライベートですか？", "それは、参ったなあ"),
            irene.talk("どういう意味？"),
            nocht.do("$ireneにひと睨みされ、$Sは肩を竦める"),
            _.do("彼女に注文は任せ、鞄を足元に置いて座ると、端末に何も連絡が入っていないことを確認してからコートのポケットに仕舞う"),
            irene.talk("もうすぐマスターアップね"),
            nocht.talk("売れるんですかね、あれ"),
            _.think("$asahiは人間同士が殺し合うゲームのどこが楽しいのかと、いつも不満そうだった",
                "見た目は人間じゃないと反論しても操作しているのは人間だから同じじゃないかと"),
            irene.talk("運が良ければ$game2くらいは売れるわよ"),
            _.do("$Sは興味無さそうに答え、上着を脱いで背もたれに掛けてから、椅子に座る","&"),
            _.look("隣に座った彼女を改めて見ると鼻筋の通った涼し気な顔は控え目に言っても美人だ", "&"),
            nocht.do("それなのに男の話を全く聞かないし、私生活についても謎が多い"),
            irene.talk("ねえ", "最近ちゃんと食べてる？"),
            irene.do("彼女はカウンターに置かれたプレート二枚を取り、$CSの前に一つを置いた","&"),
            nocht.do("乗っているのはマッシュポテトとごろっとした肉団子が幾つか、それにカリカリに焼いたライ麦パンと付け合せの野菜だ",
                "サーモンの切り身が混ぜてある", "光っているのはオリーブオイルだろうか"),
            nocht.talk("それなりに食べてますよ、$meだって"),
            _.do("続いて注文したビールの小ボトルを受け取り、自分でグラスに注いだ"),
            irene.talk("だったらどうしてそんなに元気がないのよ"),
            nocht.talk("元気ないですかね？"),
            _.do("無理矢理に口を笑わせて訊いてみたが$ireneには顔を顰めて首を振られただけだった"),
            irene.talk("気になって仕事どころじゃないんでしょ？", "話だけなら聞くから言ってみてよ"),
            _.do("彼女はフォークの先でポテトをつつきながら溜息を零した$CSを見やる"),
            nocht.talk("チーフって役職は個人的な恋愛の悩みまで解決しないといけないんですか？"),
            irene.talk("恋愛、なの？"),
            nocht.talk("何だと思ってたんですか？"),
            irene.talk("いえ、$meはてっきり$adonisとうまくいってないものだとばかり"),
            nocht.do("その答えに$Sは肩を震わせて笑う"),
            nocht.talk("別にデザインに文句つけられて落ち込んでる訳じゃないですって",
                "そもそも$adonisを人間的に好きな奴はうちにいないでしょうけど、それで思い悩むほどあいつのことは気にしてないですよ"),
            irene.talk("それじゃあ次回作も彼を使って大丈夫なのね？"),
            nocht.do("肉団子を一つ口に放り込んでから「まあいいですよ」と答えておいた"),
            nocht.talk("それより、ほんとに恋愛相談に乗ってくれるんですか？"),
            irene.do("一度考え込むように$CSを睨みつけると「仕方ないわね」と口にして、サーモンのサラダを突く"),
            irene.talk("けど恋愛っていうのは結局当人同士の問題で、愚痴を聞くくらいしかできないのよ、他人ていうのは"),
            nocht.talk("それでもいいですよ",
                "彼女のことを真面目に話せる女性の知人て、チーフくらいしかいないですから"),
            irene.do("それで何なのよ、とビールのお替りを貰いながら$ireneは尋ねる"),
            nocht.talk("実はずっと好きな女性がいるんです"),
            irene.talk("まさかそれが$meだとか言わないわよね？"),
            nocht.talk("チーフは美人だけど$meは特にそういうの興味ないです"),
            nocht.do("強く睨みつけられた気がしたが、構わずに続ける"),
            nocht.talk("彼女はここじゃなく、日本という国で研究者をやっています",
                    "$meの絵をとてもよく理解してくれて、端末でやり取りするだけですが、それでも半年ほど毎日何かメッセージを送り合っていました",
                    "それが"),
            _.explain("$Sは小休暇を貰ってオーロラ観測に出かけた日の出来事をある程度かいつまんで彼女に伝えた",
                    "もちろんあの告白のこともだ",
                    "彼女は最初は怪訝な表情をしていたけれど告白のくだりで徐々に真剣に耳を傾けるようになり、",
                    "最後には「それは違う」と$Sの考えを強く否定した"),
            nocht.talk("違うって？",
                    "じゃあどうして彼女は返事をくれないんだ？",
                    "$meのことを嫌いになったからだろう？",
                    "それとも何か？", "返信できない複雑な事情とやらが発生しているのか？"),
            irene.do("$CSがそう言うと「何も分かってないね」とビールを呷り、$Sは目を細めた"),
            irene.talk("もっとさばさばしてると思ってたけど、あんたって意外と女々しい男だったんだね"),
            nocht.talk("何言ってるんですか",
                    "誰だって恋をすればこうなりますって",
                    "それだけ本気だってことなんだから", "&"),
            nocht.talk("いないんですか？　チーフに恋人はいないんですか！"),
            irene.talk("いるよ"),
            _.do("彼女は事もなげに答える"),
            nocht.talk("それじゃあ自分が幸せだからそんな風に言えるんすよ"),
            _.do("まだ二杯目だったが、どういう訳か今日はアルコールの回りが早い",
                    "舌がもつれて言葉が怪しくなってきたが、構わずに$Sはまくしたてた"),
            _.talk("言葉も違う、国も違う、文化や風習も違う",
                    "そんな相手に対して、けれど絵だけは嘘をつかない",
                    "$meの信念です",
                    "それを彼女は理解してくれる唯一の女性だった",
                    "だから$meは、彼女と、一緒に、オーロラを見たかったんだ",
                    "なのに、なんで……"),
            irene.talk("ＳＮＳの向こう側のことなんて、相手が実際どう思ってたか分からないでしょ？",
                    "その彼女、冷ややかに見てたのかも知れないわよ？"),
            nocht.talk("$asahiはそんな女じゃないんです！",
                    "彼女はね、正に女神なんだ",
                    "$meの人生にとってかけがえのない存在で、今この瞬間だってずっとどこかで見守ってくれてる",
                    "そういう大きな存在なんですよ"),
            irene.talk("もう酔ったのかい？", "参ったわね"),
            nocht.do("既に二人ともプレートを綺麗にして、グラスにも酒がほどんと残っていなかった"),
            nocht.talk("もう一軒いきましょう"),
            irene.talk("明日に堪えるから今日はもうこの辺りで"),
            nocht.talk("今日は$meが奢りますから！", "もう一軒だけ付き合って下さいよ、お願いしますよ、$ireneさん"),
            irene.do("頭を下げた$CSを、面倒そうな表情で見ながら彼女は頷いた"),
            stage=w.on_cafebar_int,
            )

def sc_missingher(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    irene = W(w.irene)
    return w.scene("彼女はもういない",
            w.br(),
            nocht.be("暗がりの中、白い息はアルコールスプレーのようで、ふらつく足で$Sは、自分が世界を浄化しているような気になってへらへらと口を歪めた"),
            w.comment("$ireneに近所まで送ってもらった"),
            nocht.do("前後不覚になるまで飲むなんてことは久しぶりで、心を許せる誰かと一緒にいることで自制できない自分がいるということがよく分かった",
                "不意に突き上げてきた悪寒を道端へと吐き出し、まだ辿り着かない自宅への歩を進める"),
            nocht.talk("すみません"),
            nocht.do("誰かにぶつかり、頭を下げるが、顔を上げてもそこには誰もいなかった"),
            nocht.do("完全に酔っ払いだ", "熱い吐息を肺から押し出し、空を見上げた", "&"),
            _.do("星は変わらずにそこで輝いていてくれるのに、取り出した端末には$ireneからの『気をつけて帰りなさいよ』というメッセージ以外、何もない"),
            _.talk("なぜ答えてくれないんだ！　$asahi！"),
            _.do("叫び声は空へと吸い込まれ、消えていく"),
            _.do("声を上げるほどに、前に進むほどに、力が失われていくこの感覚が、$Sの精神を蝕んでいた"),
            _.think("ん？　眩しいな"),
            _.do("いつの間にか道路の上に存在していた彼が見たのは、試験中の自動運転バスと、それを避けようとして急ハンドルを切ったワゴン車だった"),
            w.comment("事故るが死なない"),
            stage=w.on_street,
            time=w.at_night,
            )

def sc_lonelypray(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    eru = W(w.erucco)
    return w.scene("寂しい祈り",
            ## NOTE
            ##  omitしたが、必要なら後で追加する
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
            ).omit()
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
