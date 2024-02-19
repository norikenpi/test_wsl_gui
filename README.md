### 使い方

1. WSL上にclone
1. WSL2 Ubuntuのターミナルで`code .` (WSL2環境で作業できる)
1. XLaunchを起動（Start no client, No Access Control）
1. 環境変数を変更`export DISPLAY=$(awk '/nameserver / {print $2; exit}' /etc/resolv.conf 2>/dev/null):0 export LIBGL_ALWAYS_INDIRECT=1`
1. pythonインタープリタがPoetryになっていることを確認（VS Cpdeなら右下に表示される）
1. scripts/test.pyを実行


> 参考
> https://qiita.com/haraken_qiita/items/6983d0ca8c0f76bd021a
