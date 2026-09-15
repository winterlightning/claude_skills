from pathlib import Path
import json,hashlib,zipfile
W=Path(__file__).resolve().parent
R=json.loads((W/'revisions.json').read_text());V=json.loads((W/'validation.json').read_text());M=json.loads((W/'build/solo48/manifest.json').read_text())['icons'];ids={v['id'] for v in R.values()}
assert {m['icon_id'] for m in M}==ids
for id in ids:
 p=W/'build/solo48'/f'{id}.svg';assert p.read_text()==V[id]['svg'],id
for r in R.values():assert (W/'snapshot'/r['file']).is_file()
readme='''# Solo icon feedback review

Open review.html in a browser. All comparison images and centerline diagrams are embedded and work offline. Use Drawing view to switch between finished icons and their construction. Blue paths show centerlines, gray shows the 4-pixel stroke, and red dots mark segment endpoints.

- 155 feedback entries are accounted for.
- 142 revised designs address 153 entries, including shared revisions for matching requests.
- All 51 previously retained entries now have changed geometry; no available icons remain unchanged.
- The monitor/download combination has two local component briefs.
- The exact knight-on-shield original is missing and remains unresolved.
- All 142 revised designs pass model validation and the full export checks.
- All 135 original parent source files in this snapshot match their recorded initial hashes.

The final proposals are in build/solo48. Their authoring files are in snapshot/icon_set/model/icons/solo. revisions.json maps each brief to its source and design ID. The snapshot includes the model and build support code needed by those revisions. Run run_build.py from this folder to reproduce the targeted export with a compatible Python environment and the repository's rendering dependencies.

The shared gallery was consolidated by another task while this work was in progress. These final revisions are isolated here; they have not been published to the shared gallery. Do not copy the whole snapshot over the active repository. Review and integrate selected revision files after checking for ID collisions.

The broader repository test suite was not green: 385 tests, 25 failures, 59 errors, 6 skipped. The tests ran inside the isolated snapshot under Python 3.10 with sandbox restrictions; some fixtures were omitted, local server tests could not bind, and a reconstruction helper required a newer Python syntax. Other failures involved existing corpus expectations. See tests.log. Successful icon exports are separate from this wider suite result.

Your review choices and notes are stored only in your browser. Use Export my review to save them. No gallery approval is recorded by this page.
'''
(W/'README.md').write_text(readme)
files=set()
for name in ['review.html','README.md','summary.json','inventory.json','revisions.json','validation.json','release-validation.json','geometry-changes.json','parent-integrity.json','build-status.json','tests.log','final-build.log','build.log','run_build.py','monitor-split.json']:
 files.add(W/name)
for root in [W/'build',W/'component-briefs',W/'snapshot/icon_set']:
 for p in root.rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ['.pyc','.sqlite3'] and not ('tests' in p.relative_to(W).parts):files.add(p)
with zipfile.ZipFile(W/'sources-and-icons.zip','w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(files):z.write(p,str(p.relative_to(W)))
(W/'delivery-check.json').write_text(json.dumps({'briefs':155,'model_valid':142,'exported_svgs_matching_report':142,'feedback_entries_changed':153,'retained':0,'original_parents_unchanged':135,'package_files':len(files),'package_bytes':(W/'sources-and-icons.zip').stat().st_size,'browser_checks':['all entries render','search','dark theme','153 revised filter','centerline view','missing original filter','review decision and note persistence','temporary decisions and notes cleared','no browser console errors']},indent=2))
print((W/'delivery-check.json').read_text())
