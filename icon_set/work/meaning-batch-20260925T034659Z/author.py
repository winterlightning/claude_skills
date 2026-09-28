import json, textwrap
from pathlib import Path

AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None  # Per-input exact IDs are read from entries.json.
SOURCE_PATH = None
ROOT = Path(__file__).parent
HELPERS = '''
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
'''
DESIGNS = {
'square-j': ('SQUARE','Conventional capital J with top bar and rounded lower hook; remove misleading right arrow.', '''
self.box('frame',6,6,42,42)
self.add_line('top',(17,15),(31,15))
self.add_line('stem',(27,15),(27,27))
self.add_arc('hook',(27,27),(17,27),radius_x=5)
self.add_contour('letter','stem','hook')
self.relate('connect','top','letter')
'''),
'square-u': ('SQUARE','Conventional capital U with equal uprights and semicircular bottom; remove right arrow.', '''
self.box('frame',6,6,42,42)
self.add_line('left',(16,15),(16,25))
self.add_arc('bottom',(16,25),(32,25),radius_x=8,sweep=False)
self.add_line('right',(32,25),(32,15))
self.add_contour('letter','left','bottom','right')
'''),
'square-v': ('SQUARE','Symmetric capital V, replacing asymmetric check mark.', '''
self.box('frame',6,6,42,42)
axis=24
self.add_polyline('letter',(axis-9,15),(axis,33),(axis+9,15))
'''),
'square-y': ('SQUARE','Capital Y with symmetric fork and descending stem, replacing dash.', '''
self.box('frame',6,6,42,42)
self.add_polyline('fork',(15,15),(24,24),(33,15))
self.add_line('stem',(24,24),(24,33))
self.relate('connect','fork','stem')
'''),
'square-z': ('SQUARE','Capital Z with two horizontal bars and connecting diagonal, replacing dash and dot.', '''
self.box('frame',6,6,42,42)
self.add_polyline('letter',(15,15),(33,15),(15,33),(33,33))
'''),
'square-right': ('SQUARE','Right-pointing arrow inside a true square, replacing tag-like frame.', '''
self.box('frame',6,6,42,42)
self.add_line('shaft',(15,24),(33,24))
self.add_polyline('head',(24,15),(33,24),(24,33))
self.relate('connect','shaft','head')
'''),
'square-up-right': ('SQUARE','Arrow points diagonally upper-right, with equal orthogonal arrowhead arms.', '''
self.box('frame',6,6,42,42)
self.add_line('shaft',(15,33),(33,15))
self.add_polyline('head',(19,15),(33,15),(33,29))
self.relate('connect','shaft','head')
'''),
'square-up-left': ('SQUARE','Arrow points diagonally upper-left, replacing bent upward arrow.', '''
self.box('frame',6,6,42,42)
self.add_line('shaft',(33,33),(15,15))
self.add_polyline('head',(15,29),(15,15),(29,15))
self.relate('connect','shaft','head')
'''),
'angle-down': ('HRECT_M','Conventional downward chevron; equal mirrored arms replace diagonal arrow.', '''
axis=24
self.add_polyline('chevron',(axis-20,10),(axis,38),(axis+20,10))
'''),
'square-q': ('SQUARE','Open Q bowl and clear diagonal tail; distinguish Q from magnifier.', '''
self.box('frame',6,6,42,42)
self.add_line('top',(21,15),(27,15))
self.add_arc('tr',(27,15),(32,20),radius_x=5)
self.add_line('right',(32,20),(32,26))
self.add_arc('br',(32,26),(27,31),radius_x=5)
self.add_line('bottom',(27,31),(21,31))
self.add_arc('bl',(21,31),(16,26),radius_x=5)
self.add_line('left',(16,26),(16,20))
self.add_arc('tl',(16,20),(21,15),radius_x=5)
self.add_contour('bowl','top','tr','right','br','bottom','bl','left','tl',closed=True)
self.add_line('tail',(25,25),(33,33))
self.relate('connect','tail','bowl')
'''),
}

DESIGNS.update({
'bitcoin-with-adjust': ('VRECT_M','Recognizable Bitcoin B with two top and bottom currency ticks; omit adjustment controls to prioritize reviewer request for bitcoin.', '''
self.add_polyline('spine',(14,12),(14,24),(14,36))
self.add_line('top',(10,12),(32,12))
self.add_arc('upper',(32,12),(32,24),radius_x=6)
self.add_line('mid',(14,24),(32,24))
self.add_arc('lower',(32,24),(32,36),radius_x=6)
self.add_line('bottom',(32,36),(10,36))
for a,b in [('spine','top'),('spine','mid'),('spine','bottom'),('top','upper'),('upper','mid'),('upper','lower'),('mid','lower'),('lower','bottom')]:
    self.relate('connect',a,b)
for x in (18,26):
    self.add_line(f'top-tick-{x}',(x,4),(x,12))
    self.add_line(f'bottom-tick-{x}',(x,36),(x,44))
    self.relate('connect',f'top-tick-{x}','top')
    self.relate('connect',f'bottom-tick-{x}','bottom')
'''),
'bow-and-arrow-reference': ('VRECT_L','Conventional curved vertical bow, taut straight string and rightward nocked arrow; remove confusing diagonal double-arrow shape.', '''
self.add_arc('bow-top',(8,4),(24,24),radius_x=16,radius_y=20)
self.add_arc('bow-bottom',(24,24),(8,44),radius_x=16,radius_y=20)
self.add_contour('bow','bow-top','bow-bottom')
self.add_polyline('string',(8,4),(8,24),(8,44))
self.add_polyline('shaft',(8,24),(24,24),(40,24))
self.add_polyline('arrowhead',(32,16),(40,24),(32,32))
self.relate('connect','bow','string')
self.relate('connect','bow','shaft')
self.relate('connect','string','shaft')
self.relate('connect','shaft','arrowhead')
'''),
'box-delivery-truck': ('HRECT_L','Delivery truck with tall rectangular cargo box, distinct cab and two large wheels; replace flattened cab silhouette.', '''
self.add_polyline('cargo',(4,28),(4,8),(28,8),(28,28))
self.add_polyline('cab',(28,16),(36,16),(44,26),(44,28))
self.relate('connect','cargo','cab')
self.add_line('chassis',(4,28),(44,28))
self.relate('connect','cargo','chassis')
self.relate('connect','cab','chassis')
for x in (12,36): self.circle(f'wheel-{x}',x,37,3)
'''),
'tog': ('SQUARE','Tag with clearly visible punched hole and clipped shoulder; interpret ambiguous Tog from its tag reference.', '''
self.add_polyline('outline',(6,6),(26,6),(42,22),(22,42),(6,26),closed=True)
self.circle('hole',17,17,3)
'''),
'square-parking-slash': ('SQUARE','No parking symbol: capital P crossed by a complete diagonal prohibition slash, replacing R-like mark.', '''
self.box('frame',6,6,42,42)
self.add_line('stem',(16,15),(16,33))
self.add_line('top',(16,15),(25,15))
self.add_arc('bowl',(25,15),(25,27),radius_x=6)
self.add_line('mid',(25,27),(16,27))
for a,b in [('stem','top'),('stem','mid'),('top','bowl'),('mid','bowl')]:self.relate('connect',a,b)
self.add_line('slash',(15,15),(33,33))
for p in ('stem','top','bowl','mid'):self.relate('connect','slash',p)
'''),
'briefcase-dollar': ('SQUARE','Briefcase with clear dollar sign and external handle; replace angular S-like mark with curved currency symbol.', '''
self.box('case',6,14,42,42)
self.add_polyline('handle',(16,14),(16,6),(32,6),(32,14))
self.relate('connect','handle','case')
self.add_line('s-top',(29,23),(23,23))
self.add_arc('s-upper',(23,23),(23,29),radius_x=3,sweep=False)
self.add_line('s-mid',(23,29),(25,29))
self.add_arc('s-lower',(25,29),(25,35),radius_x=3)
self.add_line('s-bottom',(25,35),(19,35))
self.add_contour('s','s-top','s-upper','s-mid','s-lower','s-bottom')
self.add_line('currency',(24,20),(24,38))
self.relate('connect','s','currency')
'''),
'blackberry-cluster-with-a-single-leaf': ('VRECT_L','Blackberry with lobed fruit outline, three drupelet marks and one attached leaf; simplify overlapping tiny berry circles.', '''
self.add_arc('top',(8,24),(40,24),radius_x=16,radius_y=8)
self.add_arc('right',(40,24),(24,44),radius_x=16,radius_y=20)
self.add_arc('left',(24,44),(8,24),radius_x=16,radius_y=20)
self.add_contour('fruit','top','right','left',closed=True)
self.add_dot('drupelet-left',(16,26))
self.add_dot('drupelet-right',(32,26))
self.add_dot('drupelet-bottom',(24,35))
self.add_arc('leaf-top',(24,16),(40,4),radius_x=16,sweep=True)
self.add_arc('leaf-bottom',(40,4),(24,16),radius_x=16,sweep=True)
self.add_contour('leaf','leaf-top','leaf-bottom',closed=True)
self.relate('connect','leaf','fruit')
'''),
'boxer': ('VRECT_L','Boxer in a wide fighting stance with one punching glove extended; replace generic head between disconnected mitten shapes.', '''
self.circle('head',20,8,4)
self.add_line('torso',(20,20),(20,32))
self.add_polyline('legs',(10,44),(20,32),(30,44))
self.add_line('rear-arm',(20,20),(8,28))
self.add_line('punch-arm',(20,20),(32,20))
self.circle('glove',36,20,4)
self.relate('connect','torso','legs')
self.relate('connect','torso','rear-arm')
self.relate('connect','torso','punch-arm')
self.relate('connect','rear-arm','punch-arm')
self.relate('connect','punch-arm','glove')
self.mark_human_figure('boxer',head='head',torso='torso',torso_junction='start')
'''),
'boxer-avatar': ('VRECT_L','Boxer portrait with broad shoulders and headguard framing the face; omit facial microdetails.', '''
self.add_arc('helmet',(10,18),(38,18),radius_x=14)
self.add_polyline('left-pad',(10,18),(10,28),(18,28),(18,18))
self.add_polyline('right-pad',(38,18),(38,28),(30,28),(30,18))
self.relate('connect','helmet','left-pad')
self.relate('connect','helmet','right-pad')
self.add_arc('jaw',(18,18),(30,18),radius_x=6,sweep=False)
self.relate('connect','jaw','left-pad')
self.relate('connect','jaw','right-pad')
self.add_arc('shoulder',(8,44),(40,44),radius_x=16,radius_y=12)
'''),
})

# Repair the owning constructions, preserving their meaning and all thresholds.
k,p,b=DESIGNS['box-delivery-truck']
DESIGNS['box-delivery-truck']=(k,p,b.replace('28)', '26)').replace('(28,16)', '(28,16)'))
k,p,b=DESIGNS['boxer-avatar']
DESIGNS['boxer-avatar']=(k,p,b.replace('(10,28)','(10,24)').replace('(18,28)','(18,24)').replace('(38,28)','(38,24)').replace('(30,28)','(30,24)'))
k,p,b=DESIGNS['boxer']
b=b.replace("self.add_line('punch-arm',(20,20),(32,20))\nself.circle('glove',36,20,4)","""self.add_line('punch-arm',(20,20),(28,24))
self.add_line('glove-left',(28,24),(28,16))
self.add_arc('glove-tl',(28,16),(32,12),radius_x=4)
self.add_line('glove-top',(32,12),(36,12))
self.add_arc('glove-tr',(36,12),(40,16),radius_x=4)
self.add_line('glove-right',(40,16),(40,20))
self.add_arc('glove-br',(40,20),(36,24),radius_x=4)
self.add_line('glove-bottom',(36,24),(28,24))
self.add_contour('glove','glove-left','glove-tl','glove-top','glove-tr','glove-right','glove-br','glove-bottom',closed=True)""")
DESIGNS['boxer']=(k,p,b)
k,p,b=DESIGNS['square-parking-slash']
start=b.index('for a,b in')
b=b[:start]+"""self.add_contour('bowl-shape','top','bowl','mid')
self.relate('connect','stem','bowl-shape')
self.add_line('slash',(15,33),(33,15))
self.relate('connect','slash','stem')
self.relate('connect','slash','bowl-shape')
"""
DESIGNS['square-parking-slash']=(k,p,b)
DESIGNS['blackberry-cluster-with-a-single-leaf']=('VRECT_L','Lobed blackberry cluster with curved drupelet divisions and one upright attached leaf; remove strawberry-like dots.', '''
self.add_arc('crown',(14,26),(34,26),radius_x=10,radius_y=6)
self.add_arc('right-top',(34,26),(40,32),radius_x=6)
self.add_arc('right-bottom',(40,32),(34,38),radius_x=6)
self.add_arc('bottom-right',(34,38),(24,44),radius_x=10,radius_y=6)
self.add_arc('bottom-left',(24,44),(14,38),radius_x=10,radius_y=6)
self.add_arc('left-bottom',(14,38),(8,32),radius_x=6)
self.add_arc('left-top',(8,32),(14,26),radius_x=6)
self.add_contour('fruit','crown','right-top','right-bottom','bottom-right','bottom-left','left-bottom','left-top',closed=True)
self.add_arc('divider',(14,26),(34,26),radius_x=10,radius_y=6,sweep=False)
self.add_line('lower-seam',(24,32),(24,44))
self.relate('connect','divider','fruit')
self.relate('connect','divider','lower-seam')
self.relate('connect','lower-seam','fruit')
self.add_arc('leaf-left',(24,16),(24,4),radius_x=6)
self.add_arc('leaf-right',(24,4),(24,16),radius_x=6)
self.add_contour('leaf','leaf-left','leaf-right',closed=True)
self.add_line('stem',(24,16),(24,20))
self.relate('connect','stem','leaf')
self.relate('connect','stem','fruit')
''')

k,p,b=DESIGNS['boxer']
DESIGNS['boxer']=(k,p,b.replace("20,8","18,8").replace("20,20","18,20").replace("20,32","18,32"))
k,p,b=DESIGNS['square-parking-slash']
DESIGNS['square-parking-slash']=(k,p,b.replace("(15,33),(33,15)","(16,15),(34,33)"))
k,p,b=DESIGNS['blackberry-cluster-with-a-single-leaf']
DESIGNS['blackberry-cluster-with-a-single-leaf']=(k,p,b.replace("(24,16),(24,4),radius_x=6","(24,12),(24,4),radius_x=5,radius_y=4").replace("(24,4),(24,16),radius_x=6","(24,4),(24,12),radius_x=5,radius_y=4").replace("(24,16),(24,20)","(24,12),(24,20)"))
DESIGNS['briefcase-dollar']=('VRECT_L','Briefcase with a curved S and projecting currency ticks, avoiding tiny enclosed loops; preserve handle and recognizable dollar.', '''
self.add_polyline('case',(8,12),(40,12),(40,44),(8,44),closed=True)
self.add_polyline('handle',(16,12),(16,4),(32,4),(32,12))
self.relate('connect','handle','case')
self.add_arc('s-upper',(24,22),(24,28),radius_x=5,radius_y=3,sweep=False)
self.add_arc('s-lower',(24,28),(24,34),radius_x=5,radius_y=3)
self.add_contour('s','s-upper','s-lower')
self.add_line('currency-top',(24,20),(24,22))
self.add_line('currency-bottom',(24,34),(24,36))
self.relate('connect','s','currency-top')
self.relate('connect','s','currency-bottom')
''')

for e in json.loads((ROOT/'entries.json').read_text()):
    iid=e['icon_id']
    if iid not in DESIGNS: continue
    if (Path(e['run'])/'result.json').exists(): continue
    key,plan,body=DESIGNS[iid]
    ref='Lucide square-arrow-right rounded enclosure and joined arrow construction' if iid.startswith('square') else {'angle-down':'Lucide chevron-down mirrored continuous stroke','bitcoin-with-adjust':'Lucide bitcoin double currency ticks and two bowls','box-delivery-truck':'Lucide truck cargo/cab hierarchy and wheel alignment','tog':'Lucide tag clipped shoulder and punched hole','boxer':'human_ref/full_body_ref.png round head and coherent limbs; head bottom12 to torso20 gives exact 4-unit ink gap','boxer-avatar':'human_ref/user.svg broad shoulders and circular jaw; headguard retained from original'}.get(iid,'No useful exact Lucide match; supplied reference subject and geometric arc construction')
    code=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {e['source_uuid']!r}
SOURCE_PATH = {e['reference_path']!r}
AUTHOR = {AUTHOR!r}
# Plan: {plan}
# Construction reference: {ref}.
# Envelope: {key}; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = {iid!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = {tuple(iid.split('-'))!r}
    def build(self):
'''+textwrap.indent(textwrap.dedent(body).strip()+'\n','        ')+HELPERS
    run=Path(e['run'])
    (run/(iid.replace('-','_')+'_'+e['source_uuid'].replace('-','_')+'.py')).write_text(code)
    (run/'design.json').write_text(json.dumps(dict(plan=plan,keyshape=key,references=ref,omissions='Misleading source marks replaced with named concept.'),indent=2))
