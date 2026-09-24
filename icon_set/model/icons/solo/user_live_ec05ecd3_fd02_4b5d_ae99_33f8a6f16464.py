"""User live.
Symbol plan: Frontal user: head(24,8)radius2; shoulder apex18 gives exact8 centerline/4 ink gap. LIVE baseline42; outer L/E cap26 and inner I/V cap28 clear shoulders. SQUARE bounds6..42.
Omissions: Inner broadcast ring removed; remaining signal split into flanking arcs. Condensed LIVE glyphs use taller E to retain8-unit bar pitch.
Construction references: human_ref/user.svg for head and shoulders; Lucide radio for nested signal arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ec05ecd3-fd02-4b5d-ae99-33f8a6f16464'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/user live_ec05ecd3-fd02-4b5d-ae99-33f8a6f16464.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='user-live'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('user', 'live')

    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            kind,end,*args=op
            if at==end: continue
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,at,end)
            elif kind=='A': self.add_arc(m,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            else: self.add_bezier(m,at,(args[0],args[1],end))
            members.append(m);at=end
        if closed and at!=start:
            self.add_line(n+'-close',at,start);members.append(n+'-close')
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        ops=[('L',(x,t)) for x in sorted(top) if l+k<x<r-k]
        ops += [('L',(r-k,t)),('A',(r,t+k),k,k,True)]
        ops += [('L',(r,y)) for y in sorted(right) if t+k<y<b-k]
        ops += [('L',(r,b-k)),('A',(r-k,b),k,k,True)]
        ops += [('L',(x,b)) for x in sorted(bottom,reverse=True) if l+k<x<r-k]
        ops += [('L',(l+k,b)),('A',(l,b-k),k,k,True)]
        ops += [('L',(l,y)) for y in sorted(left,reverse=True) if t+k<y<b-k]
        ops += [('L',(l,t+k)),('A',(l+k,t),k,k,True)]
        self.path(n,(l+k,t),ops,True)

    def build(self):
        self.add_arc('signal-left',(10,6),(10,18),radius_x=4,radius_y=6,sweep=False)
        self.add_arc('signal-right',(38,6),(38,18),radius_x=4,radius_y=6,sweep=True)
        self.circle('head',24,8,2)
        self.add_arc('shoulders',(20,20),(28,20),radius_x=4,radius_y=2)
        self.add_polyline('letter-l',(6,26),(6,42),(10,42))
        self.add_line('letter-i',(18,28),(18,42))
        self.add_polyline('letter-v',(26,28),(29,42),(32,28))
        self.add_polyline('letter-e',(42,26),(40,26),(40,34),(40,42),(42,42))
        self.add_line('e-middle',(40,34),(42,34));self.relate('connect','letter-e','e-middle')
