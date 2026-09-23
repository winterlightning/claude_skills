"""Targeted visual and validation repairs, retaining the initial candidates."""
from pathlib import Path
import json,shutil,textwrap,importlib.util,cairosvg
from PIL import Image,ImageOps
SOURCE_ICON_ID='7b4f6d04-e199-443e-be81-3c0acef5ca62'
SOURCE_PATH='icon_set/work/todo-references/picture polaroid landscape_7b4f6d04-e199-443e-be81-3c0acef5ca62.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch-inputs.json').read_text())
replacements={
4:'''self.add_polyline('frame',(6,6),(42,6),(42,40),(42,42),(6,42),(6,30),closed=True)
self.add_polyline('back-mountain',(6,30),(18,18),(28,30));self.relate('connect','frame','back-mountain')
self.add_polyline('front-mountain',(22,36),(28,30),(30,28),(42,40));self.relate('connect','front-mountain','back-mountain');self.relate('connect','front-mountain','frame')
self.circle('sun',32,16,2)''',
12:'''self.add_arc('dome',(10,18),(38,18),radius_x=14)
self.add_bezier('right',(38,18),((38,24),(30,28),(26,30)),((25,31),(23,31),(22,30)))
self.add_bezier('left',(22,30),((18,28),(10,24),(10,18)))
self.add_contour('pin','dome','right','left',closed=True)
self.circle('hole',24,17,3)
self.cross('ground-x',24,40,9,4)''',
17:'''self.circle('head',22,9,5)
self.add_line('torso',(22,22),(22,32))
self.add_polyline('arm-right',(22,22),(29,28),(32,28));self.relate('connect','torso','arm-right')
self.add_polyline('arm-left',(22,22),(12,25),(12,28));self.relate('connect','torso','arm-left')
self.box('bag',8,28,8,10,2);self.relate('connect','bag','arm-left')
self.add_polyline('legs',(16,44),(22,32),(34,44));self.relate('connect','torso','legs')
self.mark_human_figure('traveler',head='head',torso='torso',torso_junction='start')
# Exact detached-head gap: head bottom 14, upper torso junction 22.
self.add_polyline('plane-spine',(36,4),(36,10),(36,18))
self.add_polyline('wings',(35,12),(36,10),(40,12));self.relate('connect','plane-spine','wings')
self.add_polyline('tail',(34,20),(36,18),(38,20));self.relate('connect','plane-spine','tail')'''
}
for index in (1,4,10,11,12,14,17):
 row=rows[index];d=Path(row['result_dir']);rec=json.loads((d/'review-draft.json').read_text());p=d/rec['module'];source=p.read_text()
 old=d/'initial-attempt';old.mkdir(exist_ok=True)
 for f in list(d.iterdir()):
  if f.is_file() and (f.suffix in ('.py','.svg') or f.name.startswith(('light-','dark-','validation.','review-draft.'))):shutil.copy2(f,old/f.name)
 if index in replacements:source=source.split('    def build(self):')[0]+'    def build(self):\n'+textwrap.indent(replacements[index],'        ')+'\n'
 elif index==1:
  source=source.replace("self.circle('head',20,18,4)","self.circle('head',20,19,4)").replace('((12,35),(15,30),(20,30)),((25,30),(28,35),(28,42))','((12,35),(15,31),(20,31)),((25,31),(28,35),(28,42))').replace('Head bottom 22; shoulder apex 30','Head bottom 23; shoulder apex 31')
 elif index==10:source=source.replace("self.add_polyline('tail',(28,35),(24,44),(20,35))","self.add_line('tail-1',(28,35),(24,44));self.add_line('tail-2',(24,44),(20,35))")
 elif index==11:source=source.replace("self.circle('hole',24,18,4)","self.circle('hole',24,18,3)")
 elif index==14:source=source.replace("self.pin('pin',24,4,11,32)","self.pin('pin',24,4,12,31)").replace("self.circle('hole',24,15,3)","self.circle('hole',24,16,3)")
 # Remove unused aircraft helper; each service scene owns its explicit outline.
 start=source.find('    def aircraft(self):')
 end=source.find('    def build(self):')
 if start>=0:source=source[:start]+source[end:]
 p.write_text(source)
 spec=importlib.util.spec_from_file_location('refined_'+str(index),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon();rec['validation_status']=report.status;rec.pop('error',None)
 (d/'validation.txt').write_text(report.describe());svg=icon.to_svg();(d/(row['icon_id']+'.svg')).write_text(svg)
 for size in (48,240):
  p=d/f'light-{size}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(p),output_width=size,output_height=size,background_color='white');ImageOps.invert(Image.open(p).convert('RGB')).save(d/f'dark-{size}.png')
 (d/'review-draft.json').write_text(json.dumps(rec,indent=2));print(row['concept'],report.describe(),flush=True)
