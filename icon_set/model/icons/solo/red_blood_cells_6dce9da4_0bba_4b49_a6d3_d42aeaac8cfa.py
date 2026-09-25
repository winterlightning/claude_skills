"""Red Blood Cells.
Plan: (4,8)-(44,40). Two broad round blood cells arranged diagonally. Tiny open depression curves reduced to centered solid marks; round contours keep the centers clear.
References: supplied original source; Lucide bean: simple organic cell contours; source diagonal pair and depressed centers.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6dce9da4-0bba-4b49-a6d3-d42aeaac8cfa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pregnancy eggs_6dce9da4-0bba-4b49-a6d3-d42aeaac8cfa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'red-blood-cells-6dce9da4'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('red-blood-cells',)
    keywords = ('red', 'blood', 'cells')

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
        for j,(x,y) in enumerate(((13,17),(35,31))):
            circle(f"cell-{j}",x,y,9)
            self.add_dot(f"depression-{j}",(x,y))

