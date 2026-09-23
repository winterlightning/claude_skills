"""Standalone batch 48 originals and evidence; no publishing or registry work."""
from pathlib import Path
import importlib.util,json,textwrap,traceback
import cairosvg
SOURCE_ICON_ID='08acfc76-564e-418d-abde-1f5766d10cdc'
SOURCE_PATH='icon_set/work/todo-references/square xmark_08acfc76-564e-418d-abde-1f5766d10cdc.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ENTRIES=json.loads((ROOT/'batch-inputs.json').read_text())

HELPERS='''
    def circle(self,name,cx,cy,r):
        pts=[(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            m=f'{name}-{i}';self.add_arc(m,a,b,radius_x=r);members.append(m)
        self.add_contour(name,*members,closed=True)

    def rounded(self,name,l,t,r,b,rad,breaks=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad),(l+rad,t)]
        members=[];breaks=breaks or {}
        for i,(a,z) in enumerate(zip(pts,pts[1:])):
            if i%2:
                m=f'{name}-{i}';self.add_arc(m,a,z,radius_x=rad);members.append(m)
            else:
                nodes=[a]+breaks.get(i,[])+[z]
                for j,(start,end) in enumerate(zip(nodes,nodes[1:])):
                    if start==end:continue
                    m=f'{name}-{i}-{j}';self.add_line(m,start,end);members.append(m)
        self.add_contour(name,*members,closed=True)

    def portrait(self,style):
        # Shared circular jaw and natural neck, with exact 6-8-10 jaw/neck nodes.
        # These references show connected anatomy: there is no detached-head gap.
        jaw=[(12,16),(16,24),(22,26),(28,24),(32,16)]
        members=[]
        for i,(a,b) in enumerate(zip(jaw,jaw[1:])):
            m=f'jaw-{i}';self.add_arc(m,a,b,radius_x=10,sweep=False);members.append(m)
        if style in ('bald','boy'):
            self.add_arc('head-top',(32,16),(12,16),radius_x=10,sweep=False)
        else:
            self.add_bezier('head-top',(32,16),((29,15),(28,12),(26,10)),((22,15),(17,16),(12,16)))
        self.add_contour('head',*members,'head-top',closed=True)
        if style=='boy':
            self.add_bezier('fringe',(12,16),((15,12),(16,16),(21,15)),((25,15),(27,12),(28,12)),((30,13),(31,15),(32,16)))
            self.relate('connect','fringe','head')
        self.add_line('neck-left',(16,24),(16,28))
        self.add_arc('neck-lower-left',(16,28),(22,34),radius_x=6,sweep=False)
        self.add_arc('neck-lower-right',(22,34),(28,28),radius_x=6,sweep=False)
        self.add_line('neck-right',(28,28),(28,24))
        self.add_contour('neck','neck-left','neck-lower-left','neck-lower-right','neck-right')
        self.relate('connect','head','neck')
        self.add_bezier('shoulder-left-top',(16,28),((13,28),(12,28),(10,30)))
        self.add_bezier('shoulder-left-lower',(10,30),((7,32),(6,34),(6,36)))
        self.add_line('body-left',(6,36),(6,42))
        self.add_line('body-bottom',(6,42),(37,42))
        self.add_contour('body-left-outline','shoulder-left-top','shoulder-left-lower','body-left','body-bottom')
        self.add_bezier('shoulder-right-top',(28,28),((31,28),(32,28),(34,30)))
        self.add_bezier('shoulder-right-lower',(34,30),((35,31),(36,31),(37,32)))
        self.add_contour('body-right-outline','shoulder-right-top','shoulder-right-lower')
        for body in ('body-left-outline','body-right-outline'):self.relate('connect','neck',body)
        self.circle('relationship-badge',37,37,5)
        self.relate('connect','relationship-badge','body-left-outline')
        self.relate('connect','relationship-badge','body-right-outline')
        if style=='bob':
            self.add_bezier('hair',(16,28),((10,28),(8,28),(10,22)),((10,10),(12,6),(22,6)),((32,6),(34,10),(34,22)),((36,28),(34,28),(28,28)))
            self.relate('connect','hair','neck')
            self.relate('connect','hair','body-left-outline')
            self.relate('connect','hair','body-right-outline')
        if style=='long':
            self.add_bezier('hair',(10,30),((11,25),(10,17),(12,12)),((14,7),(17,6),(22,6)),((27,6),(30,7),(32,12)),((34,17),(33,25),(34,30)))
            self.relate('connect','hair','body-left-outline')
            self.relate('connect','hair','body-right-outline')
'''

SPECS=[
('SQUARE','A cancellation cross inside a rounded square.','square-x: paired diagonals and a shared-radius frame.','None.', '''
self.rounded('frame',6,6,42,42,5)
self.add_polyline('cross-down',(16,16),(24,24),(32,32))
self.add_polyline('cross-up',(16,32),(24,24),(32,16))
self.relate('connect','cross-down','cross-up')
'''),
('SQUARE','A single horizontal bar inside a rounded square.','square-minus: a centered bar in a rounded enclosure.','None. The supplied drawing contains a bar, not the letter Y.', '''
self.rounded('frame',6,6,42,42,5)
self.add_line('bar',(15,24),(33,24))
'''),
('SQUARE','A horizontal bar above a small circle inside a rounded square.','square-minus: frame and horizontal stroke; circle construction follows the source.','None. The supplied drawing contains a bar and circle, not the letter Z.', '''
self.rounded('frame',6,6,42,42,5)
self.add_line('bar',(15,15),(33,15))
self.circle('circle',24,29,4)
'''),
('SQUARE','A hand gripping a phone with inward-pointing arrows on both sides.','smartphone: tall frame; hand and human references: coherent finger contours.','None; four fingers, thumb, wrist and both arrows retained.', '''
self.rounded('phone',14,6,34,42,3,breaks={2:[(34,18),(34,36)],6:[(14,36)]})
self.add_line('phone-footer',(14,36),(34,36));self.relate('connect','phone-footer','phone')
for i,(top,bottom) in enumerate(((16,22),(22,28),(28,34),(34,40))):
    self.rounded(f'finger-{i}',8,top,22,bottom,3)
    if i:self.relate('connect',f'finger-{i-1}',f'finger-{i}')
self.add_bezier('thumb',(34,18),((40,18),(36,27),(42,30)))
self.relate('connect','thumb','phone')
self.add_line('wrist',(34,36),(42,40));self.relate('connect','wrist','phone')
self.add_polyline('arrow-left-head',(6,6),(10,10),(6,14))
self.add_line('arrow-left-shaft',(6,10),(10,10));self.relate('connect','arrow-left-head','arrow-left-shaft')
self.add_polyline('arrow-right-head',(42,6),(38,10),(42,14))
self.add_line('arrow-right-shaft',(42,10),(38,10));self.relate('connect','arrow-right-head','arrow-right-shaft')
'''),
('VRECT_M','A phone displaying paired inward-curving squeeze marks.','smartphone: rounded vertical enclosure; source supplies four mirrored pressure curves.','None; all four squeeze strokes and the footer are retained.', '''
self.rounded('phone',10,4,38,44,4,breaks={2:[(38,36)],6:[(10,36)]})
self.add_line('footer',(10,36),(38,36));self.relate('connect','footer','phone')
axis=24
for side,sign in [('left',1),('right',-1)]:
    def p(x,y):return (axis+sign*(x-axis),y)
    self.add_bezier('pressure-outer-'+side,p(16,14),(p(23,21),p(23,25),p(16,32)))
    self.add_bezier('pressure-inner-'+side,p(14,18),(p(18,22),p(18,25),p(14,28)))
'''),
('SQUARE','Scissors beside a diagonally oriented female medical symbol.','scissors: circular handles and crossing blades; source supplies the open ring and oblique cross.','None; the complete combined medical symbol is retained.', '''
self.circle('handle-left',10,38,4)
self.circle('handle-right',26,38,4)
self.add_line('blade-left-lower',(14,38),(14,30))
self.add_bezier('blade-left-upper',(14,30),((14,22),(16,14),(18,6)))
self.add_bezier('blade-right-upper',(18,6),((21,16),(22,22),(22,24)))
self.add_line('blade-right-lower',(22,24),(22,38))
self.add_contour('blades','blade-left-lower','blade-left-upper','blade-right-upper','blade-right-lower')
self.add_line('cutting-edge',(14,30),(22,24));self.relate('connect','cutting-edge','blades')
for h in ('handle-left','handle-right'):self.relate('connect',h,'blades')
self.add_arc('female-ring-top',(24,16),(30,18),radius_x=10)
self.add_arc('female-ring-right',(30,18),(34,26),radius_x=10)
self.add_arc('female-ring-bottom',(34,26),(30,34),radius_x=10)
self.add_contour('female-ring','female-ring-top','female-ring-right','female-ring-bottom')
self.add_polyline('female-stem',(30,18),(38,10),(42,6))
self.add_polyline('female-crossbar',(34,6),(38,10),(42,14))
self.relate('connect','female-stem','female-ring');self.relate('connect','female-stem','female-crossbar')
'''),
('VRECT_L','Three descending stacked columns with two curved unstacking arrows.','columns-3: equal-width column modules; source supplies the stepped arrangement and curved arrows.','None; both arrows and all five block cells retained.', '''
width=8
for i,(x,y,height) in enumerate(((8,4,16),(16,20,16),(24,36,8))):
    self.add_polyline(f'column-{i}',(x,y),(x+width,y),(x+width,y+height),(x,y+height),closed=True)
    if height==16:
        self.add_line(f'divider-{i}',(x,y+8),(x+width,y+8));self.relate('connect',f'divider-{i}',f'column-{i}')
    if i:self.relate('connect',f'column-{i-1}',f'column-{i}')
self.add_arc('arrow-upper-start',(28,10),(34,16),radius_x=6)
self.add_line('arrow-upper-middle',(34,16),(34,20))
self.add_arc('arrow-upper-end',(34,20),(28,26),radius_x=6)
self.add_contour('arrow-upper','arrow-upper-start','arrow-upper-middle','arrow-upper-end')
self.add_polyline('arrow-upper-head',(32,22),(28,26),(32,30));self.relate('connect','arrow-upper','arrow-upper-head')
self.add_bezier('arrow-lower',(34,26),((40,26),(40,30),(40,32)),((40,38),(38,40),(34,40)))
self.add_polyline('arrow-lower-head',(38,36),(34,40),(38,44));self.relate('connect','arrow-lower','arrow-lower-head')
'''),
('VRECT_L','Three round anthers on branching filaments above a rounded base.','sprout: smooth shared stem construction; source supplies the three-anther botanical arrangement.','Dashed lower stem made continuous; all three anthers and the base remain.', '''
axis=24
for name,cx,cy in [('left',11,13),('middle',24,7),('right',37,13)]:self.circle('anther-'+name,cx,cy,3)
self.add_bezier('filament-left',(11,16),((17,20),(20,24),(axis,28)))
self.add_line('filament-middle',(axis,10),(axis,28))
self.add_bezier('filament-right',(37,16),((31,20),(28,24),(axis,28)))
for name in ('left','middle','right'):self.relate('connect','anther-'+name,'filament-'+name)
for a,b in [('left','middle'),('middle','right'),('left','right')]:self.relate('connect','filament-'+a,'filament-'+b)
self.add_line('stem',(axis,28),(axis,36))
for name in ('left','middle','right'):self.relate('connect','stem','filament-'+name)
self.rounded('base',16,36,32,44,4,breaks={0:[(24,36)]});self.relate('connect','stem','base')
'''),
('SQUARE','A folded map beside a four-node machine-learning network.','map: fold ownership; network: nodes joined at shared endpoints.','None; map and all four connected nodes remain.', '''
self.add_polyline('map',(14,28),(6,24),(6,6),(16,10),(26,6),(26,20))
self.add_line('map-fold',(16,10),(16,23));self.relate('connect','map','map-fold')
self.circle('node-main',24,28,5)
self.circle('node-upper',36,16,3)
self.circle('node-right',39,28,3)
self.circle('node-lower',36,39,3)
edges=[('upper',(24,23),(33,16),'node-main','node-upper'),('middle',(29,28),(36,28),'node-main','node-right'),('lower',(24,33),(33,39),'node-main','node-lower'),('right-upper',(36,19),(39,25),'node-upper','node-right'),('right-lower',(39,31),(39,39),'node-right','node-lower')]
for name,a,b,node_a,node_b in edges:
    self.add_line('edge-'+name,a,b);self.relate('connect','edge-'+name,node_a);self.relate('connect','edge-'+name,node_b)
'''),
('SQUARE','A bob-haired sister portrait with an empty lower-right relationship badge.','human_ref/user.svg: broad smooth shoulders; circular jaw with natural source neck; source owns the bob and badge.','Fine facial detail absent from the input remains absent; badge kept empty.', '''
self.portrait('bob')
'''),
('SQUARE','A boy portrait with a swept fringe and an empty relationship badge.','human_ref/user.svg: circular head and broad shoulders; source supplies the hair sweep, connected neck and badge.','Fine facial detail absent from the input remains absent; badge kept empty.', '''
self.portrait('boy')
'''),
('SQUARE','A bald uncle portrait with an empty lower-right relationship badge.','human_ref/user.svg: circular head and broad shoulders; source supplies the connected neck and badge.','Fine facial detail absent from the input remains absent; badge kept empty.', '''
self.portrait('bald')
'''),
('SQUARE','A long-haired daughter portrait with an empty relationship badge.','human_ref/user.svg: circular jaw and broad shoulders; source supplies long hair, connected neck and badge.','Fine facial detail absent from the input remains absent; badge kept empty.', '''
self.portrait('long')
'''),
('CIRCLE','A story button with an inner circle and interrupted outer ring.','circle-dashed: coherent long arc and separate short marks.','No defining feature omitted; three short outer marks remain.', '''
self.add_arc('outer-long',(36,8),(8,36),radius_x=20,large_arc=True)
self.add_line('outer-left-dash',(5,20),(5,23))
self.add_line('outer-diagonal-dash',(8,13),(10,10))
self.add_line('outer-top-dash',(18,5),(22,5))
self.circle('inner-ring',24,24,11)
'''),
('SQUARE','A round empty strainer head with a diagonal open handle.','search: circular head joined to a diagonal handle; source has no mesh, so none is invented.','None; empty round head and outlined handle retained.', '''
# The 5-12-13 circle nodes own the two exact handle attachments.
pts=[(17,24),(24,31),(42,19),(29,6),(17,24)]
members=[]
for i,(a,b) in enumerate(zip(pts,pts[1:])):
    name=f'rim-{i}';self.add_arc(name,a,b,radius_x=13,sweep=False);members.append(name)
self.add_contour('rim',*members,closed=True)
self.add_line('handle-left',(17,24),(9,32))
self.add_bezier('handle-cap',(9,32),((7,34),(6,35),(6,37)),((6,40),(8,42),(11,42)),((13,42),(14,41),(16,39)))
self.add_line('handle-right',(16,39),(24,31))
self.add_contour('handle','handle-left','handle-cap','handle-right')
self.relate('connect','rim','handle')
'''),
('SQUARE','A standing person beside a map pin and street lines.','human_ref/full_body_ref.png: circular head and simple coherent limbs; map-pin: teardrop marker.','Outlined trouser/arm detail reduced to the shared stick-figure vocabulary; both street lines and pin center retained.', '''
self.circle('head',14,11,5)
self.add_line('torso',(14,24),(14,32))
self.add_polyline('arms',(6,32),(8,24),(14,24),(20,24),(22,32))
self.relate('connect','arms','torso')
self.add_polyline('legs',(8,42),(14,32),(20,42));self.relate('connect','legs','torso')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
# Head bottom 16, actual torso start 24 -> 8 centerline / 4 ink gap.
self.add_polyline('street-baseline',(6,42),(8,42),(20,42),(42,42));self.relate('connect','legs','street-baseline')
self.add_line('street-upper',(28,34),(42,34))
self.add_bezier('pin-top',(30,16),((30,8),(42,8),(42,16)))
self.add_line('pin-right',(42,16),(36,26))
self.add_line('pin-left',(36,26),(30,16))
self.add_contour('pin','pin-top','pin-right','pin-left',closed=True)
self.circle('pin-center',36,15,2)
'''),
('SQUARE','A side-profile head containing plus, minus and multiplication marks.','human reference and brain: smooth cranial contour; source supplies all three math operators.','None; all three math marks remain.', '''
self.add_polyline('neck-front',(18,42),(18,34),(14,34))
self.add_bezier('chin',(14,34),((10,34),(10,32),(10,28)))
self.add_polyline('face',(10,28),(6,28),(10,18))
self.add_bezier('forehead',(10,18),((10,8),(19,6),(25,6)))
self.add_bezier('cranium',(25,6),((35,6),(42,14),(42,22)))
self.add_bezier('head-back',(42,22),((42,29),(36,32),(36,36)))
self.add_line('neck-back',(36,36),(36,42))
self.add_contour('head','neck-front-1','neck-front-2','chin','face-1','face-2','forehead','cranium','head-back','neck-back')
self.contours=[c for c in self.contours if c.contour_id not in ('neck-front','face')]
self.add_polyline('plus-horizontal',(21,17),(24,17),(27,17))
self.add_polyline('plus-vertical',(24,14),(24,17),(24,20));self.relate('connect','plus-horizontal','plus-vertical')
self.add_line('minus',(18,28),(24,28))
self.add_polyline('multiply-down',(31,25),(34,28),(37,31))
self.add_polyline('multiply-up',(31,31),(34,28),(37,25));self.relate('connect','multiply-down','multiply-up')
'''),
('SQUARE','A rounded speech bubble containing a forward slash.','message-square: coherent bubble with one tail; source supplies the internal slash.','None; the slash is inside the bubble as shown in the input.', '''
self.add_line('bubble-top',(12,6),(36,6))
self.add_arc('bubble-tr',(36,6),(42,12),radius_x=6)
self.add_line('bubble-right',(42,12),(42,28))
self.add_arc('bubble-br',(42,28),(36,34),radius_x=6)
self.add_line('tail-right',(36,34),(36,42))
self.add_line('tail-left',(36,42),(28,34))
self.add_line('bubble-bottom',(28,34),(12,34))
self.add_arc('bubble-bl',(12,34),(6,28),radius_x=6)
self.add_line('bubble-left',(6,28),(6,12))
self.add_arc('bubble-tl',(6,12),(12,6),radius_x=6)
self.add_contour('bubble','bubble-top','bubble-tr','bubble-right','bubble-br','tail-right','tail-left','bubble-bottom','bubble-bl','bubble-left','bubble-tl',closed=True)
self.add_line('slash',(15,25),(31,15))
'''),
]

def export(e):
    d=Path(e['result_dir']);slug=e['icon_id'];plan=json.loads((d/'plan.json').read_text())
    try:
        spec=importlib.util.spec_from_file_location('draw_'+e['source_uuid'].replace('-','_'),d/plan['python'])
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        icon=module.Drawing();report=icon.validate_icon();(d/'validation.txt').write_text(report.describe()+'\n')
        svg=icon.to_svg();(d/(slug+'.svg')).write_text(svg)
        for theme in ('light','dark'):
            for size in (48,240):cairosvg.svg2png(bytestring=svg.encode(),write_to=str(d/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color='#ffffff' if theme=='light' else '#17191d',negate_colors=theme=='dark')
        (d/'export-status.json').write_text(json.dumps(dict(status=report.status,errors=len(report.errors),warnings=len(report.warnings)),indent=2)+'\n')
        print(e['position'],slug,report.status,len(report.errors),'errors',len(report.warnings),'warnings',flush=True)
    except Exception:
        error=traceback.format_exc();(d/'error.txt').write_text(error);(d/'export-status.json').write_text(json.dumps(dict(status='error',error=error),indent=2)+'\n');print(slug,error,flush=True)

def author_all():
    for e,(key,subject,reference,omissions,body) in zip(ENTRIES,SPECS):
        d=Path(e['result_dir']);slug=e['icon_id'];name=slug.replace('-','_')+'_'+e['source_uuid'].replace('-','_')+'.py'
        if list(d.parent.glob('*/result.json')):print('already done',slug);continue
        header=f'''"""{subject}
Symbol plan: {reference}
Keyshape: {key}; fixed profile bounds are recorded in ink_extremes.
Reduction: {omissions}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={e['source_uuid']!r}
SOURCE_PATH={e['reference_path']!r}
AUTHOR={AUTHOR!r}

class Drawing(Solo48):
    icon_id={slug!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords={tuple(e['concept'].split())!r}
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
'''
        (d/name).write_text(header+textwrap.indent(textwrap.dedent(body).strip()+'\n','        ')+HELPERS)
        (d/'plan.json').write_text(json.dumps(dict(subject=subject,keyshape=key,construction_reference=reference,omissions=omissions,python=name),indent=2)+'\n');export(e)

if __name__=='__main__':author_all()
