"""Batch 29 standalone SOLO48 authoring; explicit new-folder manifest only."""
from pathlib import Path
import json,importlib.util
import cairosvg
from PIL import Image,ImageDraw,ImageOps
SOURCE_ICON_ID='a119cf45-d021-460f-b469-9d1f28774714'
SOURCE_PATH='icon_set/work/todo-references/multiple users wifi_a119cf45-d021-460f-b469-9d1f28774714.svg'
AUTHOR='gpt-6'
BASE=Path(__file__).parent
ROWS=json.loads((BASE/'batch-inputs.json').read_text())
HELPERS="""
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)
"""
DESIGNS={
1:('SQUARE','Three user busts sit beneath three Wi-Fi arcs.','Small side heads reduced to two-unit-radius circles.',"""
        # Series: three centered radio arcs. Shared human_ref/user.svg bust vocabulary.
        for i,(x,y,w) in enumerate([(10,12,28),(14,19,20),(18,25,12)]):
            self.add_arc('wifi-'+str(i),(x,y),(x+w,y),radius_x=w//2,radius_y=6)
        for n,x,y,r in [('center',24,30,3),('left',10,32,2),('right',38,32,2)]:
            self.circle(n+'-head',x,y,r)
        self.add_bezier('center-body',(16,42),((16,41),(20,41),(24,41)),((28,41),(32,41),(32,42)))
        self.add_bezier('left-body',(6,42),((6,42),(10,42),(16,42)))
        self.add_bezier('right-body',(32,42),((38,42),(42,42),(42,42)))
        self.relate('connect','center-body','left-body');self.relate('connect','center-body','right-body')
        # Head bottoms 33/34, shoulder crests41/42: each exact centerline gap8.
"""),
2:('SQUARE','A hand-cranked music box sits beneath a double-beamed pair of notes.','Box lid divider omitted; crank and double beam retained.',"""
        self.add_polyline('box',(6,34),(34,34),(34,38),(34,42),(6,42),closed=True)
        self.add_polyline('crank',(34,38),(42,38),(42,28))
        self.relate('connect','box','crank')
        self.circle('note-left',16,22,3);self.circle('note-right',28,20,3)
        self.add_polyline('beam',(19,22),(19,14),(19,6),(31,6),(31,14),(31,20))
        self.add_line('second-beam',(19,14),(31,14))
        self.relate('connect','beam','second-beam');self.relate('connect','beam','note-left');self.relate('connect','beam','note-right')
"""),
3:('VRECT_L','A dog-eared file contains a single flagged music note.','Fine page corner rounding reduced to round joins.',"""
        self.add_polyline('page',(8,4),(30,4),(40,14),(40,44),(8,44),closed=True)
        self.circle('note',21,32,3)
        self.add_line('stem',(24,32),(24,16));self.relate('connect','note','stem')
        self.add_bezier('flag',(24,16),((29,20),(33,22),(29,27)))
        self.relate('connect','stem','flag')
"""),
4:('SQUARE','A person gestures toward a pair of musical notes.','Outlined torso reduced to the shared human line vocabulary; both notes retained.',"""
        self.circle('head',16,12,6)
        self.add_line('torso',(16,26),(16,42))
        self.add_bezier('left-shoulder',(6,42),((6,30),(6,26),(16,26)))
        self.add_polyline('arm',(16,26),(26,32),(42,32))
        self.relate('connect','torso','left-shoulder');self.relate('connect','torso','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.circle('note-left',32,18,2);self.circle('note-right',40,16,2)
        self.add_polyline('beam',(34,18),(34,8),(42,6),(42,16))
        self.relate('connect','beam','note-left');self.relate('connect','beam','note-right')
"""),
5:('SQUARE','A hurricane spiral sweeps past a small house.','None; spiral and complete house retained.',"""
        self.add_bezier('tail',(6,30),((22,30),(34,24),(34,16)))
        self.add_arc('outer-coil',(34,16),(14,16),radius_x=10,sweep=False)
        self.add_arc('inner-coil',(14,16),(26,16),radius_x=6,sweep=False)
        self.add_bezier('core',(26,16),((26,11),(18,11),(20,18)))
        self.add_contour('hurricane','tail','outer-coil','inner-coil','core')
        self.add_polyline('house',(26,36),(26,42),(42,42),(42,36),(34,30),(26,36))
        self.add_polyline('roof',(24,36),(34,28),(42,34))
        self.add_polyline('door',(32,42),(32,36),(36,36),(36,42));self.relate('connect','door','house')
"""),
6:('SQUARE','Two upward arrows rise above waves of floodwater.','Middle wave row and enclosing basin sides omitted to retain clear water and rise directions.',"""
        for x in (16,32):
            self.add_line('stem-'+str(x),(x,18),(x,6))
            self.add_polyline('tip-'+str(x),(x-4,10),(x,6),(x+4,10));self.relate('connect','stem-'+str(x),'tip-'+str(x))
        for row,y in enumerate((26,39)):
            ids=[]
            for j,x in enumerate((6,18,30)):
                n=f'wave-{row}-{j}';ids.append(n);self.add_arc(n,(x,y),(x+12,y),radius_x=6,radius_y=3,sweep=False)
            self.add_contour('wave-'+str(row),*ids)
"""),
7:('HRECT_L','A broad left-pointing arrow bends upward from the right.','None.',"""
        self.add_polyline('arrow',(20,8),(12,16),(4,24),(12,32),(20,40))
        self.add_line('outer-top',(12,16),(28,16))
        self.add_arc('outer-bend',(28,16),(44,32),radius_x=16)
        self.add_line('outer-end',(44,32),(44,40))
        self.add_contour('outer','outer-top','outer-bend','outer-end')
        self.add_bezier('inner',(12,32),((32,32),(34,28),(44,40)))
        self.relate('connect','arrow','outer');self.relate('connect','arrow','inner');self.relate('connect','outer','inner')
"""),
8:('VRECT_L','Three rounded horizontal menu bars decrease in length.','Arrangement made taller so all three hollow bars keep eight-unit spacing.',"""
        for n,y,w in [('top',4,32),('middle',20,24),('bottom',36,16)]:self.box(n,8,y,w,8,4)
"""),
9:('HRECT_L','A return arrow points left beside an open rounded return path.','None.',"""
        self.add_polyline('arrowhead',(12,8),(4,16),(12,24))
        self.add_line('shaft',(4,16),(22,16))
        self.add_arc('bend',(22,16),(30,24),radius_x=8)
        self.add_line('end',(30,24),(30,31))
        self.add_contour('arrow','shaft','bend','end');self.relate('connect','arrowhead','arrow')
        self.add_line('return-right',(44,8),(44,36))
        self.add_arc('return-corner',(44,36),(40,40),radius_x=4)
        self.add_line('return-bottom',(40,40),(22,40))
        self.add_arc('return-left-corner',(22,40),(18,36),radius_x=4)
        self.add_line('return-left',(18,36),(18,26))
        self.add_contour('return','return-right','return-corner','return-bottom','return-left-corner','return-left')
"""),
10:('SQUARE','A location-message bubble overlaps a smartphone.','Small home-button tick omitted; phone divider retained.',"""
        self.add_polyline('phone',(30,14),(30,6),(6,6),(6,42),(30,42),(30,30))
        self.add_polyline('bubble',(16,14),(30,14),(42,14),(42,30),(30,30),(26,30),(20,36),(20,30),(16,30),closed=True)
        self.relate('connect','phone','bubble')
        self.add_line('divider',(6,34),(20,34));self.relate('connect','divider','phone')
        self.add_arc('pin-head',(25,22),(33,22),radius_x=4)
        self.add_bezier('pin-tip',(33,22),((33,25),(29,28),(29,28)),((29,28),(25,25),(25,22)))
        self.add_contour('pin','pin-head','pin-tip',closed=True)
"""),
11:('VRECT_L','A hooded necromancer has a featureless skull-like face and robe.','Small jaw corners simplified; faceless hooded composition retained.',"""
        self.add_bezier('hood-left',(24,4),((14,4),(8,16),(12,30)))
        self.add_polyline('hood-bottom',(12,30),(24,36),(36,30))
        self.add_bezier('hood-right',(36,30),((40,16),(34,4),(24,4)))
        self.add_contour('hood','hood-left','hood-bottom-1','hood-bottom-2','hood-right',closed=True)
        self.circle('face',24,20,7)
        self.add_bezier('robe-left',(8,44),((8,36),(8,32),(12,30)))
        self.add_bezier('robe-right',(36,30),((40,32),(40,36),(40,44)))
        self.add_line('robe-seam',(24,36),(24,44))
        self.relate('connect','hood','robe-left');self.relate('connect','hood','robe-right');self.relate('connect','hood','robe-seam')
"""),
12:('SQUARE','Crossed magic strokes float above a skull.','Skull jaw fillets simplified; eyes and two tooth divisions retained.',"""
        self.add_line('magic-a',(6,6),(24,10));self.add_line('magic-b',(24,10),(42,14))
        self.add_line('magic-c',(6,14),(24,10));self.add_line('magic-d',(24,10),(42,6))
        self.add_contour('magic-one','magic-a','magic-b');self.add_contour('magic-two','magic-c','magic-d');self.relate('connect','magic-one','magic-two')
        self.add_arc('skull-top',(12,30),(36,30),radius_x=12)
        self.add_polyline('jaw',(36,30),(36,34),(32,36),(32,42),(28,42),(20,42),(16,42),(16,36),(12,34),(12,30))
        self.relate('connect','skull-top','jaw')
        self.circle('eye-left',18,30,2);self.circle('eye-right',30,30,2)
        for x in (20,28):self.add_line('tooth-'+str(x),(x,38),(x,42));self.relate('connect','tooth-'+str(x),'jaw')
"""),
13:('SQUARE','A nectar bottle bears a five-petalled flower.','Bottle cap rounding simplified; all five petals retained.',"""
        self.add_polyline('cap',(10,6),(26,6),(26,14),(10,14),closed=True)
        self.add_polyline('bottle',(10,14),(6,22),(6,42),(30,42),(30,22),(26,14))
        self.relate('connect','cap','bottle')
        self.add_dot('flower-center',(34,21))
        petals=[((34,21),(27,15),(31,8),(35,14)),((34,21),(34,8),(44,12),(40,18)),((34,21),(44,15),(45,25),(39,25)),((34,21),(43,28),(34,33),(32,26)),((34,21),(24,30),(23,20),(29,20))]
        for i,(a,c1,c2,k) in enumerate(petals):
            n='petal-'+str(i);self.add_bezier(n,a,(c1,c2,k),(k,a,a));self.relate('connect',n,'flower-center')
"""),
14:('VRECT_M','A rounded netsuke figure has a circular head and crossed looping arms.','Minor hand contours simplified into one loop.',"""
        self.circle('head',24,11,7)
        self.add_arc('shoulders',(10,32),(38,32),radius_x=14,radius_y=10)
        self.add_line('right-side',(38,32),(38,40));self.add_arc('right-bottom',(38,40),(34,44),radius_x=4)
        self.add_line('right-base',(34,44),(28,44))
        self.add_contour('right-body','shoulders','right-side','right-bottom','right-base')
        self.add_line('left-side',(10,32),(10,40));self.add_arc('left-bottom',(10,40),(14,44),radius_x=4,sweep=False)
        self.add_contour('left-body','left-side','left-bottom');self.relate('connect','right-body','left-body')
        self.relate('connect','head','right-body')
        self.add_bezier('arms',(14,44),((20,43),(26,36),(28,33)),((34,23),(16,25),(24,32)),((26,34),(28,34),(28,33)))
        self.relate('connect','arms','left-body')
        # Bust rule: head bottom18 and shoulder crest22, exactly zero visible gap.
"""),
15:('SQUARE','5G lettering is framed by paired network brackets and side ticks.','None; hand-authored 5 and G plus all framing marks retained.',"""
        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            self.add_polyline('top-'+str(side),p(18,6),p(10,6),p(6,10))
            self.add_polyline('bottom-'+str(side),p(18,42),p(10,42),p(6,38))
            for y in (16,32):self.add_line('tick-'+str(side)+'-'+str(y),p(18,y),p(14,y))
        self.add_polyline('five-top',(20,18),(12,18),(12,25))
        self.add_bezier('five-bowl',(12,25),((24,19),(24,34),(12,30)))
        self.relate('connect','five-top','five-bowl')
        self.add_bezier('g',(36,20),((27,13),(25,33),(33,32)),((36,32),(36,29),(36,26)))
        self.add_line('g-bar',(36,26),(32,26));self.relate('connect','g','g-bar')
"""),
16:('CIRCLE','The Next.js N mark sits within a circle with its diagonal extending to the rim.','None.',"""
        self.add_arc('ring-a',(12,8),(36,40),radius_x=20);self.add_arc('ring-b',(36,40),(12,8),radius_x=20)
        self.add_contour('ring','ring-a','ring-b',closed=True)
        self.add_polyline('n',(16,32),(16,16),(28,30),(36,40))
        self.add_line('n-right',(28,16),(28,30));self.relate('connect','n','n-right');self.relate('connect','ring','n')
"""),
17:('SQUARE','A crescent moon rises above an upward arrow and horizon.','Moon lower edge is interrupted as in the reference; small tip curvature simplified.',"""
        self.add_bezier('moon',(12,30),((2,18),(10,6),(24,6)),((20,18),(30,26),(40,22)),((38,26),(36,28),(34,30)))
        self.add_line('horizon',(6,42),(42,42))
        self.add_line('rise',(24,38),(24,24))
        self.add_polyline('rise-tip',(18,30),(24,24),(30,30));self.relate('connect','rise','rise-tip')
"""),
18:('SQUARE','Four musical notes rise over a nightclub building with an arched doorway.','Building cornice rounding omitted; both note pairs retained.',"""
        self.add_polyline('cornice',(6,22),(42,22),(42,30),(40,30),(8,30),(6,30),closed=True)
        self.add_polyline('building',(8,30),(8,42),(18,42),(30,42),(40,42),(40,30));self.relate('connect','building','cornice')
        self.add_line('door-left',(18,42),(18,37));self.add_arc('door-top',(18,37),(30,37),radius_x=6);self.add_line('door-right',(30,37),(30,42))
        self.add_contour('door','door-left','door-top','door-right');self.relate('connect','door','building')
        for j,x in enumerate((10,30)):
            self.circle('note-'+str(j)+'-left',x,17,2);self.circle('note-'+str(j)+'-right',x+8,15,2)
            n='beam-'+str(j);self.add_polyline(n,(x+2,17),(x+2,8),(x+10,6),(x+10,15))
            self.relate('connect',n,'note-'+str(j)+'-left');self.relate('connect',n,'note-'+str(j)+'-right')
"""),
19:('SQUARE','A car emits jagged noise marks beneath a lightning bolt.','Fine body rounding and window divider omitted; wheels and sound marks retained.',"""
        self.add_polyline('bolt',(26,6),(18,16),(25,16),(23,22),(33,12),(26,12),closed=True)
        self.add_polyline('noise-left',(6,18),(10,22),(12,20),(15,23))
        self.add_polyline('noise-right',(42,14),(38,18),(41,21),(38,24))
        self.circle('wheel-left',14,39,3);self.circle('wheel-right',34,39,3)
        self.add_bezier('front',(11,39),((6,39),(6,34),(14,32)))
        self.add_polyline('roof',(14,32),(18,28),(30,28),(34,32))
        self.add_bezier('rear',(34,32),((42,32),(42,39),(37,39)))
        self.add_line('chassis',(17,39),(31,39))
        self.relate('connect','front','wheel-left');self.relate('connect','front','roof');self.relate('connect','roof','rear');self.relate('connect','rear','wheel-right')
        self.relate('connect','chassis','wheel-left');self.relate('connect','chassis','wheel-right')
"""),
}

def author():
    for r in ROWS:
        if 'existing'in r:continue
        out=Path(r['directory']);key,subject,omit,body=DESIGNS[r['index']]
        module=r['icon_id'].replace('-','_')+'_'+r['source_uuid'].replace('-','_')+'.py'
        text=f"""\"\"\"{subject}
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 {key}; omissions: {omit}
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
        if r['index']==14:text+="    human_construction='bust'\n"
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
