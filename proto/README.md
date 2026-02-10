# Proto

このディレクトリには、roboapp で使用される共通の Protobuf 定義ファイルが含まれています。

## ファイル一覧

- `camera_port.proto`: カメラポート情報の定義
- `camera_switch.proto`: カメラ切り替え制御の定義
- `damage_panel.proto`: ダメージパネル状態の定義
- `disks.proto`: ディスク（ストレージ）情報の定義
- `flap.proto`: フラップ制御の定義
- `lidar_range.proto`: LiDAR 距離データの定義
- `lidar_vector.proto`: LiDAR ベクトルデータの定義
- `robot_state.proto`: ロボット全体のステータス定義

## 管理ツール

Protobuf のフォーマットとリンターには [buf](https://buf.build/) を使用しています。

```bash
# フォーマット
buf format -w

# リンター
buf lint
```
