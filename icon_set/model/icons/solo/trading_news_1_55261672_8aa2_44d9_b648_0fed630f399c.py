"""trading news 1: fresh parallel-spacing repair.
Plan: Headline and text rule identify a page; the rising chart forms its lower right boundary.
Keyshape SQUARE: Square envelope preserves the newspaper page.
Omissions: Header box reduced to a headline rule; two text rows reduced to one; chart takes over the lower right page boundary.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='55261672-8aa2-44d9-b648-0fed630f399c'
SOURCE_PATH='pictographic-primitives/_uncategorized_38/trading news 1_55261672-8aa2-44d9-b648-0fed630f399c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='trading-news-1'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('trading', 'news', '1')

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
        self.path('page',(22,42),[('L',(10,42)),('A',(6,38),4),('L',(6,10)),('A',(10,6),4),('L',(38,6)),('A',(42,10),4),('L',(42,26))])
        self.add_line('header',(15,15),(33,15))
        self.add_line('text',(15,25),(22,25))
        self.add_polyline('chart',(22,42),(30,34),(34,38),(42,26))
        self.add_polyline('arrowhead',(34,26),(42,26),(42,34))
        self.relate('connect','page','chart');self.relate('connect','page','arrowhead');self.relate('connect','chart','arrowhead')
