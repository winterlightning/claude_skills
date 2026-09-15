from pathlib import Path
import json
W=Path(__file__).resolve().parent
SOURCE_ICON_ID=None
SOURCE_PATH='/Users/jakesdev/Downloads/feedback-briefs 2/solo'
AUTHOR='gpt-6'
p=W/'make_report.py';s=p.read_text();s=s.replace('W=Path(__file__).resolve().parent','W=Path(__file__).resolve().parent\nfrom round2_preview import centerline,create,build_paths')
s=s.replace('rows=[];parents={}','rows=[];parents={};geometry_changes={};centerlines={}\ndef diagnostic(id):\n if id not in centerlines:centerlines[id]=centerline(create(id))\n return centerlines[id]')
s=s.replace("rows.append({'number':", "if r:\n  changed=[p['d'] for p in build_paths(create(r['parent']).draw())]!=[p['d'] for p in build_paths(create(id).draw())];assert changed,(n,'Unchanged drawing');geometry_changes[n]={'id':id,'geometry_changed':changed}\n rows.append({'beforeCenterline':encode(diagnostic(r['parent'])) if r else None,'afterCenterline':encode(diagnostic(id)) if r else None,'number':")
s=s.replace("'unique_revisions':len(V)","'unique_revisions':len({v['id'] for v in R.values()})")
s=s.replace("(W/'summary.json').write_text", "assert counts['retained']==0 and counts['revised']==153\n(W/'geometry-changes.json').write_text(json.dumps(geometry_changes,indent=2))\n(W/'summary.json').write_text")
p.write_text(s)
p=W/'report-template.html';s=p.read_text();s=s.replace('Compare the preserved icons with the proposed fixes. Every card includes your original feedback, the change made, and a true 48-pixel preview.','Every available icon has a revised drawing. Compare before and after, inspect the centerlines, and check each result at its actual 48-pixel size.')
s=s.replace('<strong>91</strong><span>new designs · 102 feedback entries</span>','<strong>142</strong><span>revised designs · 153 feedback entries</span>').replace('<strong>51</strong><span>current icons retained, with explanations</span>','<strong>0</strong><span>icons retained without changes</span>').replace('91 / 91 revised designs','142 / 142 revised designs')
s=s.replace('The 51 retained icons also pass the full icon checks. Their cards explain why they were retained; subjective recognizability still needs your judgment.','All 51 previously retained entries now have revised geometry. Every one of the 153 available entries was checked against its original drawing to confirm an actual change.')
s=s.replace('<option value="retained">Current retained</option>','').replace('minmax(200px,1fr) 195px 195px 140px','minmax(190px,1fr) 175px 185px 145px 140px')
s=s.replace('<select id="size"','<select id="drawing" aria-label="Drawing view"><option value="finished">Finished icons</option><option value="centerline">Centerlines</option></select><select id="size"')
s=s.replace('<div id="grid"','<p id="centerline-legend" class="live-note" hidden>Centerline view: blue paths · gray 4-pixel strokes · red endpoints · 4-unit grid. The small previews always show the finished icons at 48 pixels.</p>\n<div id="grid"')
s=s.replace('.dark .icon,.dark .native{filter:invert(1)}','.dark .icon:not(.diagnostic),.dark .native{filter:invert(1)}.diagnostic{background:#fff;border-radius:4px}')
s=s.replace("const labels={revised:'New revision',retained:'Current retained',split:","const labels={revised:'New revision',split:")
s=s.replace('const picture=(src,label)=>src?`<img class="icon" src="${src}"', 'const picture=(src,label,diagnostic)=>src?`<img class="icon ${$(\'drawing\').value===\'centerline\'&&diagnostic?\'diagnostic\':\'\'}" src="${$(\'drawing\').value===\'centerline\'&&diagnostic?diagnostic:src}"')
s=s.replace("const afterLabel=r.status==='retained'?'Current retained':r.status==='split'?", "const afterLabel=r.status==='split'?")
s=s.replace("'Original unavailable')}","'Original unavailable',r.beforeCenterline)}")
s=s.replace("'No replacement made')}","'No replacement made',r.afterCenterline)}")
s=s.replace("${r.status==='retained'?'Why retained':'Outcome'}",'Outcome')
s=s.replace("$('search').addEventListener", "$('drawing').addEventListener('change',()=>{$('centerline-legend').hidden=$('drawing').value!=='centerline';render()});\n$('search').addEventListener")
p.write_text(s)
p=W/'package_report.py';s=p.read_text().replace('91 new designs address 102 entries','142 revised designs address 153 entries').replace('51 current icons are retained with individual explanations.','All 51 previously retained entries now have changed geometry; no available icons remain unchanged.').replace('All 91 revised designs','All 142 revised designs').replace("'retained-validation.json','retained-notes.json',","'geometry-changes.json',").replace("'model_valid':91,'exported_svgs_matching_report':91", "'model_valid':142,'exported_svgs_matching_report':142,'feedback_entries_changed':153,'retained':0")
s=s.replace("'102 revised filter','51 retained filter'","'153 revised filter','centerline view'")
s=s.replace('All comparison images are embedded and work offline.','All comparison images and centerline diagrams are embedded and work offline. Use Drawing view to switch between finished icons and their construction. Blue paths show centerlines, gray shows the 4-pixel stroke, and red dots mark segment endpoints.')
p.write_text(s)
print('Report updated')
