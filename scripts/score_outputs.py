"""Re-score every tool's published output in a clone of opendataloader-bench, with one checker.

    python scripts/score_outputs.py path/to/opendataloader-bench
    python scripts/score_outputs.py path/to/opendataloader-bench --engine docling --engine marker
    python scripts/score_outputs.py path/to/opendataloader-bench --csv results/my-run.csv

It runs the benchmark's own src/evaluator.py on each folder under prediction/ and prints the means.
The result goes to prediction/<tool>/rescored.json, so the benchmark's stored evaluation.json files
stay as they are. Needs the evaluator's packages: rapidfuzz, apted, lxml, beautifulsoup4.
"""
import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

OUT = "rescored.json"
COLUMNS = ("overall_mean", "nid_mean", "teds_mean", "mhs_mean")

# Runs the evaluator with its own folder on the import path, whatever Python's safe-path setting is.
RUN = ("import runpy, sys; src, script = sys.argv[1:3]; sys.argv = [script] + sys.argv[3:]; "
       "sys.path.insert(0, src); runpy.run_path(script, run_name='__main__')")


def score(bench, engine):
    src = bench / "src"
    done = subprocess.run([sys.executable, "-c", RUN, str(src), str(src / "evaluator.py"), "--engine", engine,
                           "--output-filename", OUT, "--log-level", "ERROR"],
                          cwd=bench, capture_output=True, text=True, encoding="utf-8", errors="replace")
    result = bench / "prediction" / engine / OUT
    if done.returncode or not result.is_file():
        raise SystemExit(f"{engine}: the evaluator failed\n{done.stderr[-2000:]}")
    return json.loads(result.read_text(encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bench", type=Path, help="your clone of opendataloader-bench")
    ap.add_argument("--engine", action="append", help="one folder under prediction/ (repeat for more; default: all)")
    ap.add_argument("--csv", type=Path, help="also write the table to this file")
    args = ap.parse_args()
    bench = args.bench.resolve()
    if not (bench / "src" / "evaluator.py").is_file():
        raise SystemExit(f"{bench} has no src/evaluator.py: is it a clone of opendataloader-bench?")
    engines = args.engine or sorted(p.parent.name for p in (bench / "prediction").glob("*/markdown"))
    rows = []
    for engine in engines:
        ev = score(bench, engine)
        m, s = ev["metrics"], ev.get("summary") or {}
        means = [m["score"].get(c) for c in COLUMNS]
        missing = m.get("missing_predictions", sum(1 for d in ev["documents"] if not d["prediction_available"]))
        rows.append([engine, *means,
                     s.get("engine_version", ""), s.get("date", ""), missing])
    rows.sort(key=lambda r: -(r[1] or 0))
    head = ["tool", "overall", "text", "tables", "headings", "version", "run_date", "missing_files"]
    print(f"{head[0]:32}{head[1]:>9}{head[2]:>9}{head[3]:>9}{head[4]:>10}  {head[5]:16}{head[6]}")
    for r in rows:
        print(f"{r[0]:32}" + "".join(f"{'-' if v is None else format(v, '.3f'):>{w}}"
                                     for v, w in zip(r[1:5], (9, 9, 9, 10))) + f"  {r[5]:16}{r[6]}")
    if args.csv:
        with args.csv.open("w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([head, *([r[0], *["" if v is None else f"{v:.4f}" for v in r[1:5]], *r[5:]] for r in rows)])


if __name__ == "__main__":
    main()
