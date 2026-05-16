catalog = {
    "あいみょん": [
        ("0xSiBpUdW4E", "マリーゴールド"),
        ("yOAwvRmVIyo", "裸の心"),
        ("9qRCARM_LfE", "愛を伝えたいだとか"),
    ],
    "YOASOBI": [
        ("ZRtdQ81jPUQ", "アイドル"),
        ("x8VYWazR5mE", "夜に駆ける"),
        ("Y4nEEZwckuU", "群青"),
    ],
}

videos = [
    {"id": vid, "title": title, "artist": artist}
    for artist, val in catalog.items()
    for vid, title in val
]
