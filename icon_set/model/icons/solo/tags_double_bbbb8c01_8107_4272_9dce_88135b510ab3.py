"""Two overlapping straight-sided tags with an eyelet.
Plan: Room for the diagonal tag stack. Open rear top and straight front tail preserve this reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='bbbb8c01-8107-4272-9dce-88135b510ab3'
SOURCE_PATH = 'pictographic-primitives/interface-essential/tags double_bbbb8c01-8107-4272-9dce-88135b510ab3.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tags-double-bbbb8c01'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases=()
    keywords=('tags', 'double')

    # Keyshape visible extremes: (4, 4, 44, 44); centerline extremes: (6, 6, 42, 42).
    def build(self):
        # Wider leading band preserves a real circular eyelet with certified clearance.
        self.add_polyline('front',(6,14),(22,14),(38,30),(26,42),(6,32),closed=True)
        self.add_polyline('rear',(12,6),(26,6),(42,22),(42,26),(38,30))
        self.relate('connect','front','rear')
        self.circle('hole',17,25,2)

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


PLAN = 'Two overlapping straight-sided tags with an eyelet. Room for the diagonal tag stack.'
OMISSIONS = 'None.'
CONSTRUCTION_REFERENCES = ['icon_set/references/lucide/original/tag.svg', 'icon_set/references/lucide/atomic-debug/tag.svg']
PARENT_SOURCE = 'icon_set/model/icons/solo/tags_double_bbbb8c01_8107_4272_9dce_88135b510ab3.py'
