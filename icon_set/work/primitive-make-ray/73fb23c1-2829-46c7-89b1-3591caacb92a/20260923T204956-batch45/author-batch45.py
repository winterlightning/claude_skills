import json,textwrap
from pathlib import Path
rs=json.load(open('/tmp/batch45.json'))
AUTHOR='gpt-6'
SOURCE_ICON_ID=[r['source_uuid'] for r in rs]
SOURCE_PATH=[r['reference_path'] for r in rs]
helpers='''
    def box(self,name,l=6,t=6,r=42,b=42,rad=4):
        mx,my=(l+r)//2,(t+b)//2
        pts=[(mx,t),(r-rad,t),(r,t+rad),(r,my),(r,b-rad),(r-rad,b),(mx,b),(l+rad,b),(l,b-rad),(l,my),(l,t+rad),(l+rad,t)]
        for i in range(12):
            a,z=pts[i],pts[(i+1)%12]
            if i in (1,4,7,10):self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(12)),closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def arrow(self,name,start,tip,a,b):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',a,tip,b)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')
'''
specs=[]
def add(subject,plan,ref,code,key='SQUARE',omissions=()):specs.append(dict(subject=subject,plan=plan,construction_reference=ref,code=textwrap.dedent(code).strip(),keyshape=key,omissions=list(omissions)))
add('A rising zigzag trend arrow inside a rounded square.','Rounded square owns a rising zigzag and attached right-angle arrowhead; direction is intentionally asymmetric.','trending-up: zigzag and shared arrow endpoint','''
self.box('frame')
self.add_polyline('trend',(15,30),(21,24),(26,28),(33,18))
self.add_polyline('head',(27,18),(33,18),(33,24))
for i in (1,2):self.relate('connect','trend-3',f'head-{i}')
''')
add('A diagonal up-right arrow inside a rounded square.','Diagonal shaft and equal head arms share an integer tip; frame uses equal corner radii.','square-arrow-out-up-right: diagonal shaft and orthogonal arrowhead','''
self.box('frame',rad=5)
self.arrow('arrow',(15,33),(33,15),(23,15),(33,25))
''')
for variant in range(2):
 add('A square selection boundary with four corner handles.','Four identical rounded square handles derive from two repeated axis positions; connectors meet side midpoints.','square-dashed: discrete perimeter construction; handle geometry uses rounded-square construction','''
for row,y in enumerate((6,34)):
    for col,x in enumerate((6,34)):self.box(f'handle-{row}-{col}',x,y,x+8,y+8,2)
self.add_line('top',(14,10),(34,10))
self.add_line('bottom',(14,38),(34,38))
self.add_line('left',(10,14),(10,34))
self.add_line('right',(38,14),(38,34))
for edge,connections in {
 'top':[('handle-0-0',(2,3)),('handle-0-1',(8,9))],
 'bottom':[('handle-1-0',(2,3)),('handle-1-1',(8,9))],
 'left':[('handle-0-0',(5,6)),('handle-1-0',(0,11))],
 'right':[('handle-0-1',(5,6)),('handle-1-1',(0,11))]}.items():
    for handle,parts in connections:
        for part in parts:self.relate('connect',edge,f'{handle}-{part}')
''')
add('An outlined lightning bolt inside a rounded square.','One closed angular lightning silhouette nested in a rounded square.','zap: alternating diagonal bolt edges and abrupt transverse steps','''
self.box('frame',rad=5)
self.add_polyline('bolt',(27,15),(16,26),(23,26),(21,33),(32,22),(25,22),closed=True)
''')
add('Two facing square brackets.','Mirrored open bracket contours derive from a shared axis and radius.','square-chevron-left: rounded outer corner construction','''
for side in (0,1):
    def p(x,y):return (48-x if side else x,y)
    n=f'bracket-{side}'
    self.add_line(n+'-top',p(14,6),p(10,6))
    self.add_arc(n+'-upper',p(10,6),p(6,10),radius_x=4,sweep=bool(side))
    self.add_line(n+'-side',p(6,10),p(6,38))
    self.add_arc(n+'-lower',p(6,38),p(10,42),radius_x=4,sweep=bool(side))
    self.add_line(n+'-bottom',p(10,42),p(14,42))
    self.add_contour(n,*(n+s for s in ('-top','-upper','-side','-lower','-bottom')))
''')
add('A square speech bubble containing a user bust.','Rounded bubble with lower-left tail encloses circular head and symmetric shoulder arch; detached head/shoulder ink gap exactly four.','human_ref/user.svg: circular head and broad shoulder arch; message-square: integrated speech tail','''
self.add_line('top',(10,6),(38,6))
self.add_arc('upper-right',(38,6),(42,10),radius_x=4)
self.add_line('right',(42,10),(42,32))
self.add_arc('lower-right',(42,32),(38,36),radius_x=4)
self.add_polyline('tail',(38,36),(24,36),(16,42),(16,36),(10,36))
self.add_arc('lower-left',(10,36),(6,32),radius_x=4)
self.add_line('left',(6,32),(6,10))
self.add_arc('upper-left',(6,10),(10,6),radius_x=4)
self.add_contour('bubble','top','upper-right','right','lower-right',*(f'tail-{i}' for i in range(1,5)),'lower-left','left','upper-left',closed=True)
self.circle('head',24,16,3)
# Head lower centerline y19; shoulder apex y27. 27-19-4 = 4 ink units.
self.add_arc('shoulders-left',(16,33),(24,27),radius_x=8,radius_y=6)
self.add_arc('shoulders-right',(24,27),(32,33),radius_x=8,radius_y=6)
self.add_contour('shoulders','shoulders-left','shoulders-right')
''')
# Replace tail shorthand with individual lines before collecting its larger contour.
specs[-1]['code']=specs[-1]['code'].replace("self.add_polyline('tail',(38,36),(24,36),(16,42),(16,36),(10,36))","tail_points=[(38,36),(24,36),(16,42),(16,36),(10,36)]\nfor i in range(4):self.add_line(f'tail-{i+1}',tail_points[i],tail_points[i+1])")
add('A next-track button with a triangle and terminal bar.','Square enclosure holds a closed play triangle and a distinct vertical terminal.','square-code: separated interior symbols inside a rounded square','''
self.box('frame',rad=3)
self.add_polyline('play',(15,15),(24,24),(15,33),closed=True)
self.add_line('terminal',(33,15),(33,33))
''')
add('A down arrow inside a rounded square.','Centered vertical shaft shares a symmetrical chevron tip; shaft retained from reference.','square-chevron-left: geometric chevron and rounded frame','''
self.box('frame')
self.arrow('down',(24,15),(24,33),(16,25),(32,25))
''')
add('A left arrow inside a rounded square.','Centered horizontal shaft shares a symmetrical leftward chevron tip.','square-chevron-left: mirrored chevron construction','''
self.box('frame')
self.arrow('left',(33,24),(15,24),(23,16),(23,32))
''')
add('A checkmark inside a rounded square.','Asymmetric check preserves short downstroke and longer rising stroke within equal frame margins.','square-check: two coherent straight runs with a rounded join','''
self.box('frame',rad=5)
self.add_polyline('check',(15,25),(21,31),(33,19))
''')
add('A left-pointing arrow inside a rounded square.','Reference includes a shaft, retained with symmetrical chevron arms.','square-chevron-left: left chevron construction','''
self.box('frame',rad=5)
self.arrow('left',(33,24),(15,24),(24,15),(24,33))
''')
add('A right-pointing arrow inside a rounded square.','Reference includes a shaft; left-arrow definition reflected around x24.','square-chevron-right: right chevron construction','''
self.box('frame',rad=5)
self.arrow('right',(15,24),(33,24),(24,15),(24,33))
''')
add('An upward chevron inside a rounded square.','One open chevron with mirrored arms and a centered apex.','square-chevron-up: mirrored open chevron','''
self.box('frame')
self.add_polyline('chevron',(15,28),(24,19),(33,28))
''')
add('Two code chevrons inside a circular border.','Circular enclosure retained despite filename; paired chevrons reflect about x24 with an eight-unit center gap.','square-code: paired mirrored angle brackets','''
self.circle('frame',24,24,20)
for side in (0,1):
    def p(x,y):return (48-x if side else x,y)
    self.add_polyline(f'chevron-{side}',p(20,16),p(13,24),p(20,32))
''',key='CIRCLE')
add('Code angle brackets and a diagonal slash inside a rounded square.','Paired angle brackets reflect about x24; separate rising slash preserves reference code syntax.','square-code: paired angle brackets within rounded enclosure','''
self.box('frame',rad=5)
for side in (0,1):
    def p(x,y):return (48-x if side else x,y)
    self.add_polyline(f'chevron-{side}',p(19,18),p(14,24),p(19,30))
self.add_line('slash',(27,15),(21,33))
''')
add('A plus inside a dashed circular ring inside a rounded square.','Eight short ring dashes use cardinal and diagonal integer circle points; plus shares its center.','square-dashed: spaced dash series; rounded-square outer contour','''
self.box('frame',rad=5)
# Integer Pythagorean points on the radius-10 ring preserve one center.
pairs=[((21,14),(27,14)),((30,16),(32,18)),((34,21),(34,27)),((32,30),(30,32)),((27,34),(21,34)),((18,32),(16,30)),((14,27),(14,21)),((16,18),(18,16))]
for i,(a,b) in enumerate(pairs):self.add_line(f'dash-{i}',a,b)
self.add_polyline('plus-h',(20,24),(24,24),(28,24))
self.add_polyline('plus-v',(24,20),(24,24),(24,28))
for a in (1,2):
    for b in (1,2):self.relate('connect',f'plus-h-{a}',f'plus-v-{b}')
''',omissions=['Reduced dashed ring to eight repeated marks.'])
add('A square button containing a two-panel rectangle.','Nested rectangular panel has a horizontal divider at its midpoint; this preserves the drawing rather than interpreting the filename as arithmetic.','square-divide: rounded enclosure only; interior follows supplied two-panel reference','''
self.box('frame',rad=5)
self.add_polyline('panel',(15,15),(33,15),(33,24),(33,33),(15,33),(15,24),closed=True)
self.add_line('divider',(15,24),(33,24))
for part in (2,3,5,6):self.relate('connect','divider',f'panel-{part}')
''')
for full in (False,True):
 add('A dollar sign inside a '+('rounded' if full else 'slightly rounded')+' square.','Smooth S consists of four tangent cubic runs; '+('continuous vertical stem splits at all real S junctions.' if full else 'short upper and lower stem extensions preserve the open center of the reference.'),'No local square-dollar-sign match found; rounded-square construction follows square-check, and S is hand-authored from the supplied reference.',f'''
self.box('frame',rad={5 if full else 2})
self.add_bezier('s-top',(30,18),((28,16),(26,16),(24,16)))
self.add_bezier('s-upper',(24,16),((16,16),(16,22),(24,24)))
self.add_bezier('s-lower',(24,24),((32,26),(32,32),(24,32)))
self.add_bezier('s-bottom',(24,32),((22,32),(20,32),(18,30)))
self.add_contour('s','s-top','s-upper','s-lower','s-bottom')
self.add_line('stem-top',(24,15),(24,16))
self.add_line('stem-bottom',(24,32),(24,33))
for part in ('s-top','s-upper'):self.relate('connect','stem-top',part)
for part in ('s-lower','s-bottom'):self.relate('connect','stem-bottom',part)
if {full!r}:
    self.add_line('stem-upper',(24,16),(24,24))
    self.add_line('stem-lower',(24,24),(24,32))
    for part in ('s-top','s-upper','s-lower'):self.relate('connect','stem-upper',part)
    for part in ('s-upper','s-lower','s-bottom'):self.relate('connect','stem-lower',part)
    self.relate('connect','stem-top','stem-upper')
    self.relate('connect','stem-upper','stem-lower')
    self.relate('connect','stem-lower','stem-bottom')
''')
assert len(specs)==20
for r,s in zip(rs,specs):
 out=Path(r['result_dir']);r.update({k:v for k,v in s.items() if k!='code'});r['module']=r['icon_id'].replace('-','_')+'_'+r['source_uuid'].replace('-','_')+'.py'
 source=f'''"""{s['subject']}\nPlan: {s['plan']}\nConstruction: {s['construction_reference']}\nEnvelope: {'radius 22 about (24,24)' if s['keyshape']=='CIRCLE' else 'visible (4,4)-(44,44); centerlines (6,6)-(42,42)'}.\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n\nSOURCE_ICON_ID = {r['source_uuid']!r}\nSOURCE_PATH = {r['reference_path']!r}\nAUTHOR = {AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id = {r['icon_id']!r}\n    keyshape = Keyshape.{s['keyshape']}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = 'objects/interface'\n    aliases = ()\n    keywords = {tuple(r['concept'].split())!r}\n\n    def build(self):\n'''+textwrap.indent(s['code'],'        ')+'\n'+helpers
 (out/r['module']).write_text(source)
Path('/tmp/batch45.json').write_text(json.dumps(rs,indent=2))
print('Authored 20 modules in supplied order.')
