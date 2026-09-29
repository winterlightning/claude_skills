from pathlib import Path
import json,re,datetime,sys,shutil
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
ROOT=Path(__file__).parent
ITEMS=json.loads((ROOT/'items.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID={a['icon_id']:re.search(r'([0-9a-f-]{36})\.svg$',a['reference']).group(1) for a in ITEMS}
SOURCE_PATH={a['icon_id']:a['reference'] for a in ITEMS}
HELPERS='''
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def rect(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for k in range(8):
            a,b=pts[k],pts[(k+1)%8]
            if k%2:self.add_arc(n+str(k),a,b,radius_x=r)
            else:self.add_line(n+str(k),a,b)
        self.add_contour(n,*[n+str(k) for k in range(8)],closed=True)

    def curve(self,n,start,*segs):
        self.add_bezier(n,start,*segs)

    def star(self,n,x,y,s):
        # Five-point silhouette, shared integer vertices for each star instance.
        p=[(0,-6),(2,-2),(6,-2),(3,1),(4,6),(0,3),(-4,6),(-3,1),(-6,-2),(-2,-2)]
        self.add_polyline(n,*[(x+round(a*s/6),y+round(b*s/6)) for a,b in p],closed=True)
'''
# Original/rejected comparison and the specific semantic correction, recorded before geometry.
SPECS=[
('SQUARE','The two small rating stars became dots and the house was flattened. Restore three recognizable stars above an upright house.', '''
        # Rating owns one large star and a mirrored smaller pair; house retains door and pitched roof.
        self.star('rating',24,12,6)
        for x in (8,40): self.star('side-rating-'+str(x),x,16,4)
        self.add_polyline('roof',(8,31),(24,23),(40,31))
        self.add_polyline('house',(12,32),(12,42),(20,42),(20,34),(28,34),(28,42),(36,42),(36,32))
'''),
('VRECT_L','The house inside the speech bubble became a chevron and the couple became tiny face dots. Restore a complete house and two broader busts.', '''
        # Speech bubble above two equal busts; intentionally compact complete house inside.
        self.add_polyline('bubble',(9,4),(39,4),(39,23),(27,23),(22,28),(22,23),(9,23),closed=True)
        self.add_polyline('house',(17,14),(24,8),(31,14),(29,14),(29,20),(19,20),(19,14),closed=True)
        for x in (12,36):
            self.circle('head-'+str(x),x,32,3)
            self.curve('shoulders-'+str(x),(x-7,44),((x-7,42),(x-4,43),(x,43)),((x+4,43),(x+7,42),(x+7,44)))
'''),
('HRECT_L','The cargo bike lost its frame and broad rear box; the box looked like a sign on a pole. Restore a cargo box over the rear wheel and a connected bicycle frame.', '''
        # Equal wheels, a triangular chassis, rear cargo box and higher handlebar.
        for x in (12,36): self.circle('wheel-'+str(x),x,32,8)
        self.rect('cargo',4,8,16,12,2)
        self.add_polyline('frame',(12,32),(23,32),(30,20),(18,20),(23,32))
        self.add_polyline('fork',(36,32),(29,10),(35,10))
        self.add_line('seat-post',(18,20),(18,24))
        self.relate('connect','cargo','frame')
        self.relate('connect','frame','fork')
        self.relate('connect','frame','seat-post')
'''),
('SQUARE','The payment cue was reduced to an unexplained dot and the receptionist disappeared behind a T. Restore two people, a counter and a dollar payment mark.', '''
        # Receptionist behind left counter; customer reaches left; dollar below handoff.
        self.circle('staff-head',11,10,4)
        self.curve('staff-shoulders',(5,27),((5,24),(8,22),(11,22)),((14,22),(17,24),(17,27)))
        self.add_line('counter',(5,30),(19,30))
        self.add_line('counter-leg',(8,30),(8,42))
        self.relate('connect','counter','counter-leg')
        self.circle('head',36,10,4)
        self.add_line('torso',(36,22),(36,32))
        self.add_polyline('arm',(36,23),(28,28),(25,28))
        self.add_polyline('legs',(31,42),(36,32),(41,42))
        self.relate('connect','torso','legs')
        self.mark_human_figure('customer',head='head',torso='torso',torso_junction='start')
        self.curve('dollar',(25,33),((19,31),(17,35),(22,36)),((28,37),(24,41),(19,39)))
        self.add_line('currency-bar',(22,30),(22,42))
'''),
('HRECT_L','The swimmer/recliner was reduced to a floating angular mark and the umbrella nearly touched the water. Restore an articulated reclining body beneath a wide canopy.', '''
        # Broad umbrella left; detached head and reclining bent legs right; low water line.
        self.add_arc('canopy',(4,17),(24,17),radius_x=10,radius_y=9)
        self.add_line('canopy-base',(24,17),(4,17))
        self.add_contour('umbrella','canopy','canopy-base',closed=True)
        self.add_line('pole',(14,17),(12,34))
        self.circle('head',30,21,4)
        self.curve('torso',(30,33),((30,36),(25,37),(22,37)))
        self.add_polyline('legs',(22,37),(34,31),(42,37))
        self.relate('connect','torso','legs')
        self.mark_human_figure('recliner',head='head',torso='torso',torso_junction='start')
        self.curve('water',(4,40),((8,44),(11,44),(15,40)),((19,44),(22,44),(26,40)),((30,44),(33,44),(37,40)),((40,43),(42,43),(44,40)))
'''),
('SQUARE','The page became an E-shaped bracket and the candidate looked like a small bucket. Restore a document outline, portrait panel, text lines and a clear candidate bust.', '''
        # Resume page at left; person overlaps the open right edge as in the original.
        self.add_polyline('page',(29,6),(6,6),(6,42),(25,42))
        self.add_polyline('portrait',(14,14),(22,14),(22,22),(14,22),closed=True)
        self.add_line('text-1',(14,30),(23,30))
        self.add_line('text-2',(14,37),(21,37))
        self.circle('candidate-head',36,18,4)
        self.curve('candidate-shoulders',(28,42),((28,34),(31,30),(36,30)),((41,30),(44,34),(44,42)))
        self.add_line('candidate-base',(28,42),(44,42))
        self.relate('connect','candidate-shoulders','candidate-base')
'''),
('VRECT_L','The history symbol lost the clock face and recognizable return arrow. Restore a circular clock with hands and a small clockwise return arrow on the portrait card.', '''
        self.rect('card',8,4,32,40,5)
        self.curve('clock',(33,21),((31,11),(15,11),(14,23)),((13,34),(28,38),(33,29)))
        self.add_polyline('arrow',(27,21),(34,23),(35,16))
        self.add_polyline('hands',(24,18),(24,25),(28,28))
'''),
('HRECT_M','The banknote became a scalloped ticket. Restore a rectangular note with rounded corners, a central denomination medallion and balanced side marks.', '''
        # Lucide banknote construction: rounded bill, round denomination, two side marks.
        self.rect('bill',4,10,40,28,3)
        self.circle('denomination',24,24,5)
        for x in (11,37): self.add_dot('mark-'+str(x),(x,24))
'''),
('SQUARE','The Redux paths were disconnected and flattened into a generic S. Restore the three orbiting lobes and three hollow endpoint nodes.', '''
        # Three smooth lobes arranged asymmetrically around three endpoint circles.
        self.circle('upper-node',22,19,3)
        self.circle('left-node',16,33,3)
        self.circle('right-node',33,29,3)
        self.curve('upper-lobe',(14,30),((7,17),(13,6),(23,6)),((31,6),(35,11),(36,15)))
        self.curve('right-lobe',(25,19),((42,19),(49,36),(36,41)),((32,43),(28,42),(26,41)))
        self.curve('lower-lobe',(31,32),((23,48),(3,43),(6,29)),((6,26),(8,24),(9,23)))
'''),
('SQUARE','The number 10 became a bar and dot, and the battery became an angular bracket. Restore the range number, leftward distance arrow and battery silhouette.', '''
        # Preserve 10 at upper left, battery lower right, arrow to left boundary.
        self.add_polyline('one',(7,6),(10,6),(10,18))
        self.add_line('one-foot',(6,18),(14,18));self.relate('connect','one','one-foot')
        self.rect('zero',20,6,8,12,4)
        self.add_polyline('battery',(31,28),(31,24),(35,24),(35,20),(41,20),(41,24),(44,24),(44,42),(31,42),(31,36))
        self.add_line('distance',(10,32),(36,32))
        self.add_polyline('arrow',(16,26),(10,32),(16,38))
        self.relate('connect','distance','arrow')
        self.add_line('limit',(4,26),(4,38))
'''),
('HRECT_L','The isolated X and two rules no longer clearly described a table row. Restore a table grid with a delete X aligned to its middle row.', '''
        self.rect('table',18,8,26,32,2)
        for y in (18,30):self.add_line('row-'+str(y),(18,y),(44,y));self.relate('connect','table','row-'+str(y))
        self.add_polyline('delete-a',(4,20),(12,28))
        self.add_polyline('delete-b',(4,28),(12,20))
'''),
('SQUARE','The foreground car looked like a bag and the house was only a roof arch. Restore a windshield, hood, wheels and a complete rear house.', '''
        self.add_polyline('house',(21,16),(31,6),(42,16),(42,33),(34,33),(34,23),(28,23))
        self.add_polyline('windshield',(6,30),(10,21),(22,21),(26,30))
        self.rect('car',4,30,24,10,3)
        self.add_line('left-wheel',(8,40),(8,43));self.relate('connect','car','left-wheel')
        self.add_line('right-wheel',(24,40),(24,43));self.relate('connect','car','right-wheel')
        self.relate('connect','windshield','car')
        for x in (10,22):self.add_dot('lamp-'+str(x),(x,35))
'''),
('HRECT_L','The chairs were reduced to inward hooks and the table was undersized. Restore matching seats, backs and legs around a broader pedestal table.', '''
        # Mirrored chairs share seat height and leg lengths; central pedestal table.
        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            n='chair-'+str(side)
            self.add_polyline(n,p(20,8),p(18,27),p(10,27),p(10,40))
            self.add_line(n+'-leg',p(18,27),p(18,40))
            self.relate('connect',n,n+'-leg')
        self.add_line('tabletop',(15,20),(33,20))
        self.add_line('pedestal',(24,20),(24,40))
        self.add_line('foot',(19,40),(29,40))
        self.relate('connect','tabletop','pedestal');self.relate('connect','pedestal','foot')
'''),
('SQUARE','Both figures had tiny heads and stiff rectangular dress shapes. Restore the original pair of female restroom figures, round heads and flared dresses beside a divider.', '''
        # Two equal female figures as supplied, with 4-unit head-to-body ink gaps.
        for x in (12,36):
            n='person-'+str(x)
            self.circle(n+'-head',x,10,4)
            self.add_polyline(n+'-dress',(x,22),(x-7,34),(x+7,34),closed=True)
            for dx in (-3,3):
                self.add_line(n+'-leg-'+str(dx),(x+dx,34),(x+dx,42))
                self.relate('connect',n+'-dress',n+'-leg-'+str(dx))
        self.add_line('divider',(24,6),(24,42))
'''),
('SQUARE','The retouch cue became disconnected dots and a slash over a generic mountain. Restore a landscape frame with sun, mountain range and a clear sparkle at the editing corner.', '''
        self.add_polyline('frame',(25,10),(6,10),(6,42),(42,42),(42,30))
        self.circle('sun',15,20,3)
        self.add_polyline('mountains',(11,36),(19,27),(25,34),(31,24),(39,36))
        self.add_line('wand',(31,19),(41,29))
        self.add_polyline('sparkle',(36,6),(36,14))
        self.add_line('sparkle-h',(32,10),(40,10))
        self.relate('connect','sparkle','sparkle-h')
        self.add_dot('glint',(44,5))
'''),
('HRECT_L','The wheels were undersized and the retro handlebar was a heavy hook. Restore larger wheels, the diamond frame, a slim saddle and curled handlebar.', '''
        # Equal larger wheels and shared frame nodes; intentional classic bicycle asymmetry.
        for x in (13,35):self.circle('wheel-'+str(x),x,31,9)
        self.add_polyline('frame',(13,31),(24,31),(31,17),(18,17),(13,31))
        self.add_line('seat-tube',(18,12),(24,31))
        self.add_line('saddle',(13,12),(23,12));self.relate('connect','seat-tube','saddle')
        self.add_polyline('fork',(35,31),(30,8),(35,8))
        self.add_arc('handlebar',(35,8),(35,16),radius_x=4)
        self.relate('connect','fork','handlebar');self.relate('connect','frame','seat-tube')
'''),
('SQUARE','The gymnast lost the raised arm, long leg and flowing ribbon; it read like a seated person under a dome. Restore the dancing pose and near-circular ribbon sweep.', '''
        self.circle('head',24,15,4)
        self.add_line('torso',(24,27),(24,34))
        self.add_polyline('raised-arm',(24,27),(15,24),(11,16))
        self.add_line('other-arm',(24,27),(36,31))
        self.add_line('standing-leg',(24,34),(22,42))
        self.curve('raised-leg',(24,34),((29,40),(32,42),(38,42)))
        for n in ('raised-arm','other-arm','standing-leg','raised-leg'):self.relate('connect','torso',n)
        self.mark_human_figure('gymnast',head='head',torso='torso',torso_junction='start')
        self.curve('ribbon',(13,9),((25,1),(42,11),(42,28)))
        self.curve('ribbon-lower',(6,24),((7,31),(11,36),(16,38)))
'''),
('VRECT_L','The gymnast became a squat seated shape and the ribbon lost its loop. Restore a raised hand, standing leg, bent back leg and an overhead ribbon loop.', '''
        self.circle('head',27,18,4)
        self.add_line('torso',(27,30),(25,35))
        self.add_polyline('raised-arm',(27,30),(35,26),(40,18))
        self.add_line('left-arm',(27,30),(18,33))
        self.add_polyline('back-leg',(25,35),(20,40),(12,39))
        self.add_polyline('standing-leg',(25,35),(29,39),(27,44))
        for n in ('raised-arm','left-arm','back-leg','standing-leg'):self.relate('connect','torso',n)
        self.mark_human_figure('gymnast',head='head',torso='torso',torso_junction='start')
        self.curve('ribbon',(40,18),((30,-1),(6,2),(7,12)),((8,21),(22,14),(16,11)),((12,8),(9,18),(8,22)))
        self.relate('connect','raised-arm','ribbon')
'''),
('SQUARE','The rightward exit arrow was trapped inside a closed box. Open the bracket on the right and extend the arrow out through it.', '''
        # Lucide log-out: open door bracket and arrow crossing its opening.
        self.add_polyline('bracket',(24,6),(6,6),(6,42),(24,42))
        self.add_line('shaft',(16,24),(42,24))
        self.add_polyline('arrow',(32,14),(42,24),(32,34))
        self.relate('connect','shaft','arrow')
'''),
('HRECT_L','The destination line was entirely missing, leaving a plain right arrow. Add the terminal line and preserve the long rightward shaft.', '''
        self.add_line('shaft',(4,24),(34,24))
        self.add_polyline('arrow',(24,14),(34,24),(24,34))
        self.add_line('terminal',(44,8),(44,40))
        self.relate('connect','shaft','arrow')
''')]

def author(indices):
    records=json.loads((ROOT/'runs.json').read_text()) if (ROOT/'runs.json').exists() else {}
    for i in indices:
        item=ITEMS[i];uid=SOURCE_ICON_ID[item['icon_id']];keyshape,note,body=SPECS[i]
        stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        run=Path('icon_set/work/primitive-make-ray')/uid/(stamp+'-meaning-fix');run.mkdir(parents=True)
        meta=dict(concept=Path(item['reference']).stem[:-37],source_uuid=uid,reference_path=item['reference'],icon_id=item['icon_id'],author=AUTHOR,comparison=note,feedback=item['feedback'])
        (run/(item['icon_id']+'.metadata.json')).write_text(json.dumps(meta,indent=2))
        module=run/(item['icon_id'].replace('-','_')+'_'+uid.replace('-','_')+'.py')
        module.write_text('from icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n\n'+f'SOURCE_ICON_ID = {uid!r}\nSOURCE_PATH = {item["reference"]!r}\nAUTHOR = {AUTHOR!r}\n\n'+f'class Drawing(Solo48):\n    icon_id = {item["icon_id"]!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects/general"\n    aliases = ()\n    keywords = ({meta["concept"]!r},)\n\n    # Revision plan: {note}\n    def build(self):\n'+body+HELPERS)
        icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg();(run/(item['icon_id']+'.svg')).write_text(svg)
        (run/'validation.txt').write_text(report.describe());render_previews(svg,item['icon_id'],48,run)
        shutil.copyfile(ROOT/f'compare-{i//5}.png',run/'reference-before-comparison.png')
        g=gate(module);(run/'gate.json').write_text(json.dumps(g,indent=2))
        records[str(i)]={**meta,'run':str(run),'module':str(module),'keyshape':keyshape,'gate':g,'validation_status':report.status}
        print(i,item['icon_id'],report.status,g['status'],len(g['errors']),len(g['warnings']),flush=True)
        (ROOT/'runs.json').write_text(json.dumps(records,indent=2))
if __name__=='__main__':author([int(x) for x in sys.argv[1:]] if len(sys.argv)>1 else range(20))
