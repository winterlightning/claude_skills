"""Pregnant Person in Profile.
Plan: (8,4)-(40,44). Round head above curved back and prominent right-facing belly; bent arm rests across belly. Head bottom16 to shoulder24 gives exact8 gap.
References: supplied original source; human_ref/user.svg: circular head and broad curved body; source belly silhouette.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0eadf5ec-fd86-5978-bdcb-233f7e9d7630'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty pregnancy_0eadf5ec-fd86-5978-bdcb-233f7e9d7630.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pregnant-person-in-profile-0eadf5ec'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('pregnant-person-in-profile',)
    keywords = ('pregnant', 'person', 'in', 'profile')

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
        circle("head",20,10,6)
        stroke("back",(20,24),[((8,36),12,12,False),((8,44),)])
        stroke("belly",(20,24),[((40,34),20,10,True),((24,44),16,10,True)])
        self.relate("connect","back","belly")
        self.add_polyline("arm",(20,24),(20,34),(40,34));self.relate("connect","arm","belly");self.relate("connect","arm","back")

