# Localize displayed speaker names without changing Ren'Py character identifiers.
init 999 python:
    _jp_sayer_names = {
        "aoi": "葵",
        "asuka": "明日香",
        "child": "子ども",
        "children": "子どもたち",
        "comment": "コメント",
        "doctor": "医者",
        "friend": "友達",
        "friends": "友達たち",
        "irina": "イリーナ",
        "kazunari": "一成",
        "madoka": "窓果",
        "masaya": "晶也",
        "minori": "実里",
        "misaki": "みさき",
        "mother": "母",
        "perin": "ペリン",
        "rika": "莉佳",
        "saki": "沙希",
        "satou": "佐藤院",
        "see": "警備員",
        "shion": "紫苑",
        "teacher": "先生",
        "together": "みんな",
        "together2": "みんな",
        "two": "二人",
        "x1": "ルミッチ",
        "x2": "エリック",
        "x3": "ギルベルト",
        "zx2": "みんな",
    }

    for _jp_sayer_id, _jp_sayer_name in _jp_sayer_names.items():
        _jp_sayer = getattr(renpy.store, _jp_sayer_id, None)
        if _jp_sayer is not None:
            _jp_sayer.name = _jp_sayer_name
