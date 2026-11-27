# OD Seed

WordPress ブロックテーマ開発用のスターターテーマです。最小対応バージョンとローカル開発環境の WordPress は 7.1.5 です。

## ローカル環境を起動する

Node.js 24、npm、Docker Compose を利用できる Docker 環境を用意します。`nvm` を使っている場合は、リポジトリのルートで `nvm use` を実行すると `.nvmrc` のバージョンに切り替わります。Docker を起動してから、次のコマンドを実行します。

```sh
npm ci
npm run env:start
```

`wp-env` がこのディレクトリをテーマとしてマウントし、起動時に有効化します。テーマのスラッグと一致するよう、チェックアウト先のディレクトリ名は `od-bt-seed` にします。

- [フロントページ](http://localhost:8888/)
- [WordPress 管理画面](http://localhost:8888/wp-admin/)（ユーザー名 `admin`、パスワード `password`）
- [サイトエディター](http://localhost:8888/wp-admin/site-editor.php)

## 開発コマンド

| コマンド | 用途 |
| --- | --- |
| `npm run env:start` | 開発環境を起動 |
| `npm run env:status` | 起動状態と URL を表示 |
| `npm run env:logs` | ログを表示 |
| `npm run env:cli -- theme list` | WP-CLI でテーマを一覧表示 |
| `npm run env:stop` | データを残して環境を停止 |

ポートを変更する場合は、リポジトリのルートに `.wp-env.override.json` を作り、たとえば `{"port": 8890}` と記述します。接続先は `npm run env:status` で確認できます。

GitHub Actions はテーマの有効化、パターンの登録、投稿一覧と検索結果が空の場合の表示を確認します。

## テーマファイル

- `theme.json` で配色、書体、文字サイズ、余白、コンテンツ幅を設定します。
- `templates/` には投稿一覧、個別投稿、固定ページ、アーカイブ、検索結果、404 ページの基本テンプレートがあります。
- `parts/` にはナビゲーション付きヘッダーとフッターがあります。
- `patterns/` のセクション導入、2 カラムの紹介、FAQ はブロックエディターから挿入できます。

## 案件ごとのテーマを作る

OD Seed を有効化してサイトエディターでスタイルやテンプレートを調整し、[Create Block Theme](https://wordpress.org/plugins/create-block-theme/) で有効なテーマを複製します。案件用にテーマ名とスラッグを付け、複製したテーマを有効化してナビゲーションやテンプレートを確認します。

## リリースする

`style.css` の `Version` を更新してコミットし、`main` をプッシュします。次に、同じコミットを指すバージョンタグを作成してプッシュします。

```sh
git push origin main
git tag v0.1.0 main
git push origin v0.1.0
```

GitHub Actions でテーマの起動確認が通ると、タグのコミットとバージョンを検証し、`od-bt-seed-v0.1.0.zip` を GitHub Releases に添付します。この ZIP は WordPress の「外観 → テーマ → 新しいテーマを追加 → テーマのアップロード」からインストールできます。

ローカルで同じ ZIP を生成するには、Python 3.9 以降で `python3 scripts/package-theme.py v0.1.0 dist` を実行します。
