catalog = {
    "あいみょん": [
        ("0xSiBpUdW4E", "マリーゴールド"),
        ("yOAwvRmVIyo", "裸の心"),
        ("9qRCARM_LfE", "愛を伝えたいだとか"),
    ],
    "YOASOBI": [
        ("ZRtdQ81jPUQ", "アイドル"),
        ("dy90tA3TT1c", "怪物"),
        ("x8VYWazR5mE", "夜に駆ける"),
    ],
}

videos = [
    {"id": vid, "title": title, "artist": artist}
    for artist, val in catalog.items()
    for vid, title in val
]
