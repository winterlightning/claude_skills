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

REASONS={
1:'Preserve the recognizable cowboy crown, curved brim, circular jaw, hair and shoulders. Portrait details intentionally use compact spacing and anatomical contacts; the 48px light/dark views are legible.',
2:'Hands intentionally touch the client temples. Preserve two heads and front shoulders at 48px rather than removing the massage action. Client head-to-shoulder centerline gap is exactly 8 (4 ink); therapist head-to-body is also 8.',
3:'Preserve a visible eye and anatomically attached mask/neck and straps. Compact eye spacing and profile joins retain the broad protective-mask meaning at 48px.',
5:'Harp strings visibly terminate at its neck and sloping soundboard. Keep this recognizable instrument silhouette with scoped acceptance of curve-junction findings.',
6:'The natural horizontal pointing-hand silhouette uses an optical envelope and a close thumb/palm crease. It remains clearly readable on the unchanged 48px canvas with 4px strokes.',
7:'The side-view roll needs a narrow core, shared paper tangent and perforation. Retain those UI-readable details with a 3px core-to-sheet ink gap.',
8:'Three curled fingers need 6-unit centerline pitch (2px visible gaps). Native-size inspection confirms separated folds and an unmistakable upright pointing index.',
9:'The automotive hazard switch requires a second triangle, not an exclamation. Its narrowest nested gap is about 1.8px and the central opening remains visible at native size.',
10:'HBO must retain all three letters and a broad O. Use a naturally wide wordmark envelope and compact 2-3px letter spacing; every letter remains separate and legible at 48px.',
11:'The top-view field-of-view symbol needs a dashed cone and nose. Compact dash spacing and ray-to-head spacing preserve the reference arrangement at native size.',
12:'The niqab opening and fabric fold intentionally meet the outer head covering. Keep the narrow eye opening and full lower-face veil, without a misleading smile.',
13:'The monocle cord runs close to the face outline and lens. These compact distances preserve the complete face, clear round lens and hanging cord at 48px.',
16:'Preserve the horse muzzle, long neck, slim outlined legs and curved tail. Natural tapered limbs and optical bounds are intentionally retained rather than reverting to blocky proportions.',
17:'Preserve the hyena sloping back, heavy forequarters, rounded ear and lowered tail. Narrow tapered legs and optical bounds retain animal proportions at 48px.',
18:'Preserve both owl eyes, beak, brow, folded wing and standing foot. Compact face spacing and organic contacts keep the owl identifiable and its details separated at 48px.',
19:'Preserve both owl eyes, beak, brow, folded wing and standing foot. Compact face spacing and organic contacts keep the owl identifiable and its details separated at 48px.',
}
OMISSIONS={0:'Minor lip edge omitted to keep the oral passage open.',1:'Facial detail omitted as in the source.',2:'Fine hand anatomy omitted; temple contact and both people retained.',3:'Fine ear curve omitted to prioritize mask and eye.',4:'None of the defining shell, ridge or brim features omitted.',5:'Reduced the string count to two clear strings; retained curved neck, pillar, soundboard and base.',6:'Fine hand creases reduced to one thumb/palm stroke.',7:'Perforation rows reduced to one clear mark; roll core simplified to a short stroke.',8:'Fine knuckle creases omitted; all three curled fingers retained.',9:'No defining feature omitted; incorrect exclamation removed.',10:'No letters omitted; thin source letterforms reauthored as 4px strokes.',11:'Sight rays reduced to two dashes per side.',12:'Secondary cloth folds reduced to one diagonal fold.',13:'Minor facial expression omitted; uncovered eye, lens, mouth and cord retained.',14:'Facial details omitted as in the source; two pain waves retained.',15:'Outlined body and pistol reduced to coherent single strokes; standing pose retained.',16:'Far-side legs and minor anatomy omitted; horse neck, muzzle and near-side legs retained.',17:'Tiny eye omitted to avoid merging with the ear; hyena back and forequarters retained.',18:'Feather texture omitted; paired eyes, beak, wing and standing foot retained.',19:'Feather texture omitted; paired eyes, beak, wing and standing foot retained.'}
REFS={1:'Shared human avatar proportions; claimed cowboy reference. No useful local Lucide match for the cowboy hat.',2:'Shared human_ref/user.svg and full_body_ref.png: round outlined heads and smooth shoulders.',3:'Lucide ear: coherent curved head detail; claimed masked head controls silhouette.',4:'Lucide hard-hat original and atomic-debug: separate raised ridge, circular shell lobes and brim.',6:'Lucide hand original and atomic-debug: coherent outline and short interior fold.',8:'Lucide hand original and atomic-debug: repeated curled fingers and round palm.',9:'Lucide triangle-alert original and atomic-debug: stable triangular envelope; source controls nested triangle meaning.',13:'Shared human reference for circular heads; claimed monocle reference controls the lens and cord.',15:'Shared full_body_ref.png: round head, coherent stick torso/limbs. Exact head-to-torso gap: 22-(10+4)=8 centerline units, 4 ink.'}

claims=json.loads((ROOT/'claims.json').read_text())
runs=json.loads((ROOT/'runs.json').read_text())
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
for i,c in enumerate(claims):
    old=REPO/runs[str(i)]
    out=old.parent/(stamp+f'-reviewed-{i:02d}')
    shutil.copytree(old,out)
    module=run_module(out)
    icon=load_icon(module)
    sha=hashlib.sha256(icon.to_svg().encode()).hexdigest()
    old_gate=json.loads((out/'gate.json').read_text())
    if i in REASONS:
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
    result={**metadata,'validation_status':report.status,'build_gate_status':final_gate['status'],'automatic_status':final_gate.get('automatic_status',final_gate['status']),'accepted_exception':accepted,'visual_review':'Reviewed native 48px and enlarged light/dark renders. Defining features are recognizable; final revisions fix touching letters, merged pain waves and beak/wing collision. Remaining compact details documented by exact-SVG exception where used.','svg_sha256':sha,'artifacts':[p.name for p in sorted(out.iterdir()) if p.is_file()],'result_dir':str(out.relative_to(REPO))}
    (out/'result.json').write_text(json.dumps(result,indent=2))
    runs[str(i)]=str(out.relative_to(REPO))
    (ROOT/'runs.json').write_text(json.dumps(runs,indent=2))
    print(i,c['key'],'PASS · exception' if accepted else 'PASS · strict',flush=True)
