"""Python wrapper around render.js so generators can batch HTML -> PNG/PDF jobs."""
import json
import subprocess
import tempfile
from pathlib import Path

from brand import BUILD

TMP = BUILD / ".tmp"


def write_html(name: str, html: str) -> Path:
    TMP.mkdir(parents=True, exist_ok=True)
    p = TMP / name
    p.write_text(html, encoding="utf-8")
    return p


def run(jobs: list) -> None:
    if not jobs:
        return
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, dir=BUILD) as f:
        json.dump([{**j, "html": str(j["html"]), "out": str(j["out"])} for j in jobs], f)
        jobfile = f.name
    try:
        subprocess.run(["node", str(BUILD / "render.js"), jobfile], check=True, cwd=BUILD.parent)
    finally:
        Path(jobfile).unlink(missing_ok=True)
