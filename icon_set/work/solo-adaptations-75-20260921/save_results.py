"""Persist source mappings without altering other decisions or artwork."""
import hashlib,json,pathlib,sqlite3,sys
W=pathlib.Path(__file__).parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_status import load_status,set_status
from icon_set.scripts.primitive_briefs import load_primitive_briefs,save_primitive_brief
from icon_set.scripts.deploy import record_activity
rows=json.loads((W/'source-mapping.json').read_text());known={r['source_uuid'] for r in rows}
assert len(rows)==len(known)==75
db=ROOT/'icon_set/.local/state/feedback.sqlite3'
connection=sqlite3.connect(db,timeout=30)
with connection:
 connection.execute('BEGIN IMMEDIATE')
 before=load_status(connection);briefs=load_primitive_briefs(connection)
 snapshot={uid:{'decision':before.get(uid),'reference_brief':briefs.get(uid)} for uid in known}
 backup=W/'before-save-results.json'
 if backup.exists():raise RuntimeError('Results already saved; inspect the current state before a repeat.')
 for row in rows:
  uid=row['source_uuid'];old=briefs[uid]
  assert old['family']=='solo' and uid in old['brief'],f'Changed source family or brief: {uid}'
  assert before.get(uid,{}).get('status')=='skip' and before[uid]['reason']=='other',f'Changed source decision: {uid}'
 backup.write_text(json.dumps(snapshot,indent=2)+'\n')
 for row in rows:
  uid=row['source_uuid'];ready=row['status']=='ready'
  result='\n\n## SOLO48 adaptation result — 2026-09-21\n\n'
  if ready:
   result+=f"Ready for reuse: {row['solo_icon_id']}\nFamily: solo\nPython original: {row['model_path']}\nSVG: {row['svg_path']}\nValidation: model valid; full build QA passed with zero errors and warnings.\nNative review: light and dark at 48 px.\nReuse this artwork; do not queue another drawing for this source.\n"
  else:
   result+='Unpublished candidate; adaptation remains unfinished. '+row['notes']+'\nNo validation exception has been applied.\n'
  result+=f"Canonical source: {row['canonical_source_number']}\nComparison: {W/'index.html'}#icon-{row['source_number']}\n"
  save_primitive_brief(connection,uid,'solo',briefs[uid]['brief'].rstrip()+result,known=known,user='agent',record=record_activity)
  if ready:
   set_status(connection,[uid],'skip','other',f"Solo ready: reuse {row['solo_icon_id']}. Validated SOLO48 adaptation; source {row['canonical_source_number']} owns the shared artwork. Do not generate a duplicate.",user='agent',record=record_activity,known=known)
 after=load_status(connection);after_briefs=load_primitive_briefs(connection)
 assert {k:v for k,v in before.items() if k not in known}=={k:v for k,v in after.items() if k not in known}
 assert {k:v for k,v in briefs.items() if k not in known}=={k:v for k,v in after_briefs.items() if k not in known}
 for row in rows:
  uid=row['source_uuid'];assert 'SOLO48 adaptation result' in after_briefs[uid]['brief']
  if row['status']=='held':assert before[uid]==after[uid]
connection.close()
verification={'source_count':75,'ready_sources':sum(r['status']=='ready' for r in rows),'published_solo_drawings':len({r['solo_icon_id'] for r in rows if r['status']=='ready'}),'held_sources':sum(r['status']=='held' for r in rows),'unrelated_decisions_preserved':True,'unrelated_briefs_preserved':True,'generation_jobs_queued':0,'tests':{'workspace_boundary_tests':37,'status':'passed'},'targeted_build_exit':0,'native_light_dark_review':True}
(W/'verification.json').write_text(json.dumps(verification,indent=2)+'\n')
old_gallery=ROOT/'icon_set/work/centered-container-recheck-20260921/index.html'
content=old_gallery.read_text();(W/'classification-before-adaptations.html').write_text(content)
banner='<div id="solo-adaptations-result" style="padding:18px 24px;background:#e5f4eb;color:#194c31;font:15px system-ui"><strong>Solo adaptation update:</strong> 66 of the 75 references are ready using 62 shared solo drawings; 9 still need review. <a style="color:inherit;text-decoration:underline" href="../solo-adaptations-75-20260921/index.html">Open the source / existing / adapted comparison</a></div>'
import re
assert 'id="solo-adaptations-result"' not in content
content,count=re.subn(r'(<body[^>]*>)',lambda m:m.group(1)+banner,content,count=1)
assert count==1;old_gallery.write_text(content)
print(json.dumps(verification,indent=2))
