"""The rejected VR profile has a square nose and no rounded chin; restore the sloping nose and curved lower face beneath the visor. No written reviewer feedback.
Restored a sloping nose and rounded chin below the visor, preserving the continuous neck profile.
Construction: Shared human reference and Lucide headset original and atomic-debug. Continuous left-facing profile with neck; no detached head gap.
Omissions: Fine facial marks omitted.
Keyshape: SQUARE. Balanced overall composition; centerline extremes (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='019edb66-6728-4e28-ae42-b3dcaedeee84'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__vr-headset-profile-solo-019edb66/20260929T121814Z-thuan-mac/reference/vr headset 1_019edb66-6728-4e28-ae42-b3dcaedeee84.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='vr-headset-profile-solo-019edb66'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('vr', 'headset', 'profile', 'solo', '019edb66')

    def path(self,n,start,ops,closed=False):
        here=start; members=[]
        for i,(kind,end,*args) in enumerate(ops):
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,here,end)
            elif kind=='A': self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
            members.append(m); here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def build(self):

        self.path('head',(18,14),[('A',(28,6),10,8,True),('A',(42,20),14,14,True),('L',(42,26)),('A',(32,36),10,10,True),('L',(32,42))])
        self.path('visor',(10,14),[('L',(18,14)),('L',(22,14)),('A',(26,18),4,4,True),('L',(26,20)),('L',(26,22)),('A',(22,26),4,4,True),('L',(14,26)),('L',(10,26)),('A',(6,22),4,4,True),('L',(6,18)),('A',(10,14),4,4,True)],True)
        self.add_line('strap',(26,20),(42,20));self.relate('connect','strap','head');self.relate('connect','strap','visor');self.relate('connect','head','visor')
        self.path('face',(14,26),[('L',(11,34)),('L',(18,34)),('L',(18,36)),('A',(24,42),6,6,False)]);self.relate('connect','face','visor')
