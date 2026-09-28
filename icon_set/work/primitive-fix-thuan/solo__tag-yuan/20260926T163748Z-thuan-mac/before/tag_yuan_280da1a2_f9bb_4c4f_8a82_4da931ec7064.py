"""tag yuan: fresh parallel-spacing repair.
Plan: Full yuan mark retains two bars; the clipped tag corner remains visible.
Keyshape SQUARE: Square envelope widens the tag body around the complete currency symbol.
Omissions: Small punched hole omitted to make room for both currency bars.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='280da1a2-f9bb-4c4f-8a82-4da931ec7064'
SOURCE_PATH='pictographic-primitives/_uncategorized_37/tag yuan_280da1a2-f9bb-4c4f-8a82-4da931ec7064.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tag-yuan'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('tag', 'yuan')

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
        self.path('tag',(6,16),[('L',(16,6)),('L',(42,6)),('L',(42,38)),('A',(38,42),4),('L',(10,42)),('A',(6,38),4),('L',(6,16))],True)
        self.add_polyline('fork',(19,16),(24,25),(29,16))
        self.add_polyline('stem',(24,25),(24,33))
        for i,y in enumerate([25,33]):
            self.add_polyline(f'bar-{i}',(18,y),(24,y),(30,y))
        self.relate('connect','fork','stem');self.relate('connect','fork','bar-0');self.relate('connect','stem','bar-0');self.relate('connect','stem','bar-1')
