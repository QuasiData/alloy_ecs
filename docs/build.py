from pathlib import Path
import argparse
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS_BUILD = ROOT / "build" / "docs"
API = DOCS_BUILD / "site" / "html"
SITE = ROOT / "build" / "site"
DOCS_TARGET = "alloy_ecs_docs"


def run(*args: str | Path) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def build() -> None:
    run("cmake", "-S", "docs", "-B", DOCS_BUILD, "-G", "Ninja")

    if API.exists():
        shutil.rmtree(API)
    run("cmake", "--build", DOCS_BUILD, "--target", DOCS_TARGET)

    run("zensical", "build", "--clean")
    for index in (API / "index.html", SITE / "index.html"):
        if not index.is_file():
            raise FileNotFoundError(f"Missing generated page: {index}")
    shutil.copytree(API, SITE / "api")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Alloy documentation.")
    parser.add_argument("--serve", action="store_true", help="Serve after building")
    parser.add_argument("--port", type=int, default=8000, help="HTTP server port")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("--port must be between 1 and 65535")

    build()
    if args.serve:
        print(f"Serving http://127.0.0.1:{args.port}/", flush=True)
        try:
            run(sys.executable, "-m", "http.server", str(args.port),
                "--bind", "127.0.0.1", "--directory", SITE)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
