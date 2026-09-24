"""Valve logo.
Symbol plan: Full single-row VALVE, matching V widths4, rounded A aperture8, common cap/baseline10/38. Bounds4,10..44,38.
Omissions: A apex softened to enlarge its opening; no letters removed.
Construction references: Supplied VALVE reference; no useful local Lucide wordmark match.
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
        # Repeated V definition and a single shared row own all letter spacing.
        top,bottom=8,40
        for name,left in [('v-first',4),('v-second',31)]:
            self.add_polyline(name,(left,top),(left+2,bottom),(left+4,top))
        self.path('a-sides',(13,bottom),[('L',(13,26)),('L',(13,12)),('A',(23,12),5,4,True),('L',(23,26)),('L',(23,bottom))])
        self.add_line('a-bar',(13,26),(23,26));self.relate('connect','a-sides','a-bar')
        self.add_polyline('l',(26,top),(26,bottom),(27,bottom))
        self.add_polyline('e',(44,top),(42,top),(42,24),(42,bottom),(44,bottom))
        self.add_line('e-middle',(42,24),(44,24));self.relate('connect','e','e-middle')
