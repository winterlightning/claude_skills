from pathlib import Path
import json
OUT=Path(__file__).parent;ROOT=OUT.resolve().parents[2];rows=json.loads((OUT/'claims.json').read_text())
notes={
0:('Pinched sweet lobes and a squat kite.','Rebuilt a broad three-lobed mound, clear bowl opening, tapered kite and flowing tail.','Individual sweet divisions and kite spars omitted.'),
1:('A single semicircle substitutes for the three sweets; the kite dominates.','Restored the three-lobed sweet mound, bowl and tapered kite.','Individual sweet divisions and kite spars omitted.'),
2:('A parallelogram kite, compressed cloud and flattened tail differ from the reference.','Redrew a pointed kite, an open rounded cloud and curling tail.','Kite spars omitted.'),
3:('Both outlined knife handles are reduced to rods.','Restored two outlined diagonal handles attached to a broad sloping block.','Wood grain and blade seams omitted.'),
4:('The palm becomes a Y with only two fronds.','Added a third downward frond, improved the curved trunk and balanced the seated figure and laptop.','Screen logo and shoreline omitted; detached head ink gap is 4 units.'),
5:('Two bulky leaf loops per side lose the repeated laurel pattern.','Restyled six leaf strokes per branch around paired curved branches and crossed stems.','Leaf interiors replaced by single strokes for clear spacing.'),
6:('The top layer has sharp corners and the lower pasta edge is almost flat.','Rounded top corners, smoothed the wavy filling and added a curved lower edge.','Lower closed seam omitted to maintain layer clearance.'),
7:('The brain is pinched and the jaw and neck are angular.','Enlarged the brain opening and smoothed the head, jaw and neck contours.','Internal brain folds omitted.'),
8:('The lower lightning shape is completely absent.','Restored the lightning zigzag below the open wrench jaw and rounded handle end.','Intentional diagonal asymmetry preserved.'),
9:('Rigid shield-like masks and compressed expression marks.','Rebalanced the overlapping masks with rounded bottoms and opposing mouth curves.','Eyes omitted to keep the expression marks separated.'),
10:('A flat wide face and dot beak lose the owl silhouette.','Reworked the sweeping brow, rounded cheeks, paired circular eyes and small pointed beak.','Inner facial-disc seams omitted.'),
11:('Mechanical symmetry and crowded fronds compress the island scene.','Introduced a curved leaning trunk, four flowing fronds and a broad island arc.','Water ripples omitted; tree asymmetry is deliberate.'),
12:('Three straight alert rays replace the spreading firework trails.','Curved the three diverging trails and rebalanced three identical spectators.','Spark crosses omitted; each head-to-shoulder ink gap is exactly 4 units.'),
13:('The folded wing disappears into a thin generic silhouette.','Broadened the chest and tail, restored a short folded-wing contour and retained the hooked beak and foot.','Eye omitted to preserve the small head opening.'),
14:('Stacked narrow neck rectangles crowd a tiny circular bulb.','Simplified the neck, enlarged the bulb and made a taller rounded bottle with a clear hose.','Secondary neck collar omitted.'),
15:('A stiff stick torso replaces the reference bust.','Restored smooth broad shoulders behind a three-panel balcony rail.','Head-to-shoulder ink gap is exactly 4 units.'),
16:('Horizontal smoke curls surround an undersized bust.','Rebuilt tall rising smoke contours and enlarged the centered head and shoulders.','Secondary plume contours omitted; bust ink touches at the center.'),
17:('A striding person appears to hold the bucket, unlike the standing reference.','Separated the tapered beach bucket from the figure and removed the trailing foot extension.','Beach waves omitted; detached head ink gap is exactly 4 units.'),
18:('A one-legged figure stands beside a blank guitar body.','Added two legs, a straight neck and a visible soundhole in a broader waisted guitar.','Strings, bridge and tuning pegs omitted; detached head ink gap is exactly 4 units.'),
19:('The small person has sharp angular arms beside the peak.','Smoothed the hanging arms around a coherent torso and balanced the standing figure and mountain.','Snow seam omitted for spacing; detached head ink gap is exactly 4 units.'),
}
lines=['# Once-disapproved solo fix batch 06','', '20 claimed at offset 0 using `--max-disapprovals 1`. Worker: `thuan-mac`. All 20 finished through `primitive_fix.py finish`, uploaded, and returned to **Ready**.','', 'Every module has `AUTHOR = "gpt-6"`. Every final geometry report is **valid**, and every full build gate is **pass**, with **zero errors and zero warnings**. No written reviewer feedback was present for these claims; revisions follow visual comparison with each original.','', 'All original/rejected/final comparisons and native light/dark previews were visually inspected. Fresh attempts and failed validation evidence remain in their own run directories.','', '## Comparison sheets','']
for j in range(4):lines.append(f'- [Original / rejected / final, icons {j*5+1}–{j*5+5}]({(OUT/f"after-{j}.png").resolve()})')
audit=[]
for i,r in enumerate(rows):
 fix=Path(r['fix']);res=json.loads((fix/'result.json').read_text());run=Path(res['make_ray_run']);meta=json.loads((run/'result.json').read_text());before,change,omit=notes[i]
 assert res['outcome']=='done' and res['review_status']=='ready' and res['author']=='gpt-6'
 assert res['validation_status']=='valid' and not res['validation_errors'] and not res['validation_warnings']
 assert res['build_gate']['status']=='pass' and not res['build_gate']['errors'] and not res['build_gate']['warnings']
 meta['comparison_findings']=before;meta['feedback']='No written feedback';meta['changes']=change;meta['omissions_and_construction']=omit
 (run/'result.json').write_text(json.dumps(meta,indent=2)+'\n')
 svg=run/(r['id']+'.svg')
 keyshape=__import__("re").search(r"keyshape = Keyshape\.(\w+)",(run/meta["module"]).read_text()).group(1)
 lines+=['',f'## {i+1}. `{r["key"]}`','',f'Before: {before} Feedback: none recorded. {change} {omit}','',f'Author: `gpt-6`. Keyshape: `{keyshape}`. Validation: **valid / build pass / zero warnings**. Production: **Ready**.','',f'[RESULT_DIR]({run.resolve()}) · [SVG]({svg.resolve()}) · [Module]({(run/meta["module"]).resolve()}) · [Finish receipt]({(fix/"result.json").resolve()})','',f'Construction reference: {meta["references"]}']
 audit.append(dict(key=r['key'],run=str(run),svg=str(svg),author=res['author'],validation_status=res['validation_status'],build_gate=res['build_gate']['status'],review_status=res['review_status'],finished_at=res['finished_at']))
(OUT/'REPORT.md').write_text('\n'.join(lines)+'\n');(OUT/'audit.json').write_text(json.dumps(audit,indent=2)+'\n');print('Verified',len(audit),'done / ready / valid / pass; zero warnings.');print(OUT/'REPORT.md')
