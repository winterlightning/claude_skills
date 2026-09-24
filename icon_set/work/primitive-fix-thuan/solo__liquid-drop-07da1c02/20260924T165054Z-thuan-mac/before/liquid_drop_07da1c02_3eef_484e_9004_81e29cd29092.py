"""Liquid Drop.
Plan: (8,4)-(40,44). Pointed drop tip above circular lower bowl. One short inner reflection.
References: supplied original source; Lucide droplet: pointed apex and coherent rounded bowl.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07da1c02-3eef-484e-9004-81e29cd29092'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/blood drop_07da1c02-3eef-484e-9004-81e29cd29092.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'liquid-drop-07da1c02'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('liquid-drop',)
    keywords = ('liquid', 'drop')

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
        stroke("drop",(24,4),[((37,23),),((40,28),16,16,True),((24,44),16,16,True),((8,28),16,16,True),((11,23),16,16,True),((24,4),)],True)
        self.add_line("reflection",(29,32),(26,35))

