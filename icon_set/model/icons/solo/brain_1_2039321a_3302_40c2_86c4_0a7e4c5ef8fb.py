"""Top view of a brain, with paired rounded lobes and a subtle central cleft. Mirrored lobe dimensions about x24; centerline extremes6,6 to42,42.
Construction reference: Lucide brain: scalloped anatomical lobes.
Omissions: Removed unsupported winding central divider; source has only outer lobes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2039321a-3302-40c2-86c4-0a7e4c5ef8fb'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain 1_2039321a-3302-40c2-86c4-0a7e4c5ef8fb.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'brain-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('brain', '1')
    def build(self):
        self.path('brain',(24,12),[('A',(18,6),6,6,False),('A',(12,12),6,6,False),('C',(10,17),(9,12),(8,14)),('C',(6,25),(6,18),(6,21)),('C',(10,33),(6,30),(7,32)),('C',(16,42),(7,40),(11,42)),('C',(24,38),(21,42),(22,40)),('C',(32,42),(26,40),(27,42)),('C',(38,33),(37,42),(41,40)),('C',(42,25),(41,32),(42,30)),('C',(38,17),(42,21),(42,18)),('C',(36,12),(40,14),(39,12)),('A',(30,6),6,6,False),('A',(24,12),6,6,False)],True)

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,c in enumerate(commands):
            ident=f'{name}-{i}'
            if c[0]=='L': end=c[1];self.add_line(ident,start,end)
            elif c[0]=='A':
                _,end,rx,ry,sweep=c
                self.add_arc(ident,start,end,radius_x=rx,radius_y=ry,sweep=sweep)
            elif c[0]=='C':
                _,end,c1,c2=c
                self.add_bezier(ident,start,(c1,c2,end))
            members.append(ident);start=end
        self.add_contour(name,*members,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
