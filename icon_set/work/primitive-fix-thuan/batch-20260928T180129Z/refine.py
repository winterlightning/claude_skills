from pathlib import Path
import json,shutil,textwrap
ROOT=Path(__file__).resolve().parent;xs=json.loads((ROOT/'authored.json').read_text())
bodies={
12:'''self.add_arc('orbit',(8,36),(40,36),radius_x=20,large_arc=True,sweep=True)
self.circle('earth',24,20,10)
self.add_polyline('north-land',(24,10),(22,15),(25,18),(32,18))
self.add_polyline('south-land',(15,22),(21,22),(24,29))
self.circle('node',24,40,4)''',
13:'''self.rect('chip',6,15,11,11,2)
for i in range(2):
 t=9+i*5
 for n,a,b in [('t',(t,12),(t,15)),('b',(t,26),(t,29)),('l',(3,18+i*5),(6,18+i*5)),('r',(17,18+i*5),(20,18+i*5))]:self.add_line(n+str(i),a,b)
self.add_bezier('hand',(42,42),((42,34),(42,26),(39,22)),((35,17),(31,6),(25,6)),((21,6),(21,12),(25,12)),((31,12),(35,22),(31,27)),((27,32),(23,28),(21,26)),((18,23),(15,26),(18,30)),((22,35),(28,36),(28,42)))'''
}
for d in xs:
 n=d['n']
 if n not in [5,12,13,19]:continue
 old=Path(d['run']);new=old.with_name(old.name[:-2]+'r3');new.mkdir()
 for f in old.iterdir():
  if f.suffix in ['.py','.md'] or f.name.endswith('metadata.json'):shutil.copyfile(f,new/f.name)
 p=new/Path(d['module']).name;s=p.read_text()
 if n in bodies:s=s.split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(bodies[n]+'\n','        ')
 if n==5:
  s=s.replace("self.rect('body',4,30,40,10,3)","self.rect('body',4,31,40,10,3)").replace("(7,30)","(7,31)").replace("(41,30)","(41,31)").replace("x,15,3","x,16,3").replace("self.add_bezier('shoulders'+str(x),(x-5,30),((x-5,26),(x+5,26),(x+5,30)))","self.add_arc('shoulders'+str(x),(x-5,31),(x+5,31),radius_x=5,radius_y=4)").replace("(x,40),(x,43)","(x,41),(x,44)")
 if n==19:
  s=s.replace("(6,29)","(2,29)").replace("(6,34)","(2,34)").replace("(6,22),(6,13),(6,10)","(2,22),(2,13),(2,10)").replace("(6,6),(8,6),(12,6)","(2,6),(6,6),(12,6)").replace("(41,6),(42,8),(42,12)","(45,6),(46,8),(46,12)").replace("(42,18),(42,25),(42,29)","(46,18),(46,25),(46,29)").replace("(42,33),(39,33),(36,33)","(46,33),(40,33),(36,33)").replace("[(13,14),(24,14),(35,14),(13,26),(24,26)]","[(13,15),(25,15),(37,15),(13,27)]")
 p.write_text(s);d['run']=str(new);d['module']=str(p)
 if n==19:d['change']='Restored a blister sheet with four separated circular cells and a thumb lifting the lower-right pill; reduced the reference cell count to keep the gesture clear.'
(ROOT/'authored.json').write_text(json.dumps(xs,indent=2))
