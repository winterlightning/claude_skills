"""Pregnant Person in Water.
Plan: (6,6)-(42,42). Left-facing pregnant profile immersed in a broad water wave. Head bottom14 to shoulder22 gives exact8 gap; second wave and inner arm omitted to preserve belly silhouette.
References: supplied original source; human_ref/user.svg: circular head and curved body; source left-facing belly and water.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4be18d14-ebde-5dbc-99d1-0a84c2b6df94'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/prenatal massage wave_4be18d14-ebde-5dbc-99d1-0a84c2b6df94.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pregnant-person-in-water-4be18d14'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('pregnant-person-in-water',)
    keywords = ('pregnant', 'person', 'in', 'water')

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
        circle("head",28,10,4)
        stroke("front",(28,22),[((24,26),),((20,26),),((10,36),10,10,False),((10,40),)])
        stroke("back",(28,22),[((36,30),8,8,True),((34,40),)])
        self.relate("connect","front","back")
        stroke("water",(6,40),[((10,40),),((22,40),6,2,False),((34,40),6,2,True),((42,40),)])
        self.relate("connect","front","water");self.relate("connect","back","water")

