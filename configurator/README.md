# Configurator

`configurator` は、roboapp の各種設定を実行し、systemd サービスとしての管理を容易にするためのツールです。

## 特徴

- アプリケーションの systemd サービス登録
- 自動起動の設定・解除
- アプリケーションの起動・停止状態の管理
- `autostart.toml` による宣言的なサービス管理

## 環境構築

このディレクトリで以下を実行します：

1. 依存関係のインストール

   - ```bash
     mise install
     ```

2. Python 依存パッケージのインストール
   - ```bash
     mise deps
     ```

## 実行方法

- `mise start` or `uv run python3 src/configurator/main.py` で実行します。

### 起動設定のインストール

- アプリケーションの起動設定をインストールします。
自動起動は `autostart.toml` の設定に基づいて行われます。

#### autostart.toml の仕様

- 各アプリケーションごとにテーブル（例: `[app_name]`）を作成します。
- フィールド:
  - `working_dir` (**必須**, 文字列): 実行時の作業ディレクトリ
  - `executable` (**必須**, 文字列): 実行ファイル名またはパス
  - `args` (**任意**, 文字列または配列): コマンドライン引数（省略可、配列またはスペース区切り文字列）

##### 例

```toml
[my_app]
working_dir = "/home/usper/my_app"
executable = ".venv/bin/python3"
args = ["main.py", "--option", "value"]

[another_app]
working_dir = "/opt/another"
executable = "/opt/another/bin/start.sh"
args = "--debug"
```

### Roboappの起動・停止

- 起動設定のインストールが完了している場合に実行します。
- systemd サービスとして登録されているアプリケーションを起動・停止します。

### Roboappの自動起動の設定・解除

- 起動設定のインストールが完了している場合に実行します。

- systemd サービスとして登録されているアプリケーションの自動起動を設定・解除します。
- PC起動時に自動的にアプリケーションを起動したい場合、有効化してください。
