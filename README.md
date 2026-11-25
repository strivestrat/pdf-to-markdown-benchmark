# PDF to Markdown benchmark

How well do PDF to Markdown tools keep the text, the tables and the headings? This repo holds the scores, the scripts that made the main table, and our Markdown to PDF test file, so you can check the numbers or add a tool.

Made by [StriveStrat](https://strivestrat.com). **We also make [markdownwise.com](https://markdownwise.com/?ref=github), one of the tools scored here, so read the numbers with that in mind.** Where our tool is behind, the tables show it.

## 1. 200 PDFs, scored by opendataloader-bench

[opendataloader-bench](https://github.com/opendataloader-project/opendataloader-bench) has 200 PDFs, hand-made Markdown answers and an open-source checker. It also publishes the Markdown each tool produced. We did not run the other tools ourselves: we re-scored those published outputs with one version of the checker, and scored markdownwise the same way.

Scores run from 0 to 1. Text is edit distance (reading order included), tables is tree edit distance on the 42 PDFs that have a table, headings is the outline on the 107 PDFs that have headings.

| Tool | Overall | Text | Tables | Headings | Version | Run date |
|---|---|---|---|---|---|---|
| OpenDataLoader hybrid | 0.907 | 0.934 | 0.928 | 0.821 | 2.2.1 | 2026-04-06 |
| Nutrient | 0.885 | 0.925 | 0.708 | 0.819 | 1.0.1 | 2026-04-30 |
| Docling | 0.882 | 0.898 | 0.887 | 0.824 | 2.84.0 | 2026-04-06 |
| OpenDataLoader hybrid (hydrogen) * | 0.877 | 0.926 | 0.796 | 0.769 | 2.2.1 | 2026-04-08 |
| **markdownwise** (ours) | 0.873 | 0.906 | 0.825 | 0.793 | | 2026-11-21 |
| Marker | 0.867 | 0.890 | 0.808 | 0.819 | 1.10.1 | 2026-01-06 |
| OpenDataLoader hybrid (helium) * | 0.845 | 0.879 | 0.807 | 0.755 | 0.2.0-SNAPSHOT | 2026-04-17 |
| Unstructured (hi-res) | 0.841 | 0.904 | 0.588 | 0.749 | 0.17.2 | 2026-04-06 |
| EdgeParse | 0.837 | 0.894 | 0.717 | 0.706 | 0.3.0 | 2026-04-06 |
| MinerU | 0.835 | 0.857 | 0.873 | 0.759 | 2.7.0 | 2026-01-06 |
| OpenDataLoader | 0.831 | 0.902 | 0.489 | 0.739 | 2.2.1 | 2026-04-06 |
| PyMuPDF4LLM | 0.735 | 0.885 | 0.401 | 0.424 | 0.2.0 | 2025-11-27 |
| Unstructured | 0.686 | 0.882 | 0.000 | 0.388 | 0.17.2 | 2026-04-06 |
| MarkItDown | 0.589 | 0.844 | 0.273 | 0.000 | 0.1.5 | 2026-04-06 |
| LiteParse | 0.576 | 0.866 | 0.000 | 0.000 | 1.2.1 | 2026-04-06 |

\* The benchmark publishes these two outputs under code names but leaves them out of its own results table.

What to know before you use it:

- markdownwise is fourth when compared with the 12 tools in the benchmark's own table. Counting the two code-named outputs, it is fifth. Headings are its weakest score.
- Marker's stored result in the benchmark is 0.861. It was scored with an older checker; the same Markdown scores 0.867 with the one we used. MinerU and PyMuPDF4LLM moved up too (0.831 to 0.835, 0.732 to 0.735).
- The tools have moved on since these runs. A newer version of any of them may score differently.
- We used the benchmark's output files and checker as downloaded on 2 November 2026. When we looked on 24 November, its latest commit was `7af1d8f` from May 2026.
- We have used these 200 PDFs to find and fix faults in markdownwise, and no change to it ships if its score here drops noticeably. The other tools may or may not have done the same. Try your own PDFs before you choose.

Data: [results/opendataloader-bench-200.csv](results/opendataloader-bench-200.csv), and markdownwise's score on each of the 200 in [results/markdownwise-per-document.csv](results/markdownwise-per-document.csv).

## 2. Free online converters on 9 pages

Nine pages from [olmOCR-bench](https://huggingface.co/datasets/allenai/olmOCR-bench): three with running heads and footers, three in columns, three with tables. Each tool converted them once, on 3 November 2026 (pdf2md.morethan.io on 19 November), and we scored the results with olmOCR-bench's checker. The overall score is the mean of the four groups.

| Tool | Overall | Heads and feet (9) | Columns (11) | Tables (21) | Baseline (9) |
|---|---|---|---|---|---|
| markdownwise (ours), second run | 97.2% | 8 | 11 | 21 | 9 |
| Marker 1.6.2, run locally | 96.4% | 9 | 11 | 18 | 9 |
| pdfmarkdown.app | 57.0% | 2 | 9 | 5 | 9 |
| pdf2md.morethan.io | 54.3% | 4 | 8 | 0 | 9 |
| CloudConvert | 52.1% | 0 | 10 | 6 | 8 |
| PDF24 | 50.6% | 0 | 5 | 12 | 9 |

**Our 97.2% is not a fair headline.** The first run, on 3 November, scored 72.8%. We fixed what it showed, partly with these same pages, and ran again on 4 November. The others were run once. Nine pages is a direction, not a ranking; the 200-PDF table above is the better guide.

Not scored: iLovePDF (one free conversion, then a sign-up; on that one file it passed 0 of 5 checks and markdownwise 4), AnythingMD (asks for an account first), Vertopal (its upload box did not accept our test upload).

Data, with the notes for each tool: [results/hosted-converters-9-pages.csv](results/hosted-converters-9-pages.csv). The pages are listed in [tests/nine-pages.md](tests/nine-pages.md).

## 3. Markdown to PDF: one file, 20 checks

[tests/feature-test.md](tests/feature-test.md) covers what people put in Markdown: tables, code, task lists, footnotes, maths, a long table that crosses a page. The 20 checks are in [tests/feature-test-checklist.md](tests/feature-test-checklist.md). We scored each PDF by eye.

| Tool | Score | Tested |
|---|---|---|
| markdownwise (ours) | 20 of 20 | 2026-11-03 |
| md2pdf.my | 14 of 20 | 2026-11-03 |
| markdowntopdf.com * | 13 of 20 | 2026-11-19 |
| PDFCreator Online * | 12 of 20 | 2026-11-19 |
| md2file.com | 11 of 19 | 2026-11-19 |
| CodeShack | 10 of 20 | 2026-11-03 |
| Syncfusion | 9 of 20 | 2026-11-03 |
| code-format.com | 4 of 20 | 2026-11-04 |
| online-convert.com | 2 of 20 | 2026-11-03 |

We wrote this test, and our own converter scored 14 the first time. We fixed the six things it failed before testing the others, so 20 of 20 means "passes its maker's test".

\* On our 20-point test file, markdowntopdf.com and PDFCreator Online did not produce a PDF; without the file's script line they scored 13 and 12 of 20. Both converted that shorter file, so a file of yours with no script line in it may convert without trouble. code-format.com refused the file until we removed the line that tests raw HTML. md2file.com fitted our long table on one page, so one check could not be made.

Data, with what each tool missed: [results/markdown-to-pdf-20-checks.csv](results/markdown-to-pdf-20-checks.csv).

## Check the numbers yourself

You need Python 3.12 or newer and the checker's four packages.

```
git clone https://github.com/opendataloader-project/opendataloader-bench
pip install rapidfuzz apted lxml beautifulsoup4
python scripts/score_outputs.py opendataloader-bench
```

That re-scores every published output (about a minute on a laptop). It needs no PDFs, so Git LFS is not required for this step, and it leaves the benchmark's own result files alone. The markdownwise row is not in their repo; see below.

**Score another tool.** Get the PDFs (`git lfs pull` in the clone), write a function that takes a PDF path and returns Markdown, then:

```
python scripts/convert_all.py opendataloader-bench my-tool my_converter:convert
python scripts/score_outputs.py opendataloader-bench --engine my-tool
```

**Check markdownwise.** Its engine is not open source, so this repo can't re-run it. You can convert the PDFs on [markdownwise.com](https://markdownwise.com/?ref=github) and score the Markdown it gives you (the free limit is 10 PDFs a day, so a sample is more practical than all 200). Compare with `results/markdownwise-per-document.csv`; if a file scores differently, please open an issue.

## What is not here

No PDFs, no answer keys and no other tool's output. Get them from the projects that own them:

- [opendataloader-bench](https://github.com/opendataloader-project/opendataloader-bench): Apache-2.0. Its PDFs come from [DP-Bench](https://huggingface.co/datasets/upstage/dp-bench) by Upstage (MIT).
- [olmOCR-bench](https://huggingface.co/datasets/allenai/olmOCR-bench) by the Allen Institute for AI: data ODC-BY-1.0, [code](https://github.com/allenai/olmocr) Apache-2.0.

The write-up of sections 2 and 3 is at [markdownwise.com/best-pdf-to-markdown-converter](https://markdownwise.com/best-pdf-to-markdown-converter?ref=github). Product names belong to their owners.

## Corrections

Found a wrong number, or a tool scored unfairly? Open an issue with the file and what you got.

## Licence

MIT for our scripts, tables and test file (see [LICENSE](LICENSE)). It does not cover the projects linked above.
