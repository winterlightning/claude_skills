"""Asymmetric cathedral with left spire and cross, central pitched nave and right aisle. Tower and nave use broad clean compartments; bounds6,6 to42,42.
Construction reference: Lucide church: sparse architecture and cross joins.
Omissions: Tiny window marks removed; doorway remains a single stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '07f608bf-07ea-53df-b369-c2c46c926459'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cologne-cathedral/20260924T092136Z-thuan-mac/reference/cologne cathedral_07f608bf-07ea-53df-b369-c2c46c926459.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'cologne-cathedral-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/other'
    aliases = ()
    keywords = ('cologne', 'cathedral')
    def build(self):
        self.add_polyline('outline',(6,42),(6,24),(12,14),(18,24),(18,29),(28,21),(36,29),(36,33),(42,36),(42,42),(28,42),(18,42),(6,42))
        self.add_polyline('cross',(12,6),(12,10),(12,14));self.relate('connect','cross','outline')
        self.add_polyline('crossbar',(8,10),(12,10),(16,10));self.relate('connect','crossbar','cross')
        self.add_polyline('tower',(6,24),(18,24),(18,42));self.relate('connect','tower','outline')
        self.add_line('door',(28,33),(28,42));self.relate('connect','door','outline')

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
