from more_repairs import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
def patch(id,fn,note=''):
 f=W/'candidates'/f'{id}.json';x=json.loads(f.read_text())
 if x.get('final_shapes'):return
 fn(x['record']);x['final_shapes']=True
 if note:x['manual_note']=x.get('manual_note','')+' '+note
 q=check(f,x);print(id,q['status'],q['errors']+q['warnings'],flush=True)
if __name__=='__main__':
 def buds(r):
  for n in ['top','left','right']:remove(r,[n])
  for n,p in [('top',(22,4)),('left',(8,11)),('right',(36,11))]:line(r,n,p,p)
  by(r,'stem')['end']=[22,4];by(r,'twig-1')['start']=[8,11];by(r,'twig-2')['end']=[36,11]
  rel(r,'top','stem');rel(r,'left','twig');rel(r,'right','twig')
 patch('bud-branch-in-pitcher',buds,'Used three solid buds with shared branch attachment nodes.')
 def dragon(r):
  move(r,lambda x,y:({14:11,34:37}.get(x,x),y),lambda p:p['element_id'].startswith('cheek'))
 patch('chinese-dragon-head',dragon,'Broadened the paired cheek stations to clear the eyes.')
 patch('classical-head-with-book',lambda r:move(r,lambda x,y:(x,18 if y==21 else y),lambda p:p['element_id']=='back-head'),'Shortened the back-of-head ending above the open book.')
 patch('cobra-head-friendly',lambda r:move(r,lambda x,y:(19 if x==21 else 29 if x==27 else x,y),lambda p:'eye' in p['element_id']),'Separated the two eyes symmetrically.')
 def distress(r):
  reset(r);arc(r,'crown',(10,20),(38,20),14);arc(r,'ear-right',(38,20),(38,28),4);arc(r,'jaw',(38,28),(10,28),14);arc(r,'ear-left',(10,28),(10,20),4);contour(r,'face','crown','ear-right','jaw','ear-left',closed=True)
  line(r,'eye-left',(19,21),(19,21));line(r,'eye-right',(29,21),(29,21));arc(r,'frown',(20,33),(28,33),4,3)
 patch('distressed-baby-face',distress,'Rebuilt the round baby face and ears; retained the frown with simple eyes, removing crowded crosses and stress rays.')
 patch('feathered-war-bonnet',lambda r:move(r,lambda x,y:(12 if x==13 else 36 if x==35 else x,y),lambda p:p['element_id'] in ['left-feather-3','right-feather-3']),'Shortened the inward feather barbs equally.')
 def action(r):
  remove(r,['arms']);poly(r,'arm-left',[(6,11),(14,22),(21,22)]);line(r,'arm-right',(21,22),(42,22));rel(r,'arm-left','arm-right');rel(r,'arm-left','torso');rel(r,'arm-right','torso')
 patch('figure-with-outstretched-limbs',action,'Separated the true horizontal arm stroke so its exact head clearance is certified.')
 def lamb(r):
  for n in ['face-top','face-bottom']:p=by(r,n);p['start'][1]=p['end'][1]=24;p['radius_y']=6
 patch('fluffy-lamb-front',lamb,'Centered a circular six-unit face inside the fleece.');patch('woolly-lamb-front',lamb,'Centered a circular six-unit face inside the fleece.')
 patch('fortune-teller-reading',lambda r:by(r,'table-0').update(start=[29,34]),'Shortened the tabletop near the reaching hand.')
 patch('knight-armor-torso',lambda r:by(r,'visor').update(start=[24,19],end=[24,19]),'Raised the visor opening one unit.')
 patch('lidded-ceremonial-urn',lambda r:move(r,lambda x,y:(x,36 if y==37 else y)),'Raised the vessel baseline to open the pedestal gap.')
 def otter(r):
  reset(r);arc(r,'ear-left',(8,12),(20,12),6);line(r,'crown',(20,12),(28,12));arc(r,'ear-right',(28,12),(40,12),6);line(r,'side-right',(40,12),(40,22));arc(r,'cheek-right',(40,22),(35,28),5,6);arc(r,'cheek-left',(13,28),(8,22),5,6);line(r,'side-left',(8,22),(8,12));contour(r,'head','cheek-left','side-left','ear-left','crown','ear-right','side-right','cheek-right')
  circle(r,'paw-left',13,35,7);circle(r,'paw-right',35,35,7);rel(r,'head','paw-left');rel(r,'head','paw-right');line(r,'eye-left',(17,20),(17,20));line(r,'eye-right',(31,20),(31,20));line(r,'nose',(24,24),(24,24))
 patch('otter-with-paws',otter,'Rebuilt equal ears and paws; removed tiny whiskers, toe cuts and mouth to keep the paired eyes and nose clear.')
 def rings(r):
  p=by(r,'rear-bottom');p['start']=[13,32];p['radius_x']=10;p['radius_y']=10
 patch('pair-of-wedding-rings',rings,'Shortened the rear ring opening beside the foreground ring.')
 def palm(r):
  reset(r)
  line(r,'index-side',(10,26),(10,14));arc(r,'index-tip',(10,14),(18,14),4);line(r,'middle-rise',(18,14),(18,10));arc(r,'middle-tip',(18,10),(26,10),4);line(r,'middle-fall',(26,10),(26,12));arc(r,'ring-tip',(26,12),(34,12),4);line(r,'ring-fall',(34,12),(34,16));arc(r,'little-tip',(34,16),(42,16),4);line(r,'palm-side',(42,16),(42,30));arc(r,'heel-right',(42,30),(30,42),12);line(r,'wrist',(30,42),(22,42));arc(r,'heel-left',(22,42),(12,34),10,8);line(r,'thumb-side',(12,34),(6,26));arc(r,'thumb-tip',(6,26),(10,26),2)
  contour(r,'hand',*[p['element_id'] for p in r['primitives']],closed=True)
  for n,x,y in [('index',18,14),('middle',26,12),('ring',34,16)]:line(r,n+'-crease',(x,y),(x,23));rel(r,'hand',n+'-crease')
  line(r,'palm-line',(20,32),(32,32))
 patch('palmistry-hand',palm,'Rebuilt four equal-width finger openings from shared stations, with one readable palm crease.')
 def pharaoh(r):
  reset(r);arc(r,'cloth-left',(6,34),(16,14),10,20);line(r,'crown',(16,14),(24,14));line(r,'crown-right',(24,14),(32,14));arc(r,'cloth-right',(32,14),(42,34),10,20);poly(r,'drape-left',[(6,34),(14,34),(14,42)]);poly(r,'drape-right',[(42,34),(34,34),(34,42)]);line(r,'face-left',(16,14),(16,26));arc(r,'jaw-left',(16,26),(24,34),8,8,False);arc(r,'jaw-right',(24,34),(32,26),8,8,False);line(r,'face-right',(32,26),(32,14));contour(r,'face','face-left','jaw-left','jaw-right','face-right');line(r,'crest',(24,6),(24,14));line(r,'beard',(24,34),(24,42))
  for a,b in [('cloth-left','drape-left'),('cloth-right','drape-right'),('cloth-left','crown'),('cloth-right','crown-right'),('face','crown'),('face','crown-right'),('face','cloth-left'),('face','cloth-right'),('crown','crown-right'),('crest','crown'),('crest','crown-right'),('beard','face')]:rel(r,a,b)
 patch('pharaoh-nemes-mask',pharaoh,'Rebuilt the nemes cloth, face, crest and beard with open drapes; removed the undersized crest box and eye dots.')
 patch('record-turntable',lambda r:move(r,lambda x,y:(x,y+2),lambda p:p['element_id'].startswith(('platter','spindle','tonearm'))),'Lowered the platter and tonearm together to clear the deck top.')
 def rhombus(r):
  # Restore original middle stations and move all its shared nodes together twice as far.
  old={tuple(p[k]):(p[k][0]+1,p[k][1]-1) for p in r['primitives'] if p['element_id'].startswith('middle') for k in ['start','end']}
  move(r,lambda x,y:old.get((x,y),(x,y)))
  by(r,'join-lower')['end']=[23,25];by(r,'join-upper')['start']=[29,19]
 patch('rhombus-chain-links',rhombus,'Moved the middle link and shared join nodes together to retain separation.')
 patch('written-scroll',lambda r:by(r,'writing-top').update(start=[25,18],end=[28,18]),'Shortened the inscription to clear both scroll walls.')
