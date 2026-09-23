import json,textwrap
from pathlib import Path
records=json.load(open('/tmp/batch39.json'))
AUTHOR='gpt-6'
SOURCE_ICON_ID=[r['source_uuid'] for r in records]
SOURCE_PATH=[r['reference_path'] for r in records]
helpers='''
    def circle(self, name, x, y, r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, l, t, r, b, rad=2):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        for i in range(8):
            a,z=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

    def arrow(self, name, start, tip, wing1, wing2):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',wing1,tip,wing2)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')

    def heart(self, name, x, top, half, bottom):
        # Mirrored lobes share dimensions and meet the pointed lower silhouette.
        self.add_bezier(name+'-left',(x,top+2),((x-half,top-5),(x-half-3,top+4),(x-half,top+7)),((x-half+2,top+10),(x, bottom),(x,bottom)))
        self.add_bezier(name+'-right',(x,bottom),((x,bottom),(x+half-2,top+10),(x+half,top+7)),((x+half+3,top+4),(x+half,top-5),(x,top+2)))
        self.add_contour(name,name+'-left',name+'-right',closed=True)
'''
specs=[]
def add(key,summary,plan,ref,omissions,code):specs.append((key,summary,plan,ref,omissions,textwrap.dedent(code)))
add('HRECT_M','A deletion cross beside two spreadsheet row rules.','Two row rules share endpoints; cross is centered beside their gap.','table: straight repeated rules',[],'''
self.add_line('row-top',(24,10),(44,10))
self.add_line('row-bottom',(24,38),(44,38))
self.add_polyline('cross-a',(4,18),(10,24),(16,30))
self.add_polyline('cross-b',(4,30),(10,24),(16,18))
for a in (1,2):
    for b in (1,2):self.relate('connect',f'cross-a-{a}',f'cross-b-{b}')
''')
add('SQUARE','Two stacked items with a downward reorder arrow.','Equal rounded rectangles share width and corner radius; arrow remains directional.','arrow-down: shared shaft and chevron tip',[],'''
for i,y in enumerate((6,28)):self.box(f'item-{i}',6,y,18,y+14)
self.arrow('down',(34,6),(34,42),(26,34),(42,34))
''')
add('SQUARE','A spreadsheet with horizontal and vertical expansion arrows.','A two-by-two table and two orthogonal double arrows share outer limits.','table and expand: connected orthogonal grid and arrowheads',['Reduced spreadsheet from three columns to two.'],'''
self.add_polyline('table',(6,6),(18,6),(30,6),(30,18),(30,30),(18,30),(6,30),(6,18),closed=True)
self.add_polyline('vertical',(18,6),(18,18),(18,30))
self.add_polyline('horizontal',(6,18),(18,18),(30,18))
for a in ('vertical-1','vertical-2'):
    for b in ('horizontal-1','horizontal-2'):self.relate('connect',a,b)
for a,bs in [('vertical-1',['table-1','table-2']),('vertical-2',['table-5','table-6']),('horizontal-1',['table-7','table-8']),('horizontal-2',['table-3','table-4'])]:
    for b in bs:self.relate('connect',a,b)
self.arrow('right',(6,42),(30,42),(26,38),(26,46))
self.add_polyline('left-head',(10,38),(6,42),(10,46))
self.relate('connect','right-shaft','left-head-1');self.relate('connect','right-shaft','left-head-2')
self.arrow('up',(42,30),(42,6),(38,10),(46,10))
self.add_polyline('down-head',(38,26),(42,30),(46,26))
self.relate('connect','up-shaft','down-head-1');self.relate('connect','up-shaft','down-head-2')
''')
# Keep arrow heads inside the square envelope; grid occupies the upper-left area.
specs[-1]=(*specs[-1][:-1],specs[-1][-1].replace('(6,42),(30,42),(26,38),(26,46)','(6,38),(30,38),(26,34),(26,42)').replace('(10,38),(6,42),(10,46)','(10,34),(6,38),(10,42)').replace('(42,30),(42,6),(38,10),(46,10)','(38,30),(38,6),(34,10),(42,10)').replace('(38,26),(42,30),(46,26)','(34,26),(38,30),(42,26)'))
add('VRECT_L','A portable outdoor restroom with a triangular door sign.','Symmetric domed cabin owns a nested doorway and triangle.','house: continuous enclosure and open doorway',['Omitted tiny door handle.'],'''
self.add_arc('roof-left',(8,12),(16,4),radius_x=8)
self.add_line('roof-top',(16,4),(32,4))
self.add_arc('roof-right',(32,4),(40,12),radius_x=8)
self.add_polyline('walls',(40,12),(40,44),(32,44),(16,44),(8,44),(8,12))
self.add_contour('cabin','roof-left','roof-top','roof-right',*(f'walls-{i}' for i in range(1,6)),closed=True)
self.add_polyline('door',(16,44),(16,20),(32,20),(32,44))
self.add_polyline('sign',(20,33),(24,26),(28,33),closed=True)
self.relate('connect','door-1','walls-3');self.relate('connect','door-1','walls-4')
self.relate('connect','door-3','walls-2');self.relate('connect','door-3','walls-3')
''')
add('SQUARE','A landscape picture with a retouch wand and sparkle.','Open picture boundary holds two mountains and a sun; detached diagonal wand at upper right.','wand-sparkles: diagonal wand and sparse rays',['Reduced sparkle rays to three.'],'''
self.add_polyline('frame',(24,10),(6,10),(6,42),(42,42),(42,26))
self.circle('sun',16,21,3)
self.add_polyline('small-mountain',(10,42),(18,29),(25,42))
self.add_polyline('large-mountain',(22,42),(32,25),(42,42))
self.add_line('wand',(32,14),(42,24))
self.add_line('ray-up',(34,6),(34,8))
self.add_line('ray-right',(40,12),(42,10))
self.add_line('ray-left',(26,6),(28,8))
''')
add('CIRCLE','A magic retouch wand inside a circular badge.','Circular boundary encloses a diagonal outlined wand and three plus sparkles.','wand-sparkles: rounded diagonal tool and detached sparkle series',[],'''
self.circle('badge',24,24,20)
self.add_polyline('wand',(9,36),(24,21),(30,27),(15,42),closed=True)
self.add_line('tip-band',(20,25),(26,31))
for name,x,y in [('left',15,16),('top',28,12),('right',36,23)]:
    self.add_polyline(name+'-h',(x-2,y),(x,y),(x+2,y))
    self.add_polyline(name+'-v',(x,y-2),(x,y),(x,y+2))
    for a in (1,2):
        for b in (1,2):self.relate('connect',f'{name}-h-{a}',f'{name}-v-{b}')
''')
for curved in (False,True):
 add('SQUARE','A circular award medal with two '+('curved' if curved else 'angular')+' ribbon tails.','Medal circle and mirrored tails share exact circle nodes; paired ribbons derive from axis 24.','ribbon: continuous loop and paired fabric ends',[],f'''
points=[(12,30),(9,21),(24,6),(39,21),(36,30),(24,36)]
for i in range(6):self.add_arc(f'medal-{{i}}',points[i],points[(i+1)%6],radius_x=15)
self.add_contour('medal',*(f'medal-{{i}}' for i in range(6)),closed=True)
for side in (0,1):
    def p(x,y):return (48-x if side else x,y)
    name=f'tail-{{side}}'
    if {curved!r}:
        self.add_bezier(name+'-outer',p(12,30),(p(10,33),p(7,35),p(6,38)))
        self.add_polyline(name+'-fork',p(6,38),p(14,37),p(16,42))
        self.add_bezier(name+'-inner',p(16,42),(p(19,41),p(22,38),p(24,36)))
        self.add_contour(name,name+'-outer',name+'-fork-1',name+'-fork-2',name+'-inner')
        outer,inner=name+'-outer',name+'-inner'
    else:
        self.add_polyline(name,p(12,30),p(6,38),p(14,38),p(18,42),p(24,36))
        outer,inner=name+'-1',name+'-4'
    for arc in ([0,5] if not side else [3,4]):self.relate('connect',outer,f'medal-{{arc}}')
    for arc in (4,5):self.relate('connect',inner,f'medal-{{arc}}')
self.relate('connect','tail-0-'+('inner' if {curved!r} else '4'),'tail-1-'+('inner' if {curved!r} else '4'))
''')
add('SQUARE','A right-pointing arrow inside a rounded square.','Centered arrow nested in a single rounded square.','log-out: horizontal shaft and symmetric chevron',[],'''
self.box('frame',6,6,42,42,4)
self.arrow('right',(14,24),(34,24),(26,16),(26,32))
''')
add('HRECT_M','A long right-pointing arrow.','Horizontal shaft shares the chevron tip; wings mirror about y24.','arrow-right-to-line: arrow geometry',['No terminal bar added: none is visible in the supplied reference.'],'''
self.arrow('right',(4,24),(44,24),(30,10),(30,38))
''')
add('SQUARE','A right arrow between two open brackets.','Mirrored brackets enclose an independent directional arrow.','log-in: open bracket with directed shaft',[],'''
for side in (0,1):
    def p(x,y):return (48-x if side else x,y)
    n=f'bracket-{side}'
    self.add_line(n+'-top',p(14,6),p(10,6))
    self.add_arc(n+'-upper',p(10,6),p(6,10),radius_x=4,sweep=bool(side))
    self.add_line(n+'-wall',p(6,10),p(6,38))
    self.add_arc(n+'-lower',p(6,38),p(10,42),radius_x=4,sweep=bool(side))
    self.add_line(n+'-bottom',p(10,42),p(14,42))
    self.add_contour(n,*(n+s for s in ('-top','-upper','-wall','-lower','-bottom')))
self.arrow('right',(14,24),(32,24),(24,16),(24,32))
''')
add('SQUARE','An upward riser arrow in a rounded square.','Square enclosure owns centered vertical arrow.','arrow-down: mirrored arrow construction with upward direction',[],'''
self.box('frame',6,6,42,42,4)
self.arrow('up',(24,34),(24,14),(16,22),(32,22))
''')
add('VRECT_L','A padlock containing a receding road.','Symmetric lock body and arched shackle contain a trapezoidal road.','lock: arched shackle above rounded body',['Reduced road center dashes to one.'],'''
self.box('body',8,24,40,44,3)
self.add_line('shackle-left',(14,24),(14,14))
self.add_arc('shackle-top',(14,14),(34,14),radius_x=10)
self.add_line('shackle-right',(34,14),(34,24))
self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
self.relate('connect','shackle-left','body-0');self.relate('connect','shackle-right','body-0')
self.add_polyline('road',(14,44),(20,32),(28,32),(34,44))
self.relate('connect','road-1','body-4');self.relate('connect','road-3','body-4')
self.add_line('road-dash',(24,38),(24,40))
''')
add('SQUARE','A four-metre height restriction mark with vertical chevrons.','Hand-authored 4 and M retain the text; mirrored top/bottom chevrons mark height.','expand: paired directional chevrons',[],'''
self.add_polyline('four',(6,28),(18,14),(18,28),(18,34))
self.add_polyline('four-bar',(6,28),(18,28),(22,28))
for a in ('four-2','four-3'):
    for b in ('four-bar-1','four-bar-2'):self.relate('connect',a,b)
self.relate('connect','four-1','four-bar-1')
self.add_polyline('m',(28,34),(28,14),(35,26),(42,14),(42,34))
self.add_polyline('up',(20,10),(24,6),(28,10))
self.add_polyline('down',(20,38),(24,42),(28,38))
''')
add('SQUARE','A robber threatening another person with a knife for money.','Two shared circular heads with exact detached torso gap, bent threatening arm, blade and dollar symbol.','human_ref/user.svg and full_body_ref.png: circular heads and coherent bent limbs',['Omitted tiny facial expressions; retained knife and money mark.'],'''
# Heads end at y16 and y18; actual torso starts y24 and y26: 8 centerline / 4 ink gap.
self.circle('robber-head',14,11,5)
self.circle('victim-head',36,14,4)
self.add_line('robber-torso',(14,24),(14,42))
self.add_line('victim-torso',(36,26),(36,42))
self.mark_human_figure('robber',head='robber-head',torso='robber-torso',torso_junction='start')
self.mark_human_figure('victim',head='victim-head',torso='victim-torso',torso_junction='start')
self.add_polyline('arm',(14,24),(6,28),(6,34),(20,34))
self.relate('connect','arm-1','robber-torso')
self.add_polyline('knife',(20,34),(20,28),(28,28),(32,34),closed=True)
self.relate('connect','arm-3','knife-1');self.relate('connect','arm-3','knife-4')
self.add_bezier('money',(42,29),((35,26),(35,33),(40,34)),((44,35),(43,40),(38,39)))
self.add_line('money-stem',(40,26),(40,42))
''')
add('SQUARE','An articulated robot arm receiving a wireless signal.','Two circular pivots joined by parallel arm edges; base and gripper retain direction; two nested wireless arcs.','bot: circular joints and minimal machine detail',['Reduced wireless symbol to two arcs; no 5G text is present in the reference.'],'''
self.add_arc('wifi-outer',(6,10),(22,10),radius_x=8,radius_y=4)
self.add_arc('wifi-inner',(10,18),(18,18),radius_x=4,radius_y=3)
self.circle('base-joint',14,32,6)
# Four quarters expose real attachment nodes on the upper pivot.
pts=[(29,18),(34,13),(39,18),(34,23)]
for i in range(4):self.add_arc(f'upper-{i}',pts[i],pts[(i+1)%4],radius_x=5)
self.add_contour('upper-joint',*(f'upper-{i}' for i in range(4)),closed=True)
self.add_line('arm-top',(14,26),(29,18))
self.add_line('arm-bottom',(20,32),(34,23))
self.add_line('base-left',(8,32),(12,42))
self.add_line('base-right',(20,32),(24,42))
self.add_polyline('gripper',(39,18),(42,24),(42,30))
for a,bs in [('arm-top',['base-joint-top','upper-0','upper-3']),('arm-bottom',['base-joint-top','base-joint-bottom','upper-2','upper-3']),('base-left',['base-joint-top','base-joint-bottom']),('base-right',['base-joint-top','base-joint-bottom']),('gripper-1',['upper-1','upper-2'])]:
    for b in bs:self.relate('connect',a,b)
self.relate('connect','base-right','arm-bottom')
''')
add('SQUARE','A poisoned dagger beside a droplet and skull.','Diagonal blade and rounded handle form one tool, with crossguard; poison symbols occupy right side.','No useful Lucide match for the complete dagger/skull composition.',['Simplified skull jaw and omitted teeth.'],'''
self.add_polyline('blade',(15,32),(34,6),(31,22),(21,38))
self.add_arc('handle-end',(21,38),(13,42),radius_x=5)
self.add_line('handle-side',(13,42),(8,37))
self.add_arc('handle-turn',(8,37),(15,32),radius_x=5)
self.add_contour('dagger','blade-1','blade-2','blade-3','handle-end','handle-side','handle-turn',closed=True)
self.add_line('guard',(6,25),(24,41))
self.add_bezier('drop',(40,16),((40,16),(34,23),(36,26)),((38,30),(44,28),(42,23)),((41,20),(40,16),(40,16)))
self.add_bezier('skull',(28,42),((28,39),(24,37),(27,33)),((30,27),(41,29),(42,35)),((43,38),(38,39),(38,42)))
self.add_line('jaw',(28,42),(38,42))
self.relate('connect','jaw','skull')
self.add_dot('eye-left',(30,35));self.add_dot('eye-right',(37,35))
''')
add('VRECT_L','A heart within a combined male and female gender symbol.','Circular ring owns heart; diagonal male arrow and vertical female cross attach outside.','heart: mirrored lobes and point',['Small inner heart simplified to two smooth mirrored curves.'],'''
self.circle('ring',22,23,14)
self.heart('heart',22,19,6,29)
self.add_line('male-shaft',(32,13),(40,4))
self.add_polyline('male-head',(32,4),(40,4),(40,12))
for i in (1,2):self.relate('connect','male-shaft',f'male-head-{i}')
self.add_polyline('female-stem',(22,37),(22,41),(22,44))
self.add_polyline('female-cross',(14,41),(22,41),(30,41))
self.relate('connect','female-stem-1','ring-bottom')
for a in (1,2):
    for b in (1,2):self.relate('connect',f'female-stem-{a}',f'female-cross-{b}')
''')
add('HRECT_L','A rainbow arch above a heart.','Three concentric upper semicircles share center; separate mirrored heart sits below.','heart: symmetric lobes and pointed base',['Reduced rainbow to three arcs.'],'''
for i,r in enumerate((20,14,8)):self.add_arc(f'rainbow-{i}',(24-r,28),(24+r,28),radius_x=r)
self.add_polyline('baseline-left',(4,28),(10,28),(16,28))
self.add_polyline('baseline-right',(32,28),(38,28),(44,28))
for i in range(3):
    for side in ('left','right'):
        for j in (1,2):
            if (i==0 and ((side=='left' and j==1) or (side=='right' and j==2))) or i==1 or (i==2 and ((side=='left' and j==2) or (side=='right' and j==1))):self.relate('connect',f'rainbow-{i}',f'baseline-{side}-{j}')
self.heart('heart',24,32,7,40)
''')
add('HRECT_L','A house roof above a double-ended wrench.','Roof apex centered above a horizontal shaft; wrench jaws mirror around x24 and y34.','wrench: open jaws attached to a continuous shaft',[],'''
self.add_polyline('roof',(4,18),(24,8),(44,18))
for side in (0,1):
    def p(x,y):return (48-x if side else x,y)
    n=f'jaw-{side}'
    self.add_line(n+'-upper-lip',p(6,28),p(10,28))
    self.add_arc(n+'-upper',p(10,28),p(16,34),radius_x=6,sweep=not bool(side))
    self.add_arc(n+'-lower',p(16,34),p(10,40),radius_x=6,sweep=not bool(side))
    self.add_line(n+'-lower-lip',p(10,40),p(6,40))
    self.add_contour(n,*(n+s for s in ('-upper-lip','-upper','-lower','-lower-lip')))
self.add_line('shaft',(16,34),(32,34))
for side in (0,1):
    for suffix in ('-upper','-lower'):self.relate('connect','shaft',f'jaw-{side}'+suffix)
''')
assert len(specs)==20
for r,s in zip(records,specs):
 key,summary,plan,ref,omissions,code=s
 r.update(keyshape=key,subject=summary,symbol_plan=plan,construction_reference=ref,omissions=omissions)
 out=Path(r['result_dir']); filename=r['icon_id'].replace('-','_')+'_'+r['source_uuid'].replace('-','_')+'.py'
 source=f'''"""{summary}\n\nPlan: {plan}\nConstruction: {ref}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n\nSOURCE_ICON_ID = {r['source_uuid']!r}\nSOURCE_PATH = {r['reference_path']!r}\nAUTHOR = {AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id = {r['icon_id']!r}\n    keyshape = Keyshape.{key}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects/general"\n    aliases = ()\n    keywords = {tuple(r['concept'].split())!r}\n\n    def build(self):\n'''+textwrap.indent(code.strip(),'        ')+'\n'+helpers
 (out/filename).write_text(source);r['module']=filename
 (out/(r['icon_id']+'.metadata.json')).write_text(json.dumps(r,indent=2))
Path('/tmp/batch39.json').write_text(json.dumps(records,indent=2))
print('Authored',len(records),'standalone modules in input order.')
