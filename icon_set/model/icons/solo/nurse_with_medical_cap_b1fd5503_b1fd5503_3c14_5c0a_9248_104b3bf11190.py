"""Nurse with Medical Cap.
Plan: (8,4)-(40,44). Nurse portrait with broad medical cap, round jaw, side hair and detached shoulders. Jaw bottom32 to shoulder40 gives exactly8 centerline /4 ink gap. Fringe and neckline are omitted for clarity.
References: supplied original source; human_ref/user.svg: round jaw and detached broad shoulders; Lucide hard-hat: cap silhouette.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1fd5503-3c14-5c0a-9248-104b3bf11190'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__nurse-with-medical-cap-b1fd5503/20260927T133723Z-thuan-mac-1/reference/nurse with cap cloth_b1fd5503-3c14-5c0a-9248-104b3bf11190.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'nurse-with-medical-cap-b1fd5503-solo'
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
        stroke("face",(16,20),[((16,24),),((24,32),8,8,False),((32,24),8,8,False),((32,20),)])
        self.relate("connect","cap","face")
        # Long hair frames the narrower face, matching the reference silhouette.
        self.add_line("hair-left",(8,20),(8,33))
        self.add_line("hair-right",(40,20),(40,33))
        self.relate("connect","cap","hair-left")
        self.relate("connect","cap","hair-right")
        self.add_polyline("cross-h",(23,15),(24,15),(25,15))
        self.add_polyline("cross-v",(24,13),(24,15),(24,17));self.relate("connect","cross-h","cross-v")
        stroke("shoulders",(8,44),[((16,40),8,4,True),((32,40),),((40,44),8,4,True)])
