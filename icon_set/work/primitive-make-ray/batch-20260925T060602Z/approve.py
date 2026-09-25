"""Record exact-drawing approvals under the user's explicit exception authorization."""
from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts.primitive_fix import load_icon
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
BATCH=Path(__file__).parent
items=json.loads((BATCH/'items.json').read_text())
reasons={
    4:'Preserve the pointed crescent cusps. Short inner/outer curve approaches retain 3.11px visible clearance and a broad readable crescent; reviewed at 48px in both themes.',
    14:'Preserve the identifying helmet ear vent and inward cheek guard. The vent keeps 2.45px visible separation from the smooth guard; the enclosed dot opening remains visible at 48px in both themes.',
    15:'Preserve three battlements, an arched window and plinth. Compact six-unit structural bands have 2px visible clearance; all openings remain legible at 48px in both themes.',
    17:'Preserve the tilted seesaw, currency ticks and closed triangular fulcrum. The bitcoin foot retains 2.79px visible clearance above the beam; separate symbols and support read clearly at 48px in both themes.',
    18:'Preserve all four spread flaps and the perspective box base. The short diagonal flap/base approaches retain 2.86px visible clearance; all faces and flaps are distinct at 48px in both themes.',
    19:'Preserve the cube and all three complete outward arrows. Cube faces retain 3.16px visible clearance; the reduced cube and detached arrows remain clear at 48px in both themes.',
}
for i,reason in reasons.items():
    item=items[i];p=Path(item['module']);icon=load_icon(p)
    approval={'reason':reason,'approved_by':'user: delegated visual exception judgment in this request','approved_on':'2026-09-25','svg_sha256':hashlib.sha256(icon.to_svg().encode()).hexdigest()}
    source=p.read_text().split('\n# Exact-drawing visual exception')[0]
    p.write_text(source+'\n# Exact-drawing visual exception authorized by user; automatic findings remain in validation.txt.\nRevision.exception = '+repr(approval)+'\n')
    item['exception']=approval
(BATCH/'items.json').write_text(json.dumps(items,indent=2))
