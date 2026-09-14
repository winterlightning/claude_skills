from more_repairs import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
for id in ['ships-anchor','bobble-hat-with-seams','mars-astrological-symbol']:
 f=W/'candidates'/f'{id}.json';x=json.loads(f.read_text());r=x['record']
 if x.get('circles_reviewed'):continue
 if id=='ships-anchor':
  for p in r['primitives']:
   if p['element_id'].startswith('ring'):p['radius_x']=4
  note='Kept the suspension ring circular.'
 elif id.startswith('bobble'):
  move(r,lambda x,y:(x,16 if y==17 else y),lambda p:p['element_id'].startswith(('crown','bobble')))
  for p in r['primitives']:
   if p['element_id'].startswith('bobble'):p['radius_x']=p['radius_y']=4
  note='Kept a circular four-unit pompom at the shared crown apex.'
 else:
  reset(r);arc(r,'ring-top',(16,22),(22,24),10);arc(r,'ring-tr',(22,24),(26,32),10);arc(r,'ring-br',(26,32),(16,42),10);arc(r,'ring-bl',(16,42),(6,32),10);arc(r,'ring-tl',(6,32),(16,22),10);contour(r,'ring','ring-top','ring-tr','ring-br','ring-bl','ring-tl',closed=True);line(r,'shaft',(22,24),(42,6));poly(r,'arrow',[(30,6),(42,6),(42,18)]);rel(r,'ring','shaft');rel(r,'shaft','arrow');note='Rebuilt the Mars symbol with a true circular ring and a shared integer attachment for the northeast arrow.'
 x['circles_reviewed']=True;x['manual_note']=x.get('manual_note','')+' '+note;q=check(f,x);print(id,q['status'],q['internal_spacing']['status'],q['errors']+q['warnings'],flush=True)
