# -*- coding: utf-8 -*-
"""Episode: 1-4.アサヒ
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
def sc_aboutasahi(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    inside, outside = W(w.inside), W(w.outside)
    sky = W(w.sky)
    return w.scene("出逢いについて",
            w.comment("自宅前に、近所の雰囲気を描写しておく"),
            nocht.be("自宅に帰るところ"),
            sky.look("空はまだ明るい"),
            nocht.do("$asahiに東京の夜が七時にはもう星が見え始めると聞いて驚いている"),
            outside.look("夏の街の情景。まだ涼しそうな格好で出歩いて、太陽を浴びようとしている人たち",
                "今から仕事に出かけようという人も"),
            nocht.do("スーパーで色々と買い込んで、家でイラストでも描こうと思っている"),
            nocht.do("帰りながら$asahiの質問に答えていく"),
            asahi.voice("$nochtに実家に帰らないのか、等と質問"),
            w.comment("少しやり取りをしながらアパートが見えてくる"),
            outside.look("アパート周りの描写"),
            nocht.do("玄関を開けて、中に入った"),
            inside.look("部屋の様子",
                "借りているのは１ＬＤＫで二階の部屋"),
            w.comment("平均的な家賃は８００から９００ユーロ程度"),
            nocht.do("家でちびちびやりながらイラストを描いている"),
            _.do("$Sが描くのはいつも決まって神や天使が登場する宗教画だった",
                "それは$Sが常にその大きな存在に見守られているということを感じているからであり、",
                "もともとそれを何かしら形にしてみたくて絵を始めたのだ"),
            _.do("部屋の壁にはいくつかプリントアウトした自分の絵が飾られている",
                "どれもかなり抽象的で、自然の中に天使を潜ませたものばかりだ",
                "その中の一枚を、$asahiは気に入ってくれた"),
            _.do("オーロラを見上げる天使", "そう呼んでいるかなり初期の頃のものだ"),
            w.eventPoint("$nochtの絵", "オーロラを見上げる天使"),
            nocht.do("それを描き直そうと昔のデータを呼び出そうとしていたが、どこにも見当たらない"),
            nocht.talk("あれ？　おかしいな。消しちゃったか"),
            w.eventPoint("データ異常", "自分のPC内のイラストデータが消えている"),
            nocht.do("探してみたが、他のデータもなくなっている"),
            nocht.talk("どういうことだ？　またHDDいかれたのか？"),
            nocht.do("そこに$asahiから連絡がくる"),
            asahi.voice("今日はもう仕事終わったの？"),
            nocht.talk("ああ、そうだ"),
            nocht.do("データはどうも手違いか何かで消失したらしい"),
            nocht.talk("昔のイラストデータを消してしまったみたいでね"),
            asahi.voice("そう。それは残念ね", "でもデータは所詮データだわ"),
            nocht.talk("確かにその通りだ", "そういえば新しい絵を描いたんだけど"),
            nocht.do("今描いている絵をとりあえず見せて反応を見る"),
            asahi.voice("今までとは違う感じ？"),
            nocht.talk("ほら、この前$asahiが言っただろう？", "普通の絵は描かないのかって",
                "ちょっとチャレンジしてみてるけど、どうにもぴんとこない"),
            camera=w.nocht,
            stage=w.on_apart_int,
            day=w.in_summerday, time=w.at_afternoon,
            )

def sc_asahilife(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("彼女の暮らし",
            nocht.be("ある日の仕事終わり"),
            nocht.do("彼女から東京の話を聞いた"),
            nocht.talk("そっちの夏は酷いみたいだね"),
            asahi.talk("室内にいる分にはまだいいんだけどね",
                "年々温度が上がっていて昨日なんて四十度を超えていたわ"),
            nocht.talk("まるでサウナの中みたいだ", "こっちじゃ想像すらできないよ"),
            asahi.talk("人間はまだいいけど、コンピュータは困るわ",
                "ちょっとした熱ですぐに不具合を起こす"),
            nocht.talk("そっちのコンピュータは随分とセンシティブなんだね。それともそういった精度の必要なものを研究している？"),
            asahi.voice("ええ、そうね", "ちょっと普通のコンピュータとは異なるから", "詳しくは話せないけど"),
            nocht.do("休日にはこうしてメッセージをやり取りしながら一日を終える",
                "それが心地よかった"),
            stage=w.on_cafebar_int,
            time=w.at_night,
            )

def sc_promiseher(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    return w.scene("彼女にオーロラの写真を送る約束をした",
            nocht.be(),
            nocht.do("たまにバイクで遠出する"),
            _.do("適当なロケーションで写真を取り、それを仕事や趣味で使うのだ",
                "けれど彼女と出会ってからは彼女の為の写真も増えた"),
            nocht.do("まだ過ごしやすい季節", "湖畔まで出かけ、そこでパンを頬張る"),
            asahi.voice("綺麗な湖ね。まだそっちには自然が沢山残っているのね"),
            nocht.talk("日本だってマウント富士があるだろう",
                "それに山も川も多いって知ってる"),
            asahi.voice("あんな狭い島に本当に沢山の人間が住んでいるのよ",
                "東京なんてほぼ建造物で埋まってしまっているわ",
                "目に付く自然は全て人工物", "本当の自然なんてもう、希少価値なのよ"),
            nocht.do("そんな風に言うから、今までよりもずっと自然の写真を取ることが増えた",
                "海、山、空、何気ない植え込み、小動物",
                "ひょっとしたら彼女と出会ってから、以前よりもずっと自然に親しむ機会が増えたかも知れない"),
            nocht.do("タブレットで描いたイラストを$asahiに送る",
                "すぐに返事があり、今までと画風が変わったと驚いていた"),
            nocht.talk("昔はこういう絵だった",
                "ただいつからか描きたいものが変わってきて、それで画風も変わってしまった",
                "$asahiはどっちが好きだい？"),
            asahi.voice("$meはどちらも好きよ"),
            nocht.talk("どっちがいいか、という質問にはその答えは答えになっていないよ"),
            asahi.voice("率直にいえば、今もらったイラストの方が優しい気がする",
                "最近のはちょっと冷たい。でも宗教画って大概がそうでしょう？"),
            nocht.talk("宗教画ならね"),
            nocht.do("$asahiに頼まれ、オーロラの写真を取って送ると約束をする"),
            stage=w.on_bike,
            )

## episode
def ep_asahi(w: World):
    return w.episode("1-4.アサヒ",
            sc_aboutasahi(w),
            sc_asahilife(w),
            sc_promiseher(w),
            ## NOTE
            ##  - アサヒとの出逢いは、SNSに上げていた趣味のCGイラストだった
            ##  - 徐々にメッセージをやり取りするようになり、彼女がコンピュータ・サイエンスの研究者と知った
            ##  - 彼女はオーロラを見たことがない、と言った
            note="SNSに流していた$nochtの趣味のCGを好きだと言ってくれた女性$asahiに惹かれていく")
