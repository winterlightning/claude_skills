"""Gungan head: symmetric raised eye stalks, rounded muzzle, long curved ears and a small smile.
Omissions: Pupils and ear stripes omitted at 48px.
Construction references: no useful direct Lucide match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5d2544d5-2bb4-4a21-948a-315da03b0cf4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__jar-jar-binks/20260924T171046Z-thuan-mac/reference/jar jar binks gungan_5d2544d5-2bb4-4a21-948a-315da03b0cf4.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='jar-jar-binks'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('jar', 'jar', 'binks', 'gungan')

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
        # Shared eye-stalk dimensions mirror about x=24; circularly rounded stalk caps.
        self.path('face',(12,17),[('C',(16,6),(11,10),(12,6)),('C',(20,16),(20,6),(20,11)),('L',(28,16)),('C',(32,6),(28,11),(28,6)),('C',(36,17),(36,6),(37,10)),('C',(24,38),(37,31),(31,38)),('C',(12,17),(17,38),(11,31))],True)
        for name,sgn in [('left',-1),('right',1)]:
            def p(x,y):return (24+sgn*x,y)
            self.path(name,p(12,17),[('C',p(18,42),p(17,26),p(18,35)),('L',p(10,42))])
            self.relate('connect',name,'face')
        self.path('smile',(21,26),[('C',(27,26),(21,29),(27,29))])
