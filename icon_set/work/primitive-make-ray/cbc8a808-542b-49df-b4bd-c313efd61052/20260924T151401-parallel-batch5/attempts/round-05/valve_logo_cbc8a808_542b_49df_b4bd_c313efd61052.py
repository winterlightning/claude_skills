"""Valve logo.
Symbol plan: Complete VALVE word in source order; matching V construction and E halves; A aperture enlarged. Bounds4,10..44,38.
Omissions: None.
Construction references: No useful local Lucide wordmark match; supplied reference controls letter identities and ordering.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cbc8a808-542b-49df-b4bd-c313efd61052'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/valve logo_cbc8a808-542b-49df-b4bd-c313efd61052.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='valve-logo'
    keyshape=Keyshape.HRECT_L
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
        # Owning layout controls widths and all glyph origins in one row.
        x0=4; top=8; bottom=40
        self.add_polyline('v-first',(4,16),(6,bottom),(8,16))
        self.add_polyline('a-sides',(12,bottom),(18,top),(24,bottom))
        self.add_polyline('l',(29,top),(29,32),(31,32))
        self.add_polyline('v-second',(34,16),(36,bottom),(38,16))
        self.add_polyline('e',(44,top),(42,top),(42,24),(42,bottom),(44,bottom))
        self.add_line('e-middle',(42,24),(44,24));self.relate('connect','e','e-middle')
