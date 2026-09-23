"""Standalone batch 35 authoring; no registry or publication mutations."""
from pathlib import Path
import importlib.util
import json
import textwrap
import traceback
import cairosvg

SOURCE_ICON_ID = '0c038416-c2a9-4ae0-ab80-a793e4a0b0c7'
SOURCE_PATH = 'icon_set/work/todo-references/playlist album_0c038416-c2a9-4ae0-ab80-a793e4a0b0c7.svg'
AUTHOR = 'gpt-6'
ROOT = Path(__file__).parent
ENTRIES = json.loads((ROOT / 'batch-inputs.json').read_text())

HELPERS = '''
    def circle(self, name, cx, cy, r):
        points = [(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members = []
        for i, (a,b) in enumerate(zip(points, points[1:])):
            member = f"{name}-{i}"
            self.add_arc(member, a, b, radius_x=r)
            members.append(member)
        self.add_contour(name, *members, closed=True)

    def rounded(self, name, left, top, right, bottom, r):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r),(left+r,top)]
        members = []
        for i,(a,b) in enumerate(zip(points,points[1:])):
            member = f"{name}-{i}"
            if i % 2: self.add_arc(member,a,b,radius_x=r)
            else: self.add_line(member,a,b)
            members.append(member)
        self.add_contour(name,*members,closed=True)

    def plug(self, cx=24, top=21, bottom=32):
        # Shared bowl width and mirrored prongs; cable joins bottom apex.
        r=8
        self.add_polyline('plug-top',(cx-r,top),(cx-4,top),(cx+4,top),(cx+r,top))
        self.add_line('plug-right',(cx+r,top),(cx+r,bottom-r))
        self.add_arc('plug-right-curve',(cx+r,bottom-r),(cx,bottom),radius_x=r)
        self.add_arc('plug-left-curve',(cx,bottom),(cx-r,bottom-r),radius_x=r)
        self.add_line('plug-left',(cx-r,bottom-r),(cx-r,top))
        self.add_contour('plug-bowl','plug-right','plug-right-curve','plug-left-curve','plug-left')
        self.relate('connect','plug-top','plug-bowl')
        for i,x in enumerate((cx-4,cx+4)):
            self.add_line(f'prong-{i}',(x,top-8),(x,top))
            self.relate('connect',f'prong-{i}','plug-top')
'''

# Plans own their dimensions, series and symmetry; geometry is authored afresh.
SPECS = [
('SQUARE','A framed album with paired musical notes.','music: circular noteheads and a single bent stem/beam contour.','No defining features omitted.', '''
self.rounded('album',6,6,42,42,4)
for name,cx,cy in [('note-left',17,32),('note-right',31,29)]:
    self.circle(name,cx,cy,2)
self.add_polyline('music-stems',(19,32),(19,18),(33,15),(33,29))
for note in ('note-left','note-right'): self.relate('connect',note,'music-stems')
'''),
('SQUARE','A playroom house with a door and a stacking pawn toy.','house: coherent roof and walls; user.svg consulted to distinguish the toy from a person.','Toy reduced to a circular knob and broad base; roof eaves merged into house corners.', '''
axis=24
self.add_polyline('house',(6,20),(axis,6),(42,20),(42,42),(6,42),(6,20))
self.add_polyline('door',(14,42),(14,29),(22,29),(22,42))
self.relate('connect','house','door')
self.circle('toy-knob',33,26,3)
self.add_bezier('toy-base',(33,29),((39,31),(39,35),(36,36)),((42,39),(40,42),(33,42)),((26,42),(24,39),(30,36)),((27,35),(27,31),(33,29)))
self.add_contour('toy','toy-base',closed=True)
self.relate('connect','toy-knob','toy')
self.relate('connect','toy','house')
'''),
('CIRCLE','A two-prong plug inside a circular enclosure, cable descending to the rim.','plug: mirrored prongs, flat cap and rounded bowl.','No bolt is visible in the supplied reference; none was invented.', '''
self.circle('ring',24,24,20)
self.plug()
self.add_line('cable',(24,32),(24,44))
self.relate('connect','cable','plug-bowl')
self.relate('connect','cable','ring')
'''),
('CIRCLE','A plug in a circle with a cable curving down and right.','plug: shared bowl radii and mirrored prongs; circular enclosure with cable attachment.','No minus is visible in the supplied reference; none was invented.', '''
# The 12-16-20 triangle supplies exact cable/rim junctions.
self.add_arc('ring-first',(36,40),(12,8),radius_x=20)
self.add_arc('ring-second',(12,8),(36,40),radius_x=20)
self.add_contour('ring','ring-first','ring-second',closed=True)
self.plug()
self.add_bezier('cable',(24,32),((24,38),(28,40),(36,40)))
self.relate('connect','cable','plug-bowl')
self.relate('connect','cable','ring')
'''),
('SQUARE','A plug inside an open circle with a lower-right cancellation cross.','plug: bowl and equal prongs; code: matched diagonal strokes.','No defining features omitted; open ring preserves room for the cross.', '''
self.add_arc('ring-top',(6,24),(42,24),radius_x=18)
self.add_arc('ring-bottom',(24,42),(6,24),radius_x=18)
self.add_contour('ring','ring-bottom','ring-top')
self.plug(cx=22,top=19,bottom=30)
self.add_bezier('cable',(22,30),((22,37),(25,38),(29,38)))
self.relate('connect','cable','plug-bowl')
self.add_polyline('cross-down',(33,33),(37,37),(41,41))
self.add_polyline('cross-up',(33,41),(37,37),(41,33))
self.relate('connect','cross-down','cross-up')
'''),
('VRECT_M','A plug mounted inside a tall rounded rectangle, with its cable exiting below.','plug: equal pins and a semicircular lower bowl.','No defining features omitted.', '''
self.add_line('frame-top',(16,4),(32,4))
self.add_arc('frame-tr',(32,4),(38,10),radius_x=6)
self.add_line('frame-right',(38,10),(38,34))
self.add_arc('frame-br',(38,34),(32,40),radius_x=6)
self.add_polyline('frame-bottom',(32,40),(24,40),(16,40))
self.add_arc('frame-bl',(16,40),(10,34),radius_x=6)
self.add_line('frame-left',(10,34),(10,10))
self.add_arc('frame-tl',(10,10),(16,4),radius_x=6)
self.add_contour('frame','frame-top','frame-tr','frame-right','frame-br','frame-bottom-1','frame-bottom-2','frame-bl','frame-left','frame-tl',closed=True)
self.plug(top=20,bottom=31)
self.add_polyline('cable',(24,31),(24,40),(24,44))
self.relate('connect','cable','plug-bowl')
self.relate('connect','cable','frame')
'''),
('VRECT_L','A five-point star floating over an award podium.','star: alternating tips and valleys; consistent podium support spacing.','Thin doubled podium rim reduced to one rail to preserve the star-to-platform gap.', '''
axis=24
left=[(24,4),(20,11),(12,12),(18,18),(16,24),(24,20)]
right=[(2*axis-x,y) for x,y in reversed(left[1:-1])]
self.add_polyline('star',*left,*right,closed=True)
self.add_polyline('platform',(8,32),(12,32),(36,32),(40,32))
self.add_polyline('baseline',(8,44),(12,44),(36,44),(40,44))
for name,x in [('left',12),('right',36)]:
    self.add_line('post-'+name,(x,32),(x,44))
    self.relate('connect','post-'+name,'platform')
    self.relate('connect','post-'+name,'baseline')
'''),
('SQUARE','A polygraph monitor with a pulse trace and two lower controls.','activity: intentional angular waveform; rounded enclosure from printer.','Small outlined buttons reduced to round dots.', '''
self.rounded('monitor',6,6,42,42,4)
self.add_polyline('trace',(6,20),(15,20),(19,13),(25,27),(30,17),(33,20),(36,20))
self.relate('connect','trace','monitor')
self.add_line('control-divider',(6,31),(42,31))
self.relate('connect','control-divider','monitor')
for i,x in enumerate((18,30)): self.add_dot(f'control-{i}',(x,37))
'''),
('SQUARE','A folded sheet with a woven polyester grid.','grid-3x3: repeated orthogonal strands; exact shared crossing nodes.','No defining features omitted.', '''
self.add_polyline('sheet',(30,6),(10,6),(6,10),(6,38),(10,42),(38,42),(42,38),(42,18),(30,6))
self.add_polyline('fold',(30,6),(30,14),(34,18),(42,18))
self.relate('connect','sheet','fold')
xs=(15,23,31); ys=(18,26,34)
for i,x in enumerate(xs): self.add_polyline(f'vertical-{i}',(x,16),*((x,y) for y in ys),(x,36))
for j,y in enumerate(ys):
    self.add_polyline(f'horizontal-{j}',(13,y),*((x,y) for x in xs),(33,y))
    for i in range(3): self.relate('connect',f'vertical-{i}',f'horizontal-{j}')
'''),
('VRECT_M','An outlined pound sterling currency glyph.','pound-sterling: hooked upper stem, crossbar and baseline; outlined treatment retained from input.','No defining features omitted.', '''
self.add_bezier('outer-hook',(38,14),((38,7),(34,4),(27,4)),((16,4),(14,11),(17,22)))
self.add_polyline('bar-left',(17,22),(10,22),(10,30),(18,30))
self.add_bezier('lower-stem',(18,30),((19,36),(15,39),(12,40)))
self.add_polyline('foot',(12,40),(12,44),(38,44),(38,36),(24,36))
self.add_bezier('inner-stem',(24,36),((27,32),(26,30),(26,30)))
self.add_polyline('bar-right',(26,30),(32,30),(32,22),(25,22))
self.add_bezier('inner-hook',(25,22),((23,15),(22,12),(27,12)),((29,12),(30,12),(30,14)))
self.add_line('mouth',(30,14),(38,14))
self.add_contour('pound','outer-hook','bar-left-1','bar-left-2','bar-left-3','lower-stem','foot-1','foot-2','foot-3','foot-4','inner-stem','bar-right-1','bar-right-2','bar-right-3','inner-hook','mouth',closed=True)
'''),
('CIRCLE','A circular powder compact with a curved diagonal division inside.','No useful exact Lucide match; circles and one smooth divided inner disk come from the supplied reference.','No defining features omitted; inner disk reduced to give the outer ring breathing room.', '''
self.circle('rim',24,24,20)
# 6-8-10 triangle gives exact seam endpoints on the inner disk.
self.add_arc('disk-upper',(16,30),(32,18),radius_x=10)
self.add_arc('disk-lower',(32,18),(16,30),radius_x=10)
self.add_contour('disk','disk-upper','disk-lower',closed=True)
self.add_bezier('powder-seam',(16,30),((20,23),(26,18),(32,18)))
self.relate('connect','powder-seam','disk')
'''),
('VRECT_L','A preferences panel joined to a half gear.','settings: alternating teeth and gaps; half gear attached to a straight panel.','No defining features omitted.', '''
self.add_polyline('panel',(24,4),(24,12),(24,36),(24,44),(8,44),(8,4),closed=True)
for i,y in enumerate((12,28)): self.add_line(f'panel-mark-{i}',(16,y),(16,y+8))
self.add_polyline('gear',(24,12),(29,13),(33,9),(39,15),(35,20),(40,20),(40,28),(35,28),(39,33),(33,39),(29,35),(24,36))
self.relate('connect','gear','panel')
self.add_arc('gear-hub',(24,20),(24,32),radius_x=6)
self.relate('connect','gear-hub','panel')
'''),
('HRECT_L','A fan-shaped ultrasound field containing a curled fetus.','human_ref/full_body_ref.png: minimal human silhouette; source fetal pose remains a connected anatomical outline.','Tiny anatomical detail omitted; curled head and body retained as one silhouette, so no detached head gap applies.', '''
self.add_polyline('fan-sides',(4,28),(24,8),(44,28))
self.add_arc('fan-bottom',(44,28),(4,28),radius_x=20,radius_y=12)
self.add_contour('fan','fan-sides-1','fan-sides-2','fan-bottom',closed=True)
self.add_bezier('fetus',(25,26),((25,20),(32,20),(32,25)),((32,32),(24,35),(19,32)),((12,29),(18,22),(22,26)),((23,27),(24,26),(25,26)))
self.add_contour('baby','fetus',closed=True)
'''),
('VRECT_L','A lower female torso with a heart-shaped pelvic symbol.','heart: paired lobes and pointed base; human reference consulted for simple balanced anatomy.','No defining features omitted; this is a torso fragment, with no head or detached gap.', '''
axis=24
for side,sign in [('left',1),('right',-1)]:
    def p(x,y): return (axis+sign*(x-axis),y)
    self.add_bezier('body-'+side,p(12,4),(p(18,19),p(8,21),p(8,33)),(p(8,38),p(9,42),p(11,44)))
self.add_bezier('heart-left',(24,27),((18,20),(12,25),(17,31)),((19,33),(22,36),(24,38)))
self.add_bezier('heart-right',(24,38),((26,36),(29,33),(31,31)),((36,25),(30,20),(24,27)))
self.add_contour('heart','heart-left','heart-right',closed=True)
self.add_line('pelvic-line',(24,38),(24,44))
self.relate('connect','heart','pelvic-line')
'''),
('SQUARE','A curled prescription sheet with an Rx mark and writing lines.','printer: coherent paper contour; source provides Rx letter and curled page.','Two short writing lines retained; small letter proportions are limited by the complete composition.', '''
self.add_bezier('paper-top',(12,12),((12,8),(14,6),(18,6)),((22,6),(28,6),(36,6)))
self.add_bezier('curl-top',(36,6),((40,6),(42,8),(42,12)))
self.add_polyline('curl-bottom',(42,12),(42,18),(34,18))
self.add_bezier('paper-right',(36,6),((34,6),(34,10),(34,14)),((34,22),(34,30),(34,36)),((34,40),(32,42),(28,42)))
self.add_line('paper-bottom',(28,42),(6,42))
self.add_bezier('paper-left',(6,42),((12,42),(12,38),(12,34)),((12,28),(12,20),(12,12)))
self.add_contour('paper','paper-top','paper-right','paper-bottom','paper-left',closed=True)
self.add_contour('curl','curl-top','curl-bottom-1','curl-bottom-2')
self.relate('connect','paper','curl')
self.add_polyline('r-stem',(19,28),(19,22),(19,14),(23,14))
self.add_arc('r-bowl',(23,14),(23,22),radius_x=4)
self.add_line('r-return',(23,22),(19,22))
self.relate('connect','r-stem','r-bowl')
self.relate('connect','r-stem','r-return')
self.relate('connect','r-bowl','r-return')
self.add_polyline('rx-down',(23,22),(26,25),(29,28))
self.add_polyline('rx-up',(23,28),(26,25),(29,22))
self.relate('connect','rx-down','rx-up')
self.relate('connect','rx-down','r-bowl')
self.relate('connect','rx-down','r-return')
for i,end in enumerate((27,23)): self.add_line(f'writing-{i}',(19,33+6*i),(end,33+6*i))
'''),
('SQUARE','An Rx prescription mark inside a rounded square.','Source supplies letter geometry; rounded frame follows the Lucide printer enclosure vocabulary.','No defining features omitted.', '''
self.rounded('frame',6,6,42,42,5)
self.add_polyline('r-upright',(16,33),(16,24),(16,14),(24,14))
self.add_arc('r-bowl',(24,14),(24,24),radius_x=5)
self.add_line('r-return',(24,24),(16,24))
self.relate('connect','r-upright','r-bowl')
self.relate('connect','r-upright','r-return')
self.relate('connect','r-bowl','r-return')
self.add_polyline('rx-down',(24,24),(28,28),(33,33))
self.add_polyline('rx-up',(24,32),(28,28),(32,24))
self.relate('connect','rx-down','rx-up')
self.relate('connect','rx-down','r-bowl')
self.relate('connect','rx-down','r-return')
'''),
('SQUARE','A printer and output sheet crossed by a diagonal slash.','printer: nested input sheet, rounded housing and output sheet; slash keeps the input direction.','Tiny status indicator omitted, as it is absent from the supplied drawing.', '''
self.rounded('printer',6,14,42,34,5)
self.add_polyline('input-paper',(14,14),(14,6),(34,6),(34,14))
self.relate('connect','input-paper','printer')
self.rounded('output-paper',14,26,34,42,3)
self.add_line('disabled-slash',(6,42),(42,6))
'''),
('SQUARE','Two cupped hands holding angle brackets and a code slash.','code: matching opposing chevrons; hand: coherent palm/finger outlines; human reference consulted.','Small thumb creases omitted; code punctuation and both hands retained.', '''
axis=24
self.add_polyline('code-left',(12,6),(6,12),(12,18))
self.add_polyline('code-right',(36,6),(42,12),(36,18))
self.add_line('code-slash',(26,6),(22,18))
for side,sign in [('left',1),('right',-1)]:
    def p(x,y): return (axis+sign*(x-axis),y)
    self.add_bezier('hand-'+side,p(12,42),(p(12,38),p(6,35),p(6,31)),(p(6,28),p(6,26),p(6,25)),(p(6,22),p(10,22),p(10,25)))
    self.add_line('finger-'+side,p(10,25),p(10,31))
    self.add_bezier('palm-'+side,p(10,31),(p(10,28),p(12,27),p(14,29)),(p(16,31),p(20,34),p(20,37)),(p(20,39),p(20,40),p(20,42)))
    self.add_contour('cupped-'+side,'hand-'+side,'finger-'+side,'palm-'+side)
'''),
('SQUARE','A CSS3 shield bearing the angular numeral three.','shield: bilateral tapered enclosure; digit reconstructed by hand from the supplied CSS logo.','No defining features omitted; diagonal numeral is deliberately asymmetric.', '''
axis=24
self.add_polyline('shield',(6,6),(42,6),(38,37),(24,42),(10,37),closed=True)
self.add_polyline('three',(16,15),(32,15),(22,24),(30,24),(28,31),(24,33),(18,31),(17,27))
'''),
]

def author_all():
    for entry, (keyshape, description, reference, omissions, body) in zip(ENTRIES, SPECS):
        directory = Path(entry['result_dir'])
        if (directory/'result.json').exists():
            print('already done:',entry['concept']); continue
        slug = entry['icon_id']
        name = slug.replace('-','_')+'_'+entry['source_uuid'].replace('-','_')+'.py'
        header = f'''"""{description}

Symbol plan: {reference}
Envelope: {keyshape}; derive its bounds from Keyshape.bounds_for(Profile.SOLO48).
Reduction: {omissions}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = {entry['source_uuid']!r}
SOURCE_PATH = {entry['reference_path']!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {slug!r}
    keyshape = Keyshape.{keyshape}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = {tuple(entry['concept'].split())!r}
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
'''
        (directory/name).write_text(header+textwrap.indent(textwrap.dedent(body).strip()+'\n','        ')+HELPERS)
        (directory/'plan.json').write_text(json.dumps(dict(subject=description,keyshape=keyshape,construction_reference=reference,omissions=omissions,python=name),indent=2)+'\n')
        export(entry)

def export(entry):
    directory=Path(entry['result_dir']); slug=entry['icon_id']
    plan=json.loads((directory/'plan.json').read_text())
    path=directory/plan['python']
    try:
        spec=importlib.util.spec_from_file_location('candidate_'+entry['source_uuid'].replace('-','_'),path)
        module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        icon=module.Drawing(); report=icon.validate_icon()
        (directory/'validation.txt').write_text(report.describe()+'\n')
        status=report.status
        svg=icon.to_svg(); (directory/(slug+'.svg')).write_text(svg)
        for theme in ('light','dark'):
            for size in (48,240):
                cairosvg.svg2png(bytestring=svg.encode(),write_to=str(directory/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color='#ffffff' if theme=='light' else '#17191d',negate_colors=theme=='dark')
        (directory/'export-status.json').write_text(json.dumps(dict(status=status,errors=len(report.errors),warnings=len(report.warnings)),indent=2)+'\n')
        print(slug,status,len(report.errors),'errors',len(report.warnings),'warnings',flush=True)
    except Exception:
        error=traceback.format_exc()
        (directory/'error.txt').write_text(error)
        (directory/'export-status.json').write_text(json.dumps(dict(status='error',error=error),indent=2)+'\n')
        print(slug,error,flush=True)

if __name__=='__main__': author_all()
