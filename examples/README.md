# Examples

`examples` ディレクトリには、roboapp の Protobuf 定義と [Zenoh](https://zenoh.io/) を使用した通信のサンプルコードが含まれています。

## ディレクトリ構成

- `src/examples/pub/`: 各種センサデータやステータスを配信するパブリッシャーのサンプル
  - `camswitch.py`, `damagepanel.py`, `disk.py`, `flap.py`, `lidar_range.py`, `lidar_vector.py`, `robot_state.py`
- `src/examples/sub/`: 配信されたデータを購読するサブスクライバーのサンプル
  - `all.py` (すべてのメッセージを購読), `hz.py` (メッセージの頻度を計測)

## 環境構築

1. 依存関係のインストール
   ```bash
   mise install
   ```

2. Python 依存パッケージのインストール
   ```bash
   mise deps
   ```

## 実行方法

`uv` を使用してサンプルプログラムを実行できます。

```bash
# 例: ロボットのステータスを配信
uv run python src/examples/pub/robot_state.py

# 例: すべてのメッセージを購読して表示
uv run python src/examples/sub/all.py
```

## 注意事項



これらのサンプルを実行するには、Zenoh ルーターが動作している必要があります。

`configurator` を使用して `roboapp-zenohd.service` をセットアップするか、ローカルで `zenohd` を実行してください。


