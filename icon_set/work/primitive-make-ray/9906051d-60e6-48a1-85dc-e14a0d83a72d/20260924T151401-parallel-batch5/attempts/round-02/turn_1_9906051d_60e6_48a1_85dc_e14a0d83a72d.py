"""Turn 1.
Symbol plan: Diamond enclosure; one central route with opposing staggered branch arrows. Extremes6,6 to42,42.
Omissions: Outlined route reduced to single centerline; arrow heads retained.
Construction references: Lucide signpost: stem with opposing branches.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9906051d-60e6-48a1-85dc-e14a0d83a72d'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/turn 1_9906051d-60e6-48a1-85dc-e14a0d83a72d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='turn-1'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('turn', '1')

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
        self.add_polyline('diamond',(24,4),(44,24),(24,44),(4,24),closed=True)
        self.add_polyline('route',(24,17),(24,24),(24,31))
        self.add_polyline('right-turn',(24,20),(28,20),(26,18));self.relate('connect','route','right-turn')
        self.add_polyline('left-turn',(24,28),(20,28),(22,30));self.relate('connect','route','left-turn')
