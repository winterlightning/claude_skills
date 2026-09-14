from more_repairs import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
if __name__=='__main__':
 def bonnet(r):
  move(r,lambda x,y:(x,y+3),lambda p:p['element_id']=='band')
  for n in ['left-pendant','right-pendant']:p=by(r,n);p['start'][1]=34
  rel(r,'band','left-pendant');rel(r,'band','right-pendant')
  remove(r,['left-feather-4','right-feather-4'])
  # Removing an open terminal segment requires keeping the surviving coherent run.
  contour(r,'left-feather','left-feather-1','left-feather-2','left-feather-3');contour(r,'right-feather','right-feather-1','right-feather-2','right-feather-3')
 edit('feathered-war-bonnet',bonnet,'Lowered the forehead band with attached side pendants and simplified paired feather barbs.')
 def action(r):
  remove(r,['arms']);poly(r,'arms',[(6,11),(14,22),(21,22),(42,22)])
  rel(r,'arms','torso')
 edit('figure-with-outstretched-limbs',action,'Kept the action pose and round head; rebuilt the arm stations with an exact eight-unit head-to-body centerline gap.')
 def disk(r):
  move(r,lambda x,y:({13:15,35:33}.get(x,x),34 if y==35 else y),lambda p:p['element_id'].startswith(('shutter','label')))
  remove(r,['hub']);line(r,'hub',(24,25),(24,25))
 edit('floppy-disk',disk,'Inset shutter and label sides and used a solid hub mark to preserve the floppy disk structure.')
 def label(r):
  remove(r,['slot','writing'])
  move(r,lambda x,y:({13:15,35:33}.get(x,x),y),lambda p:p['element_id'].startswith(('shutter','label')))
 edit('floppy-disk-with-label',label,'Inset the shutter and label; removed the crowded slot and writing mark.')
 def lamb(r):
  remove(r,['face']);arc(r,'face-top',(18,22),(30,22),6,6);arc(r,'face-bottom',(30,22),(18,22),6,10);contour(r,'face','face-top','face-bottom',closed=True)
 for id in ['fluffy-lamb-front','woolly-lamb-front']:edit(id,lamb,'Removed the tiny inner ear notches and rebuilt a smooth oval face inside the fleece.')
 def teller(r):
  reset(r);circle(r,'head',12,11,5);poly(r,'seated-body',[(12,24),(6,34),(14,34),(18,42)]);line(r,'reaching-arm',(12,24),(20,32));rel(r,'reaching-arm','seated-body')
  arc(r,'ball-top',(26,20),(42,20),8);arc(r,'ball-br',(42,20),(34,28),8);arc(r,'ball-bl',(34,28),(26,20),8);contour(r,'ball','ball-top','ball-br','ball-bl',closed=True)
  line(r,'stand',(34,28),(34,34));poly(r,'table',[(25,34),(34,34),(42,34)]);line(r,'table-leg',(34,34),(34,42));rel(r,'ball','stand');rel(r,'stand','table');rel(r,'table-leg','table');rel(r,'table-leg','stand')
 edit('fortune-teller-reading',teller,'Rebuilt the seated human with a circular head, exact four-unit detached gap and a clear physical crystal-ball scene.')
 def keyboard(r):
  remove(r,['key-12','key-24','key-36','spacebar']);line(r,'keys',(16,33),(32,33));move(r,lambda x,y:(x,14 if y==16 else 20 if y==21 else y),lambda p:p['element_id'].startswith('cable'))
  by(r,'cable-loop')['radius_y']=4
 edit('gaming-keyboard-with-cable',keyboard,'Reduced the key rows to a single broad key strip and raised the cable loop to clear the case.')
 def geisha(r):
  reset(r,'VRECT_L')
  arc(r,'head-tl',(15,21),(24,12),9);arc(r,'head-tr',(24,12),(33,21),9);arc(r,'head-bottom',(33,21),(15,21),9);contour(r,'head','head-tl','head-tr','head-bottom',closed=True)
  circle(r,'bun',24,8,4);line(r,'pin-left',(8,4),(24,12));line(r,'pin-right',(40,4),(24,12))
  for a,b in [('head','bun'),('head','pin-left'),('head','pin-right'),('bun','pin-left'),('bun','pin-right'),('pin-left','pin-right')]:rel(r,a,b)
  arc(r,'shoulder-left',(8,44),(14,38),6);line(r,'shoulders',(14,38),(34,38));arc(r,'shoulder-right',(34,38),(40,44),6);contour(r,'garment','shoulder-left','shoulders','shoulder-right')
 edit('geisha-bust',geisha,'Rebuilt a circular nine-unit head, top bun and paired hairpins; simplified the garment to broad shoulders with exactly four visible units below the head.')
 def ionic(r):
  move(r,lambda x,y:(x,18 if y==17 else 34 if y==35 else y))
  for n in ['left-scroll-a','left-scroll-b','right-scroll-a','right-scroll-b']:p=by(r,n);p['radius_x']=p['radius_y']=6
 edit('ionic-column',ionic,'Rebuilt equal circular volutes and an eight-unit plinth depth using shared capital and shaft stations.')
 def knight(r):
  remove(r,['visor']);line(r,'visor',(24,20),(24,20));move(r,lambda x,y:(x,28 if y==30 else y),lambda p:p['element_id'].startswith('jaw'))
 edit('knight-armor-torso',knight,'Reduced the visor to a central opening and shortened the helmet chin to clear the armor shoulders.')
 def urn(r):
  move(r,lambda x,y:(x,12 if y==11 else y))
  # Equal semicircular handle extremities at x8 and40.
  for n in ['handle-left','handle-right']:p=by(r,n);p['start'][1]=20 if p['start'][1]==19 else 30;p['end'][1]=20 if p['end'][1]==19 else 30;p['radius_x']=6;p['radius_y']=5
  move(r,lambda x,y:(x,20 if y==19 else y),lambda p: not p['element_id'].startswith('handle'))
 edit('lidded-ceremonial-urn',urn,'Rebuilt equal semicircular handles and lowered the neck shoulder station to clear the lid.')
