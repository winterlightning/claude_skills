"""IV Infusion Bag.
Plan: Centerlines (10,4)-(38,44); broad bag with raised tab, one level mark and curved tube; omit tiny outlet sleeve.
References: supplied original source; no useful direct Lucide IV match; source bag silhouette.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eca26898-eb1d-5081-bbd6-4ab3ac3ba563'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/transfusion bag_eca26898-eb1d-5081-bbd6-4ab3ac3ba563.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'iv-infusion-bag-eca26898'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('iv-infusion-bag',)
    keywords = ('iv', 'infusion', 'bag')

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
        stroke("bag",(20,10),[((20,4),),((28,4),),((28,10),),((30,10),),
            ((34,14),4,4,True),((34,26),),((30,30),4,4,True),((24,30),),
            ((14,30),),((10,26),4,4,True),((10,18),),((10,14),),
            ((14,10),4,4,True),((20,10),)],True)
        stroke("tube",(24,30),[((24,36),),((32,44),8,8,False),((38,38),6,6,False)])
        self.relate("connect","bag","tube")
        self.add_line("tick-18",(10,18),(18,18));self.relate("connect","bag","tick-18")

