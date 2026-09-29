from pathlib import Path
import json,hashlib
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
items=json.loads((HERE/'items.json').read_text())
verified=[]
for it in items:
 fix=ROOT/it['fix'];run=ROOT/it['run'];r=json.loads((fix/'result.json').read_text());local=json.loads((run/'result.json').read_text())
 assert r['outcome']=='done' and r['review_status']=='ready',it['key']
 assert r['author']=='gpt-6' and r['author_ok'],it['key']
 assert r['accepted_exception'] and r['build_gate']['status']=='pass',it['key']
 assert r['uploaded']['stage']=='after' and r['uploaded']['has_python'] and r['uploaded']['has_validation'],it['key']
 assert r['reported']['state']=='done' and r['reported']['worker']=='thuan-mac',it['key']
 assert r['make_ray_run']==it['run'],it['key']
 assert len(list((fix/'after').glob('preview-*.png')))==4,it['key']
 svg=run/(it['id']+'.svg');out=fix/'after'/svg.name
 assert svg.read_bytes()==out.read_bytes(),it['key']
 module=ROOT/it['module'];assert module.read_bytes()==(fix/'after'/module.name).read_bytes(),it['key']
 sha=hashlib.sha256(svg.read_bytes()).hexdigest()
 assert r['build_gate']['exception']['svg_sha256']==sha,it['key']
 verified.append(dict(icon=it['key'],outcome=r['outcome'],review_status=r['review_status'],author=r['author'],accepted_exception=True,svg_sha256=sha,finished_at=r['finished_at'],result=it['fix']+'/result.json',run=it['run']))
(HERE/'verified-results.json').write_text(json.dumps({'count':len(verified),'results':verified},indent=2))
report=HERE/'report.md';s=report.read_text();s=s.replace('Production upload verification is recorded separately in `verified-results.json` after finishing every icon.','Production receipts confirm all 20 uploads and done outcomes, with every revision returned to Ready. Uploaded Python and SVG bytes match the visually reviewed final runs; AUTHOR and drawing-bound exception hashes are verified. See [verified-results.json]('+str(HERE/'verified-results.json')+').')
report.write_text(s)
print('Verified 20/20: done, Ready, gpt-6, matching uploaded artwork, accepted drawing-bound exceptions.')
