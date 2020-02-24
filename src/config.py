# -*- coding: utf-8 -*-
"""Story config.
"""
################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) STAGES
#       舞台基本設定
# 3) DAYS
#       年月日設定
# 4) TIMES
#       時間帯基本設定
# 5) ITEMS
#       小道具設定
# 6) WORDS
#       辞書設定
# 7) RUBIS
#       ルビ設定
# 8) LAYERS
#       レイヤ設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 誕生日 / 性別 / 職業 / 呼称 / 紹介
        ("nocht", "ノクト", "", 30,(1,1), "male", "SE", "me:ボク"),
        ("asahi", "アサヒ", "", 32,(1,1), "female", "SE", "me:私"),
        ("erucco", "エルッコ", "", 45,(1,1), "male", "神父", "me:ワタシ"),
        ("irene", "アイリーン", "", 40,(1,1), "female", "上司", "me:私"),
        ("mousa", "ムサ", "", 28,(1,1), "male", "SE", "me:俺"),
        )

AREAS = (
        # Tag / 名前 / x,y / 備考
        ("Finland", "フィンランド", 2456,6010,),# ヘルシンキ
        ("Tampere", "タンペレ", 2376,6149),
        ("Turku", "トゥルク", 2227,6052),
        )

STAGES = (
        # Tag / 名前 / エリア / 紹介
        ("church", "教会", "Tampere"),
        ("apart", "ノクトのアパート", "Tampere"),
        ("office", "ゲーム開発室", "Tampere"),
        ("market", "スーパー", "Tampere"),
        ("cafebar", "カフェバー", "Tampere"),
        ("labo", "ラボ", "Tokyo"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("autumnday", "秋のある日", 10,20, 2017),
        ("winterday", "冬のある日", 2,20, 2018),
        ("stoplabo", "ラボ停止日", 12,24, 2048),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        )

WORDS = (
        # Tag / 名前 / 紹介
        )

RUBIS = (
        # Base / Rubi / Type
        )

LAYERS = (
        # Key / Title / Words
        )

