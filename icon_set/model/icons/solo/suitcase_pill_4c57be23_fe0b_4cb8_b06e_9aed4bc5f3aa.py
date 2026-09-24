"""A medical suitcase containing a diagonal capsule.
Symbol plan and construction: briefcase-medical and pill: rounded case, attached handle and tangent capsule caps.
Keyshape: SQUARE preserves a broad case and top handle within centerlines (6,6)-(42,42).
Omissions: Capsule seam removed; the diagonal capsule and suitcase remain.
Review: Approved in both themes at 48px and enlarged size. The handle and case are symmetric; the pill follows the source diagonal."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='4c57be23-fe0b-4cb8-b06e-9aed4bc5f3aa'
SOURCE_PATH = 'pictographic-primitives/other/suitcase pill_4c57be23-fe0b-4cb8-b06e-9aed4bc5f3aa.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='suitcase-pill'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('suitcase', 'pill')

    # Keyshape visible extremes: (4, 4, 44, 44); centerline extremes: (6, 6, 42, 42).
    def build(self):
        # A short diagonal capsule with matched rounded ends and a shared seam.
        self.suitcase()
        self.add_bezier('cap-low',(20,26),((16,30),(22,36),(26,32)))
        self.add_polyline('side-low',(26,32),(27,31),(28,30))
        self.add_bezier('cap-high',(28,30),((32,26),(26,20),(22,24)))
        self.add_polyline('side-high',(22,24),(21,25),(20,26))
        self.add_contour('pill','cap-low','side-low-1','side-low-2','cap-high','side-high-1','side-high-2',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['side-low','side-high']]
        # Omit the central seam to leave one readable capsule opening.



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
