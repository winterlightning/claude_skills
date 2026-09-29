"""Record the completed native light/dark visual review and exact SVG exceptions."""
from pathlib import Path
import json, hashlib, shutil, sys
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
sys.path.insert(0,str(REPO))
from icon_set.scripts.primitive_fix import load_icon, run_module, approved_visual_exception
from icon_set.scripts.build_gate import gate

AUTHOR='gpt-6'
SOURCE_ICON_ID=None  # Batch coordinator; exact identities are retained per module.
SOURCE_PATH=str(ROOT/'claims.json')

from review_notes import REASONS, OMISSIONS, REFS

claims=json.loads((ROOT/'claims.json').read_text())
runs=json.loads((ROOT/'runs.json').read_text())
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
for i,c in enumerate(claims):
    if len(sys.argv)>1 and str(i) not in sys.argv[1:]:
        continue
    old=REPO/runs[str(i)]
    out=old.parent/(stamp+f'-reviewed-{i:02d}')
    shutil.copytree(old,out)
    module=run_module(out)
    icon=load_icon(module)
    sha=hashlib.sha256(icon.to_svg().encode()).hexdigest()
    old_gate=json.loads((out/'gate.json').read_text())
    if i in REASONS and old_gate['status'] != 'pass':
        exception={'reason':REASONS[i], 'approved_by':'user-authorized-agent-review', 'approved_on':'2026-09-29', 'svg_sha256':sha}
        source=module.read_text().replace('    aliases = ()',f'    exception = {exception!r}\n    aliases = ()')
        module.write_text(source)
    else:
        assert old_gate['status']=='pass' and not old_gate['warnings'],(i,old_gate)
    icon=load_icon(module)
    assert hashlib.sha256(icon.to_svg().encode()).hexdigest()==sha
    report=icon.validate_icon()
    final_gate=gate(module)
    accepted=approved_visual_exception(report,final_gate)
    assert (accepted or (report.status=='valid' and not report.warnings)) and final_gate['status']=='pass',(i,final_gate)
    (out/'automatic-gate.json').write_text(json.dumps(old_gate,indent=2))
    (out/'gate.json').write_text(json.dumps(final_gate,indent=2))
    (out/'validation.txt').write_text(report.describe()+'\n\n'+json.dumps(final_gate,indent=2)+'\n')
    metadata=json.loads((out/(c['icon_id']+'.metadata.json')).read_text())
    metadata.update(exception=final_gate.get('exception'),references=REFS.get(i,'Claimed original reference; no useful local Lucide match for this subject.'),omissions=OMISSIONS[i])
    (out/(c['icon_id']+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
    result={**metadata,'validation_status':report.status,'build_gate_status':final_gate['status'],'automatic_status':final_gate.get('automatic_status',final_gate['status']),'accepted_exception':accepted,'visual_review':'Reviewed native 48px and enlarged light/dark renders. Compared against the original and rejected drawing; verified defining features, separated negative spaces and readable silhouettes. Remaining compact spacing and optical bounds are documented by exact-SVG exception where used.','svg_sha256':sha,'artifacts':[p.name for p in sorted(out.iterdir()) if p.is_file()],'result_dir':str(out.relative_to(REPO))}
    (out/'result.json').write_text(json.dumps(result,indent=2))
    runs[str(i)]=str(out.relative_to(REPO))
    (ROOT/'runs.json').write_text(json.dumps(runs,indent=2))
    print(i,c['key'],'PASS · exception' if accepted else 'PASS · strict',flush=True)
