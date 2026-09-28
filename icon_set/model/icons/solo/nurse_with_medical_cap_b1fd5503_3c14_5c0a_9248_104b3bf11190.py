"""Nurse with Medical Cap.
Plan: (8,4)-(40,44). Nurse portrait with broad medical cap, round jaw and detached shoulders. Jaw bottom34 to shoulder42 gives exactly8 centerline /4 ink gap. Hair, fringe, and neckline omitted.
References: supplied original source; human_ref/user.svg: round jaw and detached broad shoulders; Lucide hard-hat: cap silhouette.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1fd5503-3c14-5c0a-9248-104b3bf11190'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/nurse with cap cloth_b1fd5503-3c14-5c0a-9248-104b3bf11190.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'nurse-with-medical-cap-b1fd5503'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('nurse-with-medical-cap',)
    keywords = ('nurse', 'with', 'medical', 'cap')

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
        stroke("cap",(14,20),[((8,20),),((8,8),),((12,4),4,4,True),((36,4),),((40,8),4,4,True),((40,20),),((34,20),)])
        stroke("face",(14,20),[((14,24),),((24,34),10,10,False),((34,24),10,10,False),((34,20),)])
        self.relate("connect","cap","face")
        self.add_polyline("cross-h",(21,16),(24,16),(27,16))
        self.add_polyline("cross-v",(24,13),(24,16),(24,19));self.relate("connect","cross-h","cross-v")
        stroke("shoulders",(8,44),[((16,42),8,2,True),((32,42),),((40,44),8,2,True)])

