"""Targeted repairs within batch 41, preserving initial evidence."""
from pathlib import Path
import json,shutil,importlib.util,textwrap,cairosvg
from PIL import Image,ImageOps
SOURCE_ICON_ID='0918c48a-7ee6-4895-9035-4645fdc17ae1'
SOURCE_PATH='icon_set/work/todo-references/scoreboard_0918c48a-7ee6-4895-9035-4645fdc17ae1.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch-inputs.json').read_text())
bodies={
9:'''self.terminal()
self.add_bezier('dollar',(22,17),((21,16),(19,16),(18,16)),((12,16),(12,19),(18,20)),((24,21),(24,24),(18,24)),((16,24),(15,24),(14,23)))
self.add_polyline('dollar-stem',(18,14),(18,16),(18,20),(18,24),(18,26));self.relate('connect','dollar','dollar-stem')''',
10:'''self.terminal()
self.add_arc('euro-top',(22,14),(16,20),radius_x=6,sweep=False)
self.add_arc('euro-bottom',(16,20),(22,26),radius_x=6,sweep=False)
self.add_contour('euro','euro-top','euro-bottom')
self.add_polyline('crossbar',(14,20),(16,20),(22,20));self.relate('connect','euro','crossbar')''',
11:'''self.terminal()
self.add_arc('pound-hook',(23,18),(15,18),radius_x=4,sweep=False)
self.add_polyline('pound-stem',(15,18),(15,21),(15,23));self.relate('connect','pound-hook','pound-stem')
self.add_arc('pound-turn',(15,23),(14,24),radius_x=1);self.relate('connect','pound-stem','pound-turn')
self.add_polyline('pound-base',(14,24),(14,26),(24,26));self.relate('connect','pound-turn','pound-base')
self.add_polyline('crossbar',(14,21),(15,21),(20,21));self.relate('connect','pound-stem','crossbar')''',
12:'''self.terminal()
self.add_polyline('yuan-top',(14,14),(19,21),(24,14))
self.add_polyline('yuan-stem',(19,21),(19,22),(19,26));self.relate('connect','yuan-top','yuan-stem')
self.add_polyline('yuan-bar',(14,22),(19,22),(24,22));self.relate('connect','yuan-stem','yuan-bar')'''
}
for index in (2,6,7,9,10,11,12):
 row=rows[index];d=Path(row['result_dir']);rec=json.loads((d/'review-draft.json').read_text());p=d/rec['module'];source=p.read_text();old=d/'initial-attempt';old.mkdir(exist_ok=True)
 for f in list(d.iterdir()):
  if f.is_file() and (f.suffix in ('.py','.svg') or f.name.startswith(('light-','dark-','validation.','review-draft.'))):shutil.copy2(f,old/f.name)
 if index==2:
  for a,b in [('(18,12)','(18,13)'),('(30,12)','(30,13)'),('(18,36)','(18,35)'),('(30,36)','(30,35)'),('(10,8)','(9,7)'),('(38,8)','(39,7)'),('(10,40)','(9,41)'),('(38,40)','(39,41)')]:source=source.replace(a,b)
 elif index==6:source=source.replace("'legs',(8,42)","'legs',(6,42)").replace('(14,22),(21,27)','(14,22),(20,28)')
 elif index==7:source=source.replace("self.add_polyline('body-side',(6,42),(6,34))","self.add_line('body-side-1',(6,42),(6,34))")
 elif index in bodies:
  source=source.split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(bodies[index],'        ')+'\n'
  source=source.replace("self.box('screen',6,6,36,28,3)","self.add_polyline('screen',(6,6),(42,6),(42,34),(24,34),(6,34),closed=True)")
  source=source.replace("(31,y),(35,y)","(32,y),(34,y)")
  rec['omissions']='No semantic elements omitted. Currency glyph reduced in height; menu rules shortened and screen corner arcs replaced by round joins.'
 p.write_text(source)
 spec=importlib.util.spec_from_file_location('refined41_'+str(index),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon();rec['validation_status']=report.status;rec.pop('error',None)
 (d/'validation.txt').write_text(report.describe());svg=icon.to_svg();(d/(row['icon_id']+'.svg')).write_text(svg)
 for size in (48,240):
  out=d/f'light-{size}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out),output_width=size,output_height=size,background_color='white');ImageOps.invert(Image.open(out).convert('RGB')).save(d/f'dark-{size}.png')
 (d/'review-draft.json').write_text(json.dumps(rec,indent=2));print(row['concept'],report.describe(),flush=True)
