# -*- coding: utf-8 -*-
"""Episode: 1-3.ゲームメーカー
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
def sc_programmer(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    mousa, irene, adonis = W(w.mousa), W(w.irene), W(w.adonis)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("プログラムな日々",
            nocht.come("会社にやってくる"),
            nocht.explain("＜会社の様子説明＞",
                "正規メンバー以外にもデバッグ時には人を増やして全体で二十人くらい。普段は十人前後でやっている"),
            inside.look("オフィスの見た目。テナントビルの二階のワンフロア"),
            _.look("オフィスの様子。机やパソコン、ハードディスクの山に、資料のファイル"),
            nocht.do("自分のデスクにやってきて"),
            mousa.be("隣のデスクででっぷりした黒人が"),
            mousa.look("$Sの外見。ナイジェリア系のスウェーデン人で、仕事の為に雇われている"),
            mousa.talk("おい$nocht、聞いたぜ、英雄"),
            nocht.talk("ほんと、よくかすり傷で済んだよ"),
            w.comment("$nochtがよく死にかけていることは周知"),
            irene.come(),
            irene.talk("あのね", "勝手に死なれたらうちは終わるんだからやめて"),
            nocht.explain("プロジェクトリーダーの$irene"),
            irene.look("金髪の綺麗な美人。いつもしっかりスーツ姿で弁護士みたいと。実際この会社を起こしたのも謎な人物"),
            w.comment("実は$asahiの性格や容姿を少し受け継いだデータになっている"),
            nocht.talk("分かってるよ",
                "それよりどうだい？　新しいデザインは"),
            mousa.talk("$adonisが怒ってた。勝手にイメージ変えるなって"),
            w.comment("$adonisは後で登場。ここでは名前と役割のみ。あと口うるさくて、$nochtと衝突しがちなこと"),
            nocht.talk("気持ち悪い悪魔より、なんか愛嬌あったり、どこか憎めないくらいの方がいいんだって"),
            mousa.talk("できるだけ醜悪じゃないとシナリオ的に困るそうだ。面倒なこった"),
            nocht.talk("美人ならいくらでも描いてやるのに"),
            mousa.talk("でもオネエチャンを撃ち殺すゲームは作りたくねえなあ"),
            nocht.talk("違いない"),
            nocht.do("二人笑い"),
            irene.do("彼女は呆れて"),
            irene.talk("とにかく九月のプレイベントには何とかＰＶ回せるようにね"),
            nocht.talk("了解"),
            nocht.explain("今十一月発売のソフトを懸命に作っていた"),
            w.comment("今までに作ったソフトを軽く紹介する。パッケージを置いておき、売上とか、内容とか、評価とかをさらっと触れる"),
            ## NOTE
            ##  普段の仕事などの、ノクトの身の回りのことと、ゲームのAIがテーマっぽいとミスリード
            stage=w.on_office_int,
            )

def sc_bothdistance(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    mirei = W(w.mirei)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("二人の距離は",
            nocht.be("仕事が終わり、行きつけのカフェバーで夕食中"),
            w.comment("カフェバー初登場、今後もよく登場するのでしっかり描写しておくこと"),
            inside.look("カフェバーの様子。客席はカウンターとテーブル席で全体で三十程度",
                "カウンターの裏にはアルコールの色とりどりのボトルが並ぶ棚"),
            mirei.be("ホール係の赤毛の娘"),
            mirei.do("注文したプレートを持ってくる"),
            nocht.do("端末を置いて、$asahiとメッセージをやり取りしている"),
            _.talk("去年出したゲーム（古い洋館をめぐり、バケモノ退治しつつ宝探しをして回る）がそれなりに売れて、今回は飛躍の機会なんだけど"),
            asahi.voice("またバケモノを殺すゲーム？"),
            nocht.talk("人殺しのゲームよりマシだろうって"),
            _.do("ＦＰＳやＴＰＳと呼ばれるオンラインを通じて対戦可能な銃を使ったゲームが流行していた"),
            nocht.talk("$asahiはゲームはやらないと言っていたね"),
            asahi.voice("仕事中にずっとデータと格闘しているのに、仕事を離れてまでもモニタをじっと見ていたくはないわ",
                "それこそ美味しいものを食べたり、ワインを飲んだり、音楽を聞いたり、そういったことの方が貴重だと思う"),
            nocht.talk("それは確かにその通りだ",
                "$meもそこまでゲームには乗り込めない。あくまで仕事だからね",
                "だからそれ以外は絵を描く",
                "そういえば、昨日の絵は気に入ってくれたかい？",
                "$asahiの意見を参考に、ちょっと風景画っぽい路線でせめてみようと思ってさ"),
            _.do("思い立って仕事の絵の合間に描き上げたのは、氷原をペガサスが駆け抜ける場面だった",
                "その背後にはオーロラが揺らめいている",
                "黙っていたがペガサスは$asahiのイメージだった"),
            asahi.voice("とても素敵だったわ",
                "そういえば気づいたことがあるんだけど、あなたの絵は天使や神以外にもオーロラってモチーフがあるのね"),
            nocht.talk("言われてみればそうだ",
                "どうしても空を描くと何か物足りなさを感じて、そこにあれを追加したくなる",
                "小さい頃から何度も見てきたものだからだろうか"),
            asahi.voice("そういえば小さい頃から不思議な体験をしてきた、と言っていたわね"),
            nocht.talk("ああ、そうだよ",
                "実は昨日も、アレがあった",
                "$meはコンビニに強盗に入った男を取り押さえたんだけど、その時にライフルで撃たれてね",
                "普通なら腕の一本くらい吹っ飛んでいてもおかしくないのに、かすり傷で済んだんだ"),
            asahi.voice("無茶をするのね", "でもそれはただの幸運では？"),
            nocht.talk("幸運というものは、神様の恵みでしかない",
                "と神父に言われたことがある",
                "だから普段の行いを大切にしなさい、とね",
                "$meはまずまず神様のことを信頼しているけれど、科学的に存在するとは思ってない"),
            nocht.do("＜神についての考えを＞"),
            ## NOTE
            ##  オーロラの話
            stage=w.on_cafebar_int,
            )

def sc_hismind(w: World):
    nocht, asahi = W(w.nocht), W(w.asahi)
    mousa, irene = W(w.mousa), W(w.irene)
    return w.scene("本当に作りたいもの",
            nocht.be(),
            _.do("ゲームの開発について$mousaと話していた"),
            mousa.be(),
            mousa.talk("どう思うって、$meらは結局あいつの指示通りに作るしかないだろ。才能ってそういうもんさ。適材適所"),
            nocht.talk("人殺しのゲームからバケモノ殺しのゲームになっただけで、やってることは何もかわらんもんな"),
            _.think("$asahiに言われたことを気にしている"),
            nocht.talk("なあ、一体$meたちは何の為にこんなゲーム作ってるんだ？"),
            mousa.talk("売って金稼ぐためじゃね？", "パンが食えなくなるのはごめんだし、酒が飲めなくなるのはもっとごめんだ"),
            nocht.talk("まあ、そうだがな"),
            mousa.talk("そもそも$meのママの国はさ、常にどんぱちやってるようなとこで、政権も軍部が握ってるし、汚職まみれでもうどうにもならねえって、",
                "酒に酔ったら愚痴るんだ",
                "一度くらいは帰って死んだパパの墓参りもしたいと思ってるけど、タクシー乗ったら銃つきつけられるなんて日常茶飯事なんだと"),
            nocht.talk("政情不安定なのは参るな"),
            mousa.talk("そういう中で暮らしているやつが、少しでも憂さ晴らしできるなら、人殺しだろうとバケモノ殺しだろうと、ゲームで楽しんでくれって思うわ"),
            nocht.think("意外と真面目な考えで笑ってしまう"),
            mousa.talk("何だよ。おかしいか？"),
            nocht.talk("えろい女の画像漁ってるだけじゃないんだなって思って"),
            mousa.talk("今はいい時代だよ",
                "だってそこら中に天国があるんだぜ？"),
            mousa.do("大笑い"),
            nocht.do("つられて笑い"),
            _.do("$asahiからのメッセージに気づく"),
            _.explain("＜彼女から何か＞"),
            stage=w.on_cafebar_int,
            time=w.at_night,
            )

## episode
def ep_gamemaker(w: World):
    return w.episode("1-3.ゲームメーカー",
            sc_programmer(w),
            sc_bothdistance(w),
            sc_hismind(w),
            ## NOTE
            ##  - ノクトはインディーズのゲームメーカーに勤めていた
            ##  - 開発しているのは新規IPで今までの人間同士の殺し合いから、ちょっと変わっている
            ##  - アサヒは人殺しのゲームばかり作って楽しいの、と質問するが
            note="$nochtはインディーゲームのメーカーに勤務していた。それは人間同士やバケモノ同士で殺し合う、陰惨な内容のものだった")
