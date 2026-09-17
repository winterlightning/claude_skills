"""Pair of Test Tubes.
Plan: (6,6)-(42,42). Two equal upright tubes with open flared rims, rounded bottoms and unequal liquid heights. Shared tube construction.
References: supplied original source; Lucide test-tubes: repeated open tube, broad rim and rounded bottom.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2869b113-eb2a-5dcb-a493-ca714b5657f9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/test tubes_2869b113-eb2a-5dcb-a493-ca714b5657f9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pair-of-test-tubes-2869b113'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('pair-of-test-tubes',)
    keywords = ('pair', 'of', 'test', 'tubes')

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
        for j,(x,level) in enumerate(((13,24),(35,30))):
            stroke(f"tube-{j}",(x-5,6),[((x-5,level),),((x-5,37),),((x+5,37),5,5,False),((x+5,level),),((x+5,6),)])
            self.add_polyline(f"rim-{j}",(x-7,6),(x-5,6),(x+5,6),(x+7,6));self.relate("connect",f"rim-{j}",f"tube-{j}")
            self.add_line(f"liquid-{j}",(x-5,level),(x+5,level));self.relate("connect",f"liquid-{j}",f"tube-{j}")

