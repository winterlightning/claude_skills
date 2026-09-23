"""Targeted final visual repairs; no changes to profile or validation rules."""
from pathlib import Path
import json, shutil, importlib.util, textwrap
import cairosvg
from PIL import Image,ImageOps
SOURCE_ICON_ID='82791e1b-7e30-4905-85e9-1bf64f1e2489'
SOURCE_PATH='icon_set/work/todo-references/online learning online course 2_82791e1b-7e30-4905-85e9-1bf64f1e2489.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch-inputs.json').read_text())
for index in (0,1,4,9,12,13,14):
 row=rows[index];d=Path(row['result_dir']);rec=json.loads((d/'review-draft.json').read_text());p=d/rec['module'];source=p.read_text()
 old=d/'before-final-refinement';old.mkdir(exist_ok=True)
 for f in list(d.iterdir()):
  if f.is_file() and (f.suffix=='.py' or f.name=='validation.txt' or f.name.startswith(('light-','dark-'))):shutil.copy2(f,old/f.name)
 if index==0:
  source=source.replace('(24,10)','(24,8)').replace('(38,14),(30,14),(24,18),(18,14),(10,14)','(38,16),(30,16),(24,18),(18,16),(10,16)')
 elif index==1:
  body='''
self.add_arc('outer',(12,40),(36,40),radius_x=20,large_arc=True)
self.add_arc('keyhole-head',(21,24),(27,24),radius_x=5,large_arc=True)
self.add_line('keyhole-right',(27,24),(29,36))
self.add_arc('keyhole-base',(29,36),(19,36),radius_x=5,radius_y=2)
self.add_line('keyhole-left',(19,36),(21,24))
self.add_contour('keyhole','keyhole-head','keyhole-right','keyhole-base','keyhole-left',closed=True)
'''
  source=source.split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n'
 elif index==4:
  body='''
self.add_polyline('panel',(22,25),(22,6),(42,6),(42,38),(24,38))
self.add_bezier('pig-lower',(6,42),((10,36),(12,33),(20,31)),((21,30),(22,27),(22,25)))
self.add_bezier('pig-upper',(22,25),((16,24),(13,21),(11,17)),((9,14),(7,14),(6,14)),((6,18),(7,20),(9,21)))
self.add_contour('pig','pig-lower','pig-upper')
self.relate('connect','panel','pig')
self.add_bezier('apple',(32,21),((28,18),(25,20),(26,25)),((27,31),(30,32),(32,30)),((34,32),(37,31),(38,25)),((39,20),(36,18),(32,21)))
self.add_line('apple-stem',(32,21),(34,16));self.relate('connect','apple','apple-stem')
'''
  source=source.split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n'
 elif index==9:
  body='''
# Human-reference.md: coherent bent limb; no head or detached-head rule applies.
self.add_polyline('waist',(16,4),(28,4),(28,12))
self.add_bezier('outer-thigh',(28,12),((32,15),(38,17),(38,22)),((38,24),(34,27),(25,32)))
self.add_line('outer-calf',(25,32),(12,40))
self.add_polyline('toe',(12,40),(10,36),(28,25))
self.add_bezier('inner-thigh',(28,25),((24,23),(17,22),(14,19)),((10,15),(16,9),(16,4)))
self.add_contour('bent-leg','waist-1','waist-2','outer-thigh','outer-calf','toe-1','toe-2','inner-thigh',closed=True)
self.add_line('rear-thigh',(14,19),(14,30));self.relate('connect','bent-leg','rear-thigh')
self.add_bezier('rear-shin',(25,32),((24,35),(24,39),(25,40)),((26,42),(29,43),(31,43)),((28,44),(24,44),(20,43)))
self.relate('connect','bent-leg','rear-shin')
'''
  source=source.split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n'
 elif index in (12,13):
  source=source.replace('(20,24),(24,24),(28,24)','(21,24),(24,24),(27,24)').replace('(24,20),(24,24),(24,28)','(24,21),(24,24),(24,27)')
 elif index==14:
  source=source.replace("(28,14),(20,28),radius_x=16","(28,14),(22,25),radius_x=16").replace("(36,17),(26,35),radius_x=22","(36,17),(26,30),radius_x=22").replace('(28,42),(35,25),(42,42)','(30,42),(36,34),(42,42)')
 p.write_text(source)
 spec=importlib.util.spec_from_file_location('final_'+str(index),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon()
 rec['validation_status']=report.status
 (d/'validation.txt').write_text(report.describe());svg=icon.to_svg();(d/(row['icon_id']+'.svg')).write_text(svg)
 for size in (48,240):
  p=d/f'light-{size}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(p),output_width=size,output_height=size,background_color='white');ImageOps.invert(Image.open(p).convert('RGB')).save(d/f'dark-{size}.png')
 (d/'review-draft.json').write_text(json.dumps(rec,indent=2));print(row['concept'],report.describe(),flush=True)
