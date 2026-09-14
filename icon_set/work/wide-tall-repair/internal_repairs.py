from more_repairs import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
def apply(id,fn,note):
 f=W/'candidates'/f'{id}.json';x=json.loads(f.read_text())
 if x.get('internal_repaired'):return
 fn(x['record']);x['internal_repaired']=True;x['manual_note']=x.get('manual_note','')+' '+note;q=check(f,x);print(id,q['status'],q['internal_spacing']['status'],q['errors']+q['warnings'],q['internal_spacing'].get('findings'),flush=True)
if __name__=='__main__':
 def bust(r):
  reset(r,'VRECT_L');arc(r,'crown',(13,13),(33,13),10,9);arc(r,'back',(33,13),(30,24),12,12);line(r,'back-neck',(30,24),(35,26));arc(r,'shoulder-right',(35,26),(40,35),5,9);line(r,'base',(40,35),(8,35));arc(r,'shoulder-left',(8,35),(13,26),5,9);poly(r,'profile',[(13,26),(20,23),(8,19),(13,13)]);contour(r,'bust','crown','back','back-neck','shoulder-right','base','shoulder-left','profile-0','profile-1','profile-2',closed=True);r['contours']=[c for c in r['contours'] if c['contour_id']!='profile'];line(r,'plinth',(13,44),(35,44))
 apply('classical-statue-bust',bust,'Rebuilt the profile and shoulder silhouette with a broad base and a clear plinth gap, omitting the tiny chin ledge.')
 apply('ribbon-bow-with-tails',lambda r:move(r,lambda x,y:(6 if x==10 else 42 if x==38 else x,y),lambda p:p['element_id'].startswith('tail')),'Broadened both ribbon tails symmetrically.')
 def helmet(r):
  move(r,lambda x,y:(x,44 if (x,y)==(37,40) else y))
  move(r,lambda x,y:(24 if (x,y)==(22,28) else 22 if (x,y)==(20,36) else x,y))
 apply('plumed-battle-helmet',helmet,'Opened the helmet cheek guards and thickened the returning face rim.')
 def bangle(r):
  move(r,lambda x,y:(13 if x==11 else 35 if x==37 else x,18 if y==15 else y),lambda p:p['element_id'].startswith(('inner','tip')))
  by(r,'inner-bottom').update(radius_x=11,radius_y=7)
  for n in ['tip-left','tip-right']:by(r,n).update(radius_x=4,radius_y=5)
 apply('open-cuff-bangle',bangle,'Widened the cuff band by shrinking the interior opening and using matched rounded ends.')
 def potty(r):
  move(r,lambda x,y:(x,24 if y==28 else 32 if y==36 else y))
  move(r,lambda x,y:(20 if x==18 else 28 if x==30 else x,y),lambda p:p['element_id'].startswith('base'));by(r,'base-3').update(radius_x=4,radius_y=4)
 apply('potty-with-lid',potty,'Raised the seat and widened the base legs around a smaller round foot opening.')
 def capital(r):
  remove(r,['volute-left','volute-right']);contour(r,'capital','capital-left','capital-top','capital-right')
 apply('column-with-open-book',capital,'Removed the tiny inward scroll hooks while retaining the paired rounded capital ends.')
 def charm(r):
  remove(r,['charm-outer-l']);p=by(r,'charm-l');p.update(start=[34,31],end=[26,31],radius_x=4,radius_y=4)
  contour(r,'charm','charm-l','charm-ls','charm-rs','charm-r',closed=True);by(r,'link').update(start=[26,27],end=[26,31]);by(r,'bead-5').update(start=[26,27],end=[26,27]);rel(r,'charm','link')
 apply('beaded-loop-with-heart-charm',charm,'Rebuilt matching circular heart lobes around the shared tip and link.')
 def two(r):
  reset(r)
  for side,x in [('left',14),('right',34)]:
   circle(r,side+'-head',x,10,4);line(r,side+'-shoulders',(x-2,22),(x+2,22));line(r,side+'-body',(x,22),(x,32));poly(r,side+'-legs',[(6 if side=='left' else 28,42),(x,32),(20 if side=='left' else 42,42)]);line(r,side+'-outer-arm',(x-2 if side=='left' else x+2,22),(6 if side=='left' else 42,28));line(r,side+'-inner-arm',(x+2 if side=='left' else x-2,22),(24,30))
   for a,b in [('shoulders','body'),('body','legs'),('shoulders','outer-arm'),('shoulders','inner-arm')]:rel(r,side+'-'+a,side+'-'+b)
  rel(r,'left-inner-arm','right-inner-arm')
 apply('two-stick-figures',two,'Rebuilt matching circular heads and detached shoulders with exactly four visible units of clearance; retained the joined hands.')
