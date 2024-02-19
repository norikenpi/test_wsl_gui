### 使い方
2
＜環境＞　Poetry (version 1.7.1), WSL2 Ubuntu

1. WSL上にclone
1. WSL2 Ubuntuのターミナルで`code .` (WSL2環境で作業できる)
1. XLaunchを起動（Start no client, No Access Control）
1. 環境変数を変更`export DISPLAY=$(awk '/nameserver / {print $2; exit}' /etc/resolv.conf 2>/dev/null):0 export LIBGL_ALWAYS_INDIRECT=1`
1. pythonインタープリタがPoetryになっていることを確認（VS Cpdeなら右下に表示される）

scripts/test.pyを実行してGUIが表示されればOK
scripts/graph.pyを実行してmatplotlibのグラフが表示されればOK
scripts/animation.pyを実行してmatplotlibのグラフ動画が表示されればOK

`poetry run python -m ipykernel install --user --name=test_env --display-name="Python test_env"`で仮想環境内で ipykernel モジュールを実行し、新しい Jupyter Notebook のカーネルをユーザーの環境にインストール
`poetry run jupyter notebook --allow-root`でJupyter Notebookを起動しanimation2.ipynbを起動
plotyによる動画が表示されればOK（Jupyter Notebookを使わないでブラウザに直に表示するのは諦めた）

scripts/animation3.pyを実行してfirst_figure.htmlが作成されてホストOSでクリックしたらブラウザに表示されたらOK
scripts/animation4.pyを実行してpygameの壁に反射する円の動画が表示されればOK


> 参考
> https://qiita.com/haraken_qiita/items/6983d0ca8c0f76bd021a
