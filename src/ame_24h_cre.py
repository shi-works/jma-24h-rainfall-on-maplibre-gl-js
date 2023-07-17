import pandas as pd

# 元のCSVをDataFrameに読み込む（全ての列を文字列として読み込む）
df = pd.read_csv('ame_master_20230323.csv', dtype=str, encoding='cp932')

# 緯度(度)と経度(度)を10進数に変換（数値として計算するために一時的に浮動小数点数に変換）
df['緯度(度)_10進数'] = df['緯度(度)'].astype(float) + df['緯度(分)'].astype(float)/60
df['経度(度)_10進数'] = df['経度(度)'].astype(float) + df['経度(分)'].astype(float)/60

# 緯度と経度の10進数変換結果を文字列に戻す
df['緯度(度)_10進数'] = df['緯度(度)_10進数'].astype(str)
df['経度(度)_10進数'] = df['経度(度)_10進数'].astype(str)

# 追加のCSVをDataFrameに読み込む（全ての列を文字列として読み込む）
df_additional = pd.read_csv(
    'pre24h_mx00_20230714-20230717.csv', dtype=str, encoding='cp932')

# 観測所番号で結合
df_combined = pd.merge(df, df_additional, on='観測所番号', how='left')

# 結果をCSVに書き出す
df_combined.to_csv('ame_24h_20230714-20230717.csv',
                   index=False, encoding='utf-8')
