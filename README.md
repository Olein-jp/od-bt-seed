# OD BT Seed

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

## テーマファイル

- `theme.json` にグローバル設定とテンプレートパーツの定義を置きます。
- `templates/` に投稿一覧などのフォールバックと、投稿・固定ページの個別表示テンプレートを置きます。
- `parts/` にヘッダーとフッターを置きます。

GitHub Actions はテーマが有効なブロックテーマとして認識されることと、フロントページに投稿一覧が表示されることを確認します。

## リリースする

`style.css` の `Version` を更新してコミットし、`main` をプッシュします。次に、同じコミットを指すバージョンタグを作成してプッシュします。

```sh
git push origin main
git tag v0.1.0 main
git push origin v0.1.0
```

GitHub Actions がタグのコミットとバージョンを検証し、`od-bt-seed-v0.1.0.zip` を GitHub Releases に添付します。この ZIP は WordPress の「外観 → テーマ → 新しいテーマを追加 → テーマのアップロード」からインストールできます。

ローカルで同じ ZIP を生成するには、Python 3.9 以降で `python3 scripts/package-theme.py v0.1.0 dist` を実行します。
