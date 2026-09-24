"""solar charging car 3: fresh parallel-spacing repair.
Plan: Sun, two-row solar panel and tall lightning charger remain in the reference arrangement.
Keyshape SQUARE: Square envelope balances the panel with the tall charger.
Omissions: Solar grid reduced to two rows; trapezoid regularized to rectangle; four sun rays joined to its rim.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='3f94101a-2b9f-45aa-9df1-583e0d6d7077'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/solar charging car 3_3f94101a-2b9f-45aa-9df1-583e0d6d7077.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='solar-charging-car-3'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('solar', 'charging', 'car', '3')

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

    def page(self):
        self.path('page',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,40)),('A',(36,44),4),('L',(12,44)),('A',(8,40),4),('L',(8,8)),('A',(12,4),4)],True)
    def phone(self,band=True):
        self.path('phone',(12,4),[('L',(36,4)),('A',(40,8),4),('L',(40,36)),('L',(40,40)),('A',(36,44),4),('L',(12,44)),('A',(8,40),4),('L',(8,36)),('L',(8,8)),('A',(12,4),4)],True)
        if band:
            self.add_line('separator',(8,36),(40,36));self.relate('connect','phone','separator')
    def house(self):
        self.path('house',(6,18),[('L',(24,6)),('L',(42,18)),('L',(42,38)),('A',(38,42),4),('L',(10,42)),('A',(6,38),4),('L',(6,18))],True)

    def build(self):
        self.add_polyline('charger',(28,6),(42,6),(42,24),(42,42),(28,42),(28,24),closed=True)
        self.add_polyline('bolt',(36,14),(28,24),(42,24),(34,34));self.relate('connect','charger','bolt')
        self.path('sun',(12,10),[('A',(15,13),3),('A',(12,16),3),('A',(9,13),3),('A',(12,10),3)],True)
        for i,(a,b) in enumerate([((12,10),(12,6)),((15,13),(18,13)),((12,16),(12,18)),((9,13),(6,13))]):
            self.add_line(f'ray-{i}',a,b);self.relate('connect',f'ray-{i}','sun')
        self.add_polyline('panel',(6,26),(20,26),(20,34),(20,42),(6,42),(6,34),closed=True)
        self.add_line('row',(6,34),(20,34));self.relate('connect','panel','row')
