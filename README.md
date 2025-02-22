# Pythonプロジェクト

このリポジトリはPythonプロジェクトのボイラープレートです。

## 機能

- setuptoolsを使用したシンプルなパッケージング
- src/とtests/ディレクトリによる構造化
- メインプログラムのエントリーポイント
- pytestを使用したテスト例
- Dockerによる開発環境のサポート

## 使い方

メインプログラムの実行:

    python -m my_project.main

### Dockerを使用する場合

開発環境をDockerで構築することもできます。

1. 開発環境の起動:

```bash
docker compose up -d
```

2. コンテナ内でコマンドを実行:

```bash
# コンテナのシェルにアクセス
docker compose exec app /bin/bash
```

3. 開発環境の停止:

```bash
docker compose down
```

## テスト

テストの実行:

    pytest

### Dockerでのテスト実行

コンテナ内でテストを実行:

```bash
docker compose exec app pytest
```
