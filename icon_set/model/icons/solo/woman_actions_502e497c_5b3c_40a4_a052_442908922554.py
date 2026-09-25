"""Woman bust with a radius-7 circular jaw, smoothly joined center-parted hair, and curved shoulders. Shared human_ref/user.svg informs circular anatomy. Bust contact has zero ink gap: jaw bottom 29 and shoulder top 33 are exactly four centerline units apart.
Omissions: Hairline is reduced to one symmetric part; facial details omitted.
Construction references: ['user-round'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='502e497c-5b3c-40a4-a052-442908922554'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__woman-bust/20260924T172356Z-thuan-mac/reference/woman actions_502e497c-5b3c-40a4-a052-442908922554.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='woman-bust-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "users"
    categories = ("users", "primitives")
    aliases=()
    keywords=('woman', 'actions')
    human_construction="bust"

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
        self.path('hair',(8,28),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,28))])
        self.path('face',(17,20),[('C',(24,13),(17,17),(21,16)),('C',(31,20),(27,16),(31,17)),('L',(31,22)),('A',(17,22),7,7,True),('L',(17,20))],True)
        self.path('shoulders',(8,44),[('A',(24,33),16,11,True),('A',(40,44),16,11,True)])
        self.relate('connect','face','shoulders')
