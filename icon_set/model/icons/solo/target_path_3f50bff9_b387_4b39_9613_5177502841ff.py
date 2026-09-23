"""Target path, drawn from its complete supplied reference.
Symbol plan: preserve the subject, nested symbols, repeats and intentional overlaps.
Each repeated part and rounded rectangle owns its parameters and attachment nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='3f50bff9-b387-4b39-9613-5177502841ff'
SOURCE_PATH='icon_set/work/todo-references/target path_3f50bff9-b387-4b39-9613-5177502841ff.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='target-path'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('target', 'path')

    # Keyshape visible extremes: (4, 4, 44, 44); centerline extremes: (6, 6, 42, 42).
    def build(self):
        # Upright outlined person on a dashed bending route and a rightward arrow.
        # human_ref/full_body_ref.png informs the round head and simple limb vocabulary.
        # Head bottom 12 and shoulder crest 20 give exactly 4 units of visible gap.
        self.circle('head',24,9,3)
        self.path('body',(20,33),[('L',(20,30)),('L',(19,28)),('L',(19,25)),
            ('A',(24,20),5),('A',(29,25),5),('L',(29,28)),('L',(28,30)),('L',(28,33))])
        self.add_bezier('route-top',(10,24),((9,24),(8,25),(8,26)))
        self.add_arc('route-left',(6,34),(8,38),radius_x=8,sweep=False)
        self.add_line('route-bottom',(16,42),(20,42))
        self.add_line('route-dash',(28,42),(30,42))
        self.add_polyline('arrow-head',(38,22),(42,26),(38,30))
        self.add_line('arrow-shaft',(38,26),(42,26))
        self.relate('connect','arrow-head','arrow-shaft')


    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)

    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        # One rounded rectangle owns paired radii, extents, and connection splits.
        seg=[('L',(x,t)) for x in sorted(set(top)) if l+k<x<r-k]
        seg += [('L',(r-k,t)),('A',(r,t+k),k)]
        seg += [('L',(r,y)) for y in sorted(set(right)) if t+k<y<b-k]
        seg += [('L',(r,b-k)),('A',(r-k,b),k)]
        seg += [('L',(x,b)) for x in sorted(set(bottom),reverse=True) if l+k<x<r-k]
        seg += [('L',(l+k,b)),('A',(l,b-k),k)]
        seg += [('L',(l,y)) for y in sorted(set(left),reverse=True) if t+k<y<b-k]
        seg += [('L',(l,t+k)),('A',(l+k,t),k)]
        self.path(n,(l+k,t),seg,True)

    def suitcase(self):
        # SQUARE: ink (4,4)-(44,44); centerlines (6,6)-(42,42).
        self.rect('case',6,14,42,42,4,top=(16,32))
        self.path('handle',(16,14),[('L',(16,10)),('A',(20,6),4),
            ('L',(28,6)),('A',(32,10),4),('L',(32,14))])
        self.relate('connect','case','handle')

    def check(self,n,x,y):
        self.add_polyline(n,(x,y),(x+3,y+3),(x+9,y-3))

