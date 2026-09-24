"""toilet use right: fresh parallel-spacing repair.
Plan: Forward-leaning seated figure, sloped lower leg, bowl and check remain visible.
Keyshape SQUARE: Square envelope separates the head, check and toilet.
Omissions: Narrow tank outline reduced to its back edge; seat and thigh share a single stroke. Folded arm omitted because it makes a narrow closed pocket.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='2dff611f-5296-466d-ac68-3fd4303496ea'
SOURCE_PATH='pictographic-primitives/_uncategorized_38/toilet use right_2dff611f-5296-466d-ac68-3fd4303496ea.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='toilet-use-right'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('toilet', 'use', 'right')

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

    def frame(self):
        self.path('frame',(10,6),[('L',(38,6)),('A',(42,10),4),('L',(42,38)),('A',(38,42),4),('L',(10,42)),('A',(6,38),4),('L',(6,10)),('A',(10,6),4)],True)

    def build(self):
        self.circle('head',20,11,5)
        self.add_line('torso',(15,23),(14,34))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_polyline('leg',(14,34),(26,34),(30,34),(36,42))
        self.add_polyline('tank',(6,24),(6,34),(6,42))
        self.add_line('seat',(6,34),(14,34))
        self.add_bezier('bowl',(26,34),((26,39),(22,39),(22,42)))
        for a,b in [('torso','leg'),('tank','seat'),('seat','torso'),('seat','leg'),('leg','bowl')]:self.relate('connect',a,b)
        self.add_polyline('check',(33,12),(37,16),(42,6))
