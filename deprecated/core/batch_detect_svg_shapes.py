#!/usr/bin/env python3
"""Recursively generate Unlimited Shapes JSON and Matplotlib preflight reports."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

from detect_svg_shapes import analyze_svg, render_detection_plot


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("input_dir", type=Path)
    result.add_argument("output_dir", type=Path)
    result.add_argument("--overwrite", action="store_true", help="regenerate outputs that already exist")
    result.add_argument("--progress-every", type=int, default=10, metavar="N")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if not args.input_dir.is_dir():
        print(f"Input folder does not exist: {args.input_dir}", file=sys.stderr)
        return 1
    sources = sorted(args.input_dir.rglob("*.svg"), key=lambda path: str(path).casefold())
    if not sources:
        print(f"No SVG files found under {args.input_dir}", file=sys.stderr)
        return 1
    args.output_dir.mkdir(parents=True, exist_ok=True)

    entries: list[dict] = []
    failures: list[dict[str, str]] = []
    categories: Counter[str] = Counter()
    totals = Counter()

    for index, source in enumerate(sources, start=1):
        relative = source.relative_to(args.input_dir)
        output_folder = args.output_dir / relative.parent
        report_path = output_folder / f"{source.stem}-shapes.json"
        plot_path = output_folder / f"{source.stem}-preflight.png"
        output_folder.mkdir(parents=True, exist_ok=True)
        try:
            if report_path.exists() and plot_path.exists() and not args.overwrite:
                report = json.loads(report_path.read_text(encoding="utf-8"))
                state = "reused"
            else:
                svg_text = source.read_text(encoding="utf-8")
                report = analyze_svg(svg_text, source.name)
                report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                render_detection_plot(svg_text, report, output_path=plot_path)
                state = "generated"
            summary = report["summary"]
            categories.update(summary["categoryCounts"])
            totals["elements"] += summary["elementCount"]
            totals["atomCandidates"] += summary["atomicCandidateCount"]
            totals["warnings"] += summary["warningCount"]
            totals["errors"] += summary["errorCount"]
            totals["ready"] += int(summary["readyForIconMaker"])
            totals["review"] += int(not summary["readyForIconMaker"])
            totals[state] += 1
            entries.append({
                "source": str(relative),
                "report": str(report_path.relative_to(args.output_dir)),
                "plot": str(plot_path.relative_to(args.output_dir)),
                "status": "ready" if summary["readyForIconMaker"] else "review-required",
                "summary": summary,
            })
        except Exception as error:  # keep the remaining batch useful
            failures.append({"source": str(relative), "error": str(error)})
            print(f"FAILED {relative}: {error}", file=sys.stderr, flush=True)
        if index == 1 or index % max(args.progress_every, 1) == 0 or index == len(sources):
            print(f"Processed {index}/{len(sources)} SVGs · ready {totals['ready']} · review {totals['review']} · failed {len(failures)}", file=sys.stderr, flush=True)

    batch_summary = {
        "schemaVersion": 1,
        "inputFolder": str(args.input_dir),
        "outputFolder": str(args.output_dir),
        "svgCount": len(sources),
        "processedCount": len(entries),
        "failedCount": len(failures),
        "readyCount": totals["ready"],
        "reviewRequiredCount": totals["review"],
        "generatedCount": totals["generated"],
        "reusedCount": totals["reused"],
        "elementCount": totals["elements"],
        "atomicCandidateCount": totals["atomCandidates"],
        "warningCount": totals["warnings"],
        "errorCount": totals["errors"],
        "categoryCounts": dict(categories.most_common()),
        "failures": failures,
        "files": entries,
    }
    summary_path = args.output_dir / "batch-summary.json"
    summary_path.write_text(json.dumps(batch_summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Batch summary written to {summary_path}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
