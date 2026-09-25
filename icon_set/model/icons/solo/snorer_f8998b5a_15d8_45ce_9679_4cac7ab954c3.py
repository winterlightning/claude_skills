"""snorer: fresh parallel-spacing repair.
Plan: Detached head, reclining torso, blanket and one large Z remain readable.
Keyshape SQUARE: Square envelope separates the sleeper from the large Z.
Omissions: Two Zs reduced to one larger Z; pillow crease and redundant outline omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='f8998b5a-15d8-45ce-9679-4cac7ab954c3'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/snorer_f8998b5a-15d8-45ce-9679-4cac7ab954c3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='snorer'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('snorer',)

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
        self.circle('head',14,24,5)
        self.add_bezier('torso',(14,37),((14,40),(20,42),(24,42)))
        self.mark_human_figure('sleeper',head='head',torso='torso',torso_junction='start')
        self.add_polyline('bed',(6,42),(24,42),(42,42),(42,34))
        self.add_bezier('blanket',(24,42),((26,32),(27,30),(32,30)),((38,30),(42,30),(42,34)))
        self.relate('connect','bed','blanket');self.relate('connect','bed','torso');self.relate('connect','torso','blanket')
        self.add_polyline('z',(30,6),(42,6),(30,14),(42,14))
