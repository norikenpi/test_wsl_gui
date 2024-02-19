import plotly.express as px
import pandas as pd
import numpy as np

# サンプルデータの生成
np.random.seed(42)
n_frames = 100
n_points = 50
df = pd.DataFrame({
    'Time': np.repeat(np.arange(n_frames), n_points),
    'x': np.tile(np.arange(n_points), n_frames) + np.random.normal(size=n_frames*n_points),
    'y': np.tile(np.arange(n_points), n_frames) + np.random.normal(size=n_frames*n_points)
})

# アニメーション化された散布図の作成
fig = px.scatter(df, x='x', y='y', animation_frame='Time', range_x=[-20,70], range_y=[-20,70])

# アニメーションの表示
fig.show()

