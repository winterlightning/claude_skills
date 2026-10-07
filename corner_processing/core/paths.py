"""Where things live. Every default path is anchored here, so the scripts run from any folder."""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))     # corner_processing/
SET_DIR = os.path.normpath(os.path.join(ROOT, "..", "solo-20261001"))  # the fetched icon set
DEFAULT_INPUT = os.path.join(SET_DIR, "svg")
OUT_DIR = os.path.join(ROOT, "outputs")
LOCKS_PATH = os.path.join(ROOT, "locks.json")
FIXES_DIR = os.path.join(ROOT, "input_fixes")
SKILLS = os.environ.get("CLAUDE_SKILLS", os.path.normpath(os.path.join(ROOT, "..", "..", "claude_skills")))
