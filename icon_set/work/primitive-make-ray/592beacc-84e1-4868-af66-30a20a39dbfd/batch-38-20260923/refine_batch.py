"""Repair the tag contour and rebalance the remains composition in this attempt."""
from pathlib import Path
import json,shutil,importlib.util,textwrap,cairosvg
from PIL import Image,ImageOps
SOURCE_ICON_ID='592beacc-84e1-4868-af66-30a20a39dbfd'
SOURCE_PATH='icon_set/work/todo-references/rectangle list_592beacc-84e1-4868-af66-30a20a39dbfd.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch-inputs.json').read_text())
bodies={
12:'''self.add_line('tag-1',(6,26),(26,6))
self.add_line('tag-2',(26,6),(36,6))
self.add_arc('tag-corner',(36,6),(38,8),radius_x=2)
points=((38,8),(38,17),(17,38),(6,28),(6,26))
for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f'tag-return-{i}',a,b)
self.add_contour('tag-outline','tag-1','tag-2','tag-corner','tag-return-1','tag-return-2','tag-return-3','tag-return-4',closed=True)
self.circle('eyelet',30,14,3)
self.add_bezier('leaf',(42,29),((32,27),(27,33),(30,38)),((34,44),(42,42),(42,29)))
self.add_polyline('stem',(26,42),(32,35),(36,33))''',
18:'''# The bone occupies the left twenty units; leaf owns the right twelve.
self.add_bezier('bone',(12,16),((12,12),(10,10),(8,10)),((4,10),(4,15),(6,18)),((4,18),(4,20),(4,22)),((4,27),(10,28),(12,24)),((14,26),(16,27),(18,29)),((15,34),(16,38),(20,38)),((23,38),(24,36),(24,34)),((24,31),(23,30),(22,29)),((24,27),(23,23),(20,24)),((18,22),(14,18),(12,16)))
self.add_bezier('leaf',(44,12),((44,24),(43,31),(36,33)),((32,33),(32,18),(44,12)))
self.add_polyline('vein',(34,38),(36,33),(40,23));self.relate('connect','leaf','vein')'''
}
for index,body in bodies.items():
 row=rows[index];d=Path(row['result_dir']);rec=json.loads((d/'review-draft.json').read_text());p=d/rec['module'];source=p.read_text()
 old=d/'initial-attempt';old.mkdir(exist_ok=True)
 for f in list(d.iterdir()):
  if f.is_file() and (f.suffix in ('.py','.svg') or f.name.startswith(('light-','dark-','validation.','review-draft.'))):shutil.copy2(f,old/f.name)
 p.write_text(source.split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(body,'        ')+'\n')
 spec=importlib.util.spec_from_file_location('refined38_'+str(index),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon();rec['validation_status']=report.status;rec.pop('error',None)
 (d/'validation.txt').write_text(report.describe());svg=icon.to_svg();(d/(row['icon_id']+'.svg')).write_text(svg)
 for size in (48,240):
  p=d/f'light-{size}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(p),output_width=size,output_height=size,background_color='white');ImageOps.invert(Image.open(p).convert('RGB')).save(d/f'dark-{size}.png')
 (d/'review-draft.json').write_text(json.dumps(rec,indent=2));print(row['concept'],report.describe(),flush=True)
