"""Ordered standalone authoring for the supplied batch; no registry writes."""
from pathlib import Path
import json, importlib.util, textwrap, traceback
import cairosvg
from PIL import Image, ImageOps, ImageDraw

SOURCE_ICON_ID = '82791e1b-7e30-4905-85e9-1bf64f1e2489'
SOURCE_PATH = 'icon_set/work/todo-references/online learning online course 2_82791e1b-7e30-4905-85e9-1bf64f1e2489.svg'
AUTHOR = 'gpt-6'
ROOT = Path(__file__).parent
ROWS = json.loads((ROOT/'batch-inputs.json').read_text())

HELPERS = '''
    def circle(self, name, cx, cy, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, x, y, w, h, r=3):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; members.append(part)
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def letter_p(self, name, x, y, w, h):
        # Stem and semicircular bowl share explicit shoulder nodes.
        mid=y+h//2; rr=h//4
        self.add_polyline(name+'-stem',(x,y+h),(x,mid),(x,y),(x+w-rr,y))
        self.add_arc(name+'-bowl',(x+w-rr,y),(x+w-rr,mid),radius_x=rr)
        self.add_line(name+'-return',(x+w-rr,mid),(x,mid))
        self.relate('connect',name+'-stem',name+'-bowl')
        self.relate('connect',name+'-bowl',name+'-return')
        self.relate('connect',name+'-return',name+'-stem')
'''

# Each entry: keyshape, subject/structural plan, construction reference, omissions, geometry.
DESIGNS = [
('SQUARE','Open book above a course entry field. Mirror the pages about x=24; the field owns its centered rule.','book-open: paired pages and center binding; monitor: rounded enclosure.','Small page curvature reduced to broad page facets.', '''
self.add_polyline('pages',(10,6),(18,6),(24,10),(30,6),(38,6),(38,23),(30,23),(24,27),(18,23),(10,23),closed=True)
self.add_line('binding',(24,10),(24,27)); self.relate('connect','pages','binding')
self.box('entry',6,35,36,7,3)
self.add_line('entry-rule',(16,39),(32,39))
'''),
('CIRCLE','OpenVPN emblem: open circular outer arch surrounding a keyhole. Shared axis x=24.','No useful exact Lucide match; circle and coherent keyhole contours are authored directly.','No semantic elements omitted.', '''
self.add_arc('outer',(10,38),(38,38),radius_x=20,large_arc=True)
self.add_arc('keyhole-head',(18,25),(30,25),radius_x=9,large_arc=True)
self.add_line('keyhole-right',(30,25),(33,41))
self.add_arc('keyhole-base',(33,41),(15,41),radius_x=9,radius_y=3)
self.add_line('keyhole-left',(15,41),(18,25))
self.add_contour('keyhole','keyhole-head','keyhole-right','keyhole-base','keyhole-left',closed=True)
'''),
('SQUARE','Side-view dog under a sloping shelter roof. Preserve right-facing muzzle and paired legs.','house: long coherent shelter strokes.','Rear far leg and minor fur contours omitted to retain a readable silhouette.', '''
self.add_polyline('shelter',(42,6),(6,16),(6,42),(42,42))
self.add_polyline('dog',(12,26),(14,22),(26,22),(31,14),(32,20),(38,23),(35,27),(31,27),(29,34),(29,35),(25,35),(25,29),(19,29),(17,35),(13,35),(13,30))
'''),
('SQUARE','Campfire above a rectangular six-section fuel bed. Grid cells share intersections.','flame: asymmetric tongue and rounded lower bowl.','None; six fuel sections retained.', '''
self.add_arc('fire-left',(19,15),(24,6),radius_x=10,sweep=False)
self.add_arc('fire-tip',(24,6),(30,17),radius_x=14,sweep=False)
self.add_arc('fire-bowl',(30,17),(18,17),radius_x=6,radius_y=7)
self.add_line('fire-notch',(18,17),(19,15))
self.add_contour('flame','fire-left','fire-tip','fire-bowl','fire-notch',closed=True)
self.box('fuel',6,30,36,12,2)
self.add_line('fuel-horizontal',(6,36),(42,36));self.relate('connect','fuel','fuel-horizontal')
for x in (18,30):
    self.add_polyline(f'fuel-divider-{x}',(x,30),(x,36),(x,42))
    self.relate('connect','fuel',f'fuel-divider-{x}')
    self.relate('connect','fuel-horizontal',f'fuel-divider-{x}')
'''),
('SQUARE','Pig head facing an apple pictured on a rectangular panel. Preserve the overlapping snout.','No useful exact Lucide match; source supplies pig/apple arrangement.','Tiny nostril and panel portion behind snout omitted.', '''
self.add_polyline('panel',(22,24),(22,6),(42,6),(42,38),(24,38))
self.add_polyline('pig',(6,42),(12,34),(20,31),(22,25),(14,22),(11,15),(6,14),(6,20))
self.add_arc('apple-left',(32,20),(26,24),radius_x=4)
self.add_arc('apple-bottom',(26,24),(38,24),radius_x=6,radius_y=7,sweep=False)
self.add_arc('apple-right',(38,24),(32,20),radius_x=4)
self.add_contour('apple','apple-left','apple-bottom','apple-right',closed=True)
self.add_line('apple-stem',(32,20),(34,15));self.relate('connect','apple','apple-stem')
'''),
('SQUARE','Roofed outpost with a central foreground rectangular device. Roof mirrors about x=24.','house: gable and side walls; monitor: rounded front object.','Short device indicator omitted; horizontal screen division retained.', '''
self.add_polyline('roof',(6,20),(24,6),(42,20))
self.add_polyline('walls',(10,17),(10,34),(16,34))
self.add_polyline('walls-right',(38,17),(38,34),(32,34))
self.box('device',16,24,16,18,3)
self.add_line('screen-rule',(16,33),(32,33));self.relate('connect','device','screen-rule')
'''),
('SQUARE','Oxygen cylinder with valve and connected circular timer. Preserve timer at upper right.','No useful exact Lucide match; capsule cylinder and clock constructed from shared centers.','Clock minute subdivisions omitted; hands retained.', '''
self.box('tank',6,20,15,22,6)
self.add_polyline('valve',(10,20),(10,13),(17,13),(17,20))
self.relate('connect','tank','valve')
self.add_polyline('valve-top',(8,6),(14,6),(20,6))
self.add_line('valve-neck',(14,6),(14,13));self.relate('connect','valve-top','valve-neck');self.relate('connect','valve','valve-neck')
self.circle('timer',33,16,9)
self.add_polyline('hands',(33,11),(33,16),(37,16))
self.add_line('hose',(17,13),(24,13));self.relate('connect','hose','valve')
'''),
('CIRCLE','Round painting palette with three equal circular wells in a triangular arrangement.','palette: common outer circle and repeated round paint wells.','None; all three wells retained.', '''
self.circle('palette',24,24,20)
for i,(x,y) in enumerate(((24,15),(16,29),(32,29))):
    self.circle(f'well-{i}',x,y,3)
'''),
('SQUARE','Panoramic picture frame containing a sun and two overlapping mountain peaks.','monitor: equal-radius frame corners.','One descending hidden mountain edge removed at the overlap.', '''
self.box('frame',6,6,36,36,4)
self.circle('sun',17,17,3)
self.add_polyline('front-mountain',(6,36),(17,25),(28,36));self.relate('connect','frame','front-mountain')
self.add_polyline('back-mountain',(23,31),(32,20),(42,30));self.relate('connect','front-mountain','back-mountain');self.relate('connect','frame','back-mountain')
'''),
('VRECT_M','Pantyhose with one straight leg and one bent crossing leg, open at the waist.','Shared human-reference.md/full_body_ref.png: coherent bent limb strokes and simple anatomy. No detached head.','Fine ankle wrinkles omitted; crossing leg and toe shapes retained.', '''
self.add_polyline('waist',(15,4),(28,4),(28,13))
self.add_arc('hip',(15,4),(13,19),radius_x=14,sweep=False)
self.add_polyline('bent-leg',(13,19),(28,26),(10,36),(12,42),(38,23),(38,21),(26,15))
self.relate('connect','hip','bent-leg');self.relate('connect','waist','hip')
self.add_polyline('straight-leg',(15,23),(15,30))
self.add_polyline('lower-leg',(22,35),(22,41),(30,44),(20,44),(18,42))
'''),
('SQUARE','Paragraph panel with an image at upper right and text rules at left and below.','monitor: rounded rectangular enclosure.','Four text rows reduced to three to improve spacing.', '''
self.box('panel',6,6,36,36,3)
self.box('image',27,14,8,8,2)
self.add_line('text-short',(14,16),(19,16))
for i,y in enumerate((26,34)):
    self.add_line(f'text-{i}',(14,y),(34,y))
'''),
('SQUARE','Text-direction T above a leftward arrow. A centered stem shares the top-bar midpoint.','No useful exact Lucide match; hand-authored directional geometry.','None.', '''
self.add_polyline('top-bar',(14,6),(26,6),(38,6))
self.add_line('stem',(26,6),(26,26));self.relate('connect','top-bar','stem')
self.add_polyline('arrow',(14,26),(6,34),(14,42))
self.add_line('arrow-shaft',(6,34),(42,34));self.relate('connect','arrow','arrow-shaft')
'''),
('HRECT_M','Park and bike represented by P plus B. Letters retain two B bowls.','No useful exact Lucide match; letter stems and tangent semicircular bowls authored on integer grid.','None; complete P+B retained.', '''
self.letter_p('p',4,10,11,28)
self.add_polyline('plus-horizontal',(20,24),(24,24),(28,24))
self.add_polyline('plus-vertical',(24,20),(24,24),(24,28));self.relate('connect','plus-horizontal','plus-vertical')
self.add_polyline('b-stem',(33,38),(33,24),(33,10),(37,10))
self.add_arc('b-upper',(37,10),(37,24),radius_x=7)
self.add_arc('b-lower',(37,24),(37,38),radius_x=7)
self.add_line('b-bottom',(37,38),(33,38));self.add_line('b-middle',(33,24),(37,24))
for a,b in [('b-stem','b-upper'),('b-upper','b-lower'),('b-lower','b-bottom'),('b-bottom','b-stem'),('b-middle','b-stem'),('b-middle','b-upper'),('b-middle','b-lower')]:self.relate('connect',a,b)
'''),
('HRECT_M','Park and ride represented by P plus R. Shared uppercase height and bowl geometry.','No useful exact Lucide match; hand-authored P/R with shared bowl parameters.','None; complete P+R retained.', '''
self.letter_p('p',4,10,11,28)
self.add_polyline('plus-horizontal',(20,24),(24,24),(28,24))
self.add_polyline('plus-vertical',(24,20),(24,24),(24,28));self.relate('connect','plus-horizontal','plus-vertical')
self.letter_p('r',33,10,11,28)
self.add_line('r-leg',(37,24),(44,38));self.relate('connect','r-bowl','r-leg');self.relate('connect','r-return','r-leg')
'''),
('SQUARE','Parking aid P emits two waves toward a triangular obstacle. Deliberate diagonal arrangement.','No useful exact Lucide match; concentric wave arcs share their logical origin.','None.', '''
self.letter_p('p',6,6,14,24)
self.add_arc('signal-inner',(28,14),(20,28),radius_x=16)
self.add_arc('signal-outer',(36,17),(26,35),radius_x=22)
self.add_polyline('obstacle',(28,42),(35,25),(42,42),closed=True)
'''),
('SQUARE','Front-facing car under an overlapping circular P parking badge. Car sides and wheels mirror about x=21.','monitor: rounded car fascia; circle construction for the parking badge.','Headlamp pair reduced to two dots; small tire outlines reduced to strokes.', '''
self.circle('badge',32,16,10)
self.letter_p('p',29,10,7,12)
self.add_polyline('roof',(8,30),(12,23),(22,23))
self.box('car',6,30,32,8,3)
for i,x in enumerate((12,32)):
    self.add_line(f'wheel-{i}',(x,38),(x,42));self.relate('connect','car',f'wheel-{i}')
for i,x in enumerate((13,31)):self.add_dot(f'lamp-{i}',(x,34))
'''),
('VRECT_M','Parking sign with tall left post, top bar, short right side and letter P.','No useful exact Lucide match; open sign and semicircular letter bowl.','None.', '''
self.add_polyline('sign',(10,44),(10,4),(38,4),(38,27))
self.letter_p('p',20,13,9,20)
'''),
('SQUARE','Rounded pass badge containing a rising check mark.','monitor: equal-radius corners and generous inner padding.','None.', '''
self.box('badge',6,6,36,36,5)
self.add_polyline('check',(15,24),(22,31),(33,17))
'''),
('SQUARE','Foreground passport with globe over a larger background world disc. Preserve overlap and continental boundary.','globe: meridian and equator construction; monitor: consistent cover corners.','Globe meridians reduced to a single central meridian; background continent simplified.', '''
self.add_arc('world',(22,32),(32,16),radius_x=13,large_arc=True)
self.add_polyline('continent',(8,16),(16,16),(16,23),(12,25),(12,31))
self.box('passport',22,16,20,26,3)
self.circle('globe',32,29,6)
self.add_polyline('equator',(26,29),(32,29),(38,29));self.relate('connect','globe','equator')
self.add_polyline('meridian',(32,23),(32,29),(32,35));self.relate('connect','globe','meridian');self.relate('connect','equator','meridian')
'''),
('VRECT_L','Passport cover with an exposed binding above and a centered globe. The source has no visible hand.','globe: equal hemispheres and central meridian; monitor: rounded enclosure.','Globe latitude pair reduced to an equator; one meridian retained.', '''
self.box('cover',8,12,32,32,3)
self.add_polyline('binding',(8,15),(8,7))
self.add_arc('binding-corner',(8,7),(11,4),radius_x=3)
self.add_line('binding-top',(11,4),(35,4))
self.add_arc('binding-right',(35,4),(38,7),radius_x=3)
self.add_line('binding-end',(38,7),(38,12))
self.add_contour('binding-outline','binding','binding-corner','binding-top','binding-right','binding-end')
self.relate('connect','binding-outline','cover')
self.circle('globe',24,28,9)
self.add_polyline('equator',(15,28),(24,28),(33,28));self.relate('connect','globe','equator')
self.add_polyline('meridian',(24,19),(24,28),(24,37));self.relate('connect','globe','meridian');self.relate('connect','equator','meridian')
'''),
]

def run():
    for row,design in zip(ROWS,DESIGNS):
        d=Path(row['result_dir']); key,plan,refs,omissions,body=design
        if (d/'result.json').exists(): continue
        module_path=d/(row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py')
        source=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = {AUTHOR!r}
PLAN = {plan!r}
CONSTRUCTION_REFERENCES = {refs!r}
OMISSIONS = {omissions!r}

class Drawing(Solo48):
    icon_id = {row['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = {tuple(row['concept'].split())!r}
{HELPERS}
    def build(self):
{textwrap.indent(textwrap.dedent(body).strip(), '        ')}
'''
        module_path.write_text(source)
        record={**row,'author':AUTHOR,'keyshape':key,'subject_and_plan':plan,'construction_references':refs,'omissions':omissions,'module':module_path.name}
        try:
            spec=importlib.util.spec_from_file_location('standalone_'+row['source_uuid'],module_path)
            mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
            icon=mod.Drawing(); report=icon.validate_icon();record['validation_status']=report.status
            (d/'validation.txt').write_text(report.describe())
            svg=icon.to_svg();(d/(row['icon_id']+'.svg')).write_text(svg)
            for size in (48,240):
                p=d/f'light-{size}.png'
                cairosvg.svg2png(bytestring=svg.encode(),write_to=str(p),output_width=size,output_height=size,background_color='white')
                ImageOps.invert(Image.open(p).convert('RGB')).save(d/f'dark-{size}.png')
            print(row['icon_id'],report.status,flush=True)
        except Exception:
            record['validation_status']='error';record['error']=traceback.format_exc();(d/'validation.txt').write_text(record['error']);print(row['icon_id'],'ERROR',flush=True)
        # Draft findings only. Final result.json follows actual visual inspection.
        (d/'review-draft.json').write_text(json.dumps(record,indent=2))

if __name__=='__main__': run()
