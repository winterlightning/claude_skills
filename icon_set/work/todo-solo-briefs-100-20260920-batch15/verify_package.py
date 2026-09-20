from pathlib import Path
import json,re,collections,zipfile,hashlib
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
rows=json.loads((P/'selection.json').read_text());triage=json.loads((P/'triage.json').read_text());manifest=json.loads((P/'sources/manifest.json').read_text());drafts=json.loads((P/'drafts.json').read_text());glyphs=json.loads((ROOT/'icon_set/typeface/glyphs.json').read_text())['glyphs']
typeface=[]
for i,char in [(44,'Q'),(54,'”'),(82,'“'),(104,'”')]:
 t=triage[i];review=P/t['review_folder'];g=next((g for g in glyphs if g['character']==char and g.get('preferred')),None)
 record={'source_uuid':rows[i]['uuid'],'reference_path':t['reference_path'],'text':char,'arrangement':'single uppercase character' if char=='Q' else 'two quotation strokes side by side','glyph_catalog':'icon_set/typeface/glyphs.json','glyph_icon_id':g['icon_id'] if g else None,'missing_characters':[] if g else [char],'generation_status':'reuse_existing_glyph' if g else 'held_missing_glyph','instructions':'Reuse the preferred stored glyph paths and natural proportions. Do not create replacement glyph geometry.'}
 (review/'typeface-reuse.json').write_text(json.dumps(record,indent=2)+'\n');typeface.append(record)
 details=f"\n## Typeface lookup\n\n- exact content: `{char}`\n- existing glyph ID: `{g['icon_id'] if g else 'MISSING'}`\n- catalog: `icon_set/typeface/glyphs.json`\n\n"+(f"Reuse the preferred `{g['icon_id']}` paths with natural proportions and baseline metrics.\n" if g else 'This exact closing quotation character is absent from the preferred glyph catalog. Generation is held until an approved existing glyph is supplied; do not substitute the opening mark or invent replacement paths.\n')
 for filename in ['generation-draft.md','component-1.md']:
  f=review/filename;f.write_text(f.read_text()+details)
 if not g:
  f=review/'review.json';d=json.loads(f.read_text());d['uncertainty']='Preferred closing double quotation glyph ” is missing; an approved glyph is required before generation.';f.write_text(json.dumps(d,indent=2)+'\n')
(P/'typeface-reuse.json').write_text(json.dumps(typeface,indent=2)+'\n')
# Regeneration preserves old sheets, so remove only this run's obsolete extra standalone sheet.
extra=P/'sheets/sheet-04.png'
if extra.exists():extra.unlink()
assert len(manifest)==100
assert len(list((P/'briefs').glob('*.md')))==100
assert {m['family'] for m in manifest}=={'solo'}
assert len({m['icon_id'] for m in manifest})==100
existing=set(json.loads((P/'existing-ids.json').read_text()))
assert not existing.intersection(m['icon_id'] for m in manifest)
assert len({r['uuid'] for r in rows})==135
prior=set()
for f in P.parent.glob('todo-solo-briefs-*/selection.json'):
 if f.parent!=P:prior.update(r['uuid'] for r in json.loads(f.read_text()))
assert not prior.intersection(r['uuid'] for r in rows)
components=0;copies=0
for i,(r,t) in enumerate(zip(rows,triage)):
 src=ROOT/t['reference_path'];assert src.is_file();assert src.name.endswith(r['uuid']+'.svg')
 for png in [t['inspected_large'],t['inspected_native']]:assert (P/png).is_file()
 if t['classification']=='standalone':
  f=P/'sources'/src.name;assert f.read_bytes()==src.read_bytes();copies+=1
  b=(P/'briefs'/(src.stem+'.md')).read_text();assert r['uuid'] in b and t['reference_path'] in b
  assert '- native 48px:' in b and '- family: solo' in b and '$icon-solo' in b
  assert 'You can try modifying a copy' in b
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
 assert 6<=len(m['tags'])<=10 and all(t==t.lower() for t in m['tags'])
for f in (P/'pending-brief').glob('*/*/*.svg'):
 original=next(ROOT/t['reference_path'] for t in triage if Path(t['reference_path']).name==f.name)
 assert f.read_bytes()==original.read_bytes();copies+=1
counts=dict(collections.Counter(t['classification'] for t in triage))
verification={'source_references_inspected':135,'standalone_solo_briefs':100,'counts':counts,'saved_review_sources':35,'saved_component_briefs':components,'verified_byte_identical_copies':copies,'duplicate_sources_from_prior_batches':0,'duplicate_or_existing_solo_ids':0,'native_size':48,'missing_glyphs':['”'],'missing_glyph_source_count':2,'nominal_remaining':500,'uninspected_in_saved_candidate_list':len(json.loads((P/'candidates.json').read_text()))-135,'gallery_synced':False,'jobs_queued':0,'artwork_generated':0}
(P/'verification.json').write_text(json.dumps(verification,indent=2)+'\n')
notes={20:'The source is named probe; its visible subject is a round handheld inspection mirror.',39:'The source remnant is a blank header panel.',44:'The source Qualcomm logo shows a single Q; prepared as typeface reuse.',53:'The source remote access is a concentric hexagonal emblem without a visible access action.',59:'The source red shows only a blank rounded rectangle, with no color information.',69:'The reflection diagram has only one diagonal stroke attached to its lower bar.',90:'The source quarter is a geometric quarter-circle wedge, not a coin.',105:'The source ridge shows a right-facing arrow.',106:'The source Quora logo shows a rounded triangular outline, not a readable wordmark.',112:'The source rectangle pro has a blank inset slot; no readable PRO text appears.',122:'The source rhubarb is a generic three-leaf sprig without identifying stalk detail.',127:'The source ring of power shows a plain ring without ornament.',131:'The source riser shows a framed up arrow.'}
(P/'source-name-notes.json').write_text(json.dumps([{'source_uuid':rows[i]['uuid'],'reference_path':triage[i]['reference_path'],'note':note} for i,note in notes.items()],indent=2)+'\n')
readme=['# Solo Briefs — Batch 15','',f"Prepared **100 standalone solo briefs**, with 320px and 48px previews. Also saved **35 review sources** and **{components} independent component/reuse briefs**.",'','Saved locally; no gallery synchronization, generation jobs, database writes, or artwork builds. This continues the prior batches without reusing their source UUIDs. The nominal running balance is 500 of the original 2,000; the saved candidate list has 325 uninspected references after excluding all inspected and held sources. Neither is a live gallery count.','','## Files','','- [Visual index](index.html)','- [Standalone manifest](sources/manifest.json)','- [Gallery-compatible export](gallery-briefs.json), saved for later import','- [Triage record](triage.json)','- [Verification](verification.json)','- [Family flags](family-flags.json)','- [Source naming notes](source-name-notes.json)','','## Classification counts','']+[f'- {k}: {v}' for k,v in counts.items()]+['','## Held and split sources','','Clear container splits are prepared as components. Side combinations, uncertain sources, and typeface reuse sources retain review evidence. Every source below has saved generation or reuse briefs.']
for i,t in enumerate(triage):
 if t['classification']=='standalone':continue
 review=P/t['review_folder'];d=json.loads((review/'review.json').read_text());readme+=['',f"- [{Path(t['reference_path']).name}]({t['review_folder']}/generation-draft.md) — {d['reason']}"+(f" **Open question:** {d['uncertainty']}" if d.get('uncertainty') else '')]
readme+=['','## Family suitability','','Simple arrows, abstract symbols, logos, blank panels, and enclosure arrangements remain solo as requested. Their exact source IDs and notes are listed in family-flags.json. No family was silently changed in the standalone manifest.','','## First authoring handoff','', '`$icon-solo planet-with-small-moon` — A round planet with two curved surface marks and a small moon overlapping its upper right edge. Use the full source UUID and path in the linked brief.','']
(P/'README.md').write_text('\n'.join(readme))
# Package only deliverables; omit authoring utilities and the unselected candidate list.
include_dirs={'briefs','sources','png','sheets','triage-sheets','combination-review','pending-brief','held-sources'}
include_files={'README.md','index.html','index.md','triage-index.html','triage-index.md','triage.json','verification.json','gallery-briefs.json','family-flags.json','source-name-notes.json','typeface-reuse.json','selection.json'}
with zipfile.ZipFile(P/'solo-briefs-100.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(P.rglob('*')):
  if f.is_file() and (f.relative_to(P).parts[0] in include_dirs or f.name in include_files):z.write(f,f.relative_to(P))
print(json.dumps(verification,indent=2));print('Zip bytes',(P/'solo-briefs-100.zip').stat().st_size)
