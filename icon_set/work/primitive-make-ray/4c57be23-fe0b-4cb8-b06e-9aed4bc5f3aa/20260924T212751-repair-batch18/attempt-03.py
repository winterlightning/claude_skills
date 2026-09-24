"""Suitcase pill, drawn from its complete supplied reference.
Symbol plan: preserve the subject, nested symbols, repeats and intentional overlaps.
Each repeated part and rounded rectangle owns its parameters and attachment nodes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4c57be23-fe0b-4cb8-b06e-9aed4bc5f3aa'
SOURCE_PATH = 'pictographic-primitives/other/suitcase pill_4c57be23-fe0b-4cb8-b06e-9aed4bc5f3aa.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='suitcase-pill'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('suitcase', 'pill')

    # Keyshape visible extremes: (4, 4, 44, 44); centerline extremes: (6, 6, 42, 42).
    def build(self):
        # Horizontal capsule retains both rounded halves and central seam.
        self.rect('case',4,16,44,40,4,top=(16,32))
        self.path('handle',(16,16),[('L',(16,12)),('A',(20,8),4),('L',(28,8)),('A',(32,12),4),('L',(32,16))])
        self.relate('connect','case','handle')
        self.add_arc('cap-left',(16,32),(16,24),radius_x=4)
        self.add_polyline('pill-top',(16,24),(24,24),(32,24))
        self.add_arc('cap-right',(32,24),(32,32),radius_x=4)
        self.add_polyline('pill-bottom',(32,32),(24,32),(16,32))
        self.add_contour('pill','cap-left','pill-top-1','pill-top-2','cap-right','pill-bottom-1','pill-bottom-2',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['pill-top','pill-bottom']]
        self.add_line('pill-seam',(24,24),(24,32));self.relate('connect','pill-seam','pill')


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

