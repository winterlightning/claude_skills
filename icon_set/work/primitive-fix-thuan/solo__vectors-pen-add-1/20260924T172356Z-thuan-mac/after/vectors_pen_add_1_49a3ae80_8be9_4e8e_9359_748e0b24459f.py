"""Diagonal pen nib with straight symmetric flanks, clean slit and square cap, beside a plus sign.
Omissions: None
Construction references: ['pen-tool'].
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='49a3ae80-8be9-4e8e-9359-748e0b24459f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__vectors-pen-add-1/20260924T172356Z-thuan-mac/reference/vectors pen add 1_49a3ae80-8be9-4e8e-9359-748e0b24459f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='vectors-pen-add-1'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('vectors', 'pen', 'add', '1')

    def path(self, name, start, commands, closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            eid=f'{name}-{i}'; ids.append(eid)
            if c[0]=='L': self.add_line(eid,here,c[1])
            elif c[0]=='A': self.add_arc(eid,here,c[1],radius_x=c[2],radius_y=c[3],sweep=c[4],large_arc=c[5] if len(c)>5 else False)
            elif c[0]=='C': self.add_bezier(eid,here,(c[2],c[3],c[1]))
            here=c[1]
        self.add_contour(name,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,x,y,w,h,r):
        self.path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)

    def build(self):
        self.add_polyline('nib',(6,42),(14,22),(24,16),(32,24),(28,36),closed=True)
        self.add_polyline('cap',(24,16),(34,6),(42,14),(32,24));self.relate('connect','nib','cap')
        self.add_line('slit',(6,42),(20,28));self.relate('connect','slit','nib')
        self.add_polyline('plus-h',(6,10),(10,10),(14,10));self.add_polyline('plus-v',(10,6),(10,10),(10,14));self.relate('connect','plus-h','plus-v')
