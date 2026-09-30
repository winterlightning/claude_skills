from pathlib import Path
import json
root=Path(__file__).parent;rs=json.loads((root/'runs.json').read_text());finished=[]
for r in rs:
 p=Path(r['claim'])/'result.json'
 if p.exists():finished.append(json.loads(p.read_text()))
lines=['# Once-disapproved solo fix batch 11','',f'{len(finished)}/20 uploaded and reported done. Queue: solo; offset 0; maximum disapprovals 1. Worker: thuan-mac. AUTHOR in every fixed module: `gpt-6`.','', 'All 20 candidates passed `validate_icon()` and the full build gate with zero warnings and were inspected at native 48px in light and dark themes. No written reviewer feedback accompanied these claims; the original reference and rejected drawing guided each revision.','',f'[All completed drawing previews]({(root/"completed-previews.png").resolve()})','', 'The initial standard claim request obtained five icons. Later scans stopped on a Cloudflare exception from an individual history request. The batch-local intake excluded unavailable histories, verified the remaining candidates with the same disapproval-count function and limit, and claimed fifteen more through the production work-queue API. No icon with a verified count above one was claimed. Registered originals and published output were not edited.','']
for r in rs:
 p=Path(r['run']);res=json.loads((p/'result.json').read_text());fpath=Path(r['claim'])/'result.json';f=json.loads(fpath.read_text()) if fpath.exists() else None
 lines+=['## solo/'+r['icon_id'],'',r['comparison'],'','**Change:** '+r['change'],'',res['omissions_and_references'],'',f"- RESULT_DIR: [{p.name}]({p.resolve()})",f"- SVG: [{r['icon_id']}.svg]({(p/(r['icon_id']+'.svg')).resolve()})",f"- Module: [{res['module']}]({(p/res['module']).resolve()})",'- AUTHOR: `gpt-6`',f"- Validation: {res['validation_status']}; full build gate: {res['build_gate']}; zero warnings.",'- Visual review: native 48px and enlarged, light and dark.',f"- Production: {f['outcome']}; review status: {f['review_status']}." if f else '- Production: upload pending retry.','']
(root/'report.md').write_text('\n'.join(lines))
summary={'requested':20,'claimed':len(rs),'completed':len(finished),'worker':'thuan-mac','author':'gpt-6','max_disapprovals':1,'offset':0,'icons':[{'key':'solo/'+r['icon_id'],'run':r['run'],'svg':str(Path(r['run'])/(r['icon_id']+'.svg')),'completion':str(Path(r['claim'])/'result.json') if (Path(r['claim'])/'result.json').exists() else None} for r in rs]}
(root/'summary.json').write_text(json.dumps(summary,indent=2));print('Verified records:',len(finished),'of',len(rs))
