from manual_repairs import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
def line(r,n,a,b):r['primitives'].append({'kind':'line','element_id':n,'start':list(a),'end':list(b)})
def arc(r,n,a,b,rx,ry=None,sweep=True):r['primitives'].append({'kind':'arc','element_id':n,'start':list(a),'end':list(b),'radius_x':rx,'radius_y':ry or rx,'sweep':sweep,'large_arc':False})
def contour(r,n,*members,closed=False):r['contours'].append({'contour_id':n,'members':list(members),'closed':closed})
def poly(r,n,pts,closed=False):
 pairs=list(zip(pts,pts[1:]));pairs+= [(pts[-1],pts[0])] if closed else []
 names=[]
 for i,(a,b) in enumerate(pairs):names.append(f'{n}-{i}');line(r,names[-1],a,b)
 contour(r,n,*names,closed=closed)
def circle(r,n,x,y,radius):
 arc(r,n+'-top',(x-radius,y),(x+radius,y),radius);arc(r,n+'-bottom',(x+radius,y),(x-radius,y),radius);contour(r,n,n+'-top',n+'-bottom',closed=True)
def rel(r,a,b):r['relationships'].append({'kind':'connect','members':[a,b]})
def reset(r,key='SQUARE'):r.update(primitives=[],contours=[],relationships=[],keyshape=key)
if __name__=='__main__':
 edit('beaded-loop-with-heart-charm',lambda r:move(r,lambda x,y:(x-1,y) if (x,y)==(18,31) else (x,y-1) if (x,y)==(31,19) else (x,y)),'Moved the two beads beside the charm outward to restore clearance without changing the loop topology.')
 def beads(r):
  reset(r)
  for i,(x,y) in enumerate([(6,6),(14,17),(42,6),(34,17)]):line(r,f'bead-{i}',(x,y),(x,y))
  poly(r,'chain-left',[(6,6),(14,17),(24,25)]);poly(r,'chain-right',[(42,6),(34,17),(24,25)]);line(r,'link',(24,25),(24,27));poly(r,'stone',[(24,27),(33,32),(33,37),(24,42),(15,37),(15,32)],True)
  for i in range(4):rel(r,f'bead-{i}','chain-left' if i<2 else 'chain-right')
  rel(r,'chain-left','chain-right');rel(r,'chain-left','link');rel(r,'chain-right','link');rel(r,'link','stone')
 edit('beaded-necklace-with-hexagon-stone',beads,'Rebuilt the repeated beads as solid points with shared wire nodes; retained the hexagonal pendant.')
 def paw(r):
  reset(r)
  for i,p in enumerate([(6,21),(16,6),(32,6),(42,21)]):line(r,f'toe-{i}',p,p)
  arc(r,'pad-top',(14,34),(34,34),10,10);arc(r,'pad-base',(34,34),(14,34),10,8);contour(r,'pad','pad-top','pad-base',closed=True)
 edit('cat-paw-print',paw,'Reduced four hollow toe rings to round solid toe pads and rebuilt the broad lower paw pad.')
 edit('cave-painting-symbols',lambda r:(move(r,lambda x,y:(x,y+2),lambda p:p['element_id']=='branch-lower'),move(r,lambda x,y:(x,17 if y==21 else y),lambda p:p['element_id'].startswith('arch'))),'Separated the branch strokes and shortened the neighboring arch above the diamond.')
 def eyes(r):
  for n,x in [('eye-left',20),('eye-right',28)]:p=by(r,n);p['start']=p['end']=[x,25]
 edit('chinese-dragon-head',eyes,'Replaced angled eye strokes with paired round dots, retaining horns, muzzle and whiskers.')
 edit('classical-head-with-book',lambda r:move(r,lambda x,y:(13 if x==16 else x,y),lambda p:not p['element_id'].startswith(('book','spine'))),'Moved the face and neck station left to clear the physical book.')
 edit('cobra-head-friendly',lambda r:remove(r,['face-left','chin','face-right']), 'Removed the crowded inner face outline; retained the flared hood, neck and paired eyes.')
 edit('column-with-open-book',lambda r:(remove(r,['shaft-right']),move(r,lambda x,y:(x,25 if y==22 else y),lambda p:p['element_id']=='shaft')),'Reduced the shaft to one stroke and opened its gap below the capital; retained the book scene.')
 def memory(r):
  reset(r,'HRECT_L');poly(r,'board',[(4,8),(44,8),(44,32),(36,32),(24,32),(12,32),(4,32)],True)
  for i,x in enumerate([12,28]):poly(r,f'chip-{i}',[(x,16),(x+8,16),(x+8,24),(x,24)],True)
  for i,x in enumerate([12,24,36]):line(r,f'contact-{i}',(x,32),(x,40));rel(r,f'contact-{i}','board')
 edit('computer-memory-module',memory,'Reauthored horizontally with two equal chips and three shared contact pins so both chip openings remain readable.')
 def elephant(r):
  move(r,lambda x,y:({15:11,33:37}.get(x,x),20 if y==16 else y),lambda p:True)
  by(r,'forehead').update(radius_x=13,radius_y=12)
  for n,x in [('eye-left',20),('eye-right',28)]:by(r,n).update(start=[x,20],end=[x,20])
 edit('elephant-head-friendly',elephant,'Broadened the forehead and shared ear attachments to make room for paired eyes, preserving the long trunk.')
