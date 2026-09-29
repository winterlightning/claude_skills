from pathlib import Path
import json,shutil,textwrap
ROOT=Path(__file__).resolve().parent;xs=json.loads((ROOT/'authored.json').read_text())
bodies={
1:'''self.add_bezier('ribbon',(36,8),((33,5),(30,5),(27,8)),((27,3),(20,2),(16,6)),((12,10),(8,14),(6,18)),((0,27),(11,36),(19,29)),((24,24),(29,19),(32,17)),((38,12),(47,20),(42,28)),((38,33),(33,38),(30,41)),((26,45),(22,44),(20,42)))
self.add_bezier('return',(20,42),((25,37),(30,32),(34,28)),((38,24),(34,21),(31,25)),((27,29),(23,33),(19,37)),((15,41),(12,40),(10,38)))
self.relate('connect','ribbon','return')''',
8:'''# Two crossing S bodies connect four pointed heads; paired bodies rotate 90 degrees.
for i in range(2):
 def p(x,y):
  x,y=x-24,y-24
  for _ in range(i):x,y=-y,x
  return (24+x,24+y)
 self.add_bezier('body'+str(i),p(11,13),(p(0,23),p(13,35),p(22,29)),(p(37,18),p(45,27),p(37,35)))
for i in range(4):
 def p(x,y):
  x,y=x-24,y-24
  for _ in range(i):x,y=-y,x
  return (24+x,24+y)
 self.add_bezier('head'+str(i),p(11,13),(p(8,9),p(15,5),p(18,7)),(p(20,7),p(21,5),p(22,4)),(p(22,11),p(17,17),p(11,13)))
 self.relate('connect','head'+str(i),'body'+str(i%2))'''
}
for d in xs:
 n=d['n']
 if n not in [1,4,8,14,15,17,19]:continue
 old=Path(d['run']);new=old.with_name(old.name[:-2]+'r2');new.mkdir()
 for f in old.iterdir():
  if f.suffix in ['.py','.md'] or f.name.endswith('metadata.json'):shutil.copyfile(f,new/f.name)
 p=new/Path(d['module']).name;s=p.read_text()
 if n in bodies:s=s.split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(bodies[n]+'\n','        ')
 if n==4:
  s=s.replace(";self.add_contour('bubble','bottom-tail','bl','left','tl','top','tr','right',closed=True)","\n        for a,b in zip(['bottom-tail','bl','left','tl','top','tr','right'],['bl','left','tl','top','tr','right','bottom-tail']):self.relate('connect',a,b)")
 if n in [14,17]:s=s.replace("    category = 'objects'","    category = 'avatars'\n    human_construction = 'bust'")
 if n==15:s=s.replace("(39,47)","(39,46)").replace("(44,42),(39,46)","(44,42),(40,46)")
 if n==19:
  s=s.replace("self.add_line('torso',(24,30),(26,36))","self.add_line('torso',(24,30),(24,33))\n        self.add_line('lower-torso',(24,33),(26,36));self.relate('connect','torso','lower-torso')").replace("'rear-leg','torso'","'rear-leg','lower-torso'").replace("'front-leg','torso'","'front-leg','lower-torso'")
 p.write_text(s);d['run']=str(new);d['module']=str(p)
(ROOT/'authored.json').write_text(json.dumps(xs,indent=2))
