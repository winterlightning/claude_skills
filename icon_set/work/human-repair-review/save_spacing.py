"""Apply the reviewed second pass once; retain the prior variants as backups."""
from spacing_repair import *
notes={1:'Open the rifle-support elbow away from the forward leg.',26:'Raise and widen the pole-side elbow away from the bent leg.',27:'Raise the sail foot to clear the board.',34:'Separate the adult elbow from the infant raised legs.',42:'Shorten and open the trailing forearm.',66:'Explicitly identify the portrait as a bust; verify exact circular-jaw/curved-shoulder ink tangency analytically.',90:'Remove the short redundant rear hair stroke that pinches the neck.',96:'Rebalance both runners’ elbows and leg bends to preserve clear separation within and between figures.',100:'Separate the outstretched arm, raised leg and stair tread.',101:'Rebalance the carrier and box together; retain both circular heads and exact torso alignment.',104:'Move the chair back outward to clear the reclining body.',133:'Lower the passport-side elbow away from the booklet.',139:'Separate the raised arm and leg while keeping the arm clear of the head.',168:'Model the real hair/fringe junctions at the sides of the circular face, deepen the hair cap, and remove the redundant rear hair stroke.',169:'Model the real hair/fringe junctions at the sides of the circular face and remove the redundant rear hair stroke.',180:'Open the lightning-holding elbow away from the gown.'}
planned=[]
for r in repairs:
 i=change(current(r),r['number']);qa=record_report(i)
 assert qa['status']=='pass',(r['number'],qa['errors'],qa['warnings'])
 fs=evaluate(i,r['after_figures'])
 for f in fs:
  if 'ink_gap' in f:assert abs(f['ink_gap']-4)<1e-8 and f['axis_error_degrees']<1e-5,(r['number'],f)
 planned.append((r,i,qa,fs))
 print(r['number'],'verified',flush=True)
# All checks above must finish before saving any model.
backup=OUT/'spacing-before';backup.mkdir(exist_ok=True)
for r,i,qa,fs in planned:
 if r['number'] in notes:
  path=ROOT/vs[r['icon_id']]['path'];prior=path.read_text()
  assert '# Second spacing pass complete.' not in prior,path
  (backup/path.name).write_text(prior)
  record=i.to_record();prefix=prior.split('    def build(self):')[0]
  if r['number']==66:prefix+="    human_construction = 'bust'\n\n"
  lines=[prefix.rstrip(),'','    # Second spacing pass complete.','    def build(self):']
  for p in record['primitives']:
   id=p['element_id'];a=tuple(p['start']);b=tuple(p['end'])
   if p['kind']=='line':line=f'self.add_line({id!r}, {a!r}, {b!r})'
   elif p['kind']=='arc':line=f'self.add_arc({id!r}, {a!r}, {b!r}, radius_x={p["radius_x"]!r}, radius_y={p["radius_y"]!r}, large_arc={p["large_arc"]!r}, sweep={p["sweep"]!r})'
   else:line=f'self.add_bezier({id!r}, {a!r}, *{tuple(tuple(tuple(v) for v in seg) for seg in p["segments"])!r})'
   lines.append('        '+line)
  for c in record['contours']:lines.append(f'        self.add_contour({c["contour_id"]!r}, *{tuple(c["members"])!r}, closed={c["closed"]!r})')
  for rel in record['relationships']:lines.append(f'        self.relate({rel["kind"]!r}, *{tuple(rel["members"])!r})')
  for f in record.get('human_figures',[]):lines.append(f'        self.mark_human_figure({f["figure_id"]!r}, head={f["head"]!r}, torso={f["torso"]!r}, torso_junction={f["torso_junction"]!r})')
  output='\n'.join(lines)+'\n';compile(output,str(path),'exec');path.write_text(output)
  r['reasons'].append(notes[r['number']])
 r.update(after_record=i.to_record(),after_qa=qa,after_figures=fs)
 (OUT/'after'/f'{r["icon_id"]}.svg').write_text(i.to_svg())
(OUT/'repairs.json').write_text(json.dumps(repairs,indent=2))
print('Saved 16 corrected variants. All 21 repairs pass full QA.')
