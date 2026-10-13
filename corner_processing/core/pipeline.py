"""The steps behind round_corner_processing.py and sharp_corner_processing.py.

  1. detect     corner detection of the input icons          -> <out>/corners48.json
  2. keyshapes  each icon's keyshape (sharp only, when missing) -> <out>/keyshapes.json
  3. toggle     the round or the sharp output + its check      -> <out>/<mode>/*.svg, toggle.json
  4. measure    how far the outputs reach past the keyshape (whole-set runs, or --measure)
  5. reports    corner48_report.html + toggle48_report.html    (skip with --no-report)

Options the steps share (--input, --out, --files, --sample, --seed, --jobs, --ready, --reviewed)
go to every step; anything else goes to the toggle step (e.g. --miter, --soft-gap, --bands).
"""

import argparse
import json
import os
import sys

from . import detect, keyshape, toggle
from .paths import DEFAULT_INPUT, OUT_DIR, ROOT


def _parse(mode, argv):
    ap = argparse.ArgumentParser(
        description=f"Build the all-{mode} output of the 48x48 icons (detect, {mode}, check, reports).",
        epilog="Any other option goes to the toggle step: see python3 -m core.toggle --help.")
    ap.add_argument("--input", default=DEFAULT_INPUT, help="folder of input SVGs (default: %(default)s)")
    ap.add_argument("--out", default=OUT_DIR, help="output folder (default: %(default)s)")
    ap.add_argument("--files", nargs="*", help="only these icons (file names)")
    ap.add_argument("--sample", type=int, default=0, help="random sample of N icons")
    ap.add_argument("--seed", type=int, default=48)
    ap.add_argument("--jobs", type=int, default=None, help="worker processes (default: all cores)")
    ap.add_argument("--ready", action="store_true", help="only icons not reviewed yet (not in locks.json)")
    ap.add_argument("--reviewed", action="store_true", help="only icons in locks.json")
    ap.add_argument("--measure", action="store_true",
                    help="re-measure keyshape overflow even on a partial run (whole-set runs always do)")
    ap.add_argument("--no-report", action="store_true", help="don't rebuild the review pages")
    return ap.parse_known_args(argv)


def _shared(cfg):
    args = ["--input", cfg.input, "--out", cfg.out, "--seed", str(cfg.seed)]
    if cfg.files:
        args += ["--files", *cfg.files]
    if cfg.sample:
        args += ["--sample", str(cfg.sample)]
    if cfg.jobs:
        args += ["--jobs", str(cfg.jobs)]
    args += ["--ready"] * cfg.ready + ["--reviewed"] * cfg.reviewed
    return args


def _keyshapes_missing(cfg):
    path = os.path.join(cfg.out, "keyshapes.json")
    try:
        with open(path, encoding="utf-8") as f:
            have = json.load(f)
    except (FileNotFoundError, ValueError):
        return True
    names = cfg.files or [n for n in os.listdir(cfg.input) if n.endswith(".svg")]
    return any(n not in have for n in names)


def _reports(cfg):
    if not os.path.isdir(os.path.join(ROOT, "reports")):    # the scripts-only copy has no pages
        print("  (no reports/ folder here: review pages skipped)")
        return
    sys.path.insert(0, os.path.join(ROOT, "reports"))
    import make_corner48_report
    import make_toggle48_report
    ks = ["--keyshapes", os.path.join(cfg.out, "keyshapes.json")]
    make_corner48_report.main(["--input", cfg.input, "--json", os.path.join(cfg.out, "corners48.json"),
                               "--out", os.path.join(cfg.out, "corner48_report.html")])
    make_toggle48_report.main(["--input", cfg.input, "--dir", cfg.out,
                               "--out", os.path.join(cfg.out, "toggle48_report.html"), *ks])


def run(mode, argv=None):
    cfg, extra = _parse(mode, argv)
    whole = not (cfg.files or cfg.sample or cfg.ready or cfg.reviewed)
    ks_path = os.path.join(cfg.out, "keyshapes.json")

    print(f"==> 1 detect corners")
    detect.main(_shared(cfg))
    if mode == "sharp" and _keyshapes_missing(cfg):
        print("==> 2 keyshapes (the sharp output slices at the keyshape)")
        keyshape.main(["--input-only", "--input", cfg.input, "--out", ks_path])
    print(f"==> 3 all-{mode} output + check")
    rc = toggle.main(_shared(cfg) + ["--mode", mode, "--keyshapes", ks_path] + extra)
    if whole or cfg.measure:
        print("==> 4 measure ink past the keyshape")
        keyshape.main(["--input", cfg.input, "--out", ks_path])
    if not cfg.no_report:
        print("==> 5 review pages")
        _reports(cfg)
    page = os.path.join(cfg.out, "toggle48_report.html")
    print(f"done — {'open ' + page if os.path.isdir(os.path.join(ROOT, 'reports')) and not cfg.no_report else 'outputs in ' + os.path.join(cfg.out, mode)}")
    return rc
