"""Standalone batch 20; writes only newly created run folders from batch-inputs.json."""
from pathlib import Path
import json,importlib.util
import cairosvg
from PIL import Image,ImageDraw,ImageOps
SOURCE_ICON_ID='177bdc8f-a349-4eb2-9256-4dda4aaf2d56'
SOURCE_PATH='icon_set/work/todo-references/house bulb_177bdc8f-a349-4eb2-9256-4dda4aaf2d56.svg'
AUTHOR='gpt-6'
BASE=Path(__file__).parent
ROWS=json.loads((BASE/'batch-inputs.json').read_text())
HELPERS="""
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def house(self):
        # One mirrored envelope, x=24 axis; centerline extremes 6,6,42,42.
        self.add_polyline('roof',(6,22),(24,6),(42,22))
        self.add_line('wall-right',(42,22),(42,40))
        self.add_arc('corner-right',(42,40),(40,42),radius_x=2)
        self.add_line('floor',(40,42),(8,42))
        self.add_arc('corner-left',(8,42),(6,40),radius_x=2)
        self.add_line('wall-left',(6,40),(6,22))
        self.add_contour('house','roof-1','roof-2','wall-right','corner-right','floor','corner-left','wall-left',closed=True)

    def lock_body(self):
        # Shared shackle nodes are vertices in the top rail.
        self.add_polyline('lock-body',(17,26),(19,26),(29,26),(31,26),(31,34),(17,34),closed=True)
"""
DESIGNS={
1:('SQUARE','A house encloses a light bulb.','Small base divider omitted because its short parallel gap cannot meet SOLO48.',"""
        self.house()
        self.add_arc('bulb-crown',(18,24),(30,24),radius_x=6)
        self.add_bezier('bulb-right',(30,24),((30,28),(28,28),(28,31)))
        self.add_polyline('bulb-base',(28,31),(28,34),(20,34),(20,31))
        self.add_bezier('bulb-left',(20,31),((20,28),(18,28),(18,24)))
        self.add_contour('bulb','bulb-crown','bulb-right','bulb-base-1','bulb-base-2','bulb-base-3','bulb-left',closed=True)
"""),
2:('SQUARE','A dollar symbol is centered inside a house.','None; S curve and currency stem retained.',"""
        self.house()
        self.add_bezier('s-top',(29,21),((18,17),(16,26),(24,27)))
        self.add_bezier('s-bottom',(24,27),((34,28),(30,36),(19,32)))
        self.add_contour('currency-s','s-top','s-bottom')
        self.add_polyline('currency-stem',(24,18),(24,27),(24,34))
        self.relate('connect','currency-s','currency-stem')
"""),
3:('SQUARE','A pointed water drop sits inside a house.','None.',"""
        self.house()
        self.add_bezier('drop-right',(24,18),((27,23),(31,26),(31,28)),((31,32),(28,34),(24,34)))
        self.add_bezier('drop-left',(24,34),((20,34),(17,32),(17,28)),((17,26),(21,23),(24,18)))
        self.add_contour('drop','drop-right','drop-left',closed=True)
"""),
4:('SQUARE','An almond-shaped eye is centered inside a house.','Subpixel central speck in the reference omitted; no substantial pupil outline appears in the reference.',"""
        self.house()
        x,y=24,27
        self.add_bezier('eye-upper',(x-10,y),((x-4,y-8),(x+4,y-8),(x+10,y)))
        self.add_bezier('eye-lower',(x+10,y),((x+4,y+8),(x-4,y+8),(x-10,y)))
        self.add_contour('eye','eye-upper','eye-lower',closed=True)
"""),
6:('SQUARE','A curved leaf and its diagonal vein are contained in a house.','None.',"""
        self.house()
        self.add_bezier('leaf-top',(16,33),((11,22),(24,24),(32,19)))
        self.add_bezier('leaf-bottom',(32,19),((34,32),(25,37),(16,33)))
        self.add_contour('leaf','leaf-top','leaf-bottom',closed=True)
        self.add_polyline('vein',(14,35),(16,33),(25,27))
        self.relate('connect','leaf','vein')
"""),
7:('SQUARE','A closed padlock sits inside a house.','Corner fillets reduced to round joins.',"""
        self.house();self.lock_body()
        self.add_line('shackle-left',(19,26),(19,23))
        self.add_arc('shackle-top',(19,23),(29,23),radius_x=5)
        self.add_line('shackle-right',(29,23),(29,26))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','shackle','lock-body')
"""),
8:('SQUARE','A beamed pair of music notes fills a house.','None; paired heads and rising beam retained.',"""
        self.house()
        for n,x,y in [('left',18,32),('right',30,30)]:
            self.circle(n+'-note',x,y,3)
        self.add_polyline('beam',(21,32),(21,22),(33,19),(33,30))
        self.relate('connect','beam','left-note')
        self.relate('connect','beam','right-note')
"""),
9:('SQUARE','Three rounded toe pads and a triangular paw pad sit inside a house.','None; the reference uses three toes and a triangular lower pad.',"""
        self.house()
        for n,x,y in [('left',16,25),('top',24,19),('right',32,25)]:self.circle(n,x,y,2)
        self.add_polyline('pad',(24,28),(18,35),(30,35),closed=True)
"""),
10:('SQUARE','A diagonal telephone receiver appears inside a house.','Tiny receiver corner fillets merged into coherent curves.',"""
        self.house()
        self.add_bezier('receiver',(16,20),((12,24),(20,34),(29,34)),((32,34),(34,31),(32,29)))
        self.add_polyline('end-right',(32,29),(29,26),(25,29))
        self.add_bezier('inside',(25,29),((22,27),(21,26),(19,24)))
        self.add_polyline('end-left',(19,24),(22,21),(18,18),(16,20))
        self.add_contour('phone','receiver','end-right-1','end-right-2','inside','end-left-1','end-left-2','end-left-3',closed=True)
"""),
11:('SQUARE','An open power ring and vertical switch mark sit inside a house.','Upper ring shoulders simplified into vertical tangents.',"""
        self.house()
        self.add_line('ring-left',(15,22),(15,25))
        self.add_arc('ring-bottom',(15,25),(33,25),radius_x=9,sweep=False)
        self.add_line('ring-right',(33,25),(33,22))
        self.add_contour('power-ring','ring-left','ring-bottom','ring-right')
        self.add_line('power-stem',(24,18),(24,25))
"""),
12:('SQUARE','A liquid thermometer is contained inside a house.','None; tube, bulb and mercury stroke retained.',"""
        self.house()
        self.add_arc('cap',(20,22),(28,22),radius_x=4)
        self.add_line('tube-right',(28,22),(28,27))
        self.add_bezier('bulb',(28,27),((34,34),(14,38),(20,27)))
        self.add_line('tube-left',(20,27),(20,22))
        self.add_contour('thermometer','cap','tube-right','bulb','tube-left',closed=True)
        self.add_line('mercury',(24,22),(24,30))
"""),
13:('SQUARE','An open padlock sits inside a house.','Body corner fillets reduced to round joins.',"""
        self.house();self.lock_body()
        self.add_line('shackle-left',(19,26),(19,23))
        self.add_arc('shackle-top',(19,23),(29,23),radius_x=5)
        self.add_contour('open-shackle','shackle-left','shackle-top')
        self.relate('connect','open-shackle','lock-body')
"""),
14:('SQUARE','A four-bladed ventilation fan is inside a house.','None; all four blades and hub retained.',"""
        self.house();self.circle('hub',24,27,2)
        # Four identical curved blades, quarter-turn series around shared hub.
        for i in range(4):
            def rot(p):
                x,y=p[0]-24,p[1]-27
                for _ in range(i):x,y=-y,x
                return (24+x,27+y)
            n='blade-'+str(i)
            self.add_bezier(n,rot((24,25)),(rot((17,18)),rot((24,15)),rot((29,20))),(rot((31,23)),rot((26,24)),rot((26,27))))
            self.relate('connect',n,'hub')
"""),
15:('SQUARE','A circular play button is contained inside a house.','None; circular bezel and triangular play mark retained.',"""
        self.house();self.circle('button',24,27,8)
        self.add_polyline('play',(22,23),(28,27),(22,31),closed=True)
"""),
17:('CIRCLE','A prohibition ring and slash cross a delivery truck.','Small cab corner fillets and wheel hubs omitted.',"""
        self.circle('prohibition',24,24,20)
        self.add_polyline('cargo',(12,29),(12,18),(27,18),(27,29))
        self.add_polyline('cab',(27,21),(32,21),(36,27),(36,31),(34,31))
        self.relate('connect','cargo','cab')
        self.circle('wheel-left',17,31,2)
        self.circle('wheel-right',31,31,2)
        self.add_line('chassis',(19,31),(29,31))
        self.relate('connect','chassis','wheel-left')
        self.relate('connect','chassis','wheel-right')
        self.add_line('slash',(10,10),(38,38))
""")}

def author():
    for r in ROWS:
        if 'existing'in r:continue
        out=Path(r['directory']);key,subject,omit,body=DESIGNS[r['index']]
        module=r['icon_id'].replace('-','_')+'_'+r['source_uuid'].replace('-','_')+'.py'
        # Exclusive creation prevents replacement of any existing source.
        header=f"""\"\"\"{subject}
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 {key}; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: {omit}
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
    category='objects/buildings'
    aliases=()
    keywords={tuple(r['concept'].split())!r}
"""
        with (out/module).open('x') as f:f.write(header+HELPERS+'\n    def build(self):\n'+body)
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
