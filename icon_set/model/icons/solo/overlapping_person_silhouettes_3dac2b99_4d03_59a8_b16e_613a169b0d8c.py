"""Overlapping Person Silhouettes.
Plan: (6,6)-(42,42). Mirrored continuous head-neck silhouettes share a central overlap lens and downward line. This source has continuous necks, not detached heads.
References: supplied original source; human_ref/user.svg: smooth head and shoulder vocabulary; source overlapping profiles.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3dac2b99-4d03-59a8-b16e-613a169b0d8c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/personality disorder symptoms_3dac2b99-4d03-59a8-b16e-613a169b0d8c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'overlapping-person-silhouettes-3dac2b99'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('overlapping-person-silhouettes',)
    keywords = ('overlapping', 'person', 'silhouettes')

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
        stroke("left",(24,8),[((10,22),10,10,False),((14,30),),((6,38),8,8,False),((6,42),)])
        stroke("right",(24,8),[((38,22),10,10,True),((34,30),),((42,38),8,8,True),((42,42),)])
        stroke("lens",(24,8),[((24,24),10,10,True),((24,8),10,10,True)],True)
        self.relate("connect","left","right");self.relate("connect","left","lens");self.relate("connect","right","lens")
        self.add_line("center",(24,24),(24,42));self.relate("connect","lens","center")

