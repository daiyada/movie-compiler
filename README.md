# movie-compiler
簡単な動画編集が可能


## 使用方法
### 1. 環境構築
```
$ pip install -r requirements.txt
```


### 2. 実行ファイル
- imgs2movie.py  
frame id を付与された file 群を動画データに変換する
- cut.py  
config/cut.yamlの設定値に則って、特定の動画を切り出す
- concatenate.py  
config/concatenate.yamlの設定値に則って、動画を合体する
    - 注意画像サイズは同じもので（後に変更対応できるようにしようとは思っています。）
    - fourcc, fps等はmovie_1に合わせています（ここも今後のPJ次第では変更しようかと思っています。）
- change_fps.py
    - 動画のfpsを変更する
        - 元の動画のfps未満にしか調整はできない
- change_resolution.py
    - 動画の解像度を変更する
- movie2gif.py
    - movieからgifに変換する


### 3. 設定ファイル  
configフォルダ内に格納  
- cut.yaml  
cut.pyの設定値を記したファイル。以下を設定可能。
    - start_time -> 切り出し開始時間（単位：秒）
    - end_time -> 切り出し終了時間（単位：秒）
    - input_path -> 元動画の絶対パス
    - output_dir -> 切り出した動画の格納先（ディレクトリ）  

- concatenate.yaml  
concatenate.pyの設定値を記したファイル。以下を設定可能。
    - concatenate_type -> 2動画か4動画を合体するか選択
    - arrangement -> 縦並びにするか横並びにするか
    - input -> 合体する動画の絶対パス
    - ourput
        - file_name -> 合体した動画のファイル名
        - dir -> 合体した動画の格納先
        - ext -> 合体した動画の拡張子
        - title -> 合体する動画それぞれのタイトル
        - color -> タイトルの文字の色
        - coordination -> それぞれの元動画にタイトルを表示する位置
        - fontsize -> タイトルの文字サイズ
        - thickness -> タイトルの文字の太さ

    **[ 注意 ]**  
        - adjust_fps.py, adjust_resolution.py, movie2gif.py の設定値は Argparser を使って設定する