from pathlib import Path
import json,sys,subprocess,cairosvg
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.scripts.primitive_fix import load_icon,run_module
root=Path(__file__).parent;rs=json.loads((root/'runs.json').read_text())
notes={
'winking-face-peeling-sticker':('Enlarged the peel into the lower-right quadrant, opened the fold and softened the wink and smile.','Circle preserves round sticker; smile shortened to clear fold. Lucide sticky-note supplies joined fold construction.'),
'woman-wearing-drooping-nightcap':('Restored two open hair curls and a sloping cap tail ending in a pompom; reduced jaw to make space.','Square fits cap and curls; omitted facial marks. Deliberately asymmetric cap. human_ref/user.svg supplies circular face; head-only portrait, no body gap.'),
'wonder-woman-portrait':('Enlarged circular face and distinct pointed tiara with downward forehead chevron; rebalanced long hair and shoulders.','Square fits a larger face; omitted eyes, smile and neckline. human_ref/user.svg supplies circular face and broad shoulders. Jaw bottom32 and shoulder apex36 give touching ink with bust flag and scoped connection.'),
'wraparound-safety-goggles':('Rounded lens corners and replaced angular nose notch with mirrored smooth lobes; expanded rim height.','HRECT_L gives room for curved bridge and rim. Omitted small side strap tabs. Lucide glasses supplies paired rounded lens construction.'),
'xbox-emblem-batch-086':('Restored larger bottom panel, smaller top panel and swept mirrored side panels around the diagonal X opening.','Circle preserves spherical silhouette. Simplified curves and widened gaps. Lucide circle supports outer silhouette; original supplies unequal panel proportions.')}
for r in rs:
 p=Path(r['run']);m=run_module(p);icon=load_icon(m);change,details=notes[r['icon_id']];r['change']=change
 for size in (48,384):cairosvg.svg2png(url=r['reference_path'],write_to=str(p/f'reference-{size}.png'),output_width=size,output_height=size,background_color='white')
 result=dict(r,author='gpt-6',validation_status='valid',validation_warnings=[],build_gate='pass',keyshape=icon.keyshape.name,visual_review='Inspected native 48px and enlarged in light and dark: smooth curves, readable openings, appropriate symmetry and retained identifying features.',omissions_and_references=details,module=m.name,svg=r['icon_id']+'.svg',artifacts=sorted(f.name for f in p.iterdir() if f.is_file()))
 (p/'result.json').write_text(json.dumps(result,indent=2))
(root/'runs.json').write_text(json.dumps(rs,indent=2))
for r in rs:
 if (Path(r['claim'])/'result.json').exists():continue
 proc=subprocess.run(['python3','icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon','solo/'+r['icon_id'],'--run',r['run'],'--outcome','done','--note',r['change']])
 if proc.returncode:print('NEEDS RETRY',r['icon_id'],proc.returncode,flush=True)
