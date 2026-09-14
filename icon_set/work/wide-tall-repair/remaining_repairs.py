from more_repairs import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
if __name__=='__main__':
 def memory(r):
  reset(r,'HRECT_L');poly(r,'board',[(4,8),(44,8),(44,40),(28,40),(28,36),(20,36),(20,40),(4,40)],True)
  for i,x in enumerate([12,28]):poly(r,f'chip-{i}',[(x,16),(x+8,16),(x+8,24),(x,24)],True)
 edit('memory-module-with-notch',memory,'Reauthored horizontally with equal readable chips and a bottom registration notch.')
 edit('minotaur-bust',lambda r:remove(r,['muzzle']),'Removed the crowded small muzzle mark, keeping the bull horns, ears, chin and broad human shoulders.')
 def monkey(r,mask):
  reset(r,'HRECT_L')
  arc(r,'skull-left',(10,20),(24,8),14,12);arc(r,'skull-right',(24,8),(38,20),14,12);line(r,'wall-right',(38,20),(38,32));line(r,'wall-left',(10,32),(10,20));arc(r,'chin-right',(38,32),(24,40),14,8);arc(r,'chin-left',(24,40),(10,32),14,8);contour(r,'head','skull-left','skull-right','wall-right','chin-right','chin-left','wall-left',closed=True)
  arc(r,'ear-left',(10,20),(10,32),6,6,False);arc(r,'ear-right',(38,20),(38,32),6,6);rel(r,'ear-left','head');rel(r,'ear-right','head')
  if mask:circle(r,'face-mask',24,24,5)
  else:
   arc(r,'muzzle',(10,32),(38,32),14,4);rel(r,'muzzle','head');line(r,'eye-left',(19,19),(19,19));line(r,'eye-right',(29,19),(29,19))
 edit('monkey-face',lambda r:monkey(r,True),'Rebuilt the paired ears and skull with exact quarter ellipses and reduced the inner face panel.')
 edit('monkey-head',lambda r:monkey(r,False),'Rebuilt the paired ears, broad muzzle and separated eyes on a horizontal envelope.')
 def monocle(r):
  reset(r);arc(r,'lens-tr',(18,6),(30,18),12);arc(r,'lens-br',(30,18),(18,30),12);arc(r,'lens-left',(18,30),(18,6),12);contour(r,'lens','lens-tr','lens-br','lens-left',closed=True)
  line(r,'cord-down',(30,18),(30,35));arc(r,'cord-bottom',(30,35),(42,35),6,7,False);line(r,'cord-up',(42,35),(42,22));contour(r,'cord','cord-down','cord-bottom','cord-up');rel(r,'cord','lens')
 edit('monocle-with-cord',monocle,'Rebuilt a true circular lens and a tangent U-shaped cord reaching the square bottom edge.')
 def necklace(r):
  reset(r)
  arc(r,'left-curl',(13,6),(6,13),7,7,False);arc(r,'left-cord',(6,13),(11,27),5,14,False);contour(r,'left','left-curl','left-cord');arc(r,'right-curl',(35,6),(42,13),7);arc(r,'right-cord',(42,13),(37,27),5,14);contour(r,'right','right-curl','right-cord')
  line(r,'left-bead',(11,27),(11,27));line(r,'right-bead',(37,27),(37,27));line(r,'thread-left',(11,27),(24,28));line(r,'thread-right',(37,27),(24,28));circle(r,'main-bead',24,35,7)
  for a,b in [('left','left-bead'),('left','thread-left'),('left-bead','thread-left'),('right','right-bead'),('right','thread-right'),('right-bead','thread-right'),('thread-left','thread-right'),('thread-left','main-bead'),('thread-right','main-bead')]:rel(r,a,b)
 edit('necklace-with-three-beads',necklace,'Used two solid side beads and one large circular bead on shared necklace links.')
 edit('open-folding-fan',lambda r:(remove(r,['pivot']),line(r,'pivot',(24,35),(24,40)),rel(r,'pivot','leaf'),rel(r,'pivot','rib')),'Replaced the tiny hollow pivot with a round-ended pin.')
 def orchid(r):
  reset(r)
  for i,(x,y) in enumerate([(10,18),(24,10),(38,18)]):
   circle(r,f'flower-{i}',x,y,4);line(r,f'stem-{i}',(x,y+4),(x,34));rel(r,f'flower-{i}',f'stem-{i}');rel(r,f'stem-{i}','planter')
  poly(r,'planter',[(6,34),(10,34),(24,34),(38,34),(42,34),(38,42),(10,42)],True)
 edit('orchid-in-shallow-planter',orchid,'Reduced crowded petals to three equal round blossoms and gave the shallow planter a full eight-unit depth.')
 def hierarchy(r):
  move(r,lambda x,y:({16:14,32:34}.get(x,x),26 if y==25 else 21 if y==20 else y),lambda p:p['element_id'].startswith(('cube','parent')))
  for side,x in [('left',6),('centre',24),('right',42)]:
   remove(r,[f'child-{side}-circle']);p=by(r,f'child-{side}-stem');p['start'][0]=p['end'][0]=x;p['end'][1]=42
  move(r,lambda x,y:(6 if x==8 else 42 if x==40 else x,y),lambda p:p['element_id'].startswith('bus'))
 edit('organizational-hierarchy-cube',hierarchy,'Broadened the cube faces and replaced tiny child rings with three round-ended branches.')
 def drops(r):
  reset(r)
  for side,x in [('left',13),('right',35)]:
   circle(r,side+'-stud',x,10,4);line(r,side+'-post',(x,14),(x,22));poly(r,side+'-sides',[(x-7,35),(x,22),(x+7,35)]);arc(r,side+'-base',(x+7,35),(x-7,35),7);contour(r,side+'-drop',side+'-sides-0',side+'-sides-1',side+'-base',closed=True);r['contours']=[c for c in r['contours'] if c['contour_id']!=side+'-sides'];rel(r,side+'-stud',side+'-post');rel(r,side+'-drop',side+'-post')
 edit('pair-of-teardrop-earrings-v2',drops,'Rebuilt mirrored teardrops with semicircular bases and equal studs; kept the pair eight units apart.')
 def rings(r):
  reset(r);circle(r,'front',32,32,10);arc(r,'rear-top',(6,24),(16,14),10);arc(r,'rear-bottom',(16,34),(6,24),10);contour(r,'rear','rear-bottom','rear-top');poly(r,'gem',[(12,6),(20,6),(24,10),(20,14),(16,14),(12,14),(8,10)],True);rel(r,'rear','gem')
 edit('pair-of-wedding-rings',rings,'Rebuilt a circular foreground ring and open rear engagement ring with a readable diamond.')
 def mitten(r):
  p=by(r,'thumb-cap');p['start']=[34,20];p['end']=[40,26];p['radius_x']=p['radius_y']=6;move(r,lambda x,y:(34 if x==33 else x,26 if (x,y)==(40,24) else y),lambda p:p['element_id']!='thumb-cap')
 edit('patterned-winter-mitten',mitten,'Rebuilt the thumb cap as an exact quarter circle and kept its shared attachment nodes.')
 def deck(r):
  remove(r,['control']);move(r,lambda x,y:(6 if x==8 else 42 if x==40 else x,y),lambda p:p['element_id'].startswith('deck'))
  r['keyshape']='SQUARE';move(r,lambda x,y:(x,6 if y==4 else 42 if y==44 else y),lambda p:p['element_id'].startswith('deck'))
  for p in r['primitives']:
   if p['element_id'].startswith('platter'):p['radius_x']=p['radius_y']=9; p['start']=[24+round((p['start'][0]-24)*.9),22+round((p['start'][1]-21)*9/11)];p['end']=[24+round((p['end'][0]-24)*.9),22+round((p['end'][1]-21)*9/11)]
  by(r,'spindle').update(start=[24,22],end=[24,22]);by(r,'tonearm').update(start=[24,22],end=[15,31])
 edit('record-turntable',deck,'Broadened the deck and made the platter circular; removed the crowded small control mark.')
 edit('rhombus-chain-links',lambda r:move(r,lambda x,y:(x+1,y-1),lambda p:p['element_id'].startswith('middle')),'Shifted the middle link along the chain axis to rebalance its spacing.')
 def sheep(r):
  move(r,lambda x,y:(x,23 if y==22 else y),lambda p:p['element_id'] in ['muzzle','jaw','wool-neck','wool-left','front-hoof'])
  by(r,'muzzle').update(radius_x=5,radius_y=6)
  move(r,lambda x,y:(x,40 if y in [37,38] else y),lambda p:p['element_id'].startswith(('post','rail')))
 edit('sheep-jumping-fence-v2',sheep,'Rebuilt the muzzle with an exact half ellipse and lowered the fence posts away from the jumping sheep.')
 def penguin(r):
  move(r,lambda x,y:(11 if x==15 else 37 if x==33 else x,y),lambda p:p['element_id'] in ['crown','neck-left','neck-right','body-left','body-right'])
  by(r,'crown').update(radius_x=13,radius_y=10)
  by(r,'eye-left').update(start=[20,14],end=[20,14]);by(r,'eye-right').update(start=[28,14],end=[28,14]);by(r,'beak').update(start=[24,23],end=[24,23])
 edit('sitting-penguin',penguin,'Broadened the penguin head and body for two separated eyes and a small round beak, keeping the paired feet.')
 def shades(r):
  remove(r,['sun']);line(r,'sun',(31,15),(31,15));move(r,lambda x,y:(20 if x==21 else 28 if x==27 else x,y),lambda p:p['element_id'].startswith(('lens','bridge')))
 edit('sunglasses-with-sun',shades,'Widened the bridge gap and reduced the small sun center to a solid dot.')
 def cauldron(r):
  move(r,lambda x,y:(x,12 if y==14 else y),lambda p:'steam' in p['element_id']);move(r,lambda x,y:(x+2,y),lambda p:p['element_id'].startswith('right-steam'))
 edit('witches-cauldron',cauldron,'Shortened and separated the two steam curls while preserving the cauldron silhouette.')
