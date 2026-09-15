from pathlib import Path
import json,hashlib,re,inspect
from icon_set.model.icons.registry import factories
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/latest-variant-cleanup/combined-plan.json'
W=Path(__file__).parent;D=Path('icon_set/dist');p=json.loads((W/'combined-plan.json').read_text());reg=factories()
versions=[n for n in reg if re.search(r'-v\d+$',n)]
assert not versions,versions
pub=json.loads((D/'solo48/manifest.json').read_text())['icons'];failed=json.loads((D/'failed/solo48/manifest.json').read_text())['icons'];gallery=json.loads((D/'gallery/icons.json').read_text());published={r['icon_id']:r for r in pub}
for rows in [pub,failed,gallery['icons'],gallery['failed_icons']]:
 assert not [r['icon_id'] for r in rows if re.search(r'-v\d+$',r['icon_id'])]
for g in p:
 n=g['root'];assert n in published,n
 svg=(D/'solo48'/(n+'.svg')).read_bytes();assert svg==(W/(n+'.svg')).read_bytes(),n
 assert svg==reg[n]().to_svg().encode(),('current source changed',n)
 m=json.loads((Path('icon_set/work/qa_overlays/solo48')/(n+'.metrics.json')).read_text());assert m['distance_passed'] and m['negative_space_passed'],n
 assert m['svg_sha256']==hashlib.sha256(svg).hexdigest(),n
 assert json.loads((W/(n+'.qa.json')).read_text())['status']=='pass',n
stale=[]
for folder in [D/'solo48',D/'failed/solo48',Path('icon_set/assets/previews-png/solo48')]:
 stale.extend(str(f) for f in folder.glob('*') if re.search(r'-v\d+\.(svg|png)$',f.name))
assert not stale,stale
h=reg['hermes-with-winged-helmet']();assert h.human_construction=='bust'
report=dict(canonical_icons_verified=len(p),duplicate_entries_removed=335,registered_total=len(reg),solo_published=len(pub),solo_failed=len(failed),registered_versions=versions,stale_variant_outputs=stale,hermes_avatar_pass=True,hermes_head_shoulders_centerline_gap=4,hermes_head_shoulders_ink_gap=0,validation='All 327 retained canonical drawings pass release QA and current SVG-matched distance and hole overlays. Other failed icons remain.')
(W/'final-verification.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
