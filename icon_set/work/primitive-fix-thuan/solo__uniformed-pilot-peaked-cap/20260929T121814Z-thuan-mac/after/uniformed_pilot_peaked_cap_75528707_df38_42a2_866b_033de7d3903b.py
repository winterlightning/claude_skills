"""The rejected pilot cap is a sharp pentagon, unlike the flatter rounded crown in the reference. No written reviewer feedback.
Replaced the pointed pentagonal cap with a flatter rounded crown; retained a circular jaw and uniform seam.
Construction: Shared human_ref/user.svg circular jaw and shoulders. Jaw bottom y=26; shoulder top y=30; 4-unit centerline separation gives zero visible ink gap, declared with an actual contact.
Omissions: Collar lapels, cap emblem and sleeve divisions omitted; uniform seam retained.
Keyshape: VRECT_L. Vertical composition; centerline extremes (8,4)-(40,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='75528707-df38-42a2-866b-033de7d3903b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__uniformed-pilot-peaked-cap/20260929T121814Z-thuan-mac/reference/airman_75528707-df38-42a2-866b-033de7d3903b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='uniformed-pilot-peaked-cap'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('uniformed', 'pilot', 'peaked', 'cap')
    human_construction='bust'

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

        self.path('cap',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(34,16)),('L',(14,16)),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.path('face',(34,16),[('A',(14,16),10,10,True)]);self.relate('connect','face','cap')
        self.path('body',(8,44),[('A',(24,30),16,14,True),('A',(40,44),16,14,True)]);self.relate('connect','face','body')
        self.add_line('uniform-seam',(24,30),(24,44));self.relate('connect','uniform-seam','body')
