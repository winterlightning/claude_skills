"""Valve logo.
Symbol plan: After enlarged aperture, rebalancing, HRECT_L and simplified-A trials, restored full letters with redistributed widths. Centerline4,10..44,38.
Omissions: None in final; simplified A trial rejected for fidelity and remaining crowding.
Construction references: No useful Lucide wordmark match; supplied VALVE reference.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cbc8a808-542b-49df-b4bd-c313efd61052'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/valve logo_cbc8a808-542b-49df-b4bd-c313efd61052.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='valve-logo'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('valve', 'logo')

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
        # Final condensed layout preserves all five letters and source ordering.
        self.add_polyline('v-first',(4,10),(7,38),(10,10))
        self.add_polyline('a-sides',(14,38),(16,24),(18,10),(20,24),(22,38))
        self.add_line('a-bar',(16,24),(20,24));self.relate('connect','a-sides','a-bar')
        self.add_polyline('l',(27,10),(27,38),(30,38))
        self.add_polyline('v-second',(32,10),(35,38),(38,10))
        self.add_polyline('e',(44,10),(42,10),(42,24),(42,38),(44,38))
        self.add_line('e-middle',(42,24),(44,24));self.relate('connect','e','e-middle')
