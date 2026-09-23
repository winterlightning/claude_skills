"""Author the twenty supplied batch-49 references as isolated SOLO48 models."""
from pathlib import Path
import json, importlib.util, io, traceback
import cairosvg
from PIL import Image, ImageDraw

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
        # One rounded rectangle owns paired radii, extents, and connection splits.
        seg=[('L',(x,t)) for x in sorted(set(top)) if l+k<x<r-k]
        seg += [('L',(r-k,t)),('A',(r,t+k),k)]
        seg += [('L',(r,y)) for y in sorted(set(right)) if t+k<y<b-k]
        seg += [('L',(r,b-k)),('A',(r-k,b),k)]
        seg += [('L',(x,b)) for x in sorted(set(bottom),reverse=True) if l+k<x<r-k]
        seg += [('L',(l+k,b)),('A',(l,b-k),k)]
        seg += [('L',(l,y)) for y in sorted(set(left),reverse=True) if t+k<y<b-k]
        seg += [('L',(l,t+k)),('A',(l+k,t),k)]
        self.path(n,(l+k,t),seg,True)

    def suitcase(self):
        # SQUARE: ink (4,4)-(44,44); centerlines (6,6)-(42,42).
        self.rect('case',6,14,42,42,4,top=(16,32))
        self.path('handle',(16,14),[('L',(16,10)),('A',(20,6),4),
            ('L',(28,6)),('A',(32,10),4),('L',(32,14))])
        self.relate('connect','case','handle')

    def check(self,n,x,y):
        self.add_polyline(n,(x,y),(x+3,y+3),(x+9,y-3))
'''

BODIES=[
'''# Case + handle + complete key: circular bow, shaft and two teeth.
        self.suitcase()
        self.circle('key-bow',18,28,3)
        self.add_polyline('key-shaft',(21,28),(24,28),(33,28),(33,24))
        self.add_line('inner-tooth',(24,28),(24,24))
        self.relate('connect','key-bow','key-shaft')
        self.relate('connect','key-shaft','inner-tooth')
''',
'''# The medical cross is reduced to its four centerline arms for legibility.
        self.suitcase()
        c=(24,28)
        for n,p in [('north',(24,23)),('south',(24,33)),('west',(19,28)),('east',(29,28))]:
            self.add_line(n,c,p)
        self.relate('connect','north','south','west','east')
''',
'''# A diagonal capsule with an explicit midpoint seam; both halves retained.
        self.suitcase()
        self.add_bezier('cap-low',(19,25),((15,29),(21,35),(25,31)))
        self.add_line('side-low',(25,31),(27,29))
        self.add_line('side-low-upper',(27,29),(29,27))
        self.add_bezier('cap-high',(29,27),((33,23),(27,17),(23,21)))
        self.add_line('side-high',(23,21),(21,23))
        self.add_line('side-high-lower',(21,23),(19,25))
        self.add_contour('pill','cap-low','side-low','side-low-upper','cap-high','side-high','side-high-lower',closed=True)
        self.add_line('pill-seam',(21,23),(27,29))
        self.relate('connect','pill','pill-seam')
''',
'''# Landscape frame, large mountain, smaller rear mountain, separate sun.
        self.rect('frame',6,6,42,42,4,right=(35,),bottom=(36,))
        self.add_polyline('mountain',(6,38),(20,26),(29,35),(36,42))
        self.add_polyline('rear-mountain',(29,35),(36,29),(42,35))
        self.relate('connect','frame','mountain')
        self.relate('connect','frame','rear-mountain')
        self.relate('connect','mountain','rear-mountain')
        self.circle('sun',30,18,3)
''',
'''# Console silhouette with screen, two left controls and two right buttons.
        # HRECT_M centerlines (4,10)-(44,38).
        self.rect('console',4,10,44,38,7)
        self.add_polyline('screen',(18,18),(30,18),(30,30),(18,30),closed=True)
        self.add_polyline('upper-control',(10,20),(12,20),(12,17))
        self.add_polyline('plus-v',(11,26),(11,28),(11,30))
        self.add_line('plus-h-left',(9,28),(11,28))
        self.add_line('plus-h-right',(11,28),(13,28))
        self.relate('connect','plus-v','plus-h-left','plus-h-right')
        for i,y in enumerate((19,29)): self.circle(f'button-{i}',37,y,2)
''',
'''# Pin above a split orbit, with a right-facing lower orbit arrow.
        # VRECT_L centerlines (8,4)-(40,44).
        self.add_arc('pin-crown',(12,16),(36,16),radius_x=12)
        self.add_bezier('pin-right',(36,16),((36,23),(28,30),(24,32)))
        self.add_bezier('pin-left',(24,32),((20,30),(12,23),(12,16)))
        self.add_contour('pin','pin-crown','pin-right','pin-left',closed=True)
        self.circle('pin-center',24,16,3)
        self.add_bezier('orbit-left-top',(10,32),((9,32),(8,33),(8,34)))
        self.add_bezier('orbit-left-bottom',(8,34),((8,38),(14,40),(20,40)))
        self.add_contour('orbit-left','orbit-left-top','orbit-left-bottom')
        self.add_polyline('orbit-arrow',(15,36),(20,40),(15,44))
        self.relate('connect','orbit-left','orbit-arrow')
        self.add_bezier('orbit-right-top',(38,32),((39,32),(40,33),(40,34)))
        self.add_bezier('orbit-right-bottom',(40,34),((40,36),(37,38),(33,39)))
        self.add_contour('orbit-right','orbit-right-top','orbit-right-bottom')
''',
'''# Empty horizontal tab, rounded at the back with a deliberate pointed tip.
        # HRECT_M centerline extremes (4,10)-(44,38).
        self.path('tab',(8,10),[('L',(32,10)),('L',(44,24)),('L',(32,38)),
            ('L',(8,38)),('A',(4,34),4),('L',(4,14)),('A',(8,10),4)],True)
''',
'''# Two overlapping blank panels; hidden portions of the rear panel are omitted.
        self.rect('front',6,6,34,34,4,right=(14,),bottom=(14,))
        self.path('rear',(34,14),[('L',(38,14)),('A',(42,18),4),('L',(42,38)),
            ('A',(38,42),4),('L',(18,42)),('A',(14,38),4),('L',(14,34))])
        self.relate('connect','front','rear')
''',
'''# Upright empty pointed tag, matching the source's pentagonal silhouette.
        # VRECT_M centerlines (10,4)-(38,44).
        self.path('tag',(24,4),[('L',(38,17)),('L',(38,40)),('A',(34,44),4),
            ('L',(14,44)),('A',(10,40),4),('L',(10,17)),('L',(24,4))],True)
''',
'''# Diagonal price tag with a circular punch hole and the complete yuan sign.
        self.add_polyline('tag',(6,28),(28,6),(42,6),(42,22),(22,42),closed=True)
        self.circle('hole',32,16,3)
        self.add_polyline('yuan-fork',(17,23),(21,28),(25,23))
        self.add_polyline('yuan-stem',(21,28),(21,34),(21,36))
        for n,y in [('upper',28),('lower',34)]:
            self.add_polyline(n,(18,y),(21,y),(24,y))
            self.relate('connect',n,'yuan-stem')
        self.relate('connect','yuan-fork','yuan-stem','upper')
''',
'''# Two complete tag silhouettes in overlap, with the rear exposed on top/right.
        self.add_polyline('front',(6,14),(14,14),(18,14),(36,32),(26,42),(6,28),closed=True)
        self.add_polyline('rear',(14,14),(14,6),(26,6),(42,22),(42,26),(36,32))
        self.relate('connect','front','rear')
        self.circle('hole',15,23,3)
''',
'''# Front tag has the distinctive inward shoulder and short pointed lower tail.
        self.add_polyline('front',(6,14),(20,14),(38,32),(31,35),(28,42),(6,28),closed=True)
        self.add_polyline('rear',(12,6),(24,6),(42,24),(42,28),(38,32))
        self.relate('connect','front','rear')
        self.circle('hole',15,23,3)
''',
'''# Standard diagonal front tag, without the notched shoulder of the other UUID.
        self.add_polyline('front',(6,14),(20,14),(38,32),(28,42),(6,28),closed=True)
        self.add_polyline('rear',(12,6),(24,6),(42,24),(42,28),(38,32))
        self.relate('connect','front','rear')
        self.circle('hole',15,23,3)
''',
'''# Four equal vertical tally strokes and one slash with exact shared junctions.
        points=[(6,34)]
        for i,x in enumerate((10,20,30,40)):
            y=37-x//2; p=(x,y); points.append(p)
            self.add_polyline(f'tally-{i}',(x,6),p,(x,42))
        points.append((42,16))
        self.add_polyline('slash',*points)
        for i in range(4): self.relate('connect',f'tally-{i}','slash')
''',
'''# Diagonal tampon, lower connector, trailing string and separate blood drop.
        self.add_line('body-left',(14,22),(26,10))
        self.add_bezier('cap-left',(26,10),((28,8),(28,6),(30,6)))
        self.add_bezier('cap-right',(30,6),((36,6),(37,12),(33,16)))
        self.add_line('body-right',(33,16),(21,28))
        self.add_bezier('body-end',(21,28),((19,30),(12,24),(14,22)))
        self.add_contour('tampon','body-left','cap-left','cap-right','body-right','body-end',closed=True)
        self.add_polyline('connector',(14,22),(10,27),(13,30),(18,27))
        self.relate('connect','tampon','connector')
        self.add_bezier('string',(10,27),((4,32),(10,37),(6,42)))
        self.relate('connect','connector','string')
        self.add_bezier('drop-right',(37,25),((40,29),(42,33),(42,36)),((42,42),(30,42),(30,36)))
        self.add_bezier('drop-left',(30,36),((30,32),(34,28),(37,25)))
        self.add_contour('blood-drop','drop-right','drop-left',closed=True)
''',
'''# Upright outlined person on a dashed bending route and a rightward arrow.
        # human_ref/full_body_ref.png informs the round head and simple limb vocabulary.
        # Head bottom 12 and shoulder crest 20 give exactly 4 units of visible gap.
        self.circle('head',24,9,3)
        self.path('body',(20,33),[('L',(20,30)),('L',(19,28)),('L',(19,25)),
            ('A',(24,20),5),('A',(29,25),5),('L',(29,28)),('L',(28,30)),('L',(28,33))])
        self.add_bezier('route-top',(10,24),((9,24),(8,25),(8,26)))
        self.add_arc('route-left',(6,34),(8,38),radius_x=8,sweep=False)
        self.add_line('route-bottom',(16,42),(20,42))
        self.add_line('route-dash',(28,42),(30,42))
        self.add_polyline('arrow-head',(38,22),(42,26),(38,30))
        self.add_line('arrow-shaft',(38,26),(42,26))
        self.relate('connect','arrow-head','arrow-shaft')
''',
'''# Two stacked task sheets, two checkmarks and three short text lines.
        self.rect('front',14,14,42,42,3,top=(34,),left=(34,))
        self.path('rear',(14,34),[('L',(10,34)),('A',(6,30),4),('L',(6,10)),
            ('A',(10,6),4),('L',(30,6)),('A',(34,10),4),('L',(34,14))])
        self.relate('connect','front','rear')
        for i,y in enumerate((23,32)): self.check(f'check-{i}',20,y)
        for i,y in enumerate((20,28,36)): self.add_line(f'text-{i}',(34,y),(36,y))
''',
'''# Folded note with three lines and a round-headed diagonal pin.
        self.path('paper',(22,6),[('L',(10,6)),('A',(6,10),4,False),
            ('L',(6,42)),('L',(30,42)),('L',(38,34)),('L',(38,24))])
        self.path('fold',(30,42),[('L',(30,38)),('A',(34,34),4),('L',(38,34))])
        self.relate('connect','paper','fold')
        self.add_arc('pin-a',(34,15),(40,7),radius_x=5)
        self.add_arc('pin-b',(40,7),(34,15),radius_x=5)
        self.add_contour('pin-head','pin-a','pin-b',closed=True)
        self.add_line('pin-stem',(34,15),(30,19))
        self.relate('connect','pin-head','pin-stem')
        for i,(y,end) in enumerate(((17,21),(25,24),(33,21))):
            self.add_line(f'text-{i}',(15,y),(end,y))
''',
'''# Clipboard, rounded clip crown, two checked rows and two diagonal text strokes.
        self.path('board',(16,14),[('L',(10,14)),('A',(6,18),4,False),('L',(6,38)),
            ('A',(10,42),4,False),('L',(38,42)),('A',(42,38),4,False),
            ('L',(42,18)),('A',(38,14),4,False),('L',(32,14))])
        self.path('clip',(16,14),[('L',(16,10)),('L',(20,10)),('A',(28,10),4),
            ('L',(32,10)),('L',(32,14)),('L',(32,18)),('L',(16,18)),('L',(16,14))],True)
        self.relate('connect','board','clip')
        for i,y in enumerate((26,35)):
            self.add_polyline(f'check-{i}',(14,y),(17,y+2),(23,y-3))
            self.add_line(f'text-{i}',(31,y+1),(34,y-2))
''',
'''# Bowl-shaped cup, open handle, saucer line and complete leaf emblem.
        # HRECT_M centerlines (4,10)-(44,38).
        self.add_polyline('rim',(6,20),(6,10),(34,10),(34,12),(34,22))
        self.add_arc('bowl-right',(34,22),(20,38),radius_x=14,radius_y=16)
        self.add_arc('bowl-left',(20,38),(6,20),radius_x=14,radius_y=18)
        self.add_contour('cup','rim-1','rim-2','rim-3','rim-4','bowl-right','bowl-left',closed=True)
        self.path('handle',(34,12),[('L',(39,12)),('A',(44,17),5),('A',(39,22),5),('L',(34,22))])
        self.relate('connect','cup','handle')
        self.add_polyline('saucer',(4,38),(20,38),(36,38))
        self.relate('connect','cup','saucer')
        self.add_bezier('leaf-upper',(13,31),((10,20),(20,16),(27,17)))
        self.add_bezier('leaf-lower',(27,17),((28,25),(21,32),(13,31)))
        self.add_contour('leaf','leaf-upper','leaf-lower',closed=True)
        self.add_line('leaf-stem',(11,33),(13,31))
        self.relate('connect','leaf','leaf-stem')
'''
]

KEYSHAPES=['SQUARE']*20
for i in (4,6,19):KEYSHAPES[i]='HRECT_M'
KEYSHAPES[8]='VRECT_M'
KEYSHAPES[5]='VRECT_L'

def author():
    for i,(row,body) in enumerate(zip(INPUTS,BODIES)):
        if 'result_dir' not in row:continue
        d=Path(row['result_dir'])
        if (d/'result.json').exists():continue
        # Reproducible modules remain entirely independent of this runner.
        code=f'''"""{row['concept'].capitalize()}, drawn from its complete supplied reference.
Symbol plan: preserve the subject, nested symbols, repeats and intentional overlaps.
Each repeated part and rounded rectangle owns its parameters and attachment nodes.
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

    def build(self):
        {body}
{HELPERS}
'''
        if i==19:
            code=code.replace("self.add_polyline('rim',(6,20),(6,10),(34,10),(34,12),(34,22))", "self.add_line('rim-1',(6,20),(6,10))\n        self.add_line('rim-2',(6,10),(34,10))\n        self.add_line('rim-3',(34,10),(34,12))\n        self.add_line('rim-4',(34,12),(34,22))")
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
    for start in (0,10):
        sheet=Image.new('RGB',(1000,780),'#dddddd');dr=ImageDraw.Draw(sheet)
        for j,row in enumerate(INPUTS[start:start+10]):
            if 'result_dir'not in row:continue
            d=Path(row['result_dir']);x=j%5*200;y=j//5*390
            for filename,dx,dy in [('reference-192.png',4,20),('light-192.png',4,190),('light-48.png',6,338),('dark-48.png',68,338)]:
                if not (d/filename).exists():continue
                im=Image.open(d/filename).convert('RGBA')
                if '192' in filename:im.thumbnail((150,150))
                sheet.paste(im,(x+dx,y+dy),im)
            dr.text((x+3,y+3),f'{start+j+1}. '+row['concept'],fill='black')
        sheet.save(ROOT/f'comparison-{start//10+1}.png')
    sheet=Image.new('RGB',(1000,1056),'#181818');dr=ImageDraw.Draw(sheet)
    for i,row in enumerate(INPUTS):
        if 'result_dir'not in row:continue
        d=Path(row['result_dir']);x=i%5*200;y=i//5*264
        if not (d/'dark-192.png').exists():continue
        sheet.paste(Image.open(d/'dark-192.png'),(x,y));sheet.paste(Image.open(d/'dark-48.png'),(x+72,y+192));dr.text((x+5,y+246),str(i+1)+' '+row['concept'],fill='white')
    sheet.save(ROOT/'dark-review.png')

if __name__=='__main__':
    author();sheets()
