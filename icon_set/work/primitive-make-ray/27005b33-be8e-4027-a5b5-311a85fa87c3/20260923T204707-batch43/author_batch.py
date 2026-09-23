"""Batch 43: independent SOLO48 models, with no library publication."""
from pathlib import Path
import json, textwrap, importlib.util, traceback
import cairosvg

SOURCE_ICON_ID='27005b33-be8e-4027-a5b5-311a85fa87c3'
SOURCE_PATH='icon_set/work/todo-references/signboard 1_27005b33-be8e-4027-a5b5-311a85fa87c3.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ENTRIES=json.loads((ROOT/'batch-inputs.json').read_text())

HELPERS='''
    def circle(self,name,cx,cy,r):
        points=[(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            member=f'{name}-{i}'
            self.add_arc(member,a,b,radius_x=r);members.append(member)
        self.add_contour(name,*members,closed=True)

    def rounded(self,name,l,t,r,b,rad,breaks=None):
        # One owner for all corner radii and genuine attachment nodes.
        points=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad),(l+rad,t)]
        members=[];breaks=breaks or {}
        for i,(a,z) in enumerate(zip(points,points[1:])):
            if i%2:
                member=f'{name}-{i}';self.add_arc(member,a,z,radius_x=rad);members.append(member)
            else:
                nodes=[a]+breaks.get(i,[])+[z]
                for j,(start,end) in enumerate(zip(nodes,nodes[1:])):
                    if start==end: continue
                    member=f'{name}-{i}-{j}';self.add_line(member,start,end);members.append(member)
        self.add_contour(name,*members,closed=True)

    def wifi(self,name,cx,y,rx,ry):
        self.add_arc(name,(cx-rx,y),(cx+rx,y),radius_x=rx,radius_y=ry)

    def watch(self,circular=False):
        if circular:
            # Circular silhouette with integer attachment knots and continuous tangents.
            self.add_bezier('case-upper-left',(8,24),((8,18),(11,12),(16,10)),((21,8),(22,8),(24,8)))
            self.add_bezier('case-upper-right',(24,8),((26,8),(27,8),(32,10)),((37,12),(40,18),(40,24)))
            self.add_bezier('case-lower-right',(40,24),((40,30),(37,36),(32,38)),((27,40),(26,40),(24,40)))
            self.add_bezier('case-lower-left',(24,40),((22,40),(21,40),(16,38)),((11,36),(8,30),(8,24)))
            self.add_contour('case','case-upper-left','case-upper-right','case-lower-right','case-lower-left',closed=True)
            self.add_polyline('strap-top',(16,10),(18,4),(30,4),(32,10))
            self.add_polyline('strap-bottom',(16,38),(18,44),(30,44),(32,38))
        else:
            self.rounded('case',8,8,40,40,5,breaks={0:[(16,8),(32,8)],4:[(32,40),(16,40)]})
            self.add_polyline('strap-top',(16,8),(17,4),(31,4),(32,8))
            self.add_polyline('strap-bottom',(16,40),(17,44),(31,44),(32,40))
        self.relate('connect','case','strap-top')
        self.relate('connect','case','strap-bottom')

    def dollar(self,cx=24,cy=24):
        self.add_bezier('dollar-upper',(cx+4,cy-6),((cx,cy-9),(cx-5,cy-8),(cx-5,cy-4)),((cx-5,cy-1),(cx-2,cy),(cx,cy)))
        self.add_bezier('dollar-lower',(cx,cy),((cx+3,cy),(cx+5,cy+1),(cx+5,cy+4)),((cx+5,cy+8),(cx,cy+9),(cx-4,cy+6)))
        self.add_contour('dollar','dollar-upper','dollar-lower')
        self.add_polyline('dollar-stem',(cx,cy-10),(cx,cy),(cx,cy+10))
        self.relate('connect','dollar','dollar-stem')

    def pound(self):
        self.add_arc('pound-hook',(30,19),(20,19),radius_x=5,sweep=False)
        self.add_polyline('pound-stem',(20,19),(20,24),(20,29),(18,32),(31,32))
        self.relate('connect','pound-hook','pound-stem')
        self.add_polyline('pound-bar',(16,24),(20,24),(26,24))
        self.relate('connect','pound-bar','pound-stem')
'''

SPECS=[
('HRECT_L','A hanging rectangular sign suspended from a right-side post.','signpost and rectangle-horizontal: shared rails, rounded panel corners, exact hanger nodes.','None.', '''
self.add_polyline('post',(4,8),(10,8),(30,8),(40,8),(44,12),(44,40))
self.rounded('sign',4,16,36,32,3,breaks={0:[(10,16),(30,16)]})
for i,x in enumerate((10,30)):
    self.add_line(f'hanger-{i}',(x,8),(x,16))
    self.relate('connect',f'hanger-{i}','post')
    self.relate('connect',f'hanger-{i}','sign')
'''),
('SQUARE','A broad blank sign on one central upright.','rectangle-horizontal: a coherent rounded rectangular contour with one centered support.','None.', '''
axis=24
self.rounded('board',6,6,42,32,3,breaks={4:[(axis,32)]})
self.add_line('post',(axis,32),(axis,42))
self.relate('connect','post','board')
'''),
('SQUARE','A broad blank sign on one central upright.','rectangle-horizontal: matched corner radii and central support, independently authored for this UUID.','None.', '''
axis=24
self.rounded('board',6,6,42,32,3,breaks={4:[(axis,32)]})
self.add_line('post',(axis,32),(axis,42))
self.relate('connect','post','board')
'''),
('HRECT_L','A wide short signboard on a central stem.','rectangle-horizontal and signpost: short rounded panel over a centered post.','None.', '''
self.rounded('board',4,8,44,26,3,breaks={4:[(24,26)]})
self.add_line('post',(24,26),(24,40))
self.relate('connect','post','board')
'''),
('SQUARE','A neutral human torso beside two checks and a cross.','human_ref/user.svg and full_body_ref.png: circular head and smooth shoulder silhouette; detached ink gap exactly 4.','Fingers and fine anatomy absent from the source remain absent.', '''
axis=15
self.circle('head',axis,12,6)
self.add_arc('shoulder-left',(6,31),(axis,26),radius_x=9,radius_y=5)
self.add_arc('shoulder-right',(axis,26),(24,31),radius_x=9,radius_y=5)
self.add_line('body-right',(24,31),(24,34))
self.add_line('hem-right',(24,34),(20,34))
self.add_line('waist-right',(20,34),(19,42))
self.add_line('body-bottom',(19,42),(11,42))
self.add_line('waist-left',(11,42),(10,34))
self.add_line('hem-left',(10,34),(6,34))
self.add_line('body-left',(6,34),(6,31))
self.add_contour('torso','shoulder-left','shoulder-right','body-right','hem-right','waist-right','body-bottom','waist-left','hem-left','body-left',closed=True)
# Head bottom 18, shoulder apex 26: 8 centerline / 4 visible units.
self.add_polyline('check-top',(34,10),(37,13),(42,7))
self.add_polyline('check-middle',(34,23),(37,26),(42,20))
self.add_polyline('cross-down',(34,34),(38,38),(42,42))
self.add_polyline('cross-up',(34,42),(38,38),(42,34))
self.relate('connect','cross-down','cross-up')
'''),
('SQUARE','A woman-shaped figure beside a three-node hierarchy.','human_ref/user.svg and full_body_ref.png: circular head and simple dress silhouette; workflow: repeated node branches.','None; all three hierarchy nodes are retained.', '''
self.circle('head',15,12,6)
self.add_arc('shoulder-left',(9,28),(15,26),radius_x=6,radius_y=2)
self.add_arc('shoulder-right',(15,26),(21,28),radius_x=6,radius_y=2)
self.add_line('dress-right',(21,28),(24,36))
self.add_line('hem-right',(24,36),(20,36))
self.add_line('leg-right',(20,36),(18,42))
self.add_line('feet',(18,42),(12,42))
self.add_line('leg-left',(12,42),(10,36))
self.add_line('hem-left',(10,36),(6,36))
self.add_line('dress-left',(6,36),(9,28))
self.add_contour('torso','shoulder-left','shoulder-right','dress-right','hem-right','leg-right','feet','leg-left','hem-left','dress-left',closed=True)
# Head bottom 18 to shoulder apex 26 proves the exact detached gap.
ys=(9,24,39)
self.add_polyline('spine',*((32,y) for y in ys))
for i,y in enumerate(ys):
    self.circle(f'node-{i}',39,y,3)
    self.add_line(f'branch-{i}',(32,y),(36,y))
    self.relate('connect',f'branch-{i}','spine')
    self.relate('connect',f'branch-{i}',f'node-{i}')
'''),
('SQUARE','A bedside sleep device with two controls and rising Z marks.','rectangle-horizontal: smooth device enclosure; source supplies control arrangement and Z letterforms.','None; both Z marks, feet, plus control and round control retained.', '''
self.add_line('device-top',(10,26),(22,26))
self.add_arc('device-tl',(6,30),(10,26),radius_x=4)
self.add_line('device-left',(6,36),(6,30))
self.add_arc('device-bl',(10,40),(6,36),radius_x=4)
self.add_polyline('device-bottom',(38,40),(10,40))
self.add_arc('device-br',(42,36),(38,40),radius_x=4)
self.add_line('device-right',(42,28),(42,36))
self.add_contour('device','device-right','device-br','device-bottom-1','device-bl','device-left','device-tl','device-top')
self.contours=[c for c in self.contours if c.contour_id!='device-bottom']
for name,x in [('left',10),('right',38)]:
    self.add_line('foot-'+name,(x,40),(x,42));self.relate('connect','foot-'+name,'device')
self.add_polyline('plus-horizontal',(12,33),(16,33),(20,33))
self.add_polyline('plus-vertical',(16,29),(16,33),(16,37))
self.relate('connect','plus-horizontal','plus-vertical')
self.circle('button',33,33,3)
self.add_polyline('z-small',(25,18),(30,18),(25,24),(30,24))
self.add_polyline('z-big',(34,6),(42,6),(34,16),(42,16))
'''),
('VRECT_L','An open clock face with two hands and rising Z marks.','clock: coherent circular rim and joined hands; source supplies the open upper-right sector.','None.', '''
self.add_arc('clock-right',(40,28),(24,44),radius_x=16)
self.add_arc('clock-bottom',(24,44),(8,28),radius_x=16)
self.add_arc('clock-left',(8,28),(24,12),radius_x=16)
self.add_contour('clock','clock-right','clock-bottom','clock-left')
self.add_polyline('hands',(17,28),(24,28),(27,34))
self.add_polyline('z-small',(26,14),(32,14),(26,22),(32,22))
self.add_polyline('z-big',(34,4),(40,4),(34,12),(40,12))
'''),
('VRECT_L','A smart house with a wireless signal and opposing open chevrons.','house: roof and wall silhouette; wifi: nested radiating arcs.','Tiny wireless dot omitted; two arcs and both opening chevrons retained.', '''
self.wifi('wifi-outer',24,8,10,4)
self.wifi('wifi-inner',24,16,5,2)
self.add_polyline('roof',(8,30),(24,20),(40,30))
self.add_polyline('walls',(10,32),(10,44),(38,44),(38,32))
self.add_polyline('open-left',(20,32),(16,36),(20,40))
self.add_polyline('open-right',(28,32),(32,36),(28,40))
'''),
('SQUARE','A wireless induction stove with sloping top and a segmented front panel.','wifi: nested arcs; rounded appliance corners from refrigerator.','Tiny front dashes and near-invisible wireless point omitted; main panel divisions retained.', '''
self.add_polyline('top',(6,28),(10,6),(38,6),(42,28))
self.add_polyline('front-top',(6,28),(18,28),(30,28),(42,28))
self.add_polyline('front',(42,28),(42,34),(38,38),(30,38),(18,38),(10,38),(6,34),(6,28))
self.relate('connect','top','front-top');self.relate('connect','top','front');self.relate('connect','front-top','front')
for x in (18,30):
    self.add_line(f'division-{x}',(x,28),(x,38));self.relate('connect',f'division-{x}','front-top');self.relate('connect',f'division-{x}','front')
self.add_polyline('base',(10,38),(12,42),(36,42),(38,38))
self.relate('connect','base','front')
self.wifi('wifi-outer',24,16,8,4)
self.wifi('wifi-inner',24,23,4,2)
'''),
('SQUARE','A refrigerator linked wirelessly to a smartphone.','refrigerator: divided tall door; monitor-smartphone: offset device pair; wifi: two quarter arcs.','Tiny extra phone controls omitted; divider, handles and wireless arcs retained.', '''
self.add_line('fridge-top',(10,6),(24,6))
self.add_arc('fridge-tr',(24,6),(28,10),radius_x=4)
self.add_line('fridge-upper-right',(28,10),(28,16))
self.add_line('fridge-bottom',(18,42),(10,42))
self.add_arc('fridge-bl',(10,42),(6,38),radius_x=4)
self.add_line('fridge-left-lower',(6,38),(6,22))
self.add_line('fridge-left-upper',(6,22),(6,10))
self.add_arc('fridge-tl',(6,10),(10,6),radius_x=4)
self.add_contour('fridge','fridge-bottom','fridge-bl','fridge-left-lower','fridge-left-upper','fridge-tl','fridge-top','fridge-tr','fridge-upper-right')
self.add_line('freezer-seam',(6,22),(18,22));self.relate('connect','freezer-seam','fridge')
for i,y in enumerate((12,30)): self.add_line(f'handle-{i}',(12,y),(12,y+4))
self.add_arc('wireless-outer',(16,24),(30,10),radius_x=14)
self.add_arc('wireless-inner',(24,24),(30,18),radius_x=6)
self.rounded('phone',26,22,42,42,3,breaks={2:[(42,34)],6:[(26,34)]})
self.add_line('phone-footer',(26,34),(42,34));self.relate('connect','phone-footer','phone')
'''),
('VRECT_L','A toaster with projecting toast and a wireless control mark.','wifi: radiating arc and point; rounded appliance shell follows refrigerator; bread silhouette from the supplied input.','One inner wireless arc and decorative bottom seam omitted to leave a readable signal and toast.', '''
self.rounded('toaster',8,18,40,44,4,breaks={0:[(14,18),(34,18)]})
self.add_line('toast-left',(14,18),(14,12))
self.add_bezier('toast-top',(14,12),((6,12),(8,4),(16,4)),((20,4),(28,4),(32,4)),((40,4),(42,12),(34,12)))
self.add_line('toast-right',(34,12),(34,18))
self.add_contour('toast','toast-left','toast-top','toast-right')
self.relate('connect','toast','toaster')
self.wifi('wireless-arc',24,29,8,4)
self.add_dot('wireless-point',(24,35))
'''),
('HRECT_L','A wireless television beside a smartphone.','monitor-smartphone: offset screen pair and open overlap region; wifi: arc above the TV.','One inner wireless arc omitted to keep signal-to-screen clearance.', '''
self.add_line('tv-top',(8,18),(23,18))
self.add_arc('tv-tl',(4,22),(8,18),radius_x=4)
self.add_line('tv-left',(4,28),(4,22))
self.add_arc('tv-bl',(8,32),(4,28),radius_x=4)
self.add_line('tv-bottom-1',(18,32),(8,32))
self.add_line('tv-bottom-2',(23,32),(18,32))
self.add_contour('tv','tv-bottom-2','tv-bottom-1','tv-bl','tv-left','tv-tl','tv-top')
self.add_line('stand',(18,32),(18,40));self.relate('connect','stand','tv')
self.add_polyline('stand-foot',(12,40),(18,40),(24,40));self.relate('connect','stand','stand-foot')
self.wifi('wireless-arc',15,10,5,2)
self.rounded('phone',32,16,44,34,3,breaks={2:[(44,26)],6:[(32,26)]})
self.add_line('phone-footer',(32,26),(44,26));self.relate('connect','phone-footer','phone')
'''),
('HRECT_L','A smart-TV app screen with three panels and navigation arrows.','monitor: screen and pedestal; source supplies three content panels and two chevrons.','None.', '''
self.rounded('screen',4,8,44,32,3,breaks={2:[(44,16),(44,24)],4:[(24,32)],6:[(4,24),(4,16)]})
for name,y in [('header',16),('footer',24)]:
    self.add_polyline(name,(4,y),(18,y),(30,y),(44,y));self.relate('connect',name,'screen')
for i,x in enumerate((18,30)):
    self.add_line(f'panel-{i}',(x,16),(x,24));self.relate('connect',f'panel-{i}','header');self.relate('connect',f'panel-{i}','footer')
self.add_polyline('previous',(13,18),(10,20),(13,22))
self.add_polyline('next',(35,18),(38,20),(35,22))
self.add_line('stand',(24,32),(24,40));self.relate('connect','stand','screen')
self.add_polyline('foot',(16,40),(24,40),(32,40));self.relate('connect','stand','foot')
'''),
('VRECT_L','A round smartwatch bearing a euro currency mark.','watch: round case and paired straps; euro: open bowl and horizontal currency stroke.','Second euro bar omitted because the supplied reference has one visible bar.', '''
self.watch(circular=True)
self.add_bezier('euro-upper',(29,17),((22,13),(18,18),(18,24)))
self.add_bezier('euro-lower',(18,24),((18,30),(22,35),(29,31)))
self.add_contour('euro','euro-upper','euro-lower')
self.add_polyline('euro-bar',(15,24),(18,24),(25,24));self.relate('connect','euro','euro-bar')
'''),
('VRECT_L','A square smartwatch bearing a dollar currency mark.','watch: attached symmetric straps; dollar-sign: continuous S curve and crossing vertical stem.','None.', '''
self.watch()
self.dollar()
'''),
('VRECT_L','A square smartwatch bearing a pound currency mark.','watch: attached symmetric straps; pound-sterling: round hook, crossbar and baseline.','None.', '''
self.watch()
self.pound()
'''),
('SQUARE','A smartphone with a dollar banknote protruding to the right.','monitor-smartphone: interrupted phone frame around a foreground object; banknote and dollar-sign: note corners and currency glyph.','No defining features omitted; both corner decorations and dollar symbol retained.', '''
self.add_line('phone-top',(10,6),(22,6))
self.add_arc('phone-tr',(22,6),(26,10),radius_x=4)
self.add_line('phone-upper-right',(26,10),(26,12))
self.add_line('phone-lower-right',(26,34),(26,38))
self.add_arc('phone-br',(26,38),(22,42),radius_x=4)
self.add_line('phone-bottom',(22,42),(10,42))
self.add_arc('phone-bl',(10,42),(6,38),radius_x=4)
self.add_line('phone-left-lower',(6,38),(6,34))
self.add_line('phone-left-upper',(6,34),(6,10))
self.add_arc('phone-tl',(6,10),(10,6),radius_x=4)
self.add_contour('phone','phone-lower-right','phone-br','phone-bottom','phone-bl','phone-left-lower','phone-left-upper','phone-tl','phone-top','phone-tr','phone-upper-right')
self.add_line('phone-footer',(6,34),(26,34));self.relate('connect','phone-footer','phone')
self.rounded('banknote',16,16,42,30,2)
self.dollar(cx=29,cy=23)
for name,a,b in [('tl',(16,22),(22,16)),('tr',(36,16),(42,22)),('br',(42,24),(36,30)),('bl',(22,30),(16,24))]:
    self.add_arc('corner-'+name,a,b,radius_x=6,sweep=False);self.relate('connect','corner-'+name,'banknote')
'''),
('VRECT_L','A blank circular smartwatch face with upper and lower straps.','watch: one circular case with mirrored strap attachments; blank face preserved.','None.', '''
self.watch(circular=True)
'''),
('VRECT_L','A blank circular smartwatch face with upper and lower straps.','watch: one circular case with mirrored strap attachments, independently authored for this source UUID.','None.', '''
self.watch(circular=True)
'''),
]

def export(entry):
    d=Path(entry['result_dir']);slug=entry['icon_id'];plan=json.loads((d/'plan.json').read_text())
    try:
        spec=importlib.util.spec_from_file_location('drawing_'+entry['source_uuid'].replace('-','_'),d/plan['python'])
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        icon=module.Drawing();report=icon.validate_icon();(d/'validation.txt').write_text(report.describe()+'\n')
        svg=icon.to_svg();(d/(slug+'.svg')).write_text(svg)
        for theme in ('light','dark'):
            for size in (48,240):
                cairosvg.svg2png(bytestring=svg.encode(),write_to=str(d/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color='#ffffff' if theme=='light' else '#17191d',negate_colors=theme=='dark')
        (d/'export-status.json').write_text(json.dumps(dict(status=report.status,errors=len(report.errors),warnings=len(report.warnings)),indent=2)+'\n')
        print(slug,entry['source_uuid'][:8],report.status,len(report.errors),'errors',len(report.warnings),'warnings',flush=True)
    except Exception:
        error=traceback.format_exc();(d/'error.txt').write_text(error)
        (d/'export-status.json').write_text(json.dumps(dict(status='error',error=error),indent=2)+'\n');print(slug,error,flush=True)

def author_all():
    for e,(key,subject,reference,omissions,body) in zip(ENTRIES,SPECS):
        d=Path(e['result_dir']);slug=e['icon_id'];name=slug.replace('-','_')+'_'+e['source_uuid'].replace('-','_')+'.py'
        if list(d.parent.glob('*/result.json')): print('already done',slug);continue
        source=f'''"""{subject}
Symbol plan: {reference}
Keyshape: {key}; inspect ink_extremes for the fixed profile envelope.
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
        (d/name).write_text(source+textwrap.indent(textwrap.dedent(body).strip()+'\n','        ')+HELPERS)
        (d/'plan.json').write_text(json.dumps(dict(subject=subject,keyshape=key,construction_reference=reference,omissions=omissions,python=name),indent=2)+'\n')
        export(e)

if __name__=='__main__': author_all()
