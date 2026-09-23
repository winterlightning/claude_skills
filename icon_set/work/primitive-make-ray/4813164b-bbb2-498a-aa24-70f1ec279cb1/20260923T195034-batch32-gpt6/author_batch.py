from pathlib import Path
import json,importlib.util,traceback,cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID='4813164b-bbb2-498a-aa24-70f1ec279cb1'
SOURCE_PATH='icon_set/work/todo-references/passport ticket_4813164b-bbb2-498a-aa24-70f1ec279cb1.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch.json').read_text())
helpers='''
    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def rounded(self,n,l,t,r,b,k=4):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        members=[]
        for i,p in enumerate(pts):
            q=pts[(i+1)%8];name=f'{n}-{i}';members.append(name)
            if i%2:self.add_arc(name,p,q,radius_x=k)
            else:self.add_line(name,p,q)
        self.add_contour(n,*members,closed=True)

    def dollar(self):
        self.add_line('s-top',(29,16),(24,16))
        self.add_arc('s-left',(24,16),(24,24),radius_x=4,sweep=False)
        self.add_arc('s-right',(24,24),(24,32),radius_x=4)
        self.add_line('s-bottom',(24,32),(19,32))
        self.add_contour('dollar','s-top','s-left','s-right','s-bottom')
        self.add_line('stem-top',(24,12),(24,16));self.relate('connect','stem-top','dollar')
        self.add_line('stem-bottom',(24,32),(24,36));self.relate('connect','stem-bottom','dollar')

    def bust(self,n,x,y,r,width,body_y,body_ry):
        # Detached head bottom = y+r; shoulder apex = body_y-body_ry.
        # Author parameters require their difference to be exactly eight.
        self.circle(n+'-head',x,y,r)
        self.add_arc(n+'-shoulders',(x-width,body_y),(x+width,body_y),radius_x=width,radius_y=body_ry)
'''
specs=[]
def add(key,subject,plan,code,ref,omit='None.',human=None):specs.append(dict(keyshape=key,subject=subject,plan=plan,code=code,construction_reference=ref,omissions=omit,human_construction=human))
add('SQUARE','A passport in front of a travel ticket.','Foreground passport with a globe; tilted notched ticket behind it, with two writing rules.', '''
        self.rounded('passport',6,18,26,42,3)
        self.add_polyline('ticket-left',(20,18),(23,6),(30,8))
        self.add_arc('notch',(30,8),(36,10),radius_x=3,sweep=False)
        self.add_polyline('ticket-right',(36,10),(42,12),(36,42),(26,40))
        self.add_contour('ticket','ticket-left-1','ticket-left-2','notch','ticket-right-1','ticket-right-2','ticket-right-3')
        self.circle('globe',16,29,6)
        self.add_line('equator',(10,29),(22,29));self.relate('connect','equator','globe')
        self.circle('meridian',16,29,2,6);self.relate('connect','meridian','globe');self.relate('connect','equator','meridian')
        for i,y in enumerate((20,28)):self.add_line(f'ticket-text-{i}',(30,y),(35,y+1))
''','ticket: notched perimeter; supplied source owns the overlapping arrangement.','Small lower ticket slot omitted; globe meridian retained.')
add('HRECT_M','A password field displaying three X characters.','Three identical diagonal crosses spaced on a common baseline inside a wide rectangle.', '''
        self.add_polyline('field',(4,10),(44,10),(44,38),(4,38),closed=True)
        for i,x in enumerate((12,24,36)):
            for j,(dx,dy) in enumerate(((-3,-3),(3,3),(-3,3),(3,-3))):self.add_line(f'x-{i}-{j}',(x,24),(x+dx,24+dy))
            self.relate('connect',*(f'x-{i}-{j}' for j in range(4)))
''','No useful Lucide match; repeated crosses and field are reconstructed from the supplied reference.')
add('VRECT_L','A patent certificate with a folded corner and ribbon seal.','Fold and page share corner nodes; circular seal interrupts the page lower boundary.', '''
        self.add_polyline('page',(24,32),(8,32),(8,4),(30,4),(40,14),(40,32))
        self.add_polyline('fold',(30,4),(30,14),(40,14));self.relate('connect','fold','page')
        self.add_line('writing',(17,15),(25,15))
        self.circle('seal',32,32,8);self.relate('connect','seal','page')
        self.add_polyline('ribbon',(26,38),(26,44),(32,41),(38,44),(38,38))
''','ticket: coherent document boundary; circular seal and ribbon from the source.','Three writing rules reduced to one to reserve seal space.')
add('VRECT_L','The outlined Path P logo.','Continuous outer lobe and descending stem with rounded lower hook; inner lobe forms the P counter.', '''
        self.add_arc('outer-top',(8,20),(40,20),radius_x=16)
        self.add_arc('outer-right',(40,20),(28,32),radius_x=12)
        self.add_line('stem-right',(28,32),(28,34))
        self.add_arc('hook-right',(28,34),(18,44),radius_x=10)
        self.add_line('hook-bottom',(18,44),(14,44))
        self.add_arc('hook-left',(14,44),(10,40),radius_x=4)
        self.add_line('hook-up',(10,40),(10,36))
        self.add_line('hook-inner',(10,36),(14,36))
        self.add_arc('stem-turn',(14,36),(18,32),radius_x=4,sweep=False)
        self.add_line('stem-left',(18,32),(18,18))
        self.add_arc('inner-top',(18,18),(26,18),radius_x=4)
        self.add_line('inner-stem',(26,18),(26,24))
        self.add_arc('inner-right',(26,24),(32,18),radius_x=6,sweep=False)
        self.add_arc('inner-lobe',(32,18),(16,18),radius_x=8,sweep=False)
        self.add_line('left-return',(16,18),(16,20))
        self.add_arc('left-cap',(16,20),(8,20),radius_x=4)
        self.add_contour('logo','outer-top','outer-right','stem-right','hook-right','hook-bottom','hook-left','hook-up','hook-inner','stem-turn','stem-left','inner-top','inner-stem','inner-right','inner-lobe','left-return','left-cap',closed=True)
''','No useful Lucide match; custom continuous arcs preserve the logo lobe and hooked stem.')
add('VRECT_M','A pedal with a rectangular tread and curved support arm.','Rounded top tread and a tapered support with a semicircular bottom.', '''
        self.rounded('tread',10,4,30,14,3)
        self.add_polyline('arm-upper',(30,10),(38,10),(38,18),(30,36),(30,40))
        self.add_arc('arm-bottom',(30,40),(22,40),radius_x=4)
        self.add_line('arm-left',(22,40),(22,14))
        self.add_contour('arm','arm-upper-1','arm-upper-2','arm-upper-3','arm-upper-4','arm-bottom','arm-left')
        self.relate('connect','arm','tread')
''','No useful subject match; rounded rectangular and capsule construction follows geometric Lucide principles.')
add('SQUARE','A pen nib beneath vector curve control handles.','Symmetric nib, central hole, repeated control nodes and a broad curve.', '''
        self.circle('left-node',8,8,2);self.circle('right-node',40,8,2)
        self.add_polyline('control-square',(20,6),(28,6),(28,14),(20,14),closed=True)
        self.add_line('left-control',(10,8),(20,8));self.relate('connect','left-control','left-node');self.relate('connect','left-control','control-square')
        self.add_line('right-control',(28,8),(38,8));self.relate('connect','right-control','right-node');self.relate('connect','right-control','control-square')
        self.add_arc('curve-left',(8,24),(20,10),radius_x=16,radius_y=16)
        self.add_arc('curve-right',(28,10),(40,24),radius_x=16,radius_y=16)
        self.relate('connect','curve-left','control-square');self.relate('connect','curve-right','control-square')
        self.add_polyline('nib',(24,18),(14,30),(18,34),(30,34),(34,30),closed=True)
        self.circle('nib-hole',24,28,2)
        self.add_line('slit',(24,18),(24,26));self.relate('connect','slit','nib');self.relate('connect','slit','nib-hole')
        self.add_polyline('base',(16,34),(32,34),(32,42),(16,42),closed=True);self.relate('connect','base','nib')
''','pen-tool: nib, slit and circular hole; source adds curve handles.','None; all defining controls and nib parts retained.')
add('SQUARE','A desktop monitor with a large diagonal editing pencil.','Open screen boundary around pencil; centered monitor stand; diagonal pencil with rounded eraser.', '''
        self.add_polyline('screen',(26,16),(6,16),(6,34),(34,34),(34,26))
        self.add_line('stand',(20,34),(20,42));self.relate('connect','stand','screen')
        self.add_polyline('foot',(12,42),(20,42),(28,42));self.relate('connect','foot','stand')
        self.add_polyline('pencil-a',(14,28),(18,16),(30,6))
        self.add_arc('eraser',(30,6),(42,18),radius_x=9)
        self.add_polyline('pencil-b',(42,18),(26,30),(14,28))
        self.add_contour('pencil','pencil-a-1','pencil-a-2','eraser','pencil-b-1','pencil-b-2',closed=True)
        self.add_line('band',(26,10),(38,22));self.relate('connect','band','pencil')
        self.add_line('tip',(18,16),(26,30));self.relate('connect','tip','pencil')
''','pencil: diagonal shaft and rounded eraser; monitor: screen with centered support.')
add('CIRCLE','A penny marked with a dollar sign.','Circular coin enclosing a smooth two-lobed dollar and aligned terminal stems.', '''
        self.circle('coin',24,24,20);self.dollar()
''','circle-percent: circular enclosure and central currency-style mark; dollar reconstructed independently.')
add('HRECT_L','Two people with a bidirectional arrow between them.','Two identical circular heads and broad shoulder arcs, plus a centered horizontal double arrow.', '''
        for i,x in enumerate((12,36)):
            self.bust(f'person-{i}',x,13,5,8,32,6)
        self.add_polyline('arrow',(12,40),(24,40),(36,40))
        self.add_polyline('arrow-left',(16,36),(12,40),(16,40))
        self.add_polyline('arrow-right',(32,36),(36,40),(32,40))
        self.relate('connect','arrow','arrow-left');self.relate('connect','arrow','arrow-right')
''','user-search: simple circular head; shared human_ref/user.svg owns head and shoulder proportions.','Lower halves of arrow wings shortened to fit the envelope.',
    'Two heads r=5 at y=13 end at y=18. Shoulder arcs have apex y=26: exact centerline gap 8, ink gap 4. Busts are not stick figures.')
add('HRECT_L','Two heads facing away with conflict sparks overhead.','Mirror-related continuous head/neck profiles; three separate lightning strokes.', '''
        for i,cx in enumerate((14,34)):
            self.add_arc(f'skull-{i}',(cx-8,30),(cx+8,30),radius_x=8)
        self.add_polyline('left-front',(6,30),(4,34),(8,34),(8,38),(14,38),(14,40))
        self.add_line('left-back',(22,30),(22,40))
        self.add_polyline('right-front',(42,30),(44,34),(40,34),(40,38),(34,38),(34,40))
        self.add_line('right-back',(26,30),(26,40))
        for a,b in [('skull-0','left-front'),('skull-0','left-back'),('skull-1','right-front'),('skull-1','right-back')]:self.relate('connect',a,b)
        for i,x in enumerate((8,24,40)):self.add_polyline(f'spark-{i}',(x+2,8),(x-2,12),(x+2,12),(x-2,16))
''','No useful Lucide match; the source defines paired continuous profile silhouettes.','Tiny chin and hair curvature simplified.',
    'Shared human_ref/user.svg reviewed for head scale. Continuous head/neck silhouettes have no detached head-body gap.')
add('SQUARE','Two people facing each other beneath a conflict burst.','Mirrored head profiles and central angular burst; faces intentionally point inward.', '''
        self.add_arc('left-skull',(6,28),(22,28),radius_x=8)
        self.add_polyline('left-back',(6,28),(8,34),(6,42));self.relate('connect','left-back','left-skull')
        self.add_polyline('left-face',(22,28),(24,34),(20,34),(20,38),(16,38),(14,42));self.relate('connect','left-face','left-skull')
        self.add_arc('right-skull',(26,28),(42,28),radius_x=8)
        self.add_polyline('right-face',(26,28),(24,34),(28,34),(28,38),(32,38),(34,42));self.relate('connect','right-face','right-skull')
        self.add_polyline('right-back',(42,28),(40,34),(42,42));self.relate('connect','right-back','right-skull')
        self.add_polyline('burst',(14,14),(14,8),(20,11),(24,6),(28,11),(34,8),(34,14))
''','No useful Lucide match; source-defined opposed profiles with a geometric burst.','Small facial rounding simplified.',
    'Shared human_ref/user.svg reviewed. Connected head/neck profiles; no detached-head gap applies.')
add('SQUARE','A hot chili pepper beside a flame.','Asymmetric tapered pepper with a short stem; detached flame silhouette on the left.', '''
        self.add_arc('pepper-top',(28,16),(42,22),radius_x=8,radius_y=7)
        self.add_arc('pepper-outside',(42,22),(20,42),radius_x=24)
        self.add_arc('pepper-inside',(20,42),(28,16),radius_x=23,sweep=False)
        self.add_contour('pepper','pepper-top','pepper-outside','pepper-inside',closed=True)
        self.add_arc('stem',(32,14),(36,6),radius_x=8)
        self.add_polyline('flame',(12,12),(14,22),(20,28),(18,36),(14,32),(12,36),(6,32),(6,26),(12,12))
''','No useful Lucide pepper match; smooth arc silhouette and asymmetry preserve the source.','Small inner flame lick omitted to keep the flame open.')
add('SQUARE','A percent sign with two circular counters.','Equal circles mirrored around the canvas center and a diagonal slash.', '''
        for i,c in enumerate((12,36)):self.circle(f'counter-{i}',c,c,6)
        self.add_line('slash',(6,42),(42,6))
''','circle-percent: clean slash and circular counters; source has no outer enclosure.')
add('SQUARE','A declining bar chart beneath a downward arrow.','Four bars in an arithmetic series; shared baseline; separate descending arrow.', '''
        xs=(8,19,30,41)
        self.add_polyline('baseline',(6,42),*((x,42) for x in xs),(42,42))
        for i,x in enumerate(xs):
            self.add_line(f'bar-{i}',(x,18+i*6),(x,42));self.relate('connect',f'bar-{i}','baseline')
        self.add_line('trend',(8,6),(40,22))
        self.add_polyline('arrow',(30,20),(40,22),(38,12));self.relate('connect','arrow','trend')
''','trending-down: distinct direction stroke and arrowhead.','Outlined bars reduced to four clean vertical strokes, retaining relative heights.')
add('SQUARE','An envelope holding an increasing chart.','Envelope boundary, three chart bars, and a rising trend arrow above.', '''
        self.add_polyline('envelope',(6,26),(24,36),(42,26),(42,42),(6,42),closed=True)
        for i,(x,y,end) in enumerate(((12,22,29),(24,18,36),(36,14,29))):self.add_line(f'bar-{i}',(x,y),(x,end))
        self.add_polyline('trend',(8,18),(16,10),(23,14),(32,6),(42,6))
        self.add_polyline('arrow',(34,6),(42,6),(42,14));self.relate('connect','arrow','trend')
''','trending-down: continuous trend stroke, reversed for increase; source owns envelope/chart layout.','Three outlined bars reduced to vertical strokes.')
add('SQUARE','A hand holding a tablet displaying a rising chart.','Open tablet boundary accommodates the gripping thumb; separate trend and bars inside.', '''
        self.add_polyline('tablet',(30,42),(6,42),(6,6),(34,6),(34,26))
        self.add_polyline('trend',(14,24),(26,12));self.add_polyline('arrow',(18,12),(26,12),(26,20));self.relate('connect','trend','arrow')
        for i,x in enumerate((14,22,30)):self.add_line(f'bar-{i}',(x,34-i*3),(x,38))
        self.add_polyline('hand',(34,20),(40,28),(40,34),(42,42))
        self.add_arc('thumb-top',(30,30),(34,26),radius_x=4)
        self.add_polyline('thumb',(30,30),(34,36),(34,40),(38,42));self.relate('connect','thumb','thumb-top')
''','monitor: clean display perimeter; pencil: coherent diagonal stroke for trend.','Tiny chart divisions omitted.',
    'Shared human_ref/user.svg reviewed; this is a hand and does not have a head/body gap.')
add('SQUARE','A snowflake inside a rounded square for permafrost.','Six snowflake arms sharing one center; repeated forked branch construction.', '''
        self.rounded('frame',6,6,42,42)
        ends=[(24,14),(33,19),(33,29),(24,34),(15,29),(15,19)]
        for i,p in enumerate(ends):self.add_line(f'arm-{i}',(24,24),p)
        self.relate('connect',*(f'arm-{i}' for i in range(6)))
        forks=[((20,14),(24,18),(28,14)),((33,15),(30,21),(36,22)),((36,26),(30,27),(33,33)),((20,34),(24,30),(28,34)),((15,33),(18,27),(12,26)),((12,22),(18,21),(15,15))]
        for i,pts in enumerate(forks):
            self.add_polyline(f'fork-{i}',*pts)
''','snowflake: repeated six-way arms and branches; rounded enclosure from monitor.')
add('HRECT_L','A person with two upward improvement arrows.','Circular head, exact detached shoulder gap, and matched arrows on both sides.', '''
        self.bust('person',24,20,6,12,40,6)
        for i,x in enumerate((10,38)):
            self.add_line(f'shaft-{i}',(x,26),(x,8))
            self.add_polyline(f'head-{i}',(x-6,14),(x,8),(x+6,14));self.relate('connect',f'shaft-{i}',f'head-{i}')
        self.add_line('crown-mark',(24,10),(24,14));self.relate('connect','crown-mark','person-head')
''','Shared human_ref/user.svg: circular head and broad curved shoulders; source arrows retain bilateral placement.','None.',
    'Head center (24,20), radius 6: lower centerline y=26. Shoulder apex (24,34): exact gap 8 centerline / 4 ink. Bust, not a stick figure.')
add('SQUARE','A magnifying glass framing a broad-shouldered person.','Lens uses exact integer circle points for shoulder and handle joins; detached inner head.', '''
        points=[(12,9),(33,12),(33,30),(30,33),(9,30)]
        for i,p in enumerate(points):self.add_arc(f'rim-{i}',p,points[(i+1)%len(points)],radius_x=15)
        self.add_contour('lens',*(f'rim-{i}' for i in range(len(points))),closed=True)
        self.add_line('handle',(30,33),(42,42));self.relate('connect','handle','lens')
        self.circle('person-head',21,16,4)
        self.add_arc('person-shoulders',(9,30),(33,30),radius_x=12,radius_y=2);self.relate('connect','person-shoulders','lens')
''','user-search: circular head and magnifier; source places the person inside the lens.','Shoulder curvature flattened to preserve the exact head gap.',
    'Shared human_ref/user.svg inspected. Head bottom y=20, shoulder apex y=28: exact 8-unit centerline / 4-unit ink gap. Broad shoulders are intentionally shallow; silhouette fidelity requires review.')
add('SQUARE','A magnifying glass framing a small upright person.','Lens and exact-circle handle attachment; inner head and narrow rounded upper torso.', '''
        self.add_arc('rim-a',(30,33),(12,9),radius_x=15)
        self.add_arc('rim-b',(12,9),(30,33),radius_x=15)
        self.add_contour('lens','rim-a','rim-b',closed=True)
        self.add_line('handle',(30,33),(42,42));self.relate('connect','handle','lens')
        self.circle('person-head',21,15,3)
        self.add_arc('shoulders',(16,31),(26,31),radius_x=5)
        self.add_line('body-left',(16,31),(16,34));self.add_line('body-right',(26,31),(26,34))
        self.relate('connect','shoulders','body-left');self.relate('connect','shoulders','body-right')
''','user-search: rounded head and shoulder construction; magnifier encircles the person as in source.','None.',
    'Shared human_ref/user.svg inspected. Head bottom y=18, shoulder apex y=26: exact centerline gap 8 / visible ink gap 4. Small upright bust, not a stick figure.')
assert len(specs)==20
for r,s in zip(rows,specs):
 d=Path(r['result_dir']);uid=r['source_uuid'];name=r['icon_id']
 source='from icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n\n'
 source+=f'SOURCE_ICON_ID = {uid!r}\nSOURCE_PATH = {r["reference_path"]!r}\nAUTHOR = {AUTHOR!r}\n\n'
 source+=f'class Drawing(Solo48):\n    """{s["subject"]}\n    Plan: {s["plan"]}\n    Reference: {s["construction_reference"]}\n    """\n'
 source+=f'    icon_id = {name!r}\n    keyshape = Keyshape.{s["keyshape"]}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(r["concept"].split())!r}\n'
 if s['human_construction']:source+=f'    # {s["human_construction"]}\n'
 source+=helpers+'\n    def build(self):\n'+s['code']
 py=d/(name.replace('-','_')+'_'+uid.replace('-','_')+'.py');py.write_text(source)
 result={**r,**{k:v for k,v in s.items() if k!='code'},'module':py.name,'svg':name+'.svg'}
 try:
  sp=importlib.util.spec_from_file_location('candidate_'+uid,py);mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod);icon=mod.Drawing()
  report=icon.validate_icon();(d/'validation.txt').write_text(report.describe());result['validation_status']=report.status
  svg=icon.to_svg();(d/result['svg']).write_text(svg)
  for theme,fg,bg in [('light','#111111','#ffffff'),('dark','#ffffff','#171717')]:
   for size in (48,288):cairosvg.svg2png(bytestring=svg.replace('currentColor',fg).replace('#000000',fg).encode(),write_to=str(d/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
 except Exception:
  result['validation_status']='error';result['error']=traceback.format_exc();(d/'error.txt').write_text(result['error'])
 (d/'candidate.json').write_text(json.dumps(result,indent=2));print(name,result['validation_status'],flush=True)
