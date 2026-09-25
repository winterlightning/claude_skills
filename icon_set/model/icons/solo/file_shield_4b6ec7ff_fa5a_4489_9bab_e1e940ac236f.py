"""Mirrored shield shoulders and flowing sides, with a crisp check mark.
Omissions: None
Construction references: ['shield-check'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='4b6ec7ff-fa5a-4489-9bab-e1e940ac236f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__file-shield/20260924T171046Z-thuan-mac/reference/file shield_4b6ec7ff-fa5a-4489-9bab-e1e940ac236f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='file-shield'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('file', 'shield')

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
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,x,y,w,h,r):
        self.path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)

    def build(self):
        self.path('shield',(24,4),[('C',(40,10),(30,8),(34,10)),('L',(40,19)),('C',(24,44),(40,30),(33,38)),('C',(8,19),(15,38),(8,30)),('L',(8,10)),('C',(24,4),(14,10),(18,8))],True)
        self.add_polyline('check',(18,24),(23,29),(31,19))
