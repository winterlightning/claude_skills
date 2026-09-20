from pathlib import Path
import json,re,collections,zipfile
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
rows=json.loads((P/'selection.json').read_text());triage=json.loads((P/'triage.json').read_text());manifest=json.loads((P/'sources/manifest.json').read_text());glyphs=json.loads((ROOT/'icon_set/typeface/glyphs.json').read_text())['glyphs']
typeface=[]
for i,chars,component in [(0,'ᚱ',2),(24,'₹',1),(64,'S',2),(69,';',1),(112,'ZZ',2),(114,'$',2)]:
 t=triage[i];review=P/t['review_folder']; gs={ch:next((g for g in glyphs if g['character']==ch and g.get('preferred')),None) for ch in set(chars)}
 record={'source_uuid':rows[i]['uuid'],'reference_path':t['reference_path'],'text':chars,'text_identification':'unconfirmed runic interpretation' if i==0 else 'readable','arrangement':'two Z letters stepping upward right, second smaller' if i==112 else 'single upright character','glyph_catalog':'icon_set/typeface/glyphs.json','glyphs':[{'character':ch,'icon_id':g['icon_id'] if g else None} for ch,g in gs.items()],'missing_characters':[ch for ch,g in gs.items() if not g],'instructions':'Reuse preferred existing paths and natural metrics; never invent replacement glyph geometry.'}
 (review/'typeface-reuse.json').write_text(json.dumps(record,indent=2)+'\n');typeface.append(record)
 detail='\n## Typeface lookup\n\n'+f'- exact content: `{chars}`'+(' (identification pending)' if i==0 else '')+'\n- catalog: `icon_set/typeface/glyphs.json`\n'+''.join(f"- {ch}: `{g['icon_id'] if g else 'MISSING'}`\n" for ch,g in gs.items())+'\nReuse preferred stored paths and natural proportions. Do not trace replacement glyphs.\n'
 if i==0:detail+='The angular inscription may be ᚱ or a stylized R. Identification and an approved matching glyph remain unresolved; hold generation of this component.\n'
 if i==64:detail+='The source S is script-like; the existing preferred glyph is a reuse handoff, not authorization to author a new script letter.\n'
 for fn in ['generation-draft.md',f'component-{component}.md']:
  f=review/fn;f.write_text(f.read_text()+detail)
(P/'typeface-reuse.json').write_text(json.dumps(typeface,indent=2)+'\n')
extra=P/'sheets/sheet-04.png'
if extra.exists():extra.unlink()
assert len(manifest)==100 and len(list((P/'briefs').glob('*.md')))==100
assert {m['family'] for m in manifest}=={'solo'}
assert len({m['icon_id'] for m in manifest})==100
existing=set(json.loads((P/'existing-ids.json').read_text()));assert not existing.intersection(m['icon_id'] for m in manifest)
prior=set()
for f in P.parent.glob('todo-solo-briefs-*/selection.json'):
 if f.parent!=P:prior.update(r['uuid'] for r in json.loads(f.read_text()))
assert len({r['uuid'] for r in rows})==127 and not prior.intersection(r['uuid'] for r in rows)
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
 assert 6<=len(m['tags'])<=10 and all(t==t.lower() for t in m['tags'])
for f in (P/'pending-brief').glob('*/*/*.svg'):
 assert f.read_bytes()==srcmap[f.name].read_bytes();copies+=1
counts=dict(collections.Counter(t['classification'] for t in triage))
v={'source_references_inspected':127,'standalone_solo_briefs':100,'counts':counts,'saved_review_sources':27,'saved_component_briefs':components,'verified_byte_identical_copies':copies,'duplicate_sources_from_prior_batches':0,'duplicate_or_existing_solo_ids':0,'native_size':48,'missing_glyphs':['ᚱ'],'unresolved_questions':['Identify rune-like inscription and approved glyph','Rainbow and heart: equal emblem subjects or modifier','Flame trails: integrated arrow tail or separate fire symbol'],'nominal_remaining':400,'uninspected_in_saved_candidate_list':len(json.loads((P/'candidates.json').read_text()))-127,'gallery_synced':False,'jobs_queued':0,'artwork_generated':0}
(P/'verification.json').write_text(json.dumps(v,indent=2)+'\n')
notes={4:'The bear is an animal profile with an open mouth; no market chart appears.',10:'The reference is a nested frame with no contents.',15:'The flag is blank; no visible lettering or stripe pattern distinguishes a specific pride flag.',18:'The visible subject is a head cupped by hands; no separate status mark is present.',28:'The bulb, battery, and wire have gaps; the description preserves the incomplete visible circuit.',31:'The source rust shows a plain gear, not corrosion detail.',32:'The drawing pairs a floating bar with its oval shadow.',35:'A person is contained in a cylindrical chamber; the abstract source name does not identify a specific physical apparatus.',40:'The source sensor on contains only a circle with a diagonal stroke.',42:'The rabbit shares a physical riding position with the scooter; retained as a coherent scene.',51:'The rocket is depicted moving above a globe, not as a small corner status badge.',61:'The helmet and goggles form a natural safety-equipment set.',63:'The broad rear form is shelter-like but has no specific architectural details.',68:'The mounted camera points toward the parked scooter; retained as a surveillance scene.',70:'The face is blank; its hands communicate the pose.',81:'The source room is only a square with a small inset.',85:'The source saffron has three leaf-like forms without a distinguishable flower center.',86:'The source sectional shows a three-sector circular chart.',99:'The source silica shows an unconnected triangle and two circles.',101:'The lower face is covered by a broad rounded band; no readable code appears.',105:'The source softball has broad curving panels, resembling a basketball rather than stitched softball seams.',109:'The source sidewalk shows one upright divided slab.',113:'No readable free-shipping label appears on the cargo truck.',122:'The visible subject is a person with monocle and tie; the brief does not infer personality.',125:'The reference shows a blank stamp or signet silhouette with a broad rectangular head.'}
(P/'source-name-notes.json').write_text(json.dumps([{'source_uuid':rows[i]['uuid'],'reference_path':triage[i]['reference_path'],'note':note} for i,note in notes.items()],indent=2)+'\n')
readme=['# Solo Briefs — Batch 16','',f'Prepared **100 standalone solo briefs** after individual inspection at 320px and 48px. Saved **27 additional review sources** with **{components} independent component/reuse briefs**.','','Saved locally. No gallery synchronization, database writes, generation jobs, or artwork builds. All source UUIDs are new relative to earlier batches. The nominal running balance is 400 of the original 2,000; 198 references remain uninspected in the saved candidate list after excluding previous held sources. These are bookkeeping figures, not a live gallery count.','','## Files','','- [Visual index](index.html)','- [Standalone manifest](sources/manifest.json)','- [Gallery-compatible export](gallery-briefs.json), saved for later import','- [Triage record](triage.json)','- [Verification](verification.json)','- [Family suitability flags](family-flags.json)','- [Source naming notes](source-name-notes.json)','- [Typeface reuse lookup](typeface-reuse.json)','','## Classification counts','']+[f'- {k}: {n}' for k,n in counts.items()]+['','## Held and split references','','Every reference below includes generation briefs or a reuse draft. Clear container splits are ready as component handoffs. Side combinations and uncertain sources preserve evidence for review.']
for i,t in enumerate(triage):
 if t['classification']=='standalone':continue
 r=json.loads((P/t['review_folder']/'review.json').read_text());readme+=['',f"- [{Path(t['reference_path']).name}]({t['review_folder']}/generation-draft.md) — {r['reason']}"+(f" **Open question:** {r['uncertainty']}" if r.get('uncertainty') else '')]
readme+=['','## Family suitability','','The standalone family remains solo as requested. Abstract symbols, diagrams, blank frames, and room-plan outlines are identified in family-flags.json for a later family decision.','','## First authoring handoff','','`$icon-solo ruined-wall-with-stepped-top` — A ruined wall with an uneven stepped top and a tall arched doorway. Preserve its full source UUID and path from the brief.','']
(P/'README.md').write_text('\n'.join(readme))
include_dirs={'briefs','sources','png','sheets','triage-sheets','combination-review','pending-brief','held-sources'}
include_files={'README.md','index.html','index.md','triage-index.html','triage-index.md','triage.json','verification.json','gallery-briefs.json','family-flags.json','source-name-notes.json','typeface-reuse.json','selection.json'}
with zipfile.ZipFile(P/'solo-briefs-100.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(P.rglob('*')):
  if f.is_file() and (f.relative_to(P).parts[0] in include_dirs or f.name in include_files):z.write(f,f.relative_to(P))
print(json.dumps(v,indent=2));print('ZIP bytes:',(P/'solo-briefs-100.zip').stat().st_size)
