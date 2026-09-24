"""Switch lite, drawn from its complete supplied reference.
Symbol plan: preserve the subject, nested symbols, repeats and intentional overlaps.
Each repeated part and rounded rectangle owns its parameters and attachment nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='a7738f9c-a514-4341-bcd3-0d5e5ba614bd'
SOURCE_PATH='icon_set/work/todo-references/switch lite_a7738f9c-a514-4341-bcd3-0d5e5ba614bd.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='switch-lite'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('switch', 'lite')

    # Keyshape visible extremes: (2, 8, 46, 40); centerline extremes: (4, 10, 44, 38).
    def build(self):
        # Console silhouette with screen, two left controls and two right buttons.
        # HRECT_M centerlines (4,10)-(44,38).
        self.rect('console',4,10,44,38,7)
        self.add_polyline('screen',(18,18),(30,18),(30,30),(18,30),closed=True)
        self.add_polyline('upper-control',(10,20),(12,20),(12,17))
        self.add_polyline('plus-v',(11,26),(11,28),(11,30))
        self.add_line('plus-h-left',(9,28),(11,28))
        self.add_line('plus-h-right',(11,28),(13,28))
        self.relate('connect','plus-v','plus-h-left','plus-h-right')
        for i,y in enumerate((19,29)): self.circle(f'button-{i}',37,y,2)


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

