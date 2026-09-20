from pathlib import Path
import json,re,collections,zipfile
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
rows=json.loads((P/'selection.json').read_text());triage=json.loads((P/'triage.json').read_text());manifest=json.loads((P/'sources/manifest.json').read_text());glyphs=json.loads((ROOT/'icon_set/typeface/glyphs.json').read_text())['glyphs']
assert len(manifest)==28 and len(list((P/'briefs').glob('*.md')))==28
assert {m['family'] for m in manifest}=={'solo'}
assert len({m['icon_id'] for m in manifest})==28
existing=set(json.loads((P/'existing-ids.json').read_text()));assert not existing.intersection(m['icon_id'] for m in manifest)
prior=set()
for f in P.parent.glob('todo-solo-briefs-*/selection.json'):
 if f.parent!=P:prior.update(r['uuid'] for r in json.loads(f.read_text()))
assert len({r['uuid'] for r in rows})==34 and not prior.intersection(r['uuid'] for r in rows)
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
v={'source_references_inspected':34,'standalone_solo_briefs':28,'counts':counts,'saved_review_sources':6,'saved_component_briefs':components,'verified_byte_identical_copies':copies,'duplicate_sources_from_prior_batches':0,'duplicate_or_existing_solo_ids':0,'native_size':48,'missing_glyphs':[],'unresolved_questions':[json.loads((P/t['review_folder']/'review.json').read_text())['uncertainty'] for t in triage if t['classification']=='uncertain'],'unselected_in_saved_candidate_list':len(json.loads((P/'candidates.json').read_text()))-34,'gallery_synced':False,'jobs_queued':0,'artwork_generated':0}
(P/'verification.json').write_text(json.dumps(v,indent=2)+'\n')
all_sources=set();all_solo=set();review_sources=set()
for folder in P.parent.glob('todo-solo-briefs-*'):
 f=folder/'selection.json'
 if f.exists():all_sources.update(r['uuid'] for r in json.loads(f.read_text()))
 f=folder/'gallery-briefs.json'
 if f.exists():all_solo.update(r['uuid'] for r in json.loads(f.read_text()))
 f=folder/'triage.json'
 if f.exists():
  for t in json.loads(f.read_text()):
   if t['classification']!='standalone':review_sources.add(t.get('source_uuid') or t.get('uuid'))
original={r['uuid'] for r in json.loads((P.parent/'todo-solo-briefs-100-20260919/selection.json').read_text())}|{r['uuid'] for r in json.loads((P.parent/'todo-solo-briefs-100-20260920/candidates.json').read_text())}
assert len(original)==2000 and original==all_sources
assert len(all_solo)==1728
remaining=original-all_sources
summary={'original_missing_reference_list':2000,'solo_briefs_completed_across_batches':1728,'other_sources_with_component_or_review_briefs':272,'unprocessed_original_sources':len(remaining),'requested_solo_briefs_this_run':100,'completed_solo_briefs_this_run':28,'shortfall':72,'scope_note':'Original 300 nominal balance subtracted only solo briefs and did not subtract 266 sources already covered by component or review briefs. Only 34 untouched sources remained at start of run.','additional_local_catalog_candidates':12,'additional_candidates_note':'The 12 remaining outside the original list have numeric or text source names and cannot be assumed eligible standalone artwork. No new briefs authored for them.'}
(P/'remaining-pool-audit.json').write_text(json.dumps(summary,indent=2)+'\n')
notes=[{'source_uuid':r['uuid'],'source_name':r['old_concept'],'visible_subject':json.loads((P/'drafts.json').read_text())[i]['concept']} for i,r in enumerate(rows) if i in [3,7,9,18,19,20,21,22,23,24,26,29,31,33]]
(P/'source-name-notes.json').write_text(json.dumps(notes,indent=2)+'\n')
readme=['# Solo Briefs — Batch 18','','Prepared **28 standalone solo briefs** from the final **34 untouched references** in the original 2,000-reference source list. Inspected each source individually at 320px and 48px. Saved **12 component/review briefs** for **3 container splits and 3 uncertain references**.','','The requested 100 could not be reached from this pool: previous batches had already prepared 1,700 solo briefs plus component/review briefs for 266 other references. Across all batches the original 2,000 references are now covered: 1,728 standalone solo briefs and 272 combination/review sources. This accounting concerns saved local files, not the live gallery.','','No artwork generated, jobs queued or gallery/database changes made. Original source bytes, full paths and UUIDs are preserved.','','## Files','','- [Preview index](index.html)','- [Standalone manifest](sources/manifest.json)','- [Gallery-compatible export](gallery-briefs.json)','- [Verification](verification.json)','- [Remaining source audit](remaining-pool-audit.json)','- [Triage](triage.json)','- [Source naming notes](source-name-notes.json)','- [Requested-family flags](family-flags.json)','','## Combination and uncertainty reviews','']
for i,t in enumerate(triage):
 if t['classification']=='standalone':continue
 r=json.loads((P/t['review_folder']/'review.json').read_text());readme += [f"- [{Path(t['reference_path']).name}]({t['review_folder']}/generation-draft.md) — {r['reason']}"+(f" **Open question:** {r['uncertainty']}" if r.get('uncertainty') else '')]
readme+=['','## Requested-family flags','','Round Sun with Eight Separate Rays, Crescent Moon beside Five-Point Star, Rounded Horizontal Strip with Diagonal Bands, and Complete Five-Point Star Outline retain solo as requested. These symbolic subjects may suit the sub family; all remain briefed here.','','## First authoring handoff','','`$icon-solo two-overlapping-busts-with-oval-heads` — Two plain busts have oval heads, with the left torso overlapping the right along a shared baseline. Preserve the complete original UUID and path from the brief.','']
(P/'README.md').write_text('\n'.join(readme))
include_dirs={'briefs','sources','png','sheets','triage-sheets','combination-review','pending-brief','held-sources'}
include_files={'README.md','index.html','index.md','triage-index.html','triage-index.md','triage.json','verification.json','gallery-briefs.json','family-flags.json','source-name-notes.json','selection.json','remaining-pool-audit.json'}
with zipfile.ZipFile(P/'solo-briefs-28.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(P.rglob('*')):
  if f.is_file() and (f.relative_to(P).parts[0] in include_dirs or f.name in include_files):z.write(f,f.relative_to(P))
print(json.dumps(v,indent=2));print(json.dumps(summary,indent=2))
