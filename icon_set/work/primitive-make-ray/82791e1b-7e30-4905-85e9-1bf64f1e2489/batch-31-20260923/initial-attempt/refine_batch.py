"""Review-driven revisions within the current attempt, preserving initial evidence."""
from pathlib import Path
import json, textwrap, importlib.util, shutil
import cairosvg
from PIL import Image, ImageOps
SOURCE_ICON_ID='82791e1b-7e30-4905-85e9-1bf64f1e2489'
SOURCE_PATH='icon_set/work/todo-references/online learning online course 2_82791e1b-7e30-4905-85e9-1bf64f1e2489.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ROWS=json.loads((ROOT/'batch-inputs.json').read_text())
FIXES={
0:('SQUARE','Page curvature simplified; field rule retained.', '''
self.add_polyline('pages',(10,6),(18,6),(24,10),(30,6),(38,6),(38,14),(30,14),(24,18),(18,14),(10,14),closed=True)
self.add_line('binding',(24,10),(24,18));self.relate('connect','pages','binding')
self.add_polyline('entry',(6,26),(42,26),(42,42),(6,42),closed=True)
self.add_line('entry-rule',(16,34),(32,34))
'''),
3:('SQUARE','All six fuel cells retained; flame reduced to a compact smooth tongue.', '''
self.add_arc('fire-left',(18,12),(24,6),radius_x=8,sweep=False)
self.add_arc('fire-tip',(24,6),(30,12),radius_x=12,sweep=False)
self.add_arc('fire-bowl',(30,12),(18,12),radius_x=6,radius_y=5)
self.add_contour('flame','fire-left','fire-tip','fire-bowl',closed=True)
self.box('fuel',6,26,36,16,2)
self.add_line('fuel-horizontal',(6,34),(42,34));self.relate('connect','fuel','fuel-horizontal')
for x in (18,30):
 self.add_polyline(f'fuel-divider-{x}',(x,26),(x,34),(x,42))
 self.relate('connect','fuel',f'fuel-divider-{x}');self.relate('connect','fuel-horizontal',f'fuel-divider-{x}')
'''),
5:('SQUARE','Short device indicator omitted; screen division retained.', '''
self.add_polyline('building',(16,34),(6,34),(6,20),(24,6),(42,20),(42,34),(32,34))
self.box('device',16,24,16,18,3)
self.relate('connect','building','device')
self.add_line('screen-rule',(16,33),(32,33));self.relate('connect','device','screen-rule')
'''),
7:('CIRCLE','None; triangular pattern and three circular wells retained.', '''
self.circle('palette',24,24,20)
for i,(x,y) in enumerate(((24,16),(17,29),(31,29))):self.circle(f'well-{i}',x,y,3)
'''),
8:('SQUARE','Hidden rear mountain edge omitted at overlap; sun retained.', '''
self.box('frame',6,6,36,36,4)
self.circle('sun',17,17,2)
self.add_polyline('front-mountain',(6,39),(17,28),(23,34),(28,39));self.relate('connect','frame','front-mountain')
self.add_polyline('back-mountain',(23,34),(32,23),(42,33));self.relate('connect','front-mountain','back-mountain');self.relate('connect','frame','back-mountain')
'''),
10:('SQUARE','Four text lines reduced to three; rectangular picture and enclosing panel retained.', '''
self.add_polyline('panel',(6,6),(42,6),(42,42),(6,42),closed=True)
self.add_polyline('image',(26,14),(34,14),(34,22),(26,22),closed=True)
for i,y in enumerate((17,25)):self.add_line(f'text-short-{i}',(14,y),(18,y))
self.add_line('text-long',(14,33),(34,33))
'''),
12:('HRECT_L','No letters omitted; narrow semicircular bowls make room for the plus.', '''
self.add_polyline('p-stem',(4,40),(4,24),(4,8))
self.add_arc('p-bowl',(4,8),(4,24),radius_x=8);self.relate('connect','p-stem','p-bowl')
self.add_polyline('plus-horizontal',(20,24),(24,24),(28,24))
self.add_polyline('plus-vertical',(24,20),(24,24),(24,28));self.relate('connect','plus-horizontal','plus-vertical')
self.add_polyline('b-stem',(36,40),(36,24),(36,8))
for i,y in enumerate((8,24)):
 self.add_arc(f'b-bowl-{i}',(36,y),(36,y+16),radius_x=8)
 self.relate('connect','b-stem',f'b-bowl-{i}')
self.relate('connect','b-bowl-0','b-bowl-1')
'''),
13:('HRECT_L','No letters omitted; narrow semicircular bowls make room for the plus.', '''
for name,x in (('p',4),('r',36)):
 self.add_polyline(name+'-stem',(x,40),(x,24),(x,8))
 self.add_arc(name+'-bowl',(x,8),(x,24),radius_x=8);self.relate('connect',name+'-stem',name+'-bowl')
self.add_polyline('plus-horizontal',(20,24),(24,24),(28,24))
self.add_polyline('plus-vertical',(24,20),(24,24),(24,28));self.relate('connect','plus-horizontal','plus-vertical')
self.add_line('r-leg',(36,24),(44,40));self.relate('connect','r-stem','r-leg');self.relate('connect','r-bowl','r-leg')
'''),
19:('VRECT_L','Latitude pair reduced to a central equator; one meridian retained. Source has no visible hand.', '''
self.box('cover',8,12,32,32,3)
self.add_line('binding',(8,15),(8,7))
self.add_arc('binding-corner',(8,7),(11,4),radius_x=3)
self.add_line('binding-top',(11,4),(35,4))
self.add_arc('binding-right',(35,4),(38,7),radius_x=3)
self.add_line('binding-end',(38,7),(38,12))
self.add_contour('binding-outline','binding','binding-corner','binding-top','binding-right','binding-end')
self.relate('connect','binding-outline','cover')
self.circle('globe',24,28,7)
self.add_polyline('equator',(17,28),(24,28),(31,28));self.relate('connect','globe','equator')
self.add_polyline('meridian',(24,21),(24,28),(24,35));self.relate('connect','globe','meridian');self.relate('connect','equator','meridian')
''')
}

for i,(key,omissions,body) in FIXES.items():
 row=ROWS[i];d=Path(row['result_dir']);rec=json.loads((d/'review-draft.json').read_text());p=d/rec['module']
 old=d/'initial-attempt';old.mkdir(exist_ok=True)
 for f in list(d.iterdir()):
  if f.is_file() and (f.suffix in ('.py','.svg') or f.name.startswith(('light-','dark-','validation.','review-draft.'))):shutil.copy2(f,old/f.name)
 source=p.read_text().split('    def build(self):')[0]
 import re
 source=re.sub(r'keyshape = Keyshape\.\w+',f'keyshape = Keyshape.{key}',source)
 source=re.sub(r'^OMISSIONS = .*$',f'OMISSIONS = {omissions!r}',source,flags=re.M)
 p.write_text(source+'    def build(self):\n'+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n')
 spec=importlib.util.spec_from_file_location('review_'+str(i),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon()
 rec.update(keyshape=key,omissions=omissions,validation_status=report.status);rec.pop('error',None)
 (d/'validation.txt').write_text(report.describe());svg=icon.to_svg();(d/(row['icon_id']+'.svg')).write_text(svg)
 for size in (48,240):
  p=d/f'light-{size}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(p),output_width=size,output_height=size,background_color='white');ImageOps.invert(Image.open(p).convert('RGB')).save(d/f'dark-{size}.png')
 (d/'review-draft.json').write_text(json.dumps(rec,indent=2));print(row['concept'],report.status,report.describe(),flush=True)
