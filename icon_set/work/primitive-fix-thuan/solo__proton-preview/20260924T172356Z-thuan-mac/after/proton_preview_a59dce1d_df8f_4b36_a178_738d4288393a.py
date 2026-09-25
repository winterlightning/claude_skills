"""Molecule with three round outer nodes and a round central node, joined by three straight bonds.
Omissions: None
Construction references: ['network'].
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a59dce1d-df8f-4b36-a178-738d4288393a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__proton-preview/20260924T172356Z-thuan-mac/reference/proton preview_a59dce1d-df8f-4b36-a178-738d4288393a.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='proton-preview'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('proton', 'preview')

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
        for n,x,y,r in [('top',13,9,5),('bottom',13,39,5),('center',24,24,5),('right',37,14,3)]:self.circle(n,x,y,r)
        for n,a,b,left,right in [('top-link',(16,13),(20,21),'top','center'),('bottom-link',(16,35),(24,29),'bottom','center'),('right-link',(28,21),(34,14),'center','right')]:
            self.add_line(n,a,b);self.relate('connect',n,left);self.relate('connect',n,right)
