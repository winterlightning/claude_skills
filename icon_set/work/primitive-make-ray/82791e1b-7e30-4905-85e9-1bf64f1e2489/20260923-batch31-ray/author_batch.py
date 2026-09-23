from pathlib import Path
import json, importlib.util
import cairosvg
from PIL import Image, ImageDraw, ImageOps

SOURCE_ICON_ID = '82791e1b-7e30-4905-85e9-1bf64f1e2489'
SOURCE_PATH = 'icon_set/work/todo-references/online learning online course 2_82791e1b-7e30-4905-85e9-1bf64f1e2489.svg'
AUTHOR = 'gpt-6'
ROOT = Path(__file__).parent
ROWS = json.loads((ROOT/'batch.json').read_text())
HELPERS = '''
    def circle(self, n, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(n+'-a', (x-r,y), (x+r,y), radius_x=r, radius_y=ry)
        self.add_arc(n+'-b', (x+r,y), (x-r,y), radius_x=r, radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=3):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for j,a in enumerate(points):
            b=points[(j+1)%8];name=f'{n}-{j}';names.append(name)
            if j%2: self.add_arc(name,a,b,radius_x=r)
            else: self.add_line(name,a,b)
        self.add_contour(n,*names,closed=True)

    def p(self,n,x,y,w,h):
        # Open P stem and a tangent semicircular bowl share the upper node.
        self.add_line(n+'-stem-1',(x,y+h),(x,y))
        self.add_line(n+'-stem-2',(x,y),(x+w//2,y))
        self.add_arc(n+'-bowl',(x+w//2,y),(x+w//2,y+h//2),radius_x=w//2,radius_y=h//4)
        self.add_line(n+'-return',(x+w//2,y+h//2),(x,y+h//2))
        self.add_contour(n,n+'-stem-1',n+'-stem-2',n+'-bowl',n+'-return')
'''
# Each entry owns its symbol arrangement and keyshape; no reference coordinates are imported.
DESIGNS = [
('SQUARE','book-open','Open book over a course input panel; shared centre fold and mirrored pages.','Page curves simplified; input dash omitted because the shallow panel cannot hold another separated stroke.', '''
        axis=24
        self.add_polyline('book',(10,6),(18,6),(axis,10),(30,6),(38,6),(38,22),(30,22),(axis,26),(18,22),(10,22),closed=True)
        self.add_line('fold',(axis,10),(axis,26))
        self.relate('connect','fold','book')
        self.box('panel',6,34,36,8,2)
'''),
('CIRCLE',None,'OpenVPN circular arch around a keyhole; bilateral logo silhouette.','Logo fill translated to consistent outline.', '''
        self.add_arc('ring',(8,36),(40,36),radius_x=20,large_arc=True)
        self.add_arc('key-head',(20,26),(28,26),radius_x=6,large_arc=True)
        self.add_polyline('key-base',(28,26),(31,40),(17,40),(20,26))
        self.relate('connect','key-head','key-base')
'''),
('SQUARE','house','Dog standing under an open sloped kennel roof; intentional side profile.','Far legs and belly stroke omitted to keep the near legs distinct.', '''
        self.add_polyline('kennel',(42,6),(6,16),(6,42),(42,42))
        self.add_polyline('dog',(14,34),(14,27),(18,24),(28,24),(33,19),(34,23),(40,25),(37,29),(31,29),(29,34))
        # Open lower silhouette retains the two leg ends.
'''),
('VRECT_L','flame','A camp flame above a segmented brick fire pit.','Six bricks reduced to two blocks to retain open spacing.', '''
        self.add_bezier('flame',(24,4),((26,13),(36,16),(32,22)),((29,29),(18,29),(16,22)),((13,17),(17,13),(18,12)),((19,19),(24,16),(24,4)))
        self.box('pit',8,36,32,8,2)
        self.add_line('joint',(24,36),(24,44))
        self.relate('connect','joint','pit')
'''),
('SQUARE',None,'A pig snout reaches toward an apple poster; asymmetry preserves the scene.','Eye and tiny ear folds omitted.', '''
        self.add_polyline('poster',(24,17),(24,6),(42,6),(42,42),(24,42),(24,34))
        self.add_bezier('pig',(6,18),((6,11),(12,13),(14,21)),((18,22),(19,26),(24,26)),((27,26),(27,33),(22,33)),((15,34),(12,37),(8,42)))
        self.add_bezier('apple',(33,23),((23,16),(26,34),(33,32)),((40,34),(43,16),(33,23)))
        self.add_line('stem',(33,23),(35,17))
        self.relate('connect','stem','apple')
'''),
('SQUARE','house','A small outpost hut behind a front security terminal.','Terminal dash omitted to keep the small opening clear.', '''
        self.add_polyline('roof',(6,20),(8,18),(24,6),(40,18),(42,20))
        for side,x in [('left',8),('right',40)]: self.add_line(side,(x,18),(x,34)); self.relate('connect',side,'roof')
        self.box('terminal',17,26,14,16,3)
        self.add_line('screen-rule',(17,34),(31,34));self.relate('connect','screen-rule','terminal')
'''),
('SQUARE',None,'An oxygen cylinder with top valve and an offset timer gauge.','Gauge numerals omitted.', '''
        self.box('tank',6,18,16,24,8)
        self.add_polyline('valve',(10,18),(10,10),(18,10),(18,18))
        # Valve contact remains uncertified in this dense candidate.
        self.add_line('stem',(14,10),(14,6));self.add_line('handle',(10,6),(18,6));self.relate('connect','stem','valve');self.relate('connect','stem','handle')
        self.circle('timer',34,14,8)
        self.add_polyline('hands',(34,10),(34,14),(38,14));
        self.add_line('hose',(18,10),(26,10));self.relate('connect','hose','valve')
'''),
('CIRCLE','palette','Circular painting palette with three circular wells in a triangular pattern.','No defining features omitted.', '''
        self.circle('rim',24,24,20)
        for n,x,y in [('top',24,16),('left',16,28),('right',32,28)]: self.circle(n,x,y,3)
'''),
('HRECT_L','image','Landscape picture frame with sun and two overlapping mountain peaks.','Fine slope extension simplified.', '''
        self.box('frame',4,8,40,32,4)
        self.circle('sun',15,19,2)
        self.add_polyline('mountains',(4,36),(16,30),(24,36),(33,23),(44,33))
        self.relate('connect','mountains','frame')
'''),
('VRECT_M',None,'Pantyhose with one straight leg and one bent leg in side view.','Toe and ankle folds simplified; asymmetry preserves the crossed pose.', '''
        self.add_polyline('waist',(17,4),(28,4),(28,12))
        self.add_bezier('hips',(17,4),((16,10),(10,14),(15,19)),((18,22),(27,24),(32,26)))
        self.add_polyline('bent-leg',(28,12),(38,22),(20,35),(18,41),(26,44),(15,44),(10,36),(15,29),(24,24))
        self.add_polyline('back-leg',(15,19),(15,29))
        self.relate('connect','waist','hips');self.relate('connect','waist','bent-leg');self.relate('connect','hips','back-leg');self.relate('connect','back-leg','bent-leg')
'''),
('SQUARE','image','Text document with a small image aligned at the upper right.','Four text rows reduced to three.', '''
        self.box('frame',6,6,36,36,4)
        self.box('image',25,15,8,9,2)
        self.add_line('short',(15,20),(17,20))
        self.add_line('row',(15,33),(33,33))
'''),
('SQUARE',None,'A text direction T above a leftward arrow.','No defining features omitted.', '''
        self.add_line('bar',(14,6),(42,6))
        self.add_line('stem',(28,6),(28,24));self.relate('connect','bar','stem')
        self.add_polyline('arrow-head',(16,22),(6,32),(16,42))
        self.add_line('arrow-shaft',(6,32),(42,32));self.relate('connect','arrow-head','arrow-shaft')
'''),
('HRECT_M','square-parking','P plus B lettering for park and bike.','No letters omitted.', '''
        self.p('p',4,10,12,28)
        self.add_line('plus-h',(20,24),(28,24));self.add_line('plus-v',(24,20),(24,28));self.relate('connect','plus-h','plus-v')
        self.add_line('b-stem-1',(32,38),(32,10));self.add_line('b-stem-2',(32,10),(38,10))
        self.add_arc('b-upper',(38,10),(38,24),radius_x=6,radius_y=7)
        self.add_arc('b-lower',(38,24),(38,38),radius_x=6,radius_y=7)
        self.add_line('b-foot',(38,38),(32,38));self.add_contour('b','b-stem-1','b-stem-2','b-upper','b-lower','b-foot',closed=True)
        self.add_line('b-middle',(32,24),(38,24));self.relate('connect','b-middle','b')
'''),
('HRECT_M','square-parking','P plus R lettering for park and ride.','No letters omitted.', '''
        self.p('p',4,10,12,28)
        self.add_line('plus-h',(20,24),(28,24));self.add_line('plus-v',(24,20),(24,28));self.relate('connect','plus-h','plus-v')
        self.p('r',32,10,12,28)
        self.add_line('r-leg',(32,24),(44,38));self.relate('connect','r-leg','r')
'''),
('SQUARE','square-parking','Parking P emits two sensor waves toward a triangular obstacle.','No defining features omitted.', '''
        self.p('p',6,6,14,20)
        self.add_arc('wave-inner',(28,14),(20,28),radius_x=16)
        self.add_arc('wave-outer',(36,16),(26,34),radius_x=21)
        self.add_polyline('obstacle',(28,42),(35,26),(42,42),closed=True)
'''),
('SQUARE','square-parking','A car under an overlapping circular P parking badge.','Small bumper marks omitted.', '''
        self.circle('sign',30,18,12)
        self.p('p',27,12,8,12)
        self.add_polyline('car-roof',(6,32),(11,24),(18,24))
        self.box('car',6,32,28,10,3)
        self.add_line('right-roof',(30,30),(34,32));self.relate('connect','right-roof','sign');self.relate('connect','right-roof','car');self.relate('connect','car-roof','car')
'''),
('VRECT_M','square-parking','An open-bottom parking sign enclosing P.','No defining features omitted.', '''
        self.add_polyline('sign',(10,44),(10,4),(38,4),(38,44))
        self.p('letter',19,14,10,20)
'''),
('SQUARE','check','A checkmark inside a rounded square communicates pass.','No features omitted.', '''
        self.box('frame',6,6,36,36,5)
        self.add_polyline('check',(15,25),(22,32),(33,18))
'''),
('SQUARE','globe','Passport in front of a globe with a second globe on its cover.','Fine geographic border simplified; meridian count reduced.', '''
        self.add_arc('earth',(20,34),(34,20),radius_x=14,large_arc=True)
        self.add_polyline('land',(6,16),(16,16),(16,24),(12,26),(12,32))
        self.box('passport',24,18,18,24,3)
        self.circle('globe',33,29,7)
        self.add_line('equator',(26,29),(40,29));self.relate('connect','equator','globe')
        self.add_line('meridian',(33,22),(33,36));self.relate('connect','meridian','globe');self.relate('connect','meridian','equator')
'''),
('VRECT_L','globe','A passport booklet with top cover flap and a latitude-longitude globe.','Latitude bands reduced to one equator; curved meridians reduced to a central vertical meridian.', '''
        self.box('cover',8,4,32,40,3)
        self.add_line('flap',(8,12),(40,12));self.relate('connect','flap','cover')
        self.circle('globe',24,28,7)
        self.add_line('meridian',(24,21),(24,35));self.relate('connect','meridian','globe')
        self.add_line('equator',(17,28),(31,28));self.relate('connect','equator','globe');self.relate('connect','equator','meridian')
'''),
]

def run():
    for row,(key,lucide,plan,omissions,body) in zip(ROWS,DESIGNS):
        out=Path(row['out']); ident=row['icon_id']
        source=out/(ident.replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py')
        text=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = {AUTHOR!r}
PLAN = {plan!r}
OMISSIONS = {omissions!r}
LUCIDE_REFERENCE = {lucide!r}

class Drawing(Solo48):
    icon_id = {ident!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = {tuple(row['concept'].split())!r}
    # Pantyhose anatomy reference: icon_set/references/human_ref/full_body_ref.png; no detached head.
{HELPERS}
    def build(self):
        # Symbol plan: {plan}
{body}
'''
        source.write_text(text)
        spec=importlib.util.spec_from_file_location('candidate',source);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        icon=module.Drawing();report=icon.validate_icon();(out/'validation.txt').write_text(report.describe())
        svg=icon.to_svg();(out/(ident+'.svg')).write_text(svg)
        for size in (48,192):
            png=out/f'light-{size}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(png),output_width=size,output_height=size,background_color='white')
            ImageOps.invert(Image.open(png).convert('RGB')).save(out/f'dark-{size}.png')
        row.update(source=source.name,keyshape=key,validation_status=report.status,plan=plan,omissions=omissions,lucide=lucide)
        print(ident,report.status,flush=True)
    (ROOT/'attempts.json').write_text(json.dumps(ROWS,indent=2))
    for start in (0,10):
        sheet=Image.new('RGB',(1000,580),'#cccccc');draw=ImageDraw.Draw(sheet)
        for j,row in enumerate(ROWS[start:start+10]):
            x=j%5*200;y=j//5*290;out=Path(row['out'])
            for theme,dx in [('light',0),('dark',100)]:
                im=Image.open(out/f'{theme}-192.png').resize((96,96));sheet.paste(im,(x+dx,y+30))
                sheet.paste(Image.open(out/f'{theme}-48.png'),(x+dx+24,y+140))
            draw.text((x+4,y+200),f'{start+j+1} '+row['icon_id'][:25],fill='black');draw.text((x+4,y+220),row['validation_status'],fill='black')
        sheet.save(ROOT/f'review-{start}.png')

if __name__=='__main__':run()
