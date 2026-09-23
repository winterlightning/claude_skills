"""Batch 23: isolated SOLO48 authoring and local exports."""
from pathlib import Path
import json,importlib.util
import cairosvg
from PIL import Image,ImageDraw,ImageOps
SOURCE_ICON_ID='223c2cf3-707e-5588-bcee-3eb48df2972c'
SOURCE_PATH='icon_set/work/todo-references/lgbt love_223c2cf3-707e-5588-bcee-3eb48df2972c.svg'
AUTHOR='gpt-6'
BASE=Path(__file__).parent
ROWS=json.loads((BASE/'batch-inputs.json').read_text())
HELPERS="""
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def heart(self):
        # Shared bilateral lobe radius and mirrored flanks; exact square extremes.
        self.add_arc('lobe-left',(24,15),(6,15),radius_x=9,sweep=False)
        self.add_bezier('flank-left',(6,15),((6,28),(16,37),(24,42)))
        self.add_bezier('flank-right',(24,42),((32,37),(42,28),(42,15)))
        self.add_arc('lobe-right',(42,15),(24,15),radius_x=9,sweep=False)
        self.add_contour('heart','lobe-left','flank-left','flank-right','lobe-right',closed=True)

    def lens(self):
        # Circle at (21,21), radius 15. Shared handle node (30,33): 9²+12²=15².
        self.add_arc('lens-a',(30,33),(12,9),radius_x=15)
        self.add_arc('lens-b',(12,9),(30,33),radius_x=15)
        self.add_contour('lens','lens-a','lens-b',closed=True)
        self.add_line('handle',(30,33),(42,42))
        self.relate('connect','lens','handle')

    def envelope(self):
        # Complete card protruding from an open envelope; bilateral fold nodes.
        self.add_polyline('body',(6,24),(6,42),(42,42),(42,24))
        self.add_polyline('fold',(6,24),(18,32),(30,32),(42,24))
        self.relate('connect','body','fold')
        self.add_polyline('card',(10,27),(10,6),(38,6),(38,27))
        self.relate('connect','card','fold')
        self.add_line('seam-left',(18,32),(13,37))
        self.add_line('seam-right',(30,32),(35,37))
        self.relate('connect','seam-left','fold')
        self.relate('connect','seam-right','fold')
"""
DESIGNS={
1:('SQUARE','The word LOVE in a two-by-two layout, with a heart as the O.','Rounded V bottom reduced to a round joined vertex.',"""
        self.add_polyline('l',(6,6),(6,18),(18,18))
        self.add_arc('heart-left',(34,10),(26,10),radius_x=4,sweep=False)
        self.add_bezier('heart-bottom',(26,10),((26,13),(30,16),(34,18)),((38,16),(42,13),(42,10)))
        self.add_arc('heart-right',(42,10),(34,10),radius_x=4,sweep=False)
        self.add_contour('o-heart','heart-left','heart-bottom','heart-right',closed=True)
        self.add_polyline('v',(6,26),(12,42),(18,26))
        self.add_polyline('e',(42,26),(28,26),(28,34),(28,42),(42,42))
        self.add_line('e-middle',(28,34),(40,34));self.relate('connect','e','e-middle')
"""),
3:('SQUARE','A lion face with rounded inner muzzle inside a heart-shaped mane.','Fine facial marks omitted, as the reference has no separate eyes.',"""
        self.heart()
        self.add_bezier('face',(24,23),((21,13),(11,17),(15,25)),((17,27),(16,29),(17,31)),((19,35),(23,32),(24,30)),((26,35),(31,35),(32,30)),((32,28),(30,26),(32,24)),((37,17),(28,13),(24,23)))
        self.add_contour('muzzle','face',closed=True)
"""),
4:('VRECT_L','A padlock contains a user head and shoulders.','Head reduced to a small circular outline to preserve the exact detached gap.',"""
        self.add_polyline('body',(8,20),(14,20),(34,20),(40,20),(40,44),(32,44),(16,44),(8,44),closed=True)
        self.add_line('shackle-left',(14,20),(14,14))
        self.add_arc('shackle-top',(14,14),(34,14),radius_x=10)
        self.add_line('shackle-right',(34,14),(34,20))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right');self.relate('connect','body','shackle')
        self.circle('head',24,30,2)
        self.add_bezier('shoulders',(16,44),((16,40),(20,40),(24,40)),((28,40),(32,40),(32,44)))
        self.relate('connect','shoulders','body')
        # human_ref/user.svg: head bottom32, shoulder crest40 = 8 centerline / 4 ink.
"""),
5:('HRECT_L','An open door with a right-pointing logout arrow.','Tiny handle arrow simplified to one horizontal handle.',"""
        self.add_polyline('door',(4,12),(24,8),(24,24),(24,40),(4,36),closed=True)
        self.add_line('shaft',(24,24),(44,24))
        self.add_polyline('arrow',(36,16),(44,24),(36,32))
        self.relate('connect','door','shaft');self.relate('connect','shaft','arrow')
        self.add_line('door-handle',(12,24),(16,24))
"""),
7:('SQUARE','A heart encloses a classic round-topped keyhole.','None.',"""
        self.heart()
        self.add_arc('keyhole-top',(21,23),(27,23),radius_x=3)
        self.add_bezier('keyhole-right',(27,23),((27,24),(26,25),(25,25)))
        self.add_polyline('keyhole-base',(25,25),(27,32),(21,32),(23,25))
        self.add_bezier('keyhole-left',(23,25),((22,25),(21,24),(21,23)))
        # One contour, shared endpoints preserve the keyhole topology.
        self.add_contour('keyhole','keyhole-top','keyhole-right','keyhole-base-1','keyhole-base-2','keyhole-base-3','keyhole-left',closed=True)
"""),
9:('VRECT_M','An uppercase E denotes the EDGE mobile network.','None.',"""
        self.add_polyline('e',(38,4),(10,4),(10,24),(10,44),(38,44))
        self.add_line('middle',(10,24),(32,24));self.relate('connect','e','middle')
"""),
10:('HRECT_L','Rear view of a car with its luggage compartment symbol centered.','Short bumper ticks omitted; wheels remain paired.',"""
        self.add_polyline('car',(4,32),(4,22),(12,8),(36,8),(44,22),(44,32),(36,32),(12,32),(4,32))
        for n,x in [('left',10),('right',38)]:
            self.add_line(n+'-wheel-side',(x-3,32),(x-3,37))
            self.add_arc(n+'-wheel-round',(x-3,37),(x+3,37),radius_x=3,sweep=False)
            self.add_line(n+'-wheel-end',(x+3,37),(x+3,32))
            self.add_contour(n+'-wheel',n+'-wheel-side',n+'-wheel-round',n+'-wheel-end');self.relate('connect',n+'-wheel','car')
        self.add_polyline('luggage',(15,32),(15,22),(33,22),(33,32))
        self.relate('connect','luggage','car')
        self.add_arc('luggage-handle',(19,22),(29,22),radius_x=5)
        self.relate('connect','luggage-handle','luggage')
"""),
12:('CIRCLE','Two interlocking triangles form a six-pointed star within a circle.','None.',"""
        self.circle('circle',24,24,20)
        self.add_polyline('triangle-up',(24,4),(41,34),(7,34),closed=True)
        self.add_polyline('triangle-down',(24,44),(7,14),(41,14),closed=True)
"""),
13:('SQUARE','A round magnifying glass with a diagonal handle.','None.',"""
        self.lens()
"""),
14:('SQUARE','A magnifier contains a centered plus sign.','None.',"""
        self.lens()
        self.add_polyline('horizontal',(15,21),(21,21),(27,21))
        self.add_polyline('vertical',(21,15),(21,21),(21,27))
        self.relate('connect','horizontal','vertical')
"""),
15:('SQUARE','A diagonal two-part medicine capsule sits inside a magnifier.','None.',"""
        self.lens()
        self.add_line('pill-upper',(15,21),(21,15))
        self.add_bezier('pill-cap-right',(21,15),((26,10),(32,16),(27,21)))
        self.add_line('pill-lower',(27,21),(21,27))
        self.add_bezier('pill-cap-left',(21,27),((16,32),(10,26),(15,21)))
        self.add_contour('pill','pill-upper','pill-cap-right','pill-lower','pill-cap-left',closed=True)
        self.add_line('pill-seam',(18,18),(24,24));self.relate('connect','pill','pill-seam')
"""),
16:('SQUARE','A serif capital T sits inside a magnifier.','Short top serifs reduced to three-unit strokes.',"""
        self.lens()
        self.add_polyline('t-top',(14,17),(14,14),(21,14),(28,14),(28,17))
        self.add_line('t-stem',(21,14),(21,28))
        self.add_polyline('t-base',(18,28),(21,28),(24,28))
        self.relate('connect','t-top','t-stem');self.relate('connect','t-stem','t-base')
"""),
17:('SQUARE','A crescent moon accompanies Shiva’s trident and circular emblem.','Minor hooked tip curvature simplified; all symbolic components retained.',"""
        self.add_arc('moon-outer',(18,6),(18,26),radius_x=12,radius_y=10,sweep=False)
        self.add_bezier('moon-inner',(18,26),((9,19),(12,12),(18,6)))
        self.add_contour('moon','moon-outer','moon-inner',closed=True)
        self.add_line('shaft-upper',(32,6),(32,29))
        self.circle('emblem',32,35,6)
        self.relate('connect','shaft-upper','emblem')
        self.add_line('shaft-lower',(32,41),(32,42));self.relate('connect','shaft-lower','emblem')
        self.add_polyline('trident-bowl',(24,10),(24,23),(32,23),(40,23),(40,10))
        self.relate('connect','trident-bowl','shaft-upper')
        self.add_line('left-ray',(22,35),(26,35));self.add_line('right-ray',(38,35),(42,35))
        self.relate('connect','left-ray','emblem');self.relate('connect','right-ray','emblem')
"""),
18:('SQUARE','A blank card protrudes from an open envelope.','Small corner fillets reduced to round joins.',"""
        self.envelope()
"""),
19:('SQUARE','A card showing a bug protrudes from an open envelope.','Antennae and legs reduced to the reference’s six radial strokes.',"""
        self.envelope();self.circle('bug',24,19,4)
        self.add_line('bug-divider',(20,19),(28,19));self.relate('connect','bug','bug-divider')
        for side in (-1,1):
            for j,dy in enumerate((-5,0,5)):
                start=(24+side*4,19+dy)
                end=(24+side*7,19+dy*2)
                self.add_line('leg-'+str(side)+'-'+str(j),start,end)
"""),
}

def author():
    for r in ROWS:
        if 'existing' in r:continue
        out=Path(r['directory']);key,subject,omit,body=DESIGNS[r['index']]
        module=r['icon_id'].replace('-','_')+'_'+r['source_uuid'].replace('-','_')+'.py'
        text=f"""\"\"\"{subject}
Plan: semantic components use coherent contours, shared nodes, and mirrored or repeated definitions.
Keyshape {key}; full composition retained on SOLO48. Omissions: {omit}
\"\"\"
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={r['source_uuid']!r}
SOURCE_PATH={r['reference_path']!r}
AUTHOR={AUTHOR!r}
class Drawing(Solo48):
    icon_id={r['icon_id']!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords={tuple(r['concept'].split())!r}
"""
        with (out/module).open('x') as f:f.write(text+HELPERS+'\n    def build(self):\n'+body)
        r.update(module=module,keyshape=key,subject=subject,omissions=omit,author=AUTHOR)
    (BASE/'batch-inputs.json').write_text(json.dumps(ROWS,indent=2))
def export():
    sheet=Image.new('RGB',(1000,((len(ROWS)+3)//4)*210),'#dddddd');draw=ImageDraw.Draw(sheet)
    for j,r in enumerate(ROWS):
        if 'existing'in r:continue
        out=Path(r['directory']);p=out/r['module']
        spec=importlib.util.spec_from_file_location('drawing_'+str(j),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
        icon=m.Drawing();report=icon.validate_icon();r['validation_status']=report.status;r['validation_findings']=report.describe()
        (out/'validation.txt').write_text(report.describe());svg=icon.to_svg();(out/(r['icon_id']+'.svg')).write_text(svg)
        for size in (48,288):
            cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out/f'light-{size}.png'),output_width=size,output_height=size,background_color='white')
            ImageOps.invert(Image.open(out/f'light-{size}.png').convert('RGB')).save(out/f'dark-{size}.png')
        x=j%4*250;y=j//4*210
        for n,t in enumerate(('light','dark')):
            sheet.paste(Image.open(out/f'{t}-288.png').resize((120,120)),(x+n*120,y));sheet.paste(Image.open(out/f'{t}-48.png'),(x+n*120,y+125))
        draw.text((x,y+177),str(r['index'])+' '+r['icon_id'],fill='black');print(r['index'],report.describe(),flush=True)
    sheet.save(BASE/'review.png');(BASE/'batch-inputs.json').write_text(json.dumps(ROWS,indent=2))

if __name__=='__main__':
    import sys
    if '--export-only' not in sys.argv:author()
    export()
