"""Nose Profile.
Plan: (10,4)-(38,44). Asymmetric nose bridge, rounded tip, nostril wing, and upper-lip turn.
References: supplied original source; no useful direct Lucide match; supplied profile anatomy.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98d13fff-c5f0-5dc8-9b5e-33923d83eb01'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty nose_98d13fff-c5f0-5dc8-9b5e-33923d83eb01.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'nose-profile-98d13fff'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('nose-profile',)
    keywords = ('nose', 'profile')

    def build(self):

        def stroke(name, start, segments, closed=False):
            members=[]
            for j,s in enumerate(segments):
                member=f"{name}-{j}"
                if len(s)==1: self.add_line(member,start,s[0])
                else: self.add_arc(member,start,s[0],radius_x=s[1],radius_y=s[2],sweep=s[3],large_arc=s[4] if len(s)>4 else False)
                members.append(member);start=s[0]
            self.add_contour(name,*members,closed=closed)
        def circle(name,cx,cy,r):
            stroke(name,(cx-r,cy),[((cx+r,cy),r,r,True),((cx-r,cy),r,r,True)],True)
        stroke("profile",(20,4),[((16,18),),((10,28),),((18,36),8,8,False),((24,36),),((24,40),),((28,44),4,4,False)])
        stroke("wing",(28,24),[((38,32),10,8,True),((34,36),4,4,True)])

