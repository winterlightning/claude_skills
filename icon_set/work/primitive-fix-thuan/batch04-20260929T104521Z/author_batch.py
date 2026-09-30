"""Standalone primitive-make-ray authoring, with input identity per specification."""
import json
from pathlib import Path
import textwrap

AUTHOR = 'gpt-6'
ROOT = Path(__file__).parent
ITEMS = json.loads((ROOT/'items.json').read_text())

HELPERS = '''
        def path(n,start,*commands,closed=False):
            here=start; members=[]
            for j,cmd in enumerate(commands):
                k=f'{n}-{j}';kind,end,*args=cmd
                if kind=='L': self.add_line(k,here,end)
                elif kind=='A': self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def bez(n,a,*parts):self.add_bezier(n,a,*parts)
        def arc(n,a,b,r,ry=None,s=True):self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(a,b):self.relate('connect',a,b)
        def rect(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)
'''

# Each body is a new reference-based SOLO48 construction, not an SVG edit.
SPECS = {
1: ('HRECT_L', 'Lucide plane: coherent wing/body contours, rounded nose. Deliberate perspective asymmetry.', '''
path('wing',(8,32),('L',(16,26)),('L',(24,21)),('L',(40,10)),('C',(44,12),(44,8),(44,8)),('L',(44,18)),('L',(31,29)),('L',(18,40)),('C',(8,36),(12,40),(8,40)),('L',(8,32)),closed=True)
path('tail',(16,26),('L',(6,22)),('L',(4,8)),('L',(10,8)),('L',(16,20)),('L',(24,21)));join('tail','wing')
bez('nose',(24,21),((35,21),(42,24),(42,28)),((42,33),(36,31),(31,29)));join('nose','wing')
'''),
2: ('HRECT_L', 'Lucide hand-helping: round thumb and coherent curved palm; paired text rules.', '''
path('card',(20,8),('L',(41,8)),('A',(44,11),3,3,True),('L',(44,29)),('A',(41,32),3,3,True),('L',(36,32)),('L',(23,32)),('A',(20,29),3,3,True),('L',(20,24)))
path('thumb',(4,20),('C',(12,16),(8,20),(8,16)),('L',(20,16)),('A',(20,24),4,4,True),('L',(16,24)),('C',(10,28),(14,26),(12,28)));join('thumb','card')
bez('palm',(4,36),((8,36),(8,40),(14,40)),((28,40),(30,40),(36,32)));join('palm','card')
for j,y in enumerate((16,24)):line(f'text-{j}',(33,y),(36,y))
'''),
3: ('SQUARE', 'Lucide book-open and hand-helping: paper planes and a rounded grasp. Asymmetric holding hand.', '''
poly('paper',(6,22),(6,6),(30,6),(30,22))
line('message',(14,14),(22,14))
poly('envelope',(6,22),(6,38),(28,38))
path('fold',(6,22),('L',(16,28)),('C',(24,28),(19,30),(21,30)),('L',(30,22)))
join('paper','envelope');join('fold','paper');join('fold','envelope')
path('hand',(42,42),('C',(38,32),(38,38),(38,35)),('L',(38,21)),('C',(30,14),(38,18),(34,15)),('L',(30,22)),('L',(25,27)),('A',(25,35),4,4,False),('C',(30,42),(28,38),(27,40)))
join('hand','paper');join('hand','fold')
'''),
4: ('SQUARE', 'Lucide hand-helping: rounded thumb around a tilted ballot, broad ballot box below.', '''
poly('box',(6,30),(22,30),(42,30),(42,42),(6,42),closed=True)
poly('paper',(22,30),(6,14),(14,6),(23,15));join('paper','box')
path('thumb',(42,22),('L',(35,22)),('L',(29,22)),('A',(29,14),4,4,True),('L',(36,14)))
line('paper-right',(35,22),(22,30));join('paper-right','thumb');join('paper-right','box')
bez('hand-back',(23,15),((27,7),(32,6),(42,9)));join('hand-back','paper')
'''),
5: ('SQUARE', 'Lucide hand-helping: curving grasp and rounded palm; diagonal paper over a slot.', '''
poly('paper',(18,16),(6,28),(20,42),(36,26),(30,20))
path('hand',(32,6),('C',(18,16),(25,11),(21,12)),('A',(24,24),5,5,False),('L',(30,20)),('C',(42,14),(35,22),(36,18)));join('paper','hand')
poly('slot',(6,42),(20,42),(38,42));join('slot','paper')
'''),
6: ('SQUARE', 'Lucide hand: round finger tip and broad palm; exact shared cube vertices.', '''
poly('cube',(24,11),(33,6),(42,11),(42,22),(33,27),(33,16),(24,11),(24,20))
line('ridge',(33,16),(42,11));join('ridge','cube')
path('hand',(6,39),('L',(6,35)),('A',(10,35),2,2,True),('L',(10,26)),('A',(18,26),4,4,True),('L',(18,36)),('C',(26,42),(24,36),(26,38)))
'''),
7: ('SQUARE', 'Lucide hand-helping: curved palm and thumb, rounded card with circular identity mark.', '''
path('card',(21,6),('L',(39,6)),('A',(42,9),3,3,True),('L',(42,27)),('A',(39,30),3,3,True),('L',(26,30)),('L',(21,30)),('A',(18,27),3,3,True),('L',(18,9)),('A',(21,6),3,3,True),closed=True)
circle('portrait',30,15,2)
line('text',(27,23),(33,23))
path('hand',(18,27),('C',(10,22),(14,26),(14,20)),('C',(6,28),(7,21),(6,24)),('C',(14,42),(6,36),(8,42)),('L',(18,42)),('A',(26,34),8,8,False),('L',(26,30)));join('hand','card')
'''),
8: ('VRECT_L', 'Lucide hand-helping for palm curves; human circular head with a small attached hair lock.', '''
path('hand',(40,4),('L',(27,4)),('C',(12,10),(21,5),(15,9)),('A',(12,18),4,4,False),('C',(25,17),(17,18),(21,19)),('L',(32,12)),('L',(40,12)))
circle('child',24,35,9)
bez('hair',(24,26),((26,28),(24,30),(21,30)));join('hair','child')
'''),
9: ('SQUARE', 'Shared human user.svg: circular jaw and smooth shoulders; Lucide hand-helping for patting hand.', '''
path('face',(14,20),('L',(14,22)),('A',(34,22),10,10,False),('L',(34,20)))
path('shoulders',(6,42),('C',(16,36),(6,39),(11,36)),('L',(32,36)),('C',(42,42),(37,36),(42,39)))
join('face','shoulders')
path('hand',(42,6),('L',(27,6)),('C',(10,12),(22,7),(15,10)),('A',(14,20),5,5,False),('L',(22,18)),('C',(34,20),(24,21),(30,21)),('L',(42,20)));join('hand','face')
'''),
10: ('SQUARE', 'Lucide hand: rounded finger tips; shared series creates calm water waves.', '''
path('hand',(42,6),('L',(29,6)),('C',(14,11),(23,6),(16,9)),('A',(14,19),4,4,False),('L',(22,15)),('L',(20,23)),('A',(28,23),4,4,False),('L',(31,16)),('C',(35,21),(36,12),(37,14)),('L',(42,21)))
path('basin',(6,32),('L',(10,42)),('L',(38,42)),('L',(42,32)))
path('water',(6,32),('A',(18,32),6,2,False),('A',(30,32),6,2,True),('A',(42,32),6,2,False));join('water','basin')
'''),
11: ('HRECT_M', 'No useful exact Lucide moustache match; mirrored flowing lobes and upturned tips derive from one axis.', '''
path('moustache',(24,17),('C',(14,10),(20,10),(18,10)),('C',(4,20),(10,10),(10,24)),('C',(14,38),(4,33),(8,38)),('C',(24,29),(19,38),(22,34)),('C',(34,38),(26,34),(29,38)),('C',(44,20),(40,38),(44,33)),('C',(34,10),(38,24),(38,10)),('C',(24,17),(30,10),(28,10)),closed=True)
'''),
12: ('SQUARE', 'Lucide hand-helping: two mirrored cupped hands; larger teardrop with a round base.', '''
path('drop',(24,6),('C',(18,18),(22,10),(18,14)),('A',(30,18),6,6,False),('C',(24,6),(30,14),(26,10)),closed=True)
for side in (-1,1):
    def p(x,y):return (24+side*x,y)
    path(f'hand-{side}',p(18,42),('L',p(18,27)),('A',p(10,27),4,4,side<0),('L',p(10,34)),('C',p(4,42),p(10,37),p(6,38)))
'''),
13: ('SQUARE', 'Shared circular baby head and hair curl; Lucide hand-helping for rounded fingertip/hand curves.', '''
circle('baby',24,32,10)
bez('curl',(24,22),((26,24),(25,27),(23,27)));join('curl','baby')
for side in (-1,1):
    def p(x,y):return (24+side*x,y)
    path(f'hand-{side}',p(18,26),('C',p(15,14),p(17,22),p(18,18)),('L',p(5,6)),('C',p(7,13),p(1,8),p(4,10)))
'''),
14: ('SQUARE', 'Lucide headphones and book-open: round band with end cups and angled pages; shared circular human head.', '''
arc('band',(8,20),(40,20),16,14)
line('ear-left',(8,20),(8,24));line('ear-right',(40,20),(40,24));join('band','ear-left');join('band','ear-right')
circle('head',24,20,6)
poly('book',(6,32),(24,36),(42,32),(42,40),(24,42),(6,40),closed=True)
line('spine',(24,36),(24,42));join('spine','book')
'''),
15: ('VRECT_L', 'Shared human circular jaw and smooth shoulders; rounded helmet shape with an outlined goatee.', '''
path('helmet',(10,25),('L',(10,18)),('A',(38,18),14,14,True),('L',(38,25)))
path('face',(14,16),('L',(14,24)),('A',(34,24),10,10,False),('L',(34,16)))
path('hairline',(14,16),('C',(24,18),(17,13),(20,18)),('C',(34,16),(28,18),(31,13)));join('hairline','face')
path('goatee',(20,29),('L',(20,25)),('A',(28,25),4,4,True),('L',(28,29)))
path('body',(8,44),('A',(20,38),12,6,True),('L',(28,38)),('A',(40,44),12,6,True));join('body','face')
'''),
16: ('SQUARE', 'No exact Lucide migration match: shared node radii, symmetric edges and upward arrow; repeated chevrons reduced to one.', '''
for n,x,y in [('ul',9,17),('ur',39,17),('ll',9,32),('lr',39,32),('bottom',24,39)]:circle(n,x,y,3)
line('left',(9,20),(9,29));join('left','ul');join('left','ll')
line('right',(39,20),(39,29));join('right','ur');join('right','lr')
line('lower-left',(12,32),(21,39));join('lower-left','ll');join('lower-left','bottom')
line('lower-right',(36,32),(27,39));join('lower-right','lr');join('lower-right','bottom')
poly('arrow',(18,12),(24,6),(30,12));line('shaft',(24,6),(24,24));join('arrow','shaft')
'''),
17: ('SQUARE', 'Shared human full_body_ref.png: aligned round head, curved arm, exact 4u ink neck gap; source triangular tent.', '''
circle('head',12,11,5)
line('torso',(12,24),(12,33));self.mark_human_figure('hiker',head='head',torso='torso',torso_junction='start')
poly('legs',(6,42),(12,33),(18,42));join('legs','torso')
bez('arm',(12,24),((15,24),(15,28),(20,28)))
line('grip',(20,28),(24,28));join('arm','grip');join('arm','torso')
poly('pole',(24,24),(24,28),(24,42));join('pole','grip')
poly('tent',(32,42),(42,42),(37,23),(32,42),closed=True)
'''),
}

def author(index, attempt=1, body=None, keyshape=None):
    item=ITEMS[index-1]
    SOURCE_ICON_ID=item['uid'];SOURCE_PATH=item['ref']
    key,reference,definition=SPECS[index]
    if body is not None:definition=body
    if keyshape is not None:key=keyshape
    out=Path(item['run']).parent/f'20260929-batch04-attempt{attempt:02}'
    out.mkdir(exist_ok=True)
    meta=dict(concept=Path(SOURCE_PATH).stem[:-37],source_uuid=SOURCE_ICON_ID,reference_path=SOURCE_PATH)
    icon_id=item['key'].split('/')[1]
    (out/(icon_id+'.metadata.json')).write_text(json.dumps(meta,indent=2))
    (out/'review.md').write_text(item['review']+'\nFeedback: none supplied.\nConstruction: '+reference+'\n')
    source=f'''"""{item['review']}
Plan: {key}; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: {reference}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {SOURCE_ICON_ID!r}
SOURCE_PATH = {SOURCE_PATH!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {icon_id!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = {tuple(icon_id.split('-'))!r}
'''
    if index in (9,15):source+='    human_construction = "bust"\n'
    source+='\n    def build(self):\n'+HELPERS+textwrap.indent(textwrap.dedent(definition).strip()+'\n','        ')
    module=out/(icon_id.replace('-','_')+'_'+SOURCE_ICON_ID.replace('-','_')+'.py')
    module.write_text(source)
    return out,module

if __name__=='__main__':
    import sys
    for n in map(int,sys.argv[1:]):print(author(n)[0])
