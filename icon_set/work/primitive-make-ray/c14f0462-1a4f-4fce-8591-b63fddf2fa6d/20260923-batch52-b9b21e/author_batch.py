"""Batch 52 standalone originals; folder-only output, no registration."""
from pathlib import Path
import json, textwrap, importlib.util
import cairosvg

AUTHOR='gpt-6'
HERE=Path(__file__).parent
INPUTS=json.loads((HERE/'batch-inputs.json').read_text())
SOURCE_ICON_ID=tuple(r['source_uuid'] for r in INPUTS)
SOURCE_PATH=tuple(r['reference_path'] for r in INPUTS)

HELPERS='''
    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,left,top,right,bottom,r):
        p=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
           (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        names=[]
        for i,start in enumerate(p):
            n=f'{name}-{i}';end=p[(i+1)%8]
            if i%2:self.add_arc(n,start,end,radius_x=r)
            else:self.add_line(n,start,end)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def cross(self,name,x,y,r,diagonal=False):
        ends=[(-r,-r),(r,r),(r,-r),(-r,r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        for i,(dx,dy) in enumerate(ends):self.add_line(f'{name}-{i}',(x,y),(x+dx,y+dy))
        self.relate('connect',*[f'{name}-{i}' for i in range(4)])

    def monitor(self,left=6,top=6,right=42,bottom=34,foot=42):
        # Matched quarter-round corners, bottom wall split at the stand junction.
        r=4;cx=(left+right)//2
        self.add_line('screen-top',(left+r,top),(right-r,top))
        self.add_arc('screen-tr',(right-r,top),(right,top+r),radius_x=r)
        self.add_line('screen-right',(right,top+r),(right,bottom-r))
        self.add_arc('screen-br',(right,bottom-r),(right-r,bottom),radius_x=r)
        self.add_line('screen-bottom-r',(right-r,bottom),(cx,bottom))
        self.add_line('screen-bottom-l',(cx,bottom),(left+r,bottom))
        self.add_arc('screen-bl',(left+r,bottom),(left,bottom-r),radius_x=r)
        self.add_line('screen-left',(left,bottom-r),(left,top+r))
        self.add_arc('screen-tl',(left,top+r),(left+r,top),radius_x=r)
        self.add_contour('screen','screen-top','screen-tr','screen-right','screen-br','screen-bottom-r','screen-bottom-l','screen-bl','screen-left','screen-tl',closed=True)
        self.add_line('stand',(cx,bottom),(cx,foot))
        self.add_polyline('foot',(cx-8,foot),(cx,foot),(cx+8,foot))
        self.relate('connect','stand','screen-bottom-r','screen-bottom-l')
        self.relate('connect','stand','foot')

    def browser(self):
        # Chrome separator joins explicitly split side walls; two tiny source
        # chrome dashes are omitted so the content keeps the available height.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right-upper',(42,10),(42,14))
        self.add_line('right-lower',(42,14),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left-lower',(6,38),(6,14))
        self.add_line('left-upper',(6,14),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('browser','top','tr','right-upper','right-lower','br','bottom','bl','left-lower','left-upper','tl',closed=True)
        self.add_line('chrome',(6,14),(42,14))
        self.relate('connect','chrome','left-upper','left-lower','right-upper','right-lower')
'''

SPECS=[
('HRECT_L','Medical truck with two wheels, cab window and outlined medical cross.','truck and ambulance: circular wheels, interrupted lower chassis and cab profile',[],'''
# Main cargo body and cab intentionally differ in height.
self.add_polyline('cargo',(4,34),(4,8),(28,8),(28,34))
self.add_polyline('cab',(28,16),(36,16),(44,26),(44,34),(40,34))
self.circle('wheel-left',12,36,4)
self.circle('wheel-right',36,36,4)
self.add_line('chassis',(16,36),(32,36))
self.relate('connect','chassis','wheel-left','wheel-right')
self.add_polyline('window',(34,18),(34,26),(44,26))
self.relate('connect','window','cab')
self.add_polyline('medical-cross',(13,15),(19,15),(19,20),(24,20),(24,26),(19,26),(19,31),(13,31),(13,26),(8,26),(8,20),(13,20),closed=True)
'''),
('SQUARE','Moving truck carrying a house above its cargo box.','truck and house: wheel pair, peaked roof and doorway',[],'''
self.add_polyline('house-roof',(8,14),(18,6),(28,14))
self.add_polyline('house-walls',(11,12),(11,22),(25,22),(25,12))
self.add_polyline('door',(15,22),(15,16),(21,16),(21,22))
self.relate('connect','house-walls','door')
self.add_polyline('cargo',(6,22),(6,34),(32,34),(32,22),(25,22))
self.relate('connect','cargo','house-walls')
self.add_polyline('cab',(32,28),(38,28),(42,32),(42,38),(40,38))
self.circle('wheel-left',18,38,4)
self.circle('wheel-right',36,38,4)
self.add_line('chassis',(22,38),(32,38))
self.relate('connect','chassis','wheel-left','wheel-right')
self.relate('connect','cab','wheel-right')
'''),
('SQUARE','Rounded speech bubble containing a diagonal telephone handset.','phone and message-square: flowing receiver silhouette and rounded speech enclosure',[],'''
self.add_line('bubble-top',(14,6),(34,6))
self.add_arc('bubble-tr',(34,6),(42,14),radius_x=8)
self.add_line('bubble-right',(42,14),(42,28))
self.add_arc('bubble-br',(42,28),(34,36),radius_x=8)
self.add_polyline('tail',(34,36),(22,36),(14,42),(14,36))
self.add_arc('bubble-bl',(14,36),(6,28),radius_x=8)
self.add_line('bubble-left',(6,28),(6,14))
self.add_arc('bubble-tl',(6,14),(14,6),radius_x=8)
self.add_contour('bubble','bubble-top','bubble-tr','bubble-right','bubble-br','tail-1','tail-2','tail-3','bubble-bl','bubble-left','bubble-tl',closed=True)
# The handset follows the source's upper-left to lower-right orientation.
self.add_bezier('receiver-outer',(16,13),((11,17),(19,30),(29,31)),((32,31),(34,28),(32,26)))
self.add_polyline('receiver-end',(32,26),(29,23),(26,26))
self.add_bezier('receiver-inner',(26,26),((22,25),(18,21),(18,19)))
self.add_polyline('receiver-start',(18,19),(21,16),(18,12),(16,13))
self.add_contour('receiver','receiver-outer','receiver-end-1','receiver-end-2','receiver-inner','receiver-start-1','receiver-start-2','receiver-start-3',closed=True)
'''),
('SQUARE','Diamond traffic sign with opposing branches on an outlined vertical route.','signpost: coherent outlined arrow corners; intentional opposing branches',[],'''
self.add_polyline('diamond',(24,6),(42,24),(24,42),(6,24),closed=True)
self.add_polyline('route',(23,14),(23,18),(27,18),(30,21),(27,24),(27,34),(23,34),(23,30),(19,30),(16,27),(19,24),(23,24),(23,14))
'''),
('SQUARE','Television on a central stand with a circled check inside.','monitor and circle: rounded screen, central stand and circular status mark',[],'''
self.monitor()
self.circle('status-ring',24,20,8)
self.add_polyline('check',(20,20),(23,23),(28,17))
'''),
('SQUARE','Television on a central stand showing two pause bars.','monitor: matched screen corners and centered stand',[],'''
self.monitor()
for x in (20,28):self.add_line(f'pause-{x}',(x,15),(x,25))
'''),
('SQUARE','Television on a central stand with an outlined right-pointing play triangle.','monitor: matched screen corners and centered stand',[],'''
self.monitor()
self.add_polyline('play',(18,15),(30,20),(18,25),closed=True)
'''),
('SQUARE','Television with a previous-track bar and left-pointing triangle.','monitor: screen and stand construction',[],'''
self.monitor()
self.add_line('previous-bar',(16,15),(16,25))
self.add_polyline('previous-triangle',(33,15),(25,20),(33,25),closed=True)
'''),
('HRECT_M','Wide flat-screen television with a centered pedestal.','monitor: smooth rounded screen and central foot',[],'''
self.monitor(left=4,top=10,right=44,bottom=30,foot=38)
'''),
('SQUARE','Television with three X-shaped password marks.','monitor: screen and foot; shared repeated X construction',[],'''
self.monitor()
for i,x in enumerate((15,24,33)):self.cross(f'password-{i}',x,23,2,True)
'''),
('SQUARE','Retro television with rabbit-ear antenna, inset screen, two buttons and two feet.','tv: antenna junction and rounded cabinet',[],'''
self.box('cabinet',6,14,42,38,4)
self.add_polyline('antenna',(16,6),(24,14),(32,6))
self.relate('connect','antenna','cabinet')
self.box('display',12,20,30,32,3)
for i,y in enumerate((22,30)):self.circle(f'button-{i}',36,y,2)
for i,x in enumerate((14,34)):
    self.add_line(f'foot-{i}',(x,38),(x,42))
    self.relate('connect',f'foot-{i}','cabinet')
'''),
('SQUARE','Two overlapping browser windows, the front window carrying a header separator.','panels-top-left: overlapping rounded frames and header rule',['Three tiny browser-control dashes omitted to preserve window spacing.'],'''
self.box('front',14,6,42,33,4)
self.add_line('header',(14,14),(42,14))
self.relate('connect','header','front')
self.add_line('rear-top',(10,14),(14,14))
self.add_arc('rear-tl',(10,14),(6,18),radius_x=4,sweep=False)
self.add_line('rear-left',(6,18),(6,38))
self.add_arc('rear-bl',(6,38),(10,42),radius_x=4,sweep=False)
self.add_line('rear-bottom',(10,42),(34,42))
self.add_contour('rear','rear-tl','rear-left','rear-bl','rear-bottom')
self.relate('connect','rear-top','rear-tl','front','header')
'''),
('HRECT_L','Rounded text input crossed by a tall cursor with a curved lower hook.','text-cursor-input: rounded field and cursor crossing the field',[],'''
# Split both horizontal field walls where the cursor passes through them.
self.add_polyline('field-top',(8,16),(34,16),(40,16))
self.add_arc('field-tr',(40,16),(44,20),radius_x=4)
self.add_line('field-right',(44,20),(44,28))
self.add_arc('field-br',(44,28),(40,32),radius_x=4)
self.add_polyline('field-bottom',(40,32),(34,32),(8,32))
self.add_arc('field-bl',(8,32),(4,28),radius_x=4)
self.add_line('field-left',(4,28),(4,20))
self.add_arc('field-tl',(4,20),(8,16),radius_x=4)
self.add_contour('field','field-top-1','field-top-2','field-tr','field-right','field-br','field-bottom-1','field-bottom-2','field-bl','field-left','field-tl',closed=True)
self.add_polyline('cursor',(34,8),(34,16),(34,32),(34,34))
self.add_arc('hook',(34,34),(28,40),radius_x=6)
self.relate('connect','cursor','field-top','field-bottom','hook')
'''),
('SQUARE','Browser page showing the hand-authored letters A and D.','panels-top-left: rounded browser chrome; hand-authored source lettering',['Two tiny chrome dashes omitted to give the lettering more space.'],'''
self.browser()
self.add_polyline('letter-a',(14,34),(18,22),(22,34))
self.add_line('a-crossbar',(16,28),(20,28))
self.relate('connect','letter-a','a-crossbar')
self.add_line('d-stem',(30,22),(30,34))
self.add_arc('d-bowl',(30,22),(30,34),radius_x=6,radius_y=6)
self.relate('connect','d-stem','d-bowl')
'''),
('SQUARE','Browser page containing a round bug with three paired legs and a horizontal crossbar.','panels-top-left and bug: browser frame and repeated bilateral legs',['Two tiny chrome dashes omitted to preserve the bug composition.'],'''
self.browser()
# Pythagorean points on radius-five body create exact leg attachments.
points=[(19,28),(21,24),(27,24),(29,28),(27,32),(21,32)]
names=[]
for i,p in enumerate(points):
    n=f'body-{i}';self.add_arc(n,p,points[(i+1)%6],radius_x=5);names.append(n)
self.add_contour('bug-body',*names,closed=True)
for name,start,end in [('tl',(21,24),(18,22)),('tr',(27,24),(30,22)),('bl',(21,32),(18,34)),('br',(27,32),(30,34))]:
    self.add_line('leg-'+name,start,end)
    self.relate('connect','leg-'+name,'bug-body')
self.add_polyline('crossbar',(16,28),(19,28),(29,28),(32,28))
self.relate('connect','crossbar','bug-body')
'''),
('SQUARE','Browser page with two opposing horizontal code arrows.','panels-top-left: browser frame; shared arrow strokes',['Two tiny chrome dashes omitted to preserve arrow spacing.'],'''
self.browser()
self.add_polyline('right-arrow',(16,24),(32,24),(30,22))
self.add_polyline('left-arrow',(32,32),(16,32),(18,34))
'''),
('SQUARE','Browser page containing an open-jawed skull with eye dots and a middle tooth stroke.','panels-top-left and skull: circular cranium with narrowed jaw; human_ref/user.svg supplies circular head principle',['Two tiny chrome dashes omitted to give the skull room.'],'''
self.browser()
self.add_arc('skull-top',(16,28),(32,28),radius_x=8)
self.add_bezier('skull-right',(32,28),((32,32),(28,33),(28,35)))
self.add_line('jaw-right',(28,35),(28,37))
self.add_bezier('skull-left',(20,35),((20,33),(16,32),(16,28)))
self.add_line('jaw-left',(20,37),(20,35))
self.add_contour('skull','jaw-left','skull-left','skull-top','skull-right','jaw-right')
for x in (21,27):self.add_dot(f'eye-{x}',(x,28))
self.add_line('middle-tooth',(24,34),(24,37))
'''),
('SQUARE','Browser page displaying a short-sleeved T-shirt with a scooped neck.','panels-top-left and shirt: browser chrome and symmetric garment outline',['Two tiny chrome dashes omitted to preserve the complete garment.'],'''
self.browser()
self.add_polyline('shirt-left',(21,22),(19,22),(14,27),(17,30),(20,28),(20,34),(28,34),(28,28),(31,30),(34,27),(29,22),(27,22))
self.add_arc('neckline',(27,22),(21,22),radius_x=3)
self.add_contour('shirt',*[f'shirt-left-{i}' for i in range(1,12)],'neckline',closed=True)
'''),
('SQUARE','Page template with horizontal rows and a lower-right add sign.','panels-top-left: repeated horizontal divisions and rounded upper corners',[],'''
self.add_line('top',(10,6),(38,6))
self.add_arc('tr',(38,6),(42,10),radius_x=4)
self.add_polyline('right',(42,10),(42,16),(42,26))
self.add_polyline('left',(6,42),(6,36),(6,26),(6,16),(6,10))
self.add_arc('tl',(6,10),(10,6),radius_x=4)
self.add_contour('page-top','tl','top','tr','right-1','right-2')
self.relate('connect','left','tl')
for y in (16,26):
    self.add_line(f'row-{y}',(6,y),(42,y))
    self.relate('connect',f'row-{y}','left','right')
self.add_line('row-last',(6,36),(24,36))
self.relate('connect','row-last','left')
self.cross('add',36,38,4)
'''),
]

def author():
    for row,(keyshape,plan,reference,omissions,body) in zip(INPUTS,SPECS):
        out=Path(row['result_dir'])
        if (out/'result.json').exists():continue
        module_name=row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py'
        source=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID={row['source_uuid']!r}
SOURCE_PATH={row['reference_path']!r}
AUTHOR={AUTHOR!r}
PLAN={plan!r}
CONSTRUCTION_REFERENCE={reference!r}

class Drawing(Solo48):
    icon_id={row['icon_id']!r}
    keyshape=Keyshape.{keyshape}
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords={tuple(row['concept'].split())!r}
{HELPERS}
    def build(self):
'''+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n'
        # Polyline segments used in a larger contour must have only one owner.
        # The helper calls above remain readable; remove superseded contours
        # from the model, never from the emitted SVG.
        used={'tty-answer':['tail','receiver-end','receiver-start'],
              'type-cursor':['field-top','field-bottom'],
              'ui-webpage-t-shirt':['shirt-left'],
              'ui-webpage-template-add':['right']}.get(row['icon_id'],[])
        if used:source+=f"        self.contours = [c for c in self.contours if c.contour_id not in {used!r}]\n"
        (out/module_name).write_text(source)
        row.update(module=module_name,keyshape=keyshape,subject=plan,construction_reference=reference,omissions=omissions)
    (HERE/'batch-inputs.json').write_text(json.dumps(INPUTS,indent=2))

def export():
    rows=json.loads((HERE/'batch-inputs.json').read_text())
    for i,row in enumerate(rows):
        out=Path(row['result_dir'])
        if (out/'result.json').exists():continue
        try:
            spec=importlib.util.spec_from_file_location(f'candidate_{i}',out/row['module'])
            m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
            icon=m.Drawing();report=icon.validate_icon();row['validation_status']=report.status
            (out/'validation.txt').write_text(report.describe());svg=icon.to_svg()
            (out/(row['icon_id']+'.svg')).write_text(svg)
            for theme,bg,neg in [('light','white',False),('dark','#181818',True)]:
                for size in (48,192):
                    cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size,background_color=bg,negate_colors=neg,write_to=str(out/f'{theme}-{size}.png'))
            row.pop('error',None);print(i+1,row['concept'],report.status,flush=True)
        except Exception as exc:
            row['validation_status']='error';row['error']=repr(exc)
            (out/'validation.txt').write_text(repr(exc));print(i+1,repr(exc),flush=True)
    (HERE/'batch-inputs.json').write_text(json.dumps(rows,indent=2))

if __name__=='__main__':
    import sys
    if 'export' not in sys.argv:author()
    export()
