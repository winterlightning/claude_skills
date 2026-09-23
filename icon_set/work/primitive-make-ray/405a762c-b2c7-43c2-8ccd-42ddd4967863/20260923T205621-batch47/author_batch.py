"""Standalone, ordered authoring for the supplied batch; no registry writes."""
from pathlib import Path
import json, importlib.util, sys, io
import cairosvg
from PIL import Image, ImageDraw, ImageOps

ROOT = Path(__file__).resolve().parent
INPUTS = json.loads((ROOT / 'batch-inputs.json').read_text())
SOURCE_ICON_ID = tuple(r['source_uuid'] for r in INPUTS)
SOURCE_PATH = tuple(r['reference_path'] for r in INPUTS)
AUTHOR = 'gpt-6'

HELPERS = '''
    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def frame(self):
        # SQUARE extremes: centerlines (6,6)-(42,42), ink (4,4)-(44,44).
        # Shared quarter-circle corners give a tangent-continuous square.
        lo, hi, r = 6, 42, 4
        nodes = [(lo+r,lo),(hi-r,lo),(hi,lo+r),(hi,hi-r),
                 (hi-r,hi),(lo+r,hi),(lo,hi-r),(lo,lo+r)]
        members=[]
        for i,a in enumerate(nodes):
            b=nodes[(i+1)%8]; name=f'frame-{i}'; members.append(name)
            if i%2: self.add_arc(name,a,b,radius_x=r)
            else: self.add_line(name,a,b)
        self.add_contour('frame',*members,closed=True)

    def up_arrow(self, name, x, top, bottom, half):
        tip=(x,top)
        self.add_polyline(name+'-head',(x-half,top+half),tip,(x+half,top+half))
        self.add_line(name+'-shaft',(x,bottom),tip)
        self.relate('connect',name+'-head',name+'-shaft')
'''

BODIES = [
'''# Frontal confined bust: shared human_ref/user.svg proportions and round head.
        # Head bottom 20; shoulder top 28: exactly 4 units of visible gap.
        self.frame()
        self.circle('head',24,16,4)
        self.add_arc('shoulder-left',(14,34),(24,28),radius_x=10,radius_y=6)
        self.add_arc('shoulder-right',(24,28),(34,34),radius_x=10,radius_y=6)
        self.add_line('body-right',(34,34),(34,36))
        self.add_line('body-base-r',(34,36),(29,36))
        self.add_line('body-base-mid',(29,36),(19,36))
        self.add_line('body-base-l',(19,36),(14,36))
        self.add_line('body-left',(14,36),(14,34))
        self.add_contour('body','shoulder-left','shoulder-right','body-right','body-base-r','body-base-mid','body-base-l','body-left',closed=True)
        for x in (19,29):
            self.add_line(f'arm-{x}',(x,31),(x,36))
            self.relate('connect',f'arm-{x}','body')
''',
'''# Curved receiver, with round earpiece transitions; deliberate diagonal pose.
        self.frame()
        self.add_bezier('receiver',(16,15),
            ((12,17),(15,26),(22,31)),
            ((27,34),(32,33),(33,30)),
            ((34,28),(31,26),(29,25)),
            ((27,24),(27,28),(25,27)),
            ((22,25),(19,22),(20,21)),
            ((23,19),(20,16),(19,15)),
            ((18,14),(17,14),(16,15)))
        self.add_contour('handset','receiver',closed=True)
''',
'''# Angular earpieces distinguish this phone from the rounded hangup source.
        self.frame()
        self.add_polyline('upper-ear',(16,15),(19,15),(23,19),(20,22))
        self.add_bezier('inner-bend',(20,22),((22,25),(23,26),(26,28)))
        self.add_polyline('lower-ear',(26,28),(29,25),(33,29),(33,32))
        self.add_bezier('outer-bend',(33,32),((27,39),(9,22),(16,15)))
        self.add_contour('handset','upper-ear-1','upper-ear-2','upper-ear-3',
                         'inner-bend','lower-ear-1','lower-ear-2','lower-ear-3',
                         'outer-bend',closed=True)
''',
'''self.frame()
        c=24
        for name,end in [('left',(15,c)),('right',(33,c)),('top',(c,15)),('bottom',(c,33))]:
            self.add_line(name,(c,c),end)
        self.relate('connect','left','right','top','bottom')
''',
'''self.frame()
        # Repeated poll bars share a left edge and an eight-unit vertical pitch.
        for i,end in enumerate((33,33,26)):
            y=16+8*i
            self.add_line(f'bar-{i}',(15,y),(end,y))
''',
'''self.frame()
        # Circular Q bowl with an exact 3-4-5 diagonal attachment.
        self.add_arc('bowl-a',(26,27),(20,19),radius_x=5)
        self.add_arc('bowl-b',(20,19),(26,27),radius_x=5)
        self.add_contour('bowl','bowl-a','bowl-b',closed=True)
        self.add_line('tail',(26,27),(33,33))
        self.relate('connect','bowl','tail')
''',
'''self.frame()
        # Nested grid: four equal cells, shared center and attachment nodes.
        lo,c,hi=15,24,33
        nodes=[(lo,lo),(c,lo),(hi,lo),(hi,c),(hi,hi),(c,hi),(lo,hi),(lo,c)]
        self.add_polyline('grid',*nodes,closed=True)
        for name,p in [('north',(c,lo)),('east',(hi,c)),('south',(c,hi)),('west',(lo,c))]:
            self.add_line(name,p,(c,c))
            self.relate('connect','grid',name)
        self.relate('connect','north','east','south','west')
''',
'''self.frame()
        # Two identical outlined commas, one shared definition and repeat pitch.
        for i,x in enumerate((18,30)):
            n=f'quote-{i}'
            self.add_bezier(n,(x+3,21),
                ((x+3,17),(x-3,17),(x-3,21)),
                ((x-3,24),(x-1,25),(x+1,25)),
                ((x+1,28),(x,30),(x-2,31)),
                ((x-1,32),(x-1,33),(x,33)),
                ((x+3,30),(x+3,26),(x+3,21)))
            self.add_contour(n+'-outline',n,closed=True)
''',
'''# The source enclosure itself points right: preserve the tag-shaped silhouette.
        self.add_polyline('frame',(6,6),(30,6),(42,18),(42,30),(30,42),(6,42),closed=True)
        tip=(32,24)
        self.add_polyline('arrow-head',(26,18),tip,(26,30))
        self.add_line('arrow-shaft',(15,24),tip)
        self.relate('connect','arrow-head','arrow-shaft')
''',
'''self.frame()
        # Three repeated rails; circular handles alternate their horizontal position.
        for i,x in enumerate((22,28,21)):
            y=16+8*i; n=f'slider-{i}'; r=3
            self.circle(n+'-knob',x,y,r)
            self.add_line(n+'-left',(15,y),(x-r,y))
            self.add_line(n+'-right',(x+r,y),(33,y))
            self.relate('connect',n+'-knob',n+'-left',n+'-right')
''',
'''self.frame()
        # Preserve the source's small degree mark and hand-authored F.
        self.add_dot('degree',(15,15))
        self.add_polyline('f-top',(33,16),(24,16),(24,24),(24,33))
        self.add_line('f-middle',(24,24),(31,24))
        self.relate('connect','f-top','f-middle')
''',
'''self.frame()
        self.add_dot('degree',(15,15))
        self.add_line('c-top',(33,15),(31,15))
        self.add_arc('c-curve',(31,15),(31,33),radius_x=9,sweep=False)
        self.add_line('c-bottom',(31,33),(33,33))
        self.add_contour('c','c-top','c-curve','c-bottom')
''',
'''self.frame()
        # Matching upright arrows and a shared baseline, as on a shipping label.
        for i,x in enumerate((18,30)):
            n=f'arrow-{i}'; tip=(x,15)
            self.add_polyline(n+'-head',(x-2,19),tip,(x+2,19))
            self.add_line(n+'-shaft',(x,25),tip)
            self.relate('connect',n+'-head',n+'-shaft')
        self.add_line('baseline',(15,33),(33,33))
''',
'''# Filename says u, but the supplied drawing is a right arrow inside a square.
        self.frame()
        tip=(33,24)
        self.add_polyline('head',(25,16),tip,(25,32))
        self.add_line('shaft',(15,24),tip)
        self.relate('connect','head','shaft')
''',
'''# Bent upward arrow with a leftward foot; intentional directional asymmetry.
        self.frame()
        tip=(27,15)
        self.add_polyline('head',(21,21),tip,(33,21))
        self.add_polyline('shaft',(15,33),(25,33))
        self.add_arc('elbow',(25,33),(27,31),radius_x=2,sweep=False)
        self.add_line('upright',(27,31),tip)
        self.add_contour('stem','shaft-1','elbow','upright')
        self.relate('connect','head','stem')
''',
'''self.frame()
        self.up_arrow('arrow',24,15,33,8)
''',
'''self.frame()
        self.up_arrow('arrow',24,15,33,8)
''',
'''self.frame()
        # human_ref/user.svg: circular head and broad shoulders, detached by 4 ink units.
        self.circle('head',24,17,4)
        self.add_arc('shoulder-left',(14,37),(24,29),radius_x=10,radius_y=8)
        self.add_arc('shoulder-right',(24,29),(34,37),radius_x=10,radius_y=8)
        self.add_line('body-base',(34,37),(14,37))
        self.add_contour('body','shoulder-left','shoulder-right','body-base',closed=True)
''',
'''# Preserve the checkmark shown in the source, including its longer rising arm.
        self.frame()
        self.add_polyline('check',(15,25),(22,32),(33,16))
''',
'''# Open box and upward export arrow. The arrow owns the top extreme.
        # VRECT_L centerlines (8,4)-(40,44), ink (6,2)-(42,46).
        self.add_line('left-lip',(14,20),(12,20))
        self.add_arc('nw',(12,20),(8,24),radius_x=4,sweep=False)
        self.add_line('left',(8,24),(8,40))
        self.add_arc('sw',(8,40),(12,44),radius_x=4,sweep=False)
        self.add_line('base',(12,44),(36,44))
        self.add_arc('se',(36,44),(40,40),radius_x=4,sweep=False)
        self.add_line('right',(40,40),(40,24))
        self.add_arc('ne',(40,24),(36,20),radius_x=4,sweep=False)
        self.add_line('right-lip',(36,20),(34,20))
        self.add_contour('box','left-lip','nw','left','sw','base','se','right','ne','right-lip')
        self.up_arrow('arrow',24,4,32,8)
'''
]

for i, (row, body) in enumerate(zip(INPUTS, BODIES)):
    if 'already_done' in row: continue
    d=Path(row['result_dir'])
    if (d/'result.json').exists(): continue
    icon_id=row['icon_id']; uid=row['source_uuid']
    module_name=icon_id.replace('-','_')+'_'+uid.replace('-','_')
    code=f'''"""{row['concept'].capitalize()}, reconstructed from the supplied reference.
Symbol plan: one complete composition; shared frame and repeated geometry parameters.
Lucide square-arrow-up informs tangent rounded corners and joined arrow construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uid!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {icon_id!r}
    keyshape = Keyshape.{'VRECT_L' if i==19 else 'SQUARE'}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/signage'
    aliases = ()
    keywords = {tuple(row['concept'].split())!r}

    def build(self):
        {body}
{HELPERS}
'''
    # Polyline contours cannot be re-used by another contour: emit the members directly.
    if i==2:
        code=code.replace("self.add_polyline('upper-ear',(16,15),(19,15),(23,19),(20,22))", "self.add_line('upper-ear-1',(16,15),(19,15))\n        self.add_line('upper-ear-2',(19,15),(23,19))\n        self.add_line('upper-ear-3',(23,19),(20,22))")
        code=code.replace("self.add_polyline('lower-ear',(26,28),(29,25),(33,29),(33,32))", "self.add_line('lower-ear-1',(26,28),(29,25))\n        self.add_line('lower-ear-2',(29,25),(33,29))\n        self.add_line('lower-ear-3',(33,29),(33,32))")
    if i==14:
        code=code.replace("self.add_polyline('shaft',(15,33),(25,33))", "self.add_line('shaft-1',(15,33),(25,33))")
    path=d/(module_name+'.py');path.write_text(code)
    spec=importlib.util.spec_from_file_location(module_name,path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    icon=mod.Drawing()
    report=icon.validate_icon(); (d/'validation.txt').write_text(report.describe())
    svg=icon.to_svg(); (d/(icon_id+'.svg')).write_text(svg)
    for size in (48,192):
        raster=cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size)
        rgba=Image.open(io.BytesIO(raster)).convert('RGBA')
        for theme,bg,fg in [('light','white','black'),('dark','#181818','white')]:
            out=Image.new('RGB',rgba.size,bg)
            out.paste(Image.new('RGB',rgba.size,fg),mask=rgba.getchannel('A'))
            out.save(d/f'{theme}-{size}.png')
    print(i+1,icon_id,report.status,flush=True)

# Comparison sheets retain the requested sequence and actual native renders.
for start in (0,10):
    sheet=Image.new('RGB',(1000,740),'#dddddd');draw=ImageDraw.Draw(sheet)
    for j,row in enumerate(INPUTS[start:start+10]):
        d=Path(row['result_dir']);x=j%5*200;y=j//5*370
        for filename,dx,dy in [('reference-192.png',4,20),('light-192.png',4,180),('light-48.png',6,320),('dark-48.png',68,320)]:
            im=Image.open(d/filename).convert('RGBA')
            if '192' in filename: im.thumbnail((150,150))
            sheet.paste(im,(x+dx,y+dy),im)
        draw.text((x+3,y+3),f'{start+j+1}. '+row['concept'][7:],fill='black')
    sheet.save(ROOT/f'comparison-{start//10+1}.png')
