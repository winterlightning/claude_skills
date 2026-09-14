from pathlib import Path
import json,shutil
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/holes-review/revision-2-results.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
backup=W/'revision-1';backup.mkdir(exist_ok=True)
for name in ['mapping.json','notes.json','results.json','review.html','review-manifest.json','make_gallery.py']:
 if not (backup/name).exists():shutil.copy2(W/name,backup/name)
revs=json.loads((W/'revision-2-results.json').read_text());assert len(revs)==9 and all(r['qa']['status']=='pass' and not r['qa']['warnings'] for r in revs)
lookup={r['original']:r for r in revs}
rows=json.loads((W/'results.json').read_text());rows=[lookup.get(r['original'],r) for r in rows]
(W/'results.json').write_text(json.dumps(rows,indent=2))
mapping=json.loads((W/'mapping.json').read_text());mlookup={m['original']:m for m in json.loads((W/'revision-2-mapping.json').read_text())};mapping=[mlookup.get(m['original'],m) for m in mapping]
(W/'mapping.json').write_text(json.dumps(mapping,indent=2))
notes=json.loads((W/'notes.json').read_text());notes.update(json.loads((W/'revision-2-notes.json').read_text()));(W/'notes.json').write_text(json.dumps(notes,indent=2))
(W/'excluded.json').write_text(json.dumps({'user-with-gear':{'reason':'Removed from the review batch at the user’s request.','source_preserved':True}},indent=2))
# Upgrade the original gallery generator without changing production gallery files.
p=W/'make_gallery.py';s=p.read_text()
s=s.replace("assert len(rows)==65 and all(r['qa']['negative_space']['status']=='pass' for r in rows)","excluded=json.loads((W/'excluded.json').read_text()) if (W/'excluded.json').exists() else {}\nrevised={r['original'] for r in json.loads((W/'revision-2-mapping.json').read_text())} if (W/'revision-2-mapping.json').exists() else set()\nrows=[r for r in rows if r['original'] not in excluded]\ntotal=len(rows)\nassert all(r['qa']['negative_space']['status']=='pass' for r in rows)")
s=s.replace("before=Path('icon_set/dist/failed/solo48',name+'.svg').read_text();after=", "before=((W/(r['previous_candidate']+'.svg')).read_text() if name in revised else Path('icon_set/dist/failed/solo48',name+'.svg').read_text());after=")
s=s.replace('data-name="{html.escape(name)}" data-status=', 'data-name="{html.escape(name)}" data-revised="{str(name in revised).lower()}" data-status=')
s=s.replace("{figure(before,'Original')}{figure(after,'Proposed fix')}","{figure(before,'Previous draft' if name in revised else 'Original')}{figure(after,'Revised' if name in revised else 'Proposed fix')}")
s=s.replace('<title>65 opening repairs — review</title>','<title>Opening repairs — latest revisions</title>')
s=s.replace('65 proposed repairs for the Undersized hole group. Compare the original and revised drawings, enlarged and at their actual 48-pixel size.','Nine requested revisions now pass all blocking checks. Compare their previous drafts and revised drawings, enlarged and at their actual 48-pixel size. Select All icons to view the full __TOTAL__-icon batch.')
s=s.replace('The live gallery was regenerated during this work and now lists 88 hole-failure icons; this batch covers the original 65 selected for repair.','User-with-gear has been removed from this review batch. All previous source versions are preserved.')
s=s.replace('<b>65 / 65</b>','<b>__TOTAL__ / __TOTAL__</b>')
s=s.replace('<option value="all">All 65 icons</option>', '<option value="revised" selected>Latest revisions (9)</option><option value="all">All __TOTAL__ icons</option>')
s=s.replace('<span id="count">65 icons</span>', '<span id="count">9 icons</span>')
s=s.replace("filter.value==='all'||card.dataset.status===filter.value", "filter.value==='all'||(filter.value==='revised'?card.dataset.revised==='true':card.dataset.status===filter.value)")
s=s.replace("filter.addEventListener('change',apply);", "filter.addEventListener('change',apply);apply();")
s=s.replace(".replace('__REMAIN__',str(65-passed))", ".replace('__REMAIN__',str(total-passed)).replace('__TOTAL__',str(total))")
s=s.replace("'opening_passes':65", "'opening_passes':total,'latest_revision_passes':len(revised),'excluded':list(excluded)").replace("'other_findings':65-passed", "'other_findings':total-passed")
p.write_text(s)
print('Applied nine review revisions and excluded user-with-gear.')
