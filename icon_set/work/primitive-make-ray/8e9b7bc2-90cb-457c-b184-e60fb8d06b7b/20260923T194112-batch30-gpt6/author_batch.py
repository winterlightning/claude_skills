from pathlib import Path
import json, importlib.util, traceback
import cairosvg
from PIL import Image, ImageDraw
SOURCE_ICON_ID='8e9b7bc2-90cb-457c-b184-e60fb8d06b7b'
SOURCE_PATH='icon_set/work/todo-references/noise pollution traffic_8e9b7bc2-90cb-457c-b184-e60fb8d06b7b.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch.json').read_text())
helpers='''
    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-a', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-b', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded(self, name, left, top, right, bottom, radius=4):
        r=radius
        pts=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
             (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        names=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]; n=f'{name}-{i}'; names.append(n)
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
        self.add_contour(name,*names,closed=True)

    def clipboard(self):
        # Clip and board share the two nodes (16,12), (32,12).
        self.add_polyline('board', (16,12),(8,12),(8,44),(40,44),(40,12),(32,12))
        self.rounded('clip',16,4,32,12,4)
        self.relate('connect','board','clip')

    def cross(self, name, cx, cy, radius):
        for suffix,end in [('l',(cx-radius,cy)),('r',(cx+radius,cy)),('t',(cx,cy-radius)),('b',(cx,cy+radius))]:
            self.add_line(name+'-'+suffix,(cx,cy),end)
        self.relate('connect',*(name+'-'+s for s in ['l','r','t','b']))
'''
specs=[]
def add(key,subject,plan,code,ref,omissions='None.',human=None):
 specs.append(dict(keyshape=key,subject=subject,plan=plan,code=code,lucide=ref,omissions=omissions,human=human))
add('HRECT_L','Two cars beneath a lightning bolt and noise marks.',
    'A repeated pair of compact car silhouettes; an asymmetric lightning zigzag centered above.', '''
        for i,x in enumerate((4,28)):
            self.add_polyline(f'car-{i}',(x,36),(x,32),(x+4,28),(x+12,28),(x+16,32),(x+16,36),(x+13,36),(x+13,40),(x+10,40),(x+10,36),(x+6,36),(x+6,40),(x+3,40),(x+3,36),closed=True)
        self.add_polyline('lightning',(26,8),(18,18),(25,18),(22,24),(32,14),(25,14),closed=True)
        self.add_polyline('noise-left',(4,17),(8,21),(12,17))
        self.add_polyline('noise-right',(40,10),(36,14),(40,18))
''','car-front: repeated car body and paired wheel placement.','Minor noise strokes reduced; tiny vehicle contour details simplified.')
for idx in range(2):
 add('VRECT_L','An empty clipboard.' if idx==0 else 'A clipboard displaying a dollar sign.',
     'U-shaped board with a centered capsule clip; dollar construction belongs to the board interior.', '''
        self.clipboard()
''' + ('''        self.add_arc('s-top',(29,22),(19,26),radius_x=6,radius_y=4,sweep=False)
        self.add_arc('s-bottom',(19,26),(29,30),radius_x=6,radius_y=4)
        self.add_line('dollar-top',(24,18),(24,21))
        self.add_line('dollar-bottom',(24,31),(24,36))
''' if idx else ''),'notebook: coherent rounded enclosure; clip is reconstructed from the input.','None.' if not idx else 'Small currency terminals simplified.')
add('VRECT_L','An empty clipboard with a broad clip.','Centered clip and board with shared attachment nodes.','''
        self.clipboard()
''','notebook: enclosure and clean joined boundary.')
add('SQUARE','A blank top-bound notepad.','Three identical binding strokes at an 8-unit pitch; top frame split at attachment nodes.', '''
        self.add_polyline('page',(16,14),(6,14),(6,42),(42,42),(42,14),(32,14),(24,14),(16,14))
        for x in (16,24,32):
            self.add_line(f'binding-{x}',(x,6),(x,14))
            self.relate('connect',f'binding-{x}','page')
''','notepad-text: repeated binding rhythm and a single page silhouette.')
add('VRECT_L','A flip notepad with a checklist.','Top header strip, a check and two rows of writing.', '''
        self.add_polyline('page',(8,12),(8,4),(40,4),(40,12),(40,44),(8,44),(8,12))
        self.add_line('header',(8,12),(40,12)); self.relate('connect','header','page')
        self.add_polyline('check',(16,24),(20,28),(24,22))
        self.add_line('row-right',(32,24),(32,24))
        self.add_line('row-bottom',(16,36),(32,36))
''','notepad-text: aligned writing rows and top binding.','Four short text rules reduced to one rule and one compact mark.')
add('SQUARE','A medical cross inside a rounded square.','Symmetric outlined cross, owned by one shared center and arm thickness.', '''
        self.rounded('frame',6,6,42,42)
        c=24; lo=c-10; hi=c+10; a=c-4; b=c+4
        self.add_polyline('medical-cross',(a,lo),(b,lo),(b,a),(hi,a),(hi,b),(b,b),(b,hi),(a,hi),(a,b),(lo,b),(lo,a),(a,a),closed=True)
''','notebook: consistent rounded enclosure; outlined medical cross from supplied reference.')
add('VRECT_L','A written page with its upper right corner folded.','Fold shares two boundary nodes; evenly spaced writing rules below the fold.', '''
        self.add_polyline('page',(28,4),(8,4),(8,44),(40,44),(40,16),(28,4))
        self.add_polyline('fold',(28,4),(28,16),(40,16)); self.relate('connect','fold','page')
        for i,y in enumerate((25,34)): self.add_line(f'text-{i}',(17,y),(31 if i==0 else 27,y))
''','sticky-note: attached corner fold and uninterrupted page outline.','Three writing rules reduced to two for clearance.')
add('VRECT_L','A written note with its lower right corner turned up.','Lower fold and page share endpoints; writing aligned above it.', '''
        self.add_polyline('page',(28,44),(8,44),(8,4),(40,4),(40,32),(28,44))
        self.add_polyline('fold',(28,44),(28,32),(40,32)); self.relate('connect','fold','page')
        for i,y in enumerate((14,23)): self.add_line(f'text-{i}',(17,y),(31 if i==0 else 27,y))
''','sticky-note: fold construction, deliberately moved to the input’s lower-right corner.','Three writing rules reduced to two.')
add('VRECT_L','A spiral flip pad with writing.','Three identical binding hooks above the page; two aligned writing rules.', '''
        self.add_polyline('page',(16,12),(8,12),(8,44),(40,44),(40,12),(32,12),(24,12),(16,12))
        for x in (16,24,32):
            self.add_line(f'binding-{x}',(x,4),(x,12)); self.relate('connect',f'binding-{x}','page')
        for i,y in enumerate((23,33)): self.add_line(f'text-{i}',(17,y),(31 if i==0 else 27,y))
''','notepad-text: evenly repeated top binding and writing rows.','Spiral loops reduced to binding strokes; three text rules reduced to two.')
add('VRECT_M','An outlined numeral zero.','One closed oval with paired elliptical semicircles.', '''
        self.circle('zero',24,24,14,20)
''','No useful subject match; two coherent elliptical arcs preserve the input oval.')
add('SQUARE','A nun wearing a veil and a cross.','Circular face, symmetric arched veil, detached shoulders and cross; shared human-reference vocabulary.', '''
        self.add_arc('veil-top',(6,24),(42,24),radius_x=18)
        self.add_polyline('veil-sides',(42,24),(42,42),(6,42),(6,24))
        self.add_contour('veil','veil-top','veil-sides-1','veil-sides-2','veil-sides-3',closed=True)
        self.circle('face',24,21,7)
        self.add_arc('shoulder-left',(6,42),(16,36),radius_x=10,radius_y=6)
        self.add_line('shoulder-top',(16,36),(32,36))
        self.add_arc('shoulder-right',(32,36),(42,42),radius_x=10,radius_y=6)
        self.add_contour('shoulders','shoulder-left','shoulder-top','shoulder-right')
        self.relate('connect','shoulders','veil')
        self.cross('cross',24,40,3)
''','No useful Lucide match; shared human_ref/user.svg supplies circular head and broad shoulders.',
    'Facial band and neck seams omitted; veil and cross retained.',
    'human_ref/user.svg inspected. Face bottom centerline y=28, shoulder top y=36: centerline gap 8, ink gap 4. Face radius 7; symmetrical shoulders.')
add('CIRCLE','A circle crossed by diagonal exclusion lines.','Four circle arcs with shared diagonal endpoints; two diagonals split at their intersection.', '''
        pts=[(12,8),(36,8),(36,40),(12,40)]
        for i in range(4): self.add_arc(f'rim-{i}',pts[i],pts[(i+1)%4],radius_x=20)
        self.add_contour('rim',*(f'rim-{i}' for i in range(4)),closed=True)
        for i,p in enumerate(pts):
            self.add_line(f'spoke-{i}',p,(24,24)); self.relate('connect',f'spoke-{i}','rim')
        self.relate('connect',*(f'spoke-{i}' for i in range(4)))
''','combine: simple Boolean geometry; circular exclusion topology from input.')
add('SQUARE','A square with an offset circular subtraction area.','Rounded square and a separate circular hole toward the lower right.', '''
        self.rounded('square',6,6,42,42)
        self.circle('cutout',27,27,6)
''','combine: distinct Boolean operands; rounded corners from notebook.','Circular cutout reduced to preserve clearance.')
add('VRECT_L','A head silhouette containing an obsessive checklist.','Left-facing profile with checklist inside; deliberate anatomical asymmetry.', '''
        self.add_arc('cranium',(12,20),(40,20),radius_x=14,radius_y=16)
        self.add_arc('back',(40,20),(35,34),radius_x=22)
        self.add_line('neck-back',(35,34),(35,44))
        self.add_polyline('face-neck',(12,20),(8,28),(12,28),(12,34),(20,34),(20,44))
        self.add_contour('profile-top','cranium','back','neck-back')
        self.relate('connect','profile-top','face-neck')
        for i,y in enumerate((15,24)):
            self.add_polyline(f'check-{i}',(19,y),(21,y+2),(24,y-2))
            self.add_line(f'text-{i}',(32,y),(33,y))
        self.add_polyline('empty-box',(25,33),(29,33),(29,37),(25,37),closed=True)
''','No useful Lucide match; supplied reference defines checklist profile.','Three writing rules reduced to two; small empty checkbox retained as a validation-risk feature.',
    'human_ref/user.svg inspected for contour economy. This is a connected head/neck profile, not a detached stick figure; no detached-head gap applies.')
add('SQUARE','An eight-sided polygon.','Four mirrored corner cuts with equal horizontal and vertical spans.', '''
        low,high,cut=6,42,11
        self.add_polyline('octagon',(low+cut,low),(high-cut,low),(high,low+cut),(high,high-cut),(high-cut,high),(low+cut,high),(low,high-cut),(low,low+cut),closed=True)
''','octagon: symmetric corner cuts and one closed contour.')
add('HRECT_L','An office desk with a monitor, clock, and cup.','Desk spans the keyshape; monitor left and clock right deliberately balance different shapes.', '''
        self.add_polyline('desk',(4,32),(44,32),(42,40))
        self.add_line('leg-left',(6,32),(4,40)); self.relate('connect','leg-left','desk')
        self.rounded('monitor',4,8,26,24,3)
        self.add_line('stand',(15,24),(15,32)); self.relate('connect','stand','monitor'); self.relate('connect','stand','desk')
        self.circle('clock',38,14,6)
        self.add_polyline('hands',(38,10),(38,14),(41,14)); self.relate('connect','hands','clock')
        self.add_polyline('cup',(34,32),(34,26),(40,26),(40,32)); self.relate('connect','cup','desk')
''','laptop: simple screen enclosure and supporting base.','Desk apron and monitor lower bezel omitted; cup and clock retained.')
add('VRECT_L','A document with a diagonal signing pen.','Open page outline around the diagonal pen; coherent pointed pen contour.', '''
        self.add_polyline('page',(40,12),(40,4),(8,4),(8,44),(40,44),(40,32))
        self.add_polyline('pen',(16,34),(20,22),(32,10),(40,18),(28,30),(16,34))
        self.add_line('pen-band',(28,14),(36,22)); self.relate('connect','pen-band','pen')
''','file-pen: diagonal writing tool with an open page boundary.','Short baseline flourish omitted.')
add('CIRCLE','A six-petal Onam flower inside a circular rim.','Six petals built as mirrored arc pairs around a central hexagon; circular frame.', '''
        self.circle('rim',24,24,20)
        core=[(20,18),(28,18),(32,24),(28,30),(20,30),(16,24)]
        self.add_polyline('center',*core,closed=True)
        petals=[((20,18),(24,7),(28,18)),((28,18),(39,13),(32,24)),((32,24),(39,35),(28,30)),((28,30),(24,41),(20,30)),((20,30),(9,35),(16,24)),((16,24),(9,13),(20,18))]
        for i,(a,tip,b) in enumerate(petals):
            self.add_arc(f'petal-{i}-a',a,tip,radius_x=12)
            self.add_arc(f'petal-{i}-b',tip,b,radius_x=12)
            self.add_contour(f'petal-{i}',f'petal-{i}-a',f'petal-{i}-b')
            self.relate('connect',f'petal-{i}','center')
''','No useful Lucide match; mirrored arc-pair petal construction follows the supplied flower.','None; all six petals and circular border retained.')
add('HRECT_L','A doctor behind an open laptop.','Circular head above smooth shoulders, cross on right chest, laptop in left foreground.', '''
        self.circle('head',30,15,7)
        self.add_arc('shoulder',(16,37),(44,37),radius_x=14,radius_y=7)
        self.add_line('body-right',(44,37),(44,40)); self.add_contour('body','shoulder','body-right')
        self.add_polyline('laptop',(4,40),(7,32),(23,32),(28,40),(4,40))
        self.add_polyline('screen',(7,32),(7,23),(12,23)); self.relate('connect','screen','laptop')
        self.cross('medical',35,36,4)
''','laptop: tapered base; human_ref/user.svg: round head and broad arched shoulders.',
    'Minor screen edge reduced; medical cross retained.',
    'human_ref/user.svg inspected. Head bottom y=22, shoulder top y=30: 8 centerline units / 4 ink units. Head radius 7, shoulder radius_x 14. Medical cross clearance is independently validated.')
assert len(specs)==20
for r,s in zip(rows,specs):
 d=Path(r['result_dir']); uid=r['source_uuid']; name=r['icon_id']
 source='from icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n\n'
 source+=f'SOURCE_ICON_ID = {uid!r}\nSOURCE_PATH = {r["reference_path"]!r}\nAUTHOR = {AUTHOR!r}\n\n'
 source+=f'class Drawing(Solo48):\n    """{s["subject"]}\n\n    Plan: {s["plan"]}\n    Construction reference: {s["lucide"]}\n    """\n'
 source+=f'    icon_id = {name!r}\n    keyshape = Keyshape.{s["keyshape"]}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(r["concept"].split())!r}\n'
 if s['human']: source+=f'    # {s["human"]}\n'
 source+=helpers+'\n    def build(self):\n'+s['code']
 py=d/(name.replace('-','_')+'_'+uid.replace('-','_')+'.py'); py.write_text(source)
 result={**r,**{k:v for k,v in s.items() if k!='code'},'module':py.name,'svg':name+'.svg'}
 try:
  spec=importlib.util.spec_from_file_location('candidate_'+uid,py); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod); icon=mod.Drawing()
  report=icon.validate_icon(); (d/'validation.txt').write_text(report.describe()); result['validation_status']=report.status
  svg=icon.to_svg(); (d/(name+'.svg')).write_text(svg)
  for theme,fg,bg in [('light','#111111','#ffffff'),('dark','#ffffff','#171717')]:
   for size in (48,288):
    cairosvg.svg2png(bytestring=svg.replace('currentColor',fg).replace('#000000',fg).encode(),write_to=str(d/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
 except Exception:
  result['validation_status']='error';result['error']=traceback.format_exc();(d/'error.txt').write_text(result['error'])
 (d/'candidate.json').write_text(json.dumps(result,indent=2))
 print(name,result['validation_status'],flush=True)
# Review sheets are evidence only, contained in the first result folder.
for group in range(4):
 sheet=Image.new('RGB',(1000,470),'#dedede'); draw=ImageDraw.Draw(sheet)
 for j,r in enumerate(rows[group*5:(group+1)*5]):
  d=Path(r['result_dir']); x=j*200
  draw.text((x+5,5),f'{group*5+j+1}. {r["concept"]}',fill='black')
  for t,theme in enumerate(('light','dark')):
   p=d/f'{theme}-288.png'
   if p.exists():
    im=Image.open(p).convert('RGB'); im=im.resize((180,180)); sheet.paste(im,(x+10,30+t*220))
    im=Image.open(d/f'{theme}-48.png').convert('RGB');sheet.paste(im,(x+76,210+t*220))
 sheet.save(ROOT/f'review-{group+1}.png')
