"""Convert all 200 benchmark PDFs with a tool of your choice, in the layout the evaluator expects.

    python scripts/convert_all.py path/to/opendataloader-bench my-tool my_converter:convert

The last argument is your own code: a module in the current folder and a function in it that takes a PDF
path (str) and returns the Markdown (str). Then score it:

    python scripts/score_outputs.py path/to/opendataloader-bench --engine my-tool

For a website: download its Markdown by hand, save each file as
prediction/<my-tool>/markdown/<same name as the PDF>.md, and run the score command.
"""
import importlib
import json
import platform
import sys
import time
from pathlib import Path


def main():
    if len(sys.argv) != 4 or ":" not in sys.argv[3]:
        raise SystemExit(__doc__)
    bench, name = Path(sys.argv[1]).resolve(), sys.argv[2]
    module, func = sys.argv[3].split(":", 1)
    sys.path.insert(0, str(Path.cwd()))
    convert = getattr(importlib.import_module(module), func)
    out = bench / "prediction" / name
    (out / "markdown").mkdir(parents=True, exist_ok=True)
    pdfs = sorted((bench / "pdfs").glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"no PDFs in {bench / 'pdfs'} (the benchmark keeps them in Git LFS: run 'git lfs pull')")
    failed, start = [], time.time()
    for pdf in pdfs:
        try:
            text = convert(str(pdf))
        except Exception as e:  # a failed file scores as an empty answer
            failed.append(f"{pdf.stem}: {type(e).__name__}: {e}")
            text = ""
        (out / "markdown" / f"{pdf.stem}.md").write_text(text, encoding="utf-8")
    total = time.time() - start
    (out / "summary.json").write_text(json.dumps({
        "engine_name": name, "engine_version": "", "processor": platform.processor(),
        "document_count": len(pdfs), "total_elapsed": total, "elapsed_per_doc": total / len(pdfs),
        "date": time.strftime("%Y-%m-%d")}, indent=2), encoding="utf-8")
    print(f"{len(pdfs)} PDFs in {total:.0f} s, {len(failed)} failed")
    for line in failed:
        print(" ", line)


if __name__ == "__main__":
    main()
