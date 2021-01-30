# HEIC-PNG_convert

iPhoneで撮った画像をパソコンで扱う際、HEIC形式からpng形式に変換するために作成した。
また、画像をリサイズするファイルも作成した。

conv.py: iPhoneで撮ったHEIC形式の画像をpng形式に変換。
png_resize.py: png形式にした画像をリサイズして小さくする。

heic
png
resize
という３つのフォルダも同じディレクトリ内に必要。

heicフォルダに元画像を入れればpngフォルダに変換後の画像が保存される。
画像をリサイズしたい場合はpng_resize.pyを実行すればresizeフォルダに画像が保存される。

参考元:
[Pythonで指定ディレクトリのHEICファイルをJPEGへ変換する](https://qiita.com/Tak3315/items/c0dc8b4d81ed2a582f22)
[Python, Pillowで画像を一括リサイズ(拡大・縮小)](https://note.nkmk.me/python-pillow-image-resize/)
