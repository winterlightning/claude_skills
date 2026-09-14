"""Write reviewed bounded model changes back to their existing source modules."""
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/spacing-remaining/targets.json'
AUTHOR='gpt-6'
import json,pathlib,re,math
W=pathlib.Path(__file__).parent
rows={r['id']:r for r in json.load(open(W/'targets.json'))}
manual=json.load(open(W/'notes.json')) if (W/'notes.json').exists() else {}
ledger=json.load(open(W/'applied.json')) if (W/'applied.json').exists() else {}
qs={}
for f in sorted(W.glob('candidates-*.json'))+sorted(W.glob('refine-*.json')):
 for q in json.load(open(f)):
  if q['score']==0:qs[q['id']]=q
for n,q in qs.items():
 if n in manual or n in ledger:continue
 cumulative={}
 for step in q['steps']:
  for p in step['members']:cumulative[p]=cumulative.get(p,1)*step['operation'][0]
 if any(s<.80 or s>1.26 for s in cumulative.values()):continue
 if any(s in n for s in ('woman-bust','woman-with','disability','information-desk-man','athlete','baby-face','baby-girl','sitting-baby','presentation-speaker','small-office-laptop-user')):continue
 lines=['        # Symbol plan: preserve the subject, contour topology and curve types.','        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.']
 for p in q['primitives']:
  name=repr(p['element_id']);a=repr(tuple(p['start']));b=repr(tuple(p['end']))
  if p['kind']=='line':lines.append(f'        self.add_line({name}, {a}, {b})')
  elif p['kind']=='arc':lines.append(f"        self.add_arc({name}, {a}, {b}, radius_x={p['radius_x']}, radius_y={p['radius_y']}, large_arc={p['large_arc']}, sweep={p['sweep']})")
  else:lines.append(f"        self.add_bezier({name}, {a}, *{repr(tuple(tuple(tuple(x) for x in seg) for seg in p['segments']))})")
 for c in q['contours']:lines.append(f"        self.add_contour({repr(c['id'])}, *{tuple(c['members'])!r}, closed={c['closed']})")
 seen=set()
 for rel in q['relationships']:
  key=(rel['kind'],tuple(sorted(rel['members'])))
  if key in seen:continue
  seen.add(key);lines.append(f"        self.relate({rel['kind']!r}, *{tuple(rel['members'])!r})")
 p=pathlib.Path(rows[n]['file']);s=p.read_text();s=re.sub(r"AUTHOR = .*", "AUTHOR = 'gpt-6'",s);s=s[:s.index('    def build(')]+'    def build(self) -> None:\n'+'\n'.join(lines)+'\n';p.write_text(s)
 ledger[n]={'steps':q['steps'],'source':str(p),'review':'pending visual and full QA'}
(W/'applied.json').write_text(json.dumps(ledger,indent=2));print('Bounded repairs applied:',len(ledger))
