from pathlib import Path
import json,re,collections,zipfile
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
rows=json.loads((P/'selection.json').read_text());triage=json.loads((P/'triage.json').read_text());manifest=json.loads((P/'sources/manifest.json').read_text());glyphs=json.loads((ROOT/'icon_set/typeface/glyphs.json').read_text())['glyphs']
assert len(manifest)==100 and len(list((P/'briefs').glob('*.md')))==100
assert {m['family'] for m in manifest}=={'solo'}
assert len({m['icon_id'] for m in manifest})==100
existing=set(json.loads((P/'existing-ids.json').read_text()));assert not existing.intersection(m['icon_id'] for m in manifest)
prior=set()
for f in P.parent.glob('todo-solo-briefs-*/selection.json'):
 if f.parent!=P:prior.update(r['uuid'] for r in json.loads(f.read_text()))
assert len({r['uuid'] for r in rows})==164 and not prior.intersection(r['uuid'] for r in rows)
components=0;copies=0;srcmap={}
for i,(r,t) in enumerate(zip(rows,triage)):
 src=ROOT/t['reference_path'];srcmap[src.name]=src;assert src.is_file() and src.name.endswith(r['uuid']+'.svg')
 for png in [t['inspected_large'],t['inspected_native']]:assert (P/png).is_file()
 if t['classification']=='standalone':
  assert (P/'sources'/src.name).read_bytes()==src.read_bytes();copies+=1
  b=(P/'briefs'/(src.stem+'.md')).read_text();assert r['uuid'] in b and t['reference_path'] in b
  assert '- native 48px:' in b and '- family: solo' in b and '$icon-solo' in b and 'You can try modifying a copy' in b
 else:
  review=P/t['review_folder'];assert (review/src.name).read_bytes()==src.read_bytes();copies+=1
  assert (P/'held-sources'/src.name).read_bytes()==src.read_bytes();copies+=1
  d=json.loads((review/'components.json').read_text());components+=len(d['components'])
  for j,c in enumerate(d['components'],1):
   assert c['name'] and c['family'] and c['description'];assert (review/f'component-{j}.md').stat().st_size>100
  assert (review/'generation-draft.md').stat().st_size>100
for m in manifest:
 assert set(m)=={'file','concept','icon_id','family','description','tags'}
 assert re.fullmatch(r'[a-z][a-z0-9]*(-[a-z0-9]+)*',m['icon_id'])
 assert 25<=len(m['description'].split())<=45
 assert 6<=len(m['tags'])<=10 and all(t==t.lower() for t in m['tags'])
for f in (P/'pending-brief').glob('*/*/*.svg'):
 assert f.read_bytes()==srcmap[f.name].read_bytes();copies+=1
counts=dict(collections.Counter(t['classification'] for t in triage))
v={'source_references_inspected':164,'standalone_solo_briefs':100,'counts':counts,'saved_review_sources':64,'saved_component_briefs':components,'verified_byte_identical_copies':copies,'duplicate_sources_from_prior_batches':0,'duplicate_or_existing_solo_ids':0,'native_size':48,'missing_glyphs':['”'],'unresolved_questions':[json.loads((P/t['review_folder']/'review.json').read_text())['uncertainty'] for t in triage if t['classification']=='uncertain'],'unselected_in_saved_candidate_list':len(json.loads((P/'candidates.json').read_text()))-164,'gallery_synced':False,'jobs_queued':0,'artwork_generated':0}
(P/'verification.json').write_text(json.dumps(v,indent=2)+'\n')
lookups=[]
for i,chars,component,uncertain in [(15,'ZZ',2,False),(26,'!',2,False),(38,'ZZ',2,False),(45,'$',3,False),(70,'&',2,False),(74,'O',2,True),(109,'”',2,False),(130,'SE',2,False),(131,'SW',2,False),(146,'i',2,False),(148,'RP',2,True),(149,'Q',2,True),(150,'P',2,False),(152,'I',2,True),(154,'Q',2,True)]:
 review=P/triage[i]['review_folder']; gs={ch:next((g for g in glyphs if g['character']==ch and g.get('preferred')),None) for ch in dict.fromkeys(chars)}
 record={'source_uuid':rows[i]['uuid'],'reference_path':triage[i]['reference_path'],'text':chars,'identification':'candidate interpretations, not final text' if uncertain else 'readable','glyph_catalog':'icon_set/typeface/glyphs.json','glyphs':[{'character':ch,'icon_id':g['icon_id'] if g else None} for ch,g in gs.items()],'missing_characters':[ch for ch,g in gs.items() if not g],'instructions':'Reuse preferred stored paths and natural metrics; do not invent replacement glyph geometry.'}
 if chars=='ZZ':record['arrangement']='two Z letters rising toward the upper right, upper letter larger'
 if i==148:record['arrangement']='R or P plus a separate diagonal stroke; requires interpretation'
 (review/'typeface-reuse.json').write_text(json.dumps(record,indent=2)+'\n');lookups.append(record)
 detail='\n## Typeface lookup\n\n'+('Conditional reuse if the text interpretation is confirmed.\n\n' if uncertain else '')+'\n'.join(f"- `{ch}`: `{g['icon_id'] if g else 'MISSING — hold component generation'}`" for ch,g in gs.items())+'\n\nReuse preferred stored glyph paths. Do not invent replacement letter geometry.\n'
 for name in ['generation-draft.md',f'component-{component}.md']:
  f=review/name;f.write_text(f.read_text()+detail)
(P/'typeface-reuse.json').write_text(json.dumps(lookups,indent=2)+'\n')
for f in (P/'sheets').glob('sheet-*.png'):
 if int(f.stem.split('-')[-1])>3:f.unlink()
notes=[]
for i,r in enumerate(rows):
 d=json.loads((P/'drafts.json').read_text())[i]
 if r['old_concept'].startswith('square') or i in [5,8,9,20,23,28,35,40,52,54,63,66,78,99,129,157,158]:
  notes.append({'source_uuid':r['uuid'],'reference_path':triage[i]['reference_path'],'source_name':r['old_concept'],'visible_subject':d['concept'],'note':'The brief follows the inspected artwork rather than inferring missing content from the source filename. Ambiguous character interpretations are recorded in the review draft.'})
(P/'source-name-notes.json').write_text(json.dumps(notes,indent=2)+'\n')
readme=['# Solo Briefs — Batch 17','','Prepared **100 standalone solo briefs**, inspected individually at 320px and 48px. Saved **64 additional review sources** with **137 independent component or typeface reuse briefs**.','','Saved locally; no gallery synchronization, database writes, generation jobs or artwork builds. Source UUIDs and proposed solo IDs were checked against prior batches. The supplied candidate list has 34 unselected references left after this run; this is not a live gallery missing-brief count. The initial triage contact sheets also show six previewed candidates beyond the final selection.','','## Files','','- [Visual index](index.html)','- [Standalone manifest](sources/manifest.json)','- [Gallery-compatible export](gallery-briefs.json)','- [Triage record](triage.json)','- [Verification](verification.json)','- [Family suitability flags](family-flags.json)','- [Source naming notes](source-name-notes.json)','- [Typeface reuse lookup](typeface-reuse.json)','','## Classification counts','']+[f'- {k}: {n}' for k,n in counts.items()]+['','## Review references','','Every reference below includes saved component briefs and its unchanged source. Side combinations and ambiguous symbols retain review evidence. The closing-double-quote glyph is absent from the preferred catalog, so its layout brief holds that component for an approved matching glyph.']
for i,t in enumerate(triage):
 if t['classification']=='standalone':continue
 r=json.loads((P/t['review_folder']/'review.json').read_text());readme+=['',f"- [{Path(t['reference_path']).name}]({t['review_folder']}/generation-draft.md) — {r['reason']}"+(f" **Open question:** {r['uncertainty']}" if r.get('uncertainty') else '')]
readme+=['','## Family suitability','','All standalone briefs retain solo as requested. Symbol groups, diagrams, empty frames and nested panels are flagged in family-flags.json; some may suit sub or container authoring better. Their briefs remain available.','','## First authoring handoff','','`$icon-solo three-tracks-with-single-slider-knob` — Three horizontal tracks with one round knob near the right end of the middle track. Preserve the complete source UUID and path in its brief.','']
(P/'README.md').write_text('\n'.join(readme))
include_dirs={'briefs','sources','png','sheets','triage-sheets','combination-review','pending-brief','held-sources'}
include_files={'README.md','index.html','index.md','triage-index.html','triage-index.md','triage.json','verification.json','gallery-briefs.json','family-flags.json','source-name-notes.json','typeface-reuse.json','selection.json'}
with zipfile.ZipFile(P/'solo-briefs-100.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(P.rglob('*')):
  if f.is_file() and (f.relative_to(P).parts[0] in include_dirs or f.name in include_files):z.write(f,f.relative_to(P))
print(json.dumps(v,indent=2));print('ZIP bytes:',(P/'solo-briefs-100.zip').stat().st_size)
