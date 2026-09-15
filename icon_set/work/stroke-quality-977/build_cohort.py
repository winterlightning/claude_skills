import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.build import build,DEFAULT_DIST,DEFAULT_PNG
rows=json.loads((ROOT/'icon_set/work/intersection-review-977/cohort.json').read_text())
raise SystemExit(build(DEFAULT_DIST,DEFAULT_PNG,only=['solo'],sources=[ROOT/r['python_source']['path'] for r in rows]))
