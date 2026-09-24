"""saving money flower: fresh spacing repair.
Plan: Central circular coin above stem, symmetric sprigs attach at shared base. Dollar uses S with actual endpoint ticks.
Keyshape VRECT_L: extrema derived from the profile's standard envelope.
Omissions: Leaf outlines reduced to open sprigs; coin enlarged to protect currency readability.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='776da6f9-d7d4-597a-a158-44ea69d4fbb8'
SOURCE_PATH='pictographic-primitives/finance/saving money flower_776da6f9-d7d4-597a-a158-44ea69d4fbb8.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='saving-money-flower'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('saving', 'money', 'flower')

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
    def cross(self,n,x,y,r):
        for i,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):
            self.add_line(f'{n}-{i}',(x,y),(x+dx,y+dy))
        for i in range(4):
            for j in range(i): self.relate('connect',f'{n}-{i}',f'{n}-{j}')

    def build(self):
        self.path('coin',(24,4),[('A',(38,18),14),('A',(24,32),14),('A',(10,18),14),('A',(24,4),14)],True)
        self.path('dollar',(27,14),[('L',(24,14)),('A',(24,18),2,False),('A',(24,22),2),('L',(21,22))])
        self.add_line('tick-top',(24,12),(24,14));self.relate('connect','dollar','tick-top')
        self.add_line('tick-bottom',(24,22),(24,24));self.relate('connect','dollar','tick-bottom')
        self.add_line('stem',(24,32),(24,44));self.relate('connect','coin','stem')
        for side in (-1,1):
            self.add_polyline(f'leaf-{side}',(24+side*16,36),(24+side*8,44),(24,44))
            self.relate('connect',f'leaf-{side}','stem')
        self.relate('connect','leaf--1','leaf-1')
