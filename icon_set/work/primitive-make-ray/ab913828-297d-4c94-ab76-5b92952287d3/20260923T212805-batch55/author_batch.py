"""Isolated, ordered SOLO48 authoring for the eighteen supplied batch-55 files."""
from pathlib import Path
import json, importlib.util, io, traceback
import cairosvg
from PIL import Image, ImageDraw
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile

ROOT=Path(__file__).resolve().parent
INPUTS=json.loads((ROOT/'batch-inputs.json').read_text())
SOURCE_ICON_ID=tuple(r['source_uuid'] for r in INPUTS)
SOURCE_PATH=tuple(r['reference_path'] for r in INPUTS)
AUTHOR='gpt-6'

HELPERS='''
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)

    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        # Shared rectangle parameters own radii, symmetry and attachment nodes.
        seg=[('L',(x,t)) for x in sorted(set(top)) if l+k<x<r-k]
        seg += [('L',(r-k,t)),('A',(r,t+k),k)]
        seg += [('L',(r,y)) for y in sorted(set(right)) if t+k<y<b-k]
        seg += [('L',(r,b-k)),('A',(r-k,b),k)]
        seg += [('L',(x,b)) for x in sorted(set(bottom),reverse=True) if l+k<x<r-k]
        seg += [('L',(l+k,b)),('A',(l,b-k),k)]
        seg += [('L',(l,y)) for y in sorted(set(left),reverse=True) if t+k<y<b-k]
        seg += [('L',(l,t+k)),('A',(l+k,t),k)]
        self.path(n,(l+k,t),seg,True)

    def shoulders(self,n,l,x,r,top,bottom):
        self.add_arc(n+'-left',(l,bottom),(x,top),radius_x=x-l,radius_y=bottom-top)
        self.add_arc(n+'-right',(x,top),(r,bottom),radius_x=r-x,radius_y=bottom-top)
        self.add_contour(n,n+'-left',n+'-right')
'''

BODIES=[
'''# Two opposite circular arrows surround one coherent pair of clock hands.
        self.add_arc('upper-orbit',(40,12),(4,24),radius_x=20,sweep=False)
        self.add_arc('lower-orbit',(8,36),(44,24),radius_x=20,sweep=False)
        self.add_polyline('left-arrow',(9,20),(4,24),(6,16))
        self.add_polyline('right-arrow',(39,28),(44,24),(42,32))
        self.relate('connect','upper-orbit','left-arrow')
        self.relate('connect','lower-orbit','right-arrow')
        self.add_polyline('clock-hands',(24,16),(24,28),(31,28))
''',
'''# One connected breaking-wave stroke inside a rounded square.
        self.rect('frame',6,6,42,42,4,left=(29,),right=(31,))
        self.add_bezier('wave-rise',(6,29),((14,29),(14,17),(24,16)),((28,15),(30,15),(32,18)))
        self.add_bezier('wave-curl',(32,18),((19,15),(20,31),(30,32)),((34,33),(38,32),(42,31)))
        self.add_contour('wave','wave-rise','wave-curl')
        self.relate('connect','frame','wave')
''',
'''# Complete sun/cloud/location composition, retaining all three symbols.
        self.add_arc('sun-upper',(8,16),(24,16),radius_x=8)
        self.add_bezier('sun-lower',(13,23),((10,23),(8,20),(8,16)))
        self.add_contour('sun','sun-lower','sun-upper')
        for n,a,b in [('north',(16,6),(16,7)),('west',(6,16),(7,16)),
                      ('northwest',(8,8),(9,9)),('northeast',(23,8),(24,7)),
                      ('southwest',(8,24),(7,25))]: self.add_line('ray-'+n,a,b)
        self.add_line('cloud-base',(22,34),(12,34))
        self.add_bezier('cloud-left',(12,34),((8,34),(6,31),(6,28)),((6,25),(9,23),(13,23)))
        self.add_bezier('cloud-crown',(13,23),((16,23),(16,16),(24,16)),((30,14),(34,18),(36,22)))
        self.add_bezier('cloud-right',(36,22),((40,22),(42,24),(42,28)),((42,30),(41,32),(40,33)))
        self.add_contour('cloud','cloud-base','cloud-left','cloud-crown','cloud-right')
        self.relate('connect','sun','cloud')
        self.add_arc('pin-top',(26,30),(42,30),radius_x=8)
        self.add_bezier('pin-lower',(42,30),((42,34),(36,40),(34,42)),((32,40),(26,34),(26,30)))
        self.add_contour('pin','pin-top','pin-lower',closed=True)
        self.circle('pin-hole',34,30,3)
''',
'''# Two circular nodes, connecting line and central X; preserve the thin-row aspect.
        # This aspect cannot fill the minimum-height SOLO48 horizontal keyshape.
        self.circle('left-node',10,24,6)
        self.circle('right-node',38,24,6)
        self.add_polyline('connector',(16,24),(24,24),(32,24))
        self.add_polyline('cross-a',(20,20),(24,24),(28,28))
        self.add_polyline('cross-b',(20,28),(24,24),(28,20))
        self.relate('connect','left-node','connector')
        self.relate('connect','right-node','connector')
        self.relate('connect','connector','cross-a','cross-b')
''',
'''# Two overlapping speech bubbles, exactly as the eye-free supplied logo shows.
        self.add_bezier('rear-lower',(16,30),((14,30),(13,29),(11,29)))
        self.add_polyline('rear-tail',(11,29),(6,33),(7,27))
        self.add_bezier('rear-left',(7,27),((5,25),(4,22),(4,19)))
        self.add_bezier('rear-crown',(4,19),((4,13),(10,8),(18,8)),((26,8),(32,13),(32,18)))
        self.add_contour('rear','rear-lower','rear-tail-1','rear-tail-2','rear-left','rear-crown')
        self.add_bezier('front-crown',(32,18),((39,18),(44,22),(44,28)),((44,31),(42,34),(41,35)))
        self.add_polyline('front-tail',(41,35),(44,40),(36,37))
        self.add_bezier('front-base',(36,37),((26,40),(16,36),(16,30)))
        self.add_line('front-left',(16,30),(16,28))
        self.add_bezier('front-upper',(16,28),((16,22),(23,18),(32,18)))
        self.add_contour('front','front-crown','front-tail-1','front-tail-2','front-base','front-left','front-upper',closed=True)
        self.relate('connect','rear','front')
''',
'''# One broad speech bubble with a checkmark and a lower-left tail.
        self.add_bezier('crown',(4,22),((4,14),(13,8),(24,8)),((35,8),(44,14),(44,22)))
        self.add_bezier('lower',(44,22),((44,30),(35,36),(24,36)),((20,36),(16,35),(13,34)))
        self.add_polyline('tail',(13,34),(4,40),(6,30))
        self.add_bezier('left',(6,30),((5,28),(4,25),(4,22)))
        self.add_contour('bubble','crown','lower','tail-1','tail-2','left',closed=True)
        self.add_polyline('check',(14,21),(21,27),(33,19))
''',
'''# Three bunting flags above two overlapping hearts.
        self.add_polyline('cord',(6,6),(10,7),(18,8),(21,9),(29,9),(32,9),(40,8),(42,8))
        for i,points in enumerate([((10,7),(13,14),(18,8)),((21,9),(25,14),(29,9)),((32,9),(36,15),(40,8))]):
            self.add_polyline(f'flag-{i}',*points)
            self.relate('connect','cord',f'flag-{i}')
        self.add_bezier('rear-heart',(32,29),((32,22),(24,20),(20,26)),
            ((16,20),(6,22),(6,29)),((6,33),(12,37),(18,39)))
        self.add_line('rear-heart-end',(18,39),(24,35))
        self.add_contour('heart-back','rear-heart','rear-heart-end')
        self.add_bezier('heart-front',(24,35),((23,34),(22,32),(22,30)),
            ((22,24),(29,24),(32,29)),((35,24),(42,24),(42,30)),
            ((42,35),(35,40),(32,42)),((29,40),(26,38),(24,35)))
        self.add_contour('heart-front-outline','heart-front',closed=True)
        self.relate('connect','heart-back','heart-front-outline')
''',
'''# Circular wheat emblem; the source contains no exclamation mark.
        self.circle('ring',24,24,20)
        self.add_bezier('terminal-grain',(24,13),((18,19),(21,23),(24,24)),((27,23),(30,19),(24,13)))
        self.add_contour('grain-top','terminal-grain',closed=True)
        self.add_polyline('stem',(24,24),(24,29),(24,35))
        self.relate('connect','stem','grain-top')
        for row,y in enumerate((23,29)):
            join_y=29+6*row
            for side in (-1,1):
                x=24+side*10; n=f'grain-{row}-{side}'
                self.add_bezier(n,(x,y),((x,y+5),(24+side*4,join_y),(24,join_y)),
                    ((24+side*3,y+1),(24+side*7,y),(x,y)))
                self.add_contour(n+'-outline',n,closed=True)
                self.relate('connect','stem',n+'-outline')
''',
'''# Pentagram in a circle. Integer 12-16-20 circle points own all five tips.
        # The upper pair is higher than a regular pentagon to keep exact attachments.
        tips=[(24,4),(40,12),(36,40),(12,40),(8,12)]
        for i,p in enumerate(tips):
            self.add_arc(f'ring-{i}',p,tips[(i+1)%5],radius_x=20)
        self.add_contour('ring',*(f'ring-{i}' for i in range(5)),closed=True)
        self.add_polyline('pentagram',tips[0],tips[2],tips[4],tips[1],tips[3],closed=True)
        self.relate('connect','ring','pentagram')
''',
'''# Cropped portrait with the source's continuous neck, inside a wide window.
        # human_ref/user.svg informs head/shoulder proportions; no detached gap applies.
        self.rect('window',4,10,44,38,5,bottom=(14,34))
        self.add_bezier('shoulder-left',(14,38),((14,34),(18,34),(21,32)),((24,31),(19,29),(19,24)))
        self.add_arc('head-crown',(19,24),(29,24),radius_x=5)
        self.add_bezier('shoulder-right',(29,24),((29,29),(24,31),(27,32)),((30,34),(34,34),(34,38)))
        self.add_contour('portrait','shoulder-left','head-crown','shoulder-right')
        self.relate('connect','window','portrait')
''',
'''# Curved windshield: arched top, leaning sides and concave lower edge.
        self.add_bezier('upper-left',(8,12),((12,11),(18,10),(24,10)))
        self.add_bezier('upper-right',(24,10),((30,10),(36,11),(40,12)),((43,13),(44,14),(44,16)))
        self.add_line('right',(44,16),(40,35))
        self.add_bezier('lower-right',(40,35),((40,37),(39,38),(38,38)),((34,38),(30,36),(24,36)))
        self.add_bezier('lower-left',(24,36),((18,36),(14,38),(10,38)),((9,38),(8,37),(8,35)))
        self.add_line('left',(8,35),(4,16))
        self.add_bezier('upper-corner',(4,16),((4,14),(5,13),(8,12)))
        self.add_contour('windshield','upper-left','upper-right','right','lower-right','lower-left','left','upper-corner',closed=True)
''',
'''# Nonsexual frontal female torso, preserving the chest, waist and navel.
        # Shared human guidance owns smooth paired anatomy; the source has no head.
        self.rect('frame',6,6,42,42,3)
        for side in (-1,1):
            def p(x,y): return (24+side*x,y)
            n='torso-'+str(side)
            self.add_bezier(n,p(8,15),(p(9,17),p(10,20),p(9,22)),
                (p(8,25),p(5,27),p(6,29)),(p(6,31),p(7,32),p(8,34)))
        self.add_bezier('chest',(15,22),((15,27),(20,27),(24,25)),((28,27),(33,27),(33,22)))
        self.relate('connect','chest','torso--1')
        self.relate('connect','chest','torso-1')
        for i,x in enumerate((20,28)): self.add_dot(f'nipple-{i}',(x,21))
        self.add_dot('navel',(24,31))
''',
'''# Hand-authored serif W, preserving the standalone WordPress letterform.
        self.add_polyline('w',(8,8),(16,40),(24,8),(32,38),(40,8))
        for i,x in enumerate((8,24,40)):
            self.add_polyline(f'serif-{i}',(x-4,8),(x,8),(x+4,8))
            self.relate('connect','w',f'serif-{i}')
''',
'''# Large dismissal X above three repeated busts.
        # human_ref/user.svg: head cy=26,r=3; shoulder crest=37 gives 4 ink units.
        self.add_polyline('cross-a',(18,8),(24,12),(30,16))
        self.add_polyline('cross-b',(18,16),(24,12),(30,8))
        self.relate('connect','cross-a','cross-b')
        for i,(l,x,r) in enumerate(((4,10,17),(17,24,31),(31,38,44))):
            self.circle(f'head-{i}',x,26,3)
            self.shoulders(f'body-{i}',l,x,r,37,40)
        self.relate('connect','body-0','body-1')
        self.relate('connect','body-1','body-2')
''',
'''# Agreement bubble, checkmark, two tails and two detached human busts.
        self.path('bubble',(18,6),[('L',(30,6)),('A',(34,10),4),('L',(34,18)),
            ('A',(30,22),4),('L',(30,25)),('L',(24,22)),('L',(18,25)),
            ('L',(18,22)),('A',(14,18),4),('L',(14,10)),('A',(18,6),4)],True)
        self.add_polyline('check',(20,13),(23,16),(28,11))
        for i,x in enumerate((11,37)):
            self.circle(f'head-{i}',x,28,3)
            self.shoulders(f'body-{i}',x-5,x,x+5,39,42)
        # Actual head bottom 31 and shoulder crest 39: centerline gap 8, ink gap 4.
''',
'''# Rising zigzag arrow above a stepped four-row data grid.
        self.add_polyline('growth',(6,26),(14,16),(20,20),(27,12),(32,16),(42,6))
        self.add_polyline('arrow-head',(34,6),(42,6),(42,14))
        self.relate('connect','growth','arrow-head')
        self.add_polyline('table',(14,27),(24,27),(24,22),(33,22),(42,22),(42,27),
            (42,32),(42,37),(42,42),(33,42),(24,42),(14,42),(14,37),(14,32),closed=True)
        for x in (24,33):
            ys=(27,32,37,42) if x==24 else (22,27,32,37,42)
            self.add_polyline(f'column-{x}',*((x,y) for y in ys))
            self.relate('connect','table',f'column-{x}')
        for y in (27,32,37):
            xs=(24,33,42) if y==27 else (14,24,33,42)
            self.add_polyline(f'row-{y}',*((x,y) for x in xs))
            self.relate('connect','table',f'row-{y}')
            for x in (24,33): self.relate('connect',f'column-{x}',f'row-{y}')
''',
'''# Three concentric quarter-wave arcs above-left of a circular Z badge.
        for i,r in enumerate((18,12,6)):
            self.add_arc(f'wave-{i}',(24-r,24),(24,24-r),radius_x=r)
        self.circle('badge',32,32,10)
        self.add_polyline('z',(29,28),(35,28),(29,36),(35,36))
''',
'''# Three flame tips over a round lower bowl with an independently drawn Z.
        self.add_bezier('flame-upper',(30,6),((30,11),(29,14),(28,17)),
            ((34,17),(38,14),(40,12)),((40,18),(38,23),(36,26)),((38,27),(40,27),(42,26)),
            ((41,30),(39,33),(37,34)),((36,40),(30,42),(24,42)))
        self.add_bezier('flame-lower',(24,42),((12,42),(6,38),(6,26)),
            ((6,18),(12,12),(21,11)),((25,10),(28,8),(30,6)))
        self.add_contour('flame','flame-upper','flame-lower',closed=True)
        self.add_polyline('z',(17,25),(25,25),(17,33),(25,33))
'''
]

KEYSHAPES=['CIRCLE','SQUARE','SQUARE','HRECT_M','HRECT_L','HRECT_L','SQUARE','CIRCLE','CIRCLE','HRECT_M','HRECT_M','SQUARE','HRECT_L','HRECT_L','SQUARE','SQUARE','SQUARE','SQUARE']

def author():
    for i,(row,body) in enumerate(zip(INPUTS,BODIES)):
        if 'result_dir' not in row:continue
        d=Path(row['result_dir'])
        if (d/'result.json').exists():continue
        bounds=Keyshape[KEYSHAPES[i]].bounds_for(Profile.SOLO48)
        extrema=tuple(v+2 if j<2 else v-2 for j,v in enumerate(bounds))
        code=f'''"""{row['concept'].capitalize()}, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={row['source_uuid']!r}
SOURCE_PATH={row['reference_path']!r}
AUTHOR={AUTHOR!r}

class Drawing(Solo48):
    icon_id={row['icon_id']!r}
    keyshape=Keyshape.{KEYSHAPES[i]}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords={tuple(row['concept'].split())!r}

    # Visible extrema {bounds}; centerline extremes {extrema}.
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        {body}
{HELPERS}
'''
        # Contour membership is exclusive; replace polyline shorthand when its
        # members belong to the larger continuous contour.
        if i in (4,5):
            replacements={
              "self.add_polyline('rear-tail',(11,29),(6,33),(7,27))":"self.add_line('rear-tail-1',(11,29),(6,33))\n        self.add_line('rear-tail-2',(6,33),(7,27))",
              "self.add_polyline('front-tail',(41,35),(44,40),(36,37))":"self.add_line('front-tail-1',(41,35),(44,40))\n        self.add_line('front-tail-2',(44,40),(36,37))",
              "self.add_polyline('tail',(13,34),(4,40),(6,30))":"self.add_line('tail-1',(13,34),(4,40))\n        self.add_line('tail-2',(4,40),(6,30))"}
            for a,b in replacements.items():code=code.replace(a,b)
        name=row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')
        module=d/(name+'.py');module.write_text(code)
        try:
            spec=importlib.util.spec_from_file_location(name,module);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
            icon=mod.Drawing();report=icon.validate_icon();(d/'validation.txt').write_text(report.describe())
            svg=icon.to_svg();(d/(row['icon_id']+'.svg')).write_text(svg)
            for size in (48,192):
                raw=cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size)
                rgba=Image.open(io.BytesIO(raw)).convert('RGBA')
                for theme,bg,fg in [('light','white','black'),('dark','#181818','white')]:
                    im=Image.new('RGB',rgba.size,bg);im.paste(Image.new('RGB',rgba.size,fg),mask=rgba.getchannel('A'));im.save(d/f'{theme}-{size}.png')
            print(i+1,row['concept'],report.status,flush=True)
        except Exception:
            (d/'error.txt').write_text(traceback.format_exc());print(i+1,row['concept'],'ERROR',traceback.format_exc(),flush=True)

def sheets():
    for start in (0,9):
        sheet=Image.new('RGB',(900,1170),'#dddddd');dr=ImageDraw.Draw(sheet)
        for j,row in enumerate(INPUTS[start:start+9]):
            if 'result_dir'not in row:continue
            d=Path(row['result_dir']);x=j%3*300;y=j//3*390
            for filename,dx,dy in [('reference-192.png',4,20),('light-192.png',4,190),('light-48.png',170,210),('dark-48.png',230,210)]:
                if not (d/filename).exists():continue
                im=Image.open(d/filename).convert('RGBA')
                if '192' in filename:im.thumbnail((150,150))
                sheet.paste(im,(x+dx,y+dy),im)
            dr.text((x+3,y+3),f'{start+j+1}. '+row['concept'],fill='black')
        sheet.save(ROOT/f'comparison-{start//9+1}.png')
    sheet=Image.new('RGB',(1200,810),'#181818');dr=ImageDraw.Draw(sheet)
    for i,row in enumerate(INPUTS):
        if 'result_dir'not in row:continue
        d=Path(row['result_dir']);x=i%6*200;y=i//6*270
        if not (d/'dark-192.png').exists():continue
        sheet.paste(Image.open(d/'dark-192.png'),(x,y));sheet.paste(Image.open(d/'dark-48.png'),(x+72,y+192));dr.text((x+5,y+245),str(i+1)+' '+row['concept'][:26],fill='white')
    sheet.save(ROOT/'dark-review.png')

if __name__=='__main__':
    author();sheets()
