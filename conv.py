from PIL import Image
import pyheif
import pathlib
import glob

def heic_png(image_path, save_path):
    # HEICファイルpyheifで読み込み
    heif_file = pyheif.read(image_path)
    # 読み込んだファイルの中身をdata変数へ
    data = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
        )
    
    # PNGで保存
    data.save(str(save_path), "PNG")


# 変換対象のファイルがあるディレクトリ
# カレントの下のtempディレクトリを指定
image_dir = pathlib.Path('./heic')
# globでディレクトリ内のHEICファイルをリストで取得
heic_path = list(image_dir.glob('**/*.HEIC' or '**/*.heic'))

# リストのHEICファイルを１個づつPNGへ変換
for i in heic_path:
    m = "./" + str(i)
    n = './png/' + str(i.stem) + '.png'
    heic_png(m, n)
