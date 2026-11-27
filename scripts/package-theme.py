import argparse
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile

THEME_SLUG = "od-bt-seed"
THEME_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = ("style.css", "theme.json", "templates/index.html", "LICENSE")
OPTIONAL_FILES = ("functions.php", "screenshot.png", "readme.txt")
THEME_DIRECTORIES = ("assets", "inc", "languages", "parts", "patterns", "styles", "templates")


def main():
    parser = argparse.ArgumentParser(description="WordPress にインストールできるテーマ ZIP を作成する")
    parser.add_argument("tag", help="style.css と一致するリリースタグ（例 v0.1.0）")
    parser.add_argument("output_dir", type=Path, help="ZIP の出力先")
    args = parser.parse_args()

    if not re.fullmatch(r"v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", args.tag):
        parser.error("タグは vMAJOR.MINOR.PATCH の形式で指定してください")

    for name in REQUIRED_FILES:
        if not (THEME_ROOT / name).is_file():
            parser.error(f"テーマの必須ファイルがありません: {name}")

    stylesheet = (THEME_ROOT / "style.css").read_text(encoding="utf-8")
    version = re.search(r"^Version:[ \t]*(\S+)[ \t]*$", stylesheet, re.MULTILINE)
    if not version or f"v{version[1]}" != args.tag:
        parser.error("リリースタグが style.css の Version と一致しません")

    files = [THEME_ROOT / name for name in (*REQUIRED_FILES, *OPTIONAL_FILES)]
    for directory in THEME_DIRECTORIES:
        files.extend((THEME_ROOT / directory).rglob("*"))

    args.output_dir.mkdir(parents=True, exist_ok=True)
    archive = args.output_dir / f"{THEME_SLUG}-{args.tag}.zip"
    with ZipFile(archive, "w", ZIP_DEFLATED) as package:
        for file in sorted(set(files)):
            relative = file.relative_to(THEME_ROOT)
            if file.is_file() and file.resolve().is_relative_to(THEME_ROOT) and not any(
                part.startswith(".") for part in relative.parts
            ):
                package.write(file, Path(THEME_SLUG) / relative)
    print(archive)


if __name__ == "__main__":
    main()
