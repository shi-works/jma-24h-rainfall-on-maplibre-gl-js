import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# CSVファイルを読み込み、DataFrameに格納する
df = pd.read_csv('ame_24h_20230714-20230717.csv', dtype=str, encoding='utf-8')

# '緯度(度)_10進数'と'経度(度)_10進数'の列を浮動小数点数に変換する
df['緯度(度)_10進数'] = df['緯度(度)_10進数'].astype(float)
df['経度(度)_10進数'] = df['経度(度)_10進数'].astype(float)

# '期間最大値（mm）'列を浮動小数点数に変換する
df['期間最大値（mm）'] = df['期間最大値（mm）'].astype(float)

# '緯度(度)_10進数'と'経度(度)_10進数'の列を使って新しい列'geometry'を作成する
# この'geometry'列は、各行の緯度と経度を基にPointオブジェクトを作成する
df['geometry'] = df.apply(lambda row: Point(
    row['経度(度)_10進数'], row['緯度(度)_10進数']), axis=1)

# GeoDataFrameを作成する
gdf = gpd.GeoDataFrame(df, geometry='geometry')

# GeoDataFrameをGeoJSONファイルとして出力する
gdf.to_file('ame_24h_20230714-20230717.geojson',
            driver='GeoJSON', encoding='utf-8')
