# roboapp_utils

roboapp に関する共通の Protobuf 定義、設定ツール、およびサンプルコードを管理するモノレポです。

## ディレクトリ構成

- `proto/`: 各種アプリケーションで使用される共通の Protobuf 定義
- `configurator/`: アプリケーションのシステム設定（systemd サービス登録、自動起動など）を管理するツール
- `examples/`: roboapp の Protobuf 定義を使用した Python サンプルコード

## セットアップ

このプロジェクトでは [mise](https://mise.jdx.co/) を使用してツールチェーンを管理しています。

```bash
# mise のインストール（未インストールの場合）
curl https://mise.jdx.co/install.sh | sh

# 依存ツールのインストール
mise install
```

### 実行の準備

本リポジトリのexamplesや、その他の [roboapp](https://github.com/CoRE-MA-KING/roboapp.git) と接続するツールを実行する前に、Zenoh ルーター（`zenohd`）を起動しておく必要があります。
`configurator` でセットアップ済みの場合は、以下のコマンドでサービスを起動してください。

```bash
systemctl --user start roboapp-zenohd.service
```

## 各プロジェクトの利用方法

詳細については各ディレクトリの README を参照してください。

- [Configurator](./configurator/README.md)
- [Examples](./examples/README.md)

## 開発用タスク

ルートディレクトリで以下のコマンドを実行できます：

```bash
# Protobuf のフォーマット
mise run format_proto

# Protobuf のリンター実行
mise run lint_proto

# コード生成のテスト
mise test
```
