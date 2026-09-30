"""The rejected drawing has an undersized cap and an unbalanced face/veil relationship. No written reviewer feedback.
Enlarged the domed cap and rebalanced its spacing above the circular face and veil.
Construction: Shared human reference for circular jaw; supplied domed cap and veil. Mirror axis x=24.
Omissions: No facial microdetails added; source cap, face and veil retained.
Keyshape: VRECT_L. Vertical composition; centerline extremes (8,4)-(40,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='35c53f50-e535-49f3-ac90-8d416600029e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__veiled-head-beneath-a-domed-cap/20260929T121814Z-thuan-mac/reference/avatar islamic women niqab 1_35c53f50-e535-49f3-ac90-8d416600029e.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='veiled-head-beneath-a-domed-cap'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('veiled', 'head', 'beneath', 'a', 'domed', 'cap')

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

        self.path('cap',(10,18),[('A',(24,4),14,14,True),('A',(38,18),14,14,True),('L',(10,18))],True)
        self.path('face',(14,27),[('A',(34,27),10,10,False)])
        self.add_line('veil-left',(14,27),(8,44));self.add_line('veil-right',(34,27),(40,44))
        self.relate('connect','face','veil-left');self.relate('connect','face','veil-right')
