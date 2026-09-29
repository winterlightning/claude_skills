from pathlib import Path
import json,shutil,textwrap
ROOT=Path(__file__).resolve().parent;xs=json.loads((ROOT/'authored.json').read_text())
bodies={1:'''self.add_bezier('ribbon',(36,8),((33,5),(30,5),(27,8)),((27,3),(20,2),(16,6)),((12,10),(8,14),(6,18)),((0,27),(11,36),(19,29)),((24,24),(29,19),(32,17)),((40,11),(49,21),(44,30)),((40,35),(35,41),(32,43)),((28,46),(25,44),(24,42)))
self.add_bezier('return',(24,42),((29,37),(34,32),(38,28)),((42,24),(37,20),(34,24)),((29,29),(24,34),(20,38)),((16,42),(12,41),(10,39)))
self.relate('connect','ribbon','return')''',
8:'''# Two offset serpentine bodies preserve the intertwined-snakes concept at native size.
self.add_bezier('snake-left',(12,15),((0,21),(10,31),(24,31)),((40,31),(41,44),(26,44)))
self.add_bezier('head-left',(12,15),((7,11),(11,6),(17,7)),((20,7),(20,5),(22,4)),((23,12),(19,18),(12,15)))
self.add_bezier('snake-right',(36,18),((44,26),(31,28),(25,22)),((13,9),(4,20),(7,29)),((9,34),(13,36),(17,36)))
self.add_bezier('head-right',(36,18),((31,15),(33,8),(36,7)),((40,6),(42,11),(41,15)),((41,17),(43,18),(44,20)),((40,21),(38,20),(36,18)))
self.relate('connect','snake-left','head-left');self.relate('connect','snake-right','head-right')'''}
for d in xs:
 if d['n'] not in bodies:continue
 old=Path(d['run']);new=old.with_name(old.name[:-2]+'r3');new.mkdir()
 for f in old.iterdir():
  if f.suffix in ['.py','.md'] or f.name.endswith('metadata.json'):shutil.copyfile(f,new/f.name)
 p=new/Path(d['module']).name;s=p.read_text().split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(bodies[d['n']]+'\n','        ');p.write_text(s)
 d['run']=str(new);d['module']=str(p)
 if d['n']==8:d['change']='Restored pointed snake heads and offset serpentine coils; reduced the four-head reference motif to two snakes so the animals remain identifiable at 48px.'
(ROOT/'authored.json').write_text(json.dumps(xs,indent=2))
