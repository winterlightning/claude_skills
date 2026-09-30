from pathlib import Path
import json,sys,cairosvg
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.scripts import primitive_fix as pf,work_queue as w
ROOT=Path(__file__).parent
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH=None
rs=json.loads((ROOT/'runs.json').read_text())
details={
'clove-bud-with-pointed-sepals':'Square fits diagonal stem, pointed sepals and round bud. Widened stem and calyx; no identifying element omitted. No useful exact Lucide match; source asymmetry retained.',
'coin-passing-between-two-hands':'VRECT_L fits vertically separated opposing hands. Retained one outlined coin; hand creases omitted. Lucide hand-coins informed outlined coin and rounded fingertip construction. Human-reference.md consulted for hand construction.',
'computer-monitor-with-code-upload-a3ccb7c42eee5d1f':'Square balances screen and stand. Omitted central slash to preserve readable code chevrons. Lucide monitor informed rounded frame and centered stand. Current rejected drawing was the only available reference.',
'cost-explorer':'Square fits axes, rising chart and magnifier. Reduced three nodes to two outlined nodes for clearance. Lucide circle informed round lens and nodes; directional chart asymmetry retained.',
'diagonal-pencil-writing-line':'Square fits diagonal pencil and writing baseline. Retained separate eraser, barrel and nib. Rounded cap and wider compartments; no useful exact Lucide match.',
'diagonal-slashed-circle-with-notch-upload-6656f349e715eebc':'Square fits crossed ring with short protruding notch. Current rejected drawing was the only available reference. Lucide circle informed round ring; no element omitted.',
'donkey-pinata-banded-body':'HRECT_L accommodates long banded torso, muzzle, ear and two visible legs. Small fringe and facial marks omitted for native-size clarity. No useful exact Lucide match; source profile asymmetry retained.',
'drag-gesture-in-all-directions':'Square fits four balanced arrows around fingertip. Nail detail omitted for clearance. Lucide move informed shared-axis arrows; Lucide hand and human-reference.md informed rounded finger.',
'drifting-jellyfish':'Square fits broad diagonal bell and three trailing tentacles. Fine subdivisions omitted. No useful exact Lucide match; asymmetric orientation retained with smooth curves.',
'dual-mesh-wireless-routers':'VRECT_L fits two upright rounded router towers beneath signals. Reduced three wifi marks to two arcs and omitted base seams. Matched tower dimensions and centered arcs; no useful exact Lucide match.',
'feather':'VRECT_L fits long diagonal quill and pointed vane with open notch. Shortened interior quill to preserve clearance. Lucide feather original and atomic geometry informed open vane and diagonal shaft.',
'female-user-profile-icon-upload-ba893b6ce54bc48b':'Square fits circular head and tapered blouse torso. Current rejected drawing was the only reference. human_ref/user.svg and human-reference.md informed circular head and shoulder arch. Bust flag plus scoped connection: head jaw22 and shoulder apex26, touching ink. No detached head gap applies; facial and clothing marks omitted.',
'finger-point':'VRECT_L fits raised index, thumb and folded fingers. Lucide hand and human-reference.md informed round finger caps and palm. Index placed on left to avoid middle-finger reading; simplified folded finger anatomy.',
'four-diamond-flecks':'Square fits four outlined diamond flecks. Large lower-right, medium upper-left and two smaller companions preserve hierarchy. Repeated diamond definition; no features omitted. No useful exact Lucide match.',
'gabled-house-paired-windows':'HRECT_L balances gable above two square outlined windows. Doorway and separate eave line omitted to keep paired windows readable. Shared window dimensions; no useful exact Lucide match.',
'game-immersive-vr':'HRECT_M fits broad visor, side straps and centered X. Smooth mirrored nose recess; no identifying element omitted. Lucide monitor supplied rounded enclosure principles; source supplies visor shape.',
'glasses-sun':'Square fits paired curved lenses beneath outlined upper-right sun. Simplified sun rays to two line marks and omitted fine lens details. Lucide glasses informed paired lens construction; source asymmetry retained.',
'hand-gesture-swipe-up':'Square fits open horizontal fingertip, curved contact mark and up arrow. Simplified nail/crease details. Lucide hand and human-reference.md informed rounded fingertip, Lucide move informed arrow.',
'hand-gesture-vertical-swipe-down':'HRECT_L fits pointing hand, raised thumb and curved downward arrow. Spread arrow wings to avoid crossing shaft. Simplified creases; no defining element omitted. Lucide hand and human-reference.md informed rounded hand construction.',
'hand-swipe-up-gesture':'HRECT_L fits long pointing finger, compact palm and up arrow. Simplified hooked thumb into a smooth tapered palm contour to remove tight overlap. Lucide hand and human-reference.md informed finger and palm construction.'
}
for r in rs:
 p=Path(r['run']);m=pf.run_module(p);icon=pf.load_icon(m);v=icon.validate_icon();g=json.loads((p/'gate.json').read_text())
 assert v.status=='valid' and not v.errors and not v.warnings
 assert g['status']=='pass' and not g['errors'] and not g['warnings'] and not g.get('exception')
 assert getattr(sys.modules[type(icon).__module__],'AUTHOR')=='gpt-6'
 assert pf.latest_run('solo/'+r['icon_id']).resolve()==Path(r['claim']).resolve()
 assert (p/(r['icon_id']+'.svg')).read_text()==icon.to_svg()
 for size in (48,384):cairosvg.svg2png(url=r['reference_path'],write_to=str(p/f'reference-{size}.png'),output_width=size,output_height=size,background_color='white')
 (p/(r['icon_id']+'.metadata.json')).write_text(json.dumps(r,indent=2))
 result=dict(r,author='gpt-6',validation_status='valid',validation_errors=[],validation_warnings=[],build_gate=g,keyshape=icon.keyshape.name,visual_review='Inspected native48 and enlarged light/dark previews. Clear subject, readable openings and intentional directional asymmetry; all final candidates visually accepted.',omissions_and_references=details[r['icon_id']],module=m.name,svg=r['icon_id']+'.svg',artifacts=sorted(f.name for f in p.iterdir() if f.is_file()))
 (p/'result.json').write_text(json.dumps(result,indent=2))
print('Finalized 20 valid runs',flush=True)
w.TIMEOUT=60
for r in rs:
 if (Path(r['claim'])/'result.json').exists():continue
 print('FINISHING',r['icon_id'],flush=True)
 try:
  code=pf.main(['finish','--worker','thuan-mac','--icon','solo/'+r['icon_id'],'--run',r['run'],'--outcome','done','--note',r['change']])
  if code:print('NEEDS_RETRY',r['icon_id'],code,flush=True)
 except Exception as e:
  (ROOT/(r['icon_id']+'-finish-error.txt')).write_text(repr(e));print('NEEDS_RETRY',r['icon_id'],repr(e),flush=True)
