# About "量子コンピュータ" material

量子コンピュータが現実味を帯びてきている。2011年5月にカナダのベンチャーD-Wave社が「世界初の商用量子コンピュータ」を謳ったD-Wave Oneを発表したのを皮切りに、2013年5月にNASA、Google等が共同で後継機D-Wave2を導入し、量子コンピューティングAI研究所(Quantum Computing AI Lab)を開始した。この頃から徐々に実用化への懐疑的な見方は影をひそめ、実現への期待が大きくなってきた。2016年5月にIBMが量子コンピュータをクラウド公開し、日本でも2017年11月に国立情報学研究所 (NII)、NTT、東京大学が内閣府の革新的研究開発推進プログラム (ImPACT) において量子ニューラルネットワーク（Quantum Neural Network: QNN）をクラウドで公開した。この領域の研究者の成果について、利用する立場からも注視していく時期に入ってきたと思われる。

幅広く捉えた場合、量子コンピュータには大きく2種類あると考えて良いと思われる。デジタル型とアナログ型である（図1）。

デジタル型は量子ゲート型とも言われる。量子ビットと呼ばれるものを最小単位として演算をしていくもので、古典的コンピュータのように、汎用的に利用できるものを目指して研究開発が進められている。量子ビット(quantum bit, qubit)というのは、量子情報の最小単位で、古典的コンピュータの情報の最小単位ビット(bit)と異なり、0と1だけでなく、0と1の重ね合わせの状態をとることができるものだ。量子ビットを実現するために、イオンや超伝導電気回路等が研究されている。実際に演算を実現するには、量子状態を自在に操り、長時間保持し続けることが必要であり、これを満たしつつ、演算の高速化の鍵である量子ビット数を増やすことに注力されている。

アナログ型には、量子アニーリング型と量子ニューラルネットワーク型といったものがあるが、これらの原理を応用し半導体技術を使ったものも本稿では見ていきたい。これらアナログ型はイジングマシンとも呼ばれるもので、量子現象をアナログ的に使い、特定の問題の解決に特化したものと言える。量子アニーリング型は、日本の東京工業大学の西森教授らによって基本理論が考えられた。上述したとおり2011年にはカナダのベンチャー企業D-Wave社により商用化されている。量子ニューラルネットワーク型はコヒーレント・イジング・マシン(Coherent Izing Machine: CIM)とも呼ばれ、光のパルスと半導体素子であるFPGAを使って計算するものである。その他、量子力学的な振る舞いを古典的コンピュータの応用により実現することにより処理の高速化を実現するものとして、日立製作所によるCMOSアニーリングや富士通のデジタルアニーラといったものがある。

量子コンピュータの定義については国際学会で議論されていると言われ、上記の方式のどれが定義に合致するのかまだ分からないが、本稿では名称の如何にかかわらず、より良いものをより早く使いたいという利用者の立場から話を進めたい。

## いつ頃使えるようになるのか?
それぞれの方式で研究開発が加速しているところであるが、方式毎にそのフェーズは異なる。汎用を目指しているデジタル型すなわち量子ゲート型は研究段階、量子アニーリング型と量子ニューラルネットワーク型等のアナログ型は商用に近づこうとする段階と言える。

＜デジタル型＞
まず、量子ゲート型について見ていきたい。量子ゲート型の進歩は、大まかには量子ビットの数や寿命で捉えられる(図2)。光、イオン等、様々な物理現象が量子ビットの表現方法として提案されている。何れも数個の量子ビットという段階であるが、年内に、数十個の量子ビットを実現するというのが目標になっているようだ。50個の量子ビットが実現すると、古典的コンピュータを上回る能力を示すことが可能になり(「量子超越」という)、一つの目標となっているのである。一方、エラーを訂正しながら大規模な計算をするには1万～1億個の量子ビットが必要とされている。

以下に各社の取り組みを紹介する。

Google
2018年3月にGoogleの量子AI研究所は72量子ビットの量子プロセッサBristleconeを発表した(図3)。Googleはカリフォルニア大学サンタバーバラ校John Martinis（ジョン・マルティニス）教授の開発グループを2014年に迎えて以降、開発を加速させている。同社が行っているのは超伝導素子を用いるアプローチである。

ジョン・マルティニス教授は「2018年中に量子超越を示せるだろう。」「量子超越を示すには50個の量子ビットに40回の演算をさせる必要があり、それにはエラー率0.2%の量子ビットが要る」「ハードな目標だが、他のグループは私たちよりエラー率が1桁高く、もっと難しいだろう。」「2018年中に私たちの量子コンピュータをクラウド化する。」と述べている。

Googleの量子プロセッサ” Bristlecone”
【図３】Googleの量子プロセッサ” Bristlecone”
（出典：https://research.googleblog.com/ 2018/03/a-preview-of-bristlecone-googles-new.html）

Intel
Intelは2018年1月に49量子ビットの量子チップTangle Lakeを開発したと発表した。絶対零度(-273℃)で動作する超伝導による量子チップで2017年の17量子ビットから大きく進歩している。Intelは超伝導ではない量子ビットの研究開発にも取り組んでいる。スピン量子ビットと呼ばれるもので、半導体であるシリコン上で動作するものだ。既存の半導体製造工程である300mmプロセスの技術を使ってスピン量子ビットを製造するフローも発明したとしている。

IBM
IBMは2017年5月に16量子ビットの量子コンピュータを発表した。これも超伝導による量子コンピュータで絶対零度近くまで冷却する必要があるものだ。また、2016年には"IBM Q Experience"という名前でクラウドを通して誰もが利用できるように公開し、2017年12月には有料での提供も始めた。この"有料"というのは商用ベースではなく、”利用者へコストの負担を前提に共同研究を呼びかける”というスタンスとなっている。IBMは量子コンピュータそのものの研究開発だけでなく、コミュニティ化することにより、ソフト等利用段階を見据えた取り組みを行っているのである。

現状についてIBMのJay Gambetta（ジェイ・ガンベッタ）Manager、Jerry Chow（ジェリー・チョウ）Managerは「私たちは50～100量子ビットの量子コンピュータを手にしようとしている。」と言っている。

IonQ
IonQはメリーランド大学などの研究者らが2016年に設立したベンチャーである。IonQの量子コンピュータはGoogle等と異なり、電場の力で空中に浮かべたイオンの列を量子ビットとして使う。精密な原子時計にも使われている技術で、超伝導と並ぶ有力候補とされる。どの量子ビットも他のすべてのビットと直接結合できるのが超伝導にはない特徴で、アルゴリズムを容易に実装できる。

中心人物のデューク大学Jungsang Kim（ジュンサン・キム） 教授は「ここ5年以内に量子コンピュータがスーパーコンピュータに対抗できるとは思わないが、古典コンピュータではなく、量子コンピュータの独特の特性にマッチした問題が、我々の知らないどこかにあると思う。」「この分野の研究者の多くは物理学者だ。量子ビットの作り方や、ゲートの操作の実現法といったことばかり考えてきた。だがこれからは、システム全体を考えなくてはいけない。コンピュータアーキテクチャの専門家や回路の設計家など、物理学者以外の専門家とのコラボレーションを増やしていく必要がある。」と言っている。

<アナログ型>
アナログ型には、量子アニーリング型、量子ニューラルネットワーク型等いくつかのタイプがあるが(図1)、この中にはD-Wave社の量子コンピュータのように既に商用化されているものもある。今後はビット数やビット間の結合の仕方（結合グラフ、図4）が注目すべきポイントとなるだろう。ここでビット間の結合というのは1つの量子ビットがどのように他の量子ビットにつながっているかということであり、すべての量子ビットが他のすべての量子ビットとつながっている場合、全結合と呼ばれ、そのような形態は完全グラフと呼ばれている。部分的につながっていても計算は可能だが、全結合と同様な演算をするためには複数のビットを使うことになるため、全結合換算ビット数を見ておく必要がある。もちろん、実用面では、消費電力や本体の大きさ等も普及のための大きな要素となっていくだろう。

様々なグラフ
【図４】様々なグラフ
（出典：https://quantum.fixstars.com/introduction_to_quantum _computer/quantum_annealing/ising_model/（左）
https://en.wikipedia.org/wiki/King's_graph（中）
https://www.quora.com/What-is-a-chimera-graph（右））

以下に各社の取り組みを記述する（表1）。

各アニーリングマシンの比較
【表１】各アニーリングマシンの比較
（出典：https://quantum.fixstars.com/introduction_to_quantum_computer/quantum_annealing/programming/）

D-Wave
初めて量子コンピュータを商用化したD-Wave社は2年毎に量子プロセッシングユニット(Quantum Processing Units: QPUs)の量子ビット数を2倍にするとしていたが、2017年1月には、その宣言どおり、1000量子ビットを搭載した"D-Wave 2X"（2015年8月発表）の2倍にあたる2048量子ビット搭載を達成した"D-Wave 2000Q"を発表した。D-Waveはニオブという金属が極低温(9.2K)になると超伝導状態になり、電流が量子論的な振る舞いをすることを利用している。

NII・NTT他
NII、NTT、スタンフォード大学、東京大学、大阪大学、東北大学、東京理科大学は、ImPACTの支援を受け研究開発したQNN（図5）を2017年11月にクラウドで公開した。上述のとおり、これはCIMとも呼ばれており、NTTはこの技術を用いたコンピュータをLASOLVと呼んでいる。全結合(完全グラフ)で2048ビットを実現している。物理現象としてパルス光を使っているのが特徴で、このため、超伝導のような極低温の環境を必要とせず、消費電力や本体の大きさといった面で普及に向けた有利な要素を備えている。

量子ニューラルネットワーク(QNN)
【図５】量子ニューラルネットワーク(QNN)
（出典：http://www.ntt.co.jp/news2017/1711/171120a.html）

日立
日立は量子アニーリング型の動作を半導体チップ上で模するCMOSアニーリングと呼ばれる技術に取り組んでいる。2015年に第1世代を発表し、現在、第2世代の開発、ソフトウェアの拡充へと進んでいる。これは量子力学的現象そのものを利用するのではなく、古典的コンピュータの技術にランダムな要素を加えることにより、高速に最適解を得ることを可能にしたものである。ビット数で2万を超え、全結合換算でも128ビットを超えるとされている。

CMOSアニーリングチップは、従来の半導体技術で作られているため、多くの量子力学的現象を使ったコンピュータで必要な極低温への冷却が不要で、室温でも作動する。そのため管理も比較的容易で、大規模化にも容易に対応できるとのことだ。また、通常のコンピュータと比べて1,800倍の電力効率を実現し、エネルギー消費量の大幅な低減も可能になると言う。

富士通
富士通研究所はカナダのトロント大学と共同開発でデジタルアニーラという技術を開発している。これは量子アニーリング型の動作をデジタル回路で高速に実行できるようにしたものだ。2016年10月の発表では1024ビットで全結合であることを訴求している。

## Comment

これまで述べてきたとおり、利用者としては、当面、アナログ型をどう使うのかを考えるのが第一歩と言えるだろう。

これまで、組合せの数が多過ぎて"しらみつぶし"、"総当たり"で調べるには膨大な時間がかかり事実上解けなかった問題でも量子コンピュータを使えば短時間でより正確な解が求められるようになる訳である。化学の領域では新材料や新薬の開発において分子の並べ方を検討する際に使えると考えられているし、交通や通信のように様々な経路を取り得るものでは最適化に使えると考えられている。また、AIの学習アルゴリズムの開発にも適用できると考えられている。

また、今後は、量子コンピュータというハードをどう使うかについても考えていく必要がある。現在、IBMやNTTがクラウドで量子コンピュータを使えるように公開しているが、今後、APIなどで外部から使いやすくする等の動きも出てくるかもしれない。

広い意味でのソフトウェアも大切である。ソフトウェアを開発する際には、対象となる問題を量子コンピュータの能力が発揮できるように再構成し、プログラムに載せる必要がある。デジタル型、すなわち量子ゲート型向けの基本は、古典的コンピュータが0,1を表すビットであるのに対し、0,1の重ね合わせを表す量子ビットであり、プログラム言語も異なってくる。現時点での量子プログラミング言語としては、最初に実装されたQCL(Quantum Computation Language)、2番目のQ言語(Q Language)などがある。2017年12月にはMicrosoftが量子コンピュータ用ソフトウェア開発環境のQuantum Development Kitの無料プレビュー版をリリースしたが、この中には新たに開発されたQ#言語が入っている。C言語等の既存のコンピュータ言語とほぼ同様な開発環境が簡単に手に入るようになってきた訳である。こういった環境にも注視が必要だ。

アナログ型については組合せ最適化問題に特化していることもあり、既存の古典的コンピュータとの連携が重視されていくだろう(図6)。富士通研究所が量子コンピュータ向けのソフトウェアを開発しているカナダの1QBit社との協業を2017年に開始したことも注目すべき動きだ。日立もCMOSイジング計算機の実用化に向けて、組合せ最適化問題のイジングモデルへのマッピングやハードウェアへの埋め込みを研究しており、現実の問題への適用を見据えているようだ。既にクラウドに公開しているNTT・NIIも含めて日本の各社の取り組みからは目が離せない。

量子コンピュータと聞くと、物理の教科書を思い出して及び腰になってしまいそうだが、よく考えると半導体の原理を知らなくても、スマートフォンも電卓も皆が使っている。新たな技術が一日でも早く、簡単に使えるようになることを期待したい。

## Notes

## References

- [量子コンピュータ](https://www.icr.co.jp/newsletter/wtr349-20180427-onodera.html)

---
(C)2020 N.T.Works