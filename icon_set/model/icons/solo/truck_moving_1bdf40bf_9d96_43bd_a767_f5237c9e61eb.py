"""Truck moving.
Symbol plan: House rides on the truck chassis; wheel pair radius3 shares y39; house doorway width8. Extremes6,6 to42,42.
Omissions: Separate cargo box merged with house body, window omitted.
Construction references: Lucide truck and house: paired circular wheels and simple pitched house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1bdf40bf-9d96-43bd-a767-f5237c9e61eb'
SOURCE_PATH='pictographic-primitives/_uncategorized_38/truck moving_1bdf40bf-9d96-43bd-a767-f5237c9e61eb.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='truck-moving'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('truck', 'moving')

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
        self.add_polyline('house',(6,28),(6,16),(18,6),(30,16),(30,20),(30,28),(22,28),(14,28),closed=True)
        self.add_polyline('door',(14,28),(14,18),(22,18),(22,28));self.relate('connect','door','house')
        self.add_polyline('cab',(30,20),(36,20),(42,28),(42,39),(39,39));self.relate('connect','house','cab')
        for n,x in [('left',12),('right',36)]:self.circle('wheel-'+n,x,39,3)
        self.add_line('axle',(15,39),(33,39))
        self.relate('connect','axle','wheel-left');self.relate('connect','axle','wheel-right');self.relate('connect','cab','wheel-right')
