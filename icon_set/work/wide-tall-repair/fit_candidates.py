from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
skip={'left-double-click-mouse','right-double-click-mouse','monitor-download-arrow','monitor-upload-arrow','monitor-in-security-shield','knight-helm-on-shield','open-locket-with-portrait','baby-figure','pair-of-teardrop-earrings','scorpio-zodiac-symbol','cd-rom-drive'}
for r in json.loads((W/'targets.json').read_text()):
 if r['id'] in skip:continue
 out=W/'candidates'/f"{r['id']}.json";out.parent.mkdir(exist_ok=True)
 if out.exists():continue
 o=create(r['id']);k=o.keyshape.name;k='VRECT_L' if k.startswith('VRECT') else 'HRECT_L' if k.startswith('HRECT') else k
 f=o.fit_to_keyshape(Keyshape[k],force_stretch=True)
 out.write_text(json.dumps({'record':f.icon.to_record(),'report':f.report},indent=2))
 print(r['id'],f.report['validation']['status'],flush=True)
