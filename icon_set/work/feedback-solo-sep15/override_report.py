from pathlib import Path
import json,base64,hashlib,shutil,zipfile,re,sys
ROOT=Path(__file__).resolve().parents[3];W=Path(__file__).resolve().parent
SOURCE_ICON_ID=None
SOURCE_PATH='/Users/jakesdev/Downloads/feedback-briefs 2/solo'
AUTHOR='gpt-6'
sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import render_svg,build_paths
plan=json.loads((W/'override-plan.json').read_text());R=json.loads((W/'revisions.json').read_text());old=json.loads((W/'review-data.json').read_text());by_number={x['number']:x for x in old};by_brief={n:p for p in plan for n in p['feedback_numbers']};result=json.loads((W/'override-build-status.json').read_text());assert result['exit_code']==0,result
qa=[]
for path in (ROOT/'icon_set/dist/qa/results').glob('*.json'):qa.extend(json.loads(path.read_text())['icons'])
qa={x['icon_id']:x for x in qa if x.get('family')=='solo'};sources=W/'applied/sources';exports=W/'applied/solo48';sources.mkdir(parents=True,exist_ok=True);exports.mkdir(parents=True,exist_ok=True);applied={}
encode=lambda s:'data:image/svg+xml;base64,'+base64.b64encode(s.encode()).decode()
for row in plan:
 id=row['id'];assert qa[id]['status']=='pass' and not qa[id]['errors'] and not qa[id]['warnings'],(id,qa[id]['status']);target=ROOT/row['target'];assert hashlib.sha256(target.read_bytes()).hexdigest()==row['after_sha256'],('Original changed during build',id)
 icon=create(id);svg=render_svg(icon);published=ROOT/'icon_set/dist/solo48'/f'{id}.svg';assert published.read_text()==svg,(id,'export mismatch')
 previous=base64.b64decode(by_number[row['selected_brief']]['after'].split(',',1)[1]).decode();strip_title=lambda s:re.sub(r'<title>.*?</title>','',s);assert strip_title(previous)==strip_title(svg),(id,'geometry differs from proposal')
 shutil.copy2(target,sources/target.name);shutil.copy2(published,exports/published.name);applied[id]={'svg':svg,'keyshape':icon.keyshape.name,'qa':{k:qa[id].get(k) for k in ['status','errors','warnings']},'source':str((sources/target.name).relative_to(W))}
rows=[]
for oldrow in old:
 row=dict(oldrow);p=by_brief.get(row['number'])
 if p:
  selected=by_number[p['selected_brief']];current=applied[p['id']];different=R[str(row['number'])]['id']!=p['selected_proposal'];row.update(id=p['id'],after=encode(current['svg']),afterCenterline=selected['afterCenterline'],qa=current['qa'],keyshape=current['keyshape'],file=current['source'],download=f'applied/solo48/{p["id"]}.svg',related=p['feedback_numbers'],reference=selected['reference'],status='superseded' if different else 'revised',note=selected['note']+' Applied directly to the original icon file.')
  if different:row['note']+=f' This brief’s alternative was superseded by brief {p["selected_brief"]}, the highest-numbered brief for this original. Both cards show the version now applied.'
 rows.append(row)
counts={k:sum(x['status']==k for x in rows) for k in ['revised','superseded','split','missing']};summary={'brief_count':155,'original_icons_overwritten':135,'new_variant_files':0,'counts':counts,'full_export_validation':{'pass':135,'errors':0,'warnings':0},'backup':'originals-before-override.tar.gz','selection_rule':'Highest-numbered feedback brief chooses the applied drawing when proposals differ for one original.'}
template=(W/'report-template.html').read_text();template=template.replace('Every available icon has a revised drawing. Compare before and after, inspect the centerlines, and check each result at its actual 48-pixel size.','The original icon files have been updated in place, keeping their existing names and IDs. Compare the previous drawings with the versions now applied, including their centerlines and actual 48-pixel size.')
template=template.replace('<strong>142</strong><span>revised designs · 153 feedback entries</span>','<strong>135</strong><span>original icons overwritten · 153 feedback entries</span>').replace('icons retained without changes','new variant files added').replace('142 / 142 revised designs','135 / 135 updated originals').replace('These are proposals for your visual review. Original sources are preserved in this report’s isolated snapshot.','The applied drawings are now published under the original icon IDs in the local library. A backup preserves the files from before replacement.')
start=template.index('<details class="audit">');end=template.index('</details>',start)+len('</details>');template=template[:start]+'''<details class="audit"><summary>Applied changes and validation</summary><p>135 original model files were overwritten and rebuilt in the local icon library. No new variant files were added to the library. Every applied icon passed geometry, spacing, symmetry and enclosed-gap checks, and each exported SVG matches its model.</p><p>Six originals had multiple proposals. The highest-numbered brief supplies the applied version. Seven earlier alternative entries are marked “Superseded proposal”; their cards show the actual applied drawing and identify the brief used.</p><p>The two combination cases remain separate: the monitor has two component briefs, while the knight-on-shield original is still missing.</p><p><a href="override-summary.json">Applied summary</a> · <a href="override-applied.json">Files overwritten</a> · <a href="override-build.log">Build log</a> · <a href="originals-before-override.tar.gz">Previous originals backup</a> · <a href="applied-originals.zip">Updated originals and SVGs</a></p></details>'''+template[end:]
template=template.replace('<option value="revised">New revisions</option>','<option value="revised">Applied feedback</option><option value="superseded">Superseded proposals</option>').replace("revised:'New revision'","revised:'Original updated',superseded:'Superseded proposal'").replace("'Proposed fix'","'Applied original'").replace('This proposal also serves briefs','This updated original appears in briefs').replace('These controls do not approve or modify icons in the shared gallery.','The original icon files have already been updated; these controls only record your review.').replace('pictographic-feedback-solo-2026-09-15-v1','pictographic-feedback-solo-2026-09-15-applied-v1')
archive=W/'before-override-report';archive.mkdir(exist_ok=True)
for name in ['review.html','review-data.json','summary.json','README.md']:
 shutil.copy2(W/name,archive/name)
(W/'override-summary.json').write_text(json.dumps(summary,indent=2));(W/'summary.json').write_text(json.dumps(summary,indent=2));(W/'review-data.json').write_text(json.dumps(rows,indent=2));(W/'review.html').write_text(template.replace('__REPORT_DATA__',json.dumps({'summary':summary,'rows':rows},ensure_ascii=False).replace('</','<\\/')))
(W/'README.md').write_text('''# Applied original icon fixes

135 original icon files were overwritten in icon_set/model/icons/solo, keeping their original IDs and filenames. All 135 passed the current full icon export checks and were published in icon_set/dist/solo48.

Open review.html for before/after and centerline comparisons. Seven earlier proposals are marked superseded because six originals had differing feedback proposals; the highest-numbered brief was applied in each case. The two combination/missing-source cases remain unresolved as described in the report.

applied-originals.zip contains the actual updated original model files and SVG exports. originals-before-override.tar.gz preserves the previous live originals. The older snapshot and sources-and-icons.zip are historical proposal artifacts, not the applied library version.
''')
with zipfile.ZipFile(W/'applied-originals.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in (W/'applied').rglob('*'):
  if p.is_file():z.write(p,str(p.relative_to(W)))
 for name in ['review.html','README.md','override-summary.json','override-applied.json','override-build.log']:z.write(W/name,name)
print(json.dumps(summary,indent=2))
