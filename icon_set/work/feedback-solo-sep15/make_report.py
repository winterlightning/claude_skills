from pathlib import Path
import json,base64,hashlib,re,shutil
W=Path(__file__).resolve().parent
from round2_preview import centerline,create,build_paths
A=json.loads((W/'inventory.json').read_text());R=json.loads((W/'revisions.json').read_text());V=json.loads((W/'validation.json').read_text());Q=json.loads((W/'release-validation.json').read_text());B=json.loads((W/'retained-validation.json').read_text());N=json.loads((W/'retained-notes.json').read_text())
extras={150:'The hands were also changed to a clear asymmetric right angle.',163:'The hands were also changed to a clear asymmetric right angle.',164:'The hands were also changed to a clear asymmetric right angle.',167:'Removed the result divider because it created undersized apertures.',148:'The folded corner was enlarged to keep its opening usable.',183:'Raised the broad body clear of both wheels and joined it with short supports.',185:'Squared the side wings to keep their gaps clear.',229:'Simplified the frame to an open construction so the larger wheels have clear space.',234:'Removed the small sail seam to avoid a tiny closed opening.',236:'Kept one short horizontal arm so it stays clear of both head and raised leg.',50:'Narrowed the bowl to leave room for the two hanging trails.',197:'Narrowed the stance and raised the elbow to separate arm and leg.'}
rows=[];parents={};geometry_changes={};centerlines={}
def diagnostic(id):
 if id not in centerlines:centerlines[id]=centerline(create(id))
 return centerlines[id]
for x in A:
 n=str(x['number']);r=R.get(n);before=x.get('before_svg');after=V[r['id']]['svg'] if r else before
 if r:
  status='revised';note=r['note']+' '+extras.get(x['number'],'');id=r['id'];qa=Q[id];keyshape=V[id]['keyshape'];file='snapshot/'+r['file'];ref=r['reference']
 elif x['number']==37:
  status='split';note='This is a monitor frame containing a separate download arrow. Prepared two component briefs: container monitor frame and sub download arrow. The original generated parent is unavailable; the preview below is the recovered source reference. Handoffs are local files and are not marked approved.';id=x['parent'];qa=None;keyshape=None;file='monitor-split.json';ref='Recovered monitor-download source';before=(W/'component-briefs/container/monitor-download_7adf19ee-e35e-403f-8547-7156c16131ae-f59284411ff94abf/source.svg').read_text() if (W/'component-briefs/container/monitor-download_7adf19ee-e35e-403f-8547-7156c16131ae-f59284411ff94abf/source.svg').exists() else Path('pictographic-primitives/computers/batch-05/monitor download_7adf19ee-e35e-403f-8547-7156c16131ae.svg').read_text();after=None
 elif x['number']==32:
  status='missing';note='The knight-helm-on-shield parent and its exact source could not be located. A nearby knight reference contained a different multi-object scene, so it was not substituted. This item remains unresolved; the exact original is needed to prepare reliable component briefs.';id=x['parent'];qa=None;keyshape=None;file=None;ref=None
 else:
  status='retained';note=N[n];id=x['parent'];qa=B[id];keyshape=x['keyshape'];file=str(Path(x['path']).relative_to(W));ref='Preserved current parent'
 encode=lambda s:'data:image/svg+xml;base64,'+base64.b64encode(s.encode()).decode() if s else None
 if x.get('path'):
  observed=hashlib.sha256(Path(x['path']).read_bytes()).hexdigest();assert observed==x['hash'],(n,'Parent changed');parents[x['parent']]={'source':file if not r else str(Path(x['path']).relative_to(W)),'sha256':observed,'unchanged':True}
 if r:
  changed=[p['d'] for p in build_paths(create(r['parent']).draw())]!=[p['d'] for p in build_paths(create(id).draw())];assert changed,(n,'Unchanged drawing');geometry_changes[n]={'id':id,'geometry_changed':changed}
 rows.append({'beforeCenterline':encode(diagnostic(r['parent'])) if r else None,'afterCenterline':encode(diagnostic(id)) if r else None,'number':x['number'],'name':x['parent'].removeprefix('solo/'),'id':id,'status':status,'feedback':x['feedback'],'note':note.strip(),'before':encode(before),'after':encode(after),'qa':qa,'keyshape':keyshape,'file':file,'reference':ref,'related':r['brief_numbers'] if r else [x['number']],'download':f'build/solo48/{id}.svg' if r else None})
assert len(rows)==155 and len({x['number'] for x in rows})==155
assert all(Q[x['id']]['status']=='pass' for x in R.values())
counts={s:sum(x['status']==s for x in rows) for s in ['revised','retained','split','missing']}
summary={'brief_count':155,'unique_revisions':len({v['id'] for v in R.values()}),'counts':counts,'model_validation':{'valid':sum(v['status']=='valid' for v in V.values())},'full_export_validation':{'pass':len(set(v['id'] for v in R.values()))},'unchanged_parents':len(parents),'tests':{'run':385,'failures':25,'errors':59,'skipped':6,'status':'not green','limitations':'The isolated snapshot omitted some documentation and reference fixtures; the sandbox blocked local-server tests; Python 3.10 cannot parse one reconstruction helper. Other failures include existing corpus expectations. The suite does not certify this batch.'}}
assert counts['retained']==0 and counts['revised']==153
(W/'geometry-changes.json').write_text(json.dumps(geometry_changes,indent=2))
(W/'summary.json').write_text(json.dumps(summary,indent=2));(W/'parent-integrity.json').write_text(json.dumps(parents,indent=2));(W/'review-data.json').write_text(json.dumps(rows,indent=2))
data=json.dumps({'summary':summary,'rows':rows},ensure_ascii=False).replace('</','<\\/')
html=(W/'report-template.html').read_text().replace('__REPORT_DATA__',data)
(W/'review.html').write_text(html)
print(json.dumps(summary,indent=2))
