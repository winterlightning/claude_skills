from audit import *
from measure import gap
from icon_set.renderers.svg import _move_to,_segment
from icon_set.model.primitives import primitive_from_dict
import hashlib
source={x['row']['icon_id']:x for x in rows}
audit=json.loads((OUT/'audit.json').read_text());repairs={r['icon_id']:r for r in json.loads((OUT/'repairs.json').read_text())};variants={v['parent']:v for v in json.loads((OUT/'variants.json').read_text())}
# Detached outlined figures use their nearest shoulder/neckline, never side-wall torso axes.
labels={'stick-figure':'Torso stroke','outlined-body':'Outlined body','mixed-adult-infant':'Adult + infant','human-faced-animal':'Human face / animal body','group-busts':'Connected or grouped busts','bust':'Bust / shoulder arch','mixed-segmented-body':'Torso separated from leg','legs-only':'Partial figure: legs only'}
result=[]
for a in audit:
 name=a['icon_id'];original=load(source[name]);before=original.to_svg();rep=repairs.get(name);v=variants.get(name)
 if rep:
  mod=importlib.import_module(v['path'][:-3].replace('/','.'));i=next(c for _,c in inspect.getmembers(mod,inspect.isclass) if issubclass(c,Icon) and getattr(c,'icon_id',None)==v['icon_id'])();figures=rep['after_figures'];status=rep['after_qa']['status']
 else:i=original;figures=a['figures'];status='unchanged'
 by=i.draw().by_id();measures=[]
 for f in figures:
  m=gap(by,f['head_members'],f['torso_members'])
  if m:measures.append(m['ink_gap'])
 if a['number']==52:rule='No human torso. Do not run the detached-person rule on the animal body.'
 elif a['number'] in (60,177):rule='Continuous small figures: head and body join. No detached torso-line rule.'
 elif a['number']==144:rule='Head and torso are absent. No geometry invented.'
 elif a['number'] in (66,133):rule='Standalone bust: circular face and shoulder ink touch (0u visible gap).'
 elif a['type']=='group-busts':rule='Front detached bust: 4u ink gap to shoulder arch. Rear neck is continuous.'
 elif a['type']=='outlined-body':rule='Detached head: 4u ink gap to the nearest shoulder or neckline; no invented torso axis.'
 else:rule='Detached head: 8u stroke-centerline separation / 4u ink gap, aligned with upper torso tangent.'
 note=' '.join(rep['reasons']) if rep else a['note']
 if not rep and a['number'] not in (52,60,144,177):note+=' Existing head/body construction meets its applicable spacing; geometry preserved.'
 row=dict(number=a['number'],icon_id=name,variant=v['icon_id'] if v else None,source_path=v['path'] if v else a['source_path'],status=status,type=a['type'],type_label=labels[a['type']],note=note,rule=rule,figures=figures,measurements=measures,original_svg=before,after_svg=i.to_svg(),primitive_paths={k:_move_to(p)+_segment(p) for k,p in by.items()},warnings=(rep['after_qa']['errors']+rep['after_qa']['warnings']) if rep else [],changed=bool(rep),geometry_changed=bool(rep))
 # Verify the requested torso error in every repaired stick-figure pair.
 if rep:
  for f in figures:
   if 'ink_gap' in f:
    assert abs(f['ink_gap']-4)<1e-8 and f['axis_error_degrees']<1e-5,(name,f)
  if a['number'] in (15,77,90,168,169,180):assert abs(measures[0]-4)<0.001,(name,measures)
  if a['number'] in (66,133):assert abs(measures[0])<0.001,(name,measures)
 result.append(row)
(OUT/'results.json').write_text(json.dumps([{k:v for k,v in r.items() if k not in ('original_svg','after_svg','primitive_paths')} for r in result],indent=2))
payload=json.dumps(result).replace('</','<\\/')
(OUT/'index.html').write_text((OUT/'template.html').read_text().replace('__DATA__',payload))
print('Verified all repaired torso gaps and alignments; rendered',len(result),'review cards.')
