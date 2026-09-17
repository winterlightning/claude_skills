"""IV Drip Bag.
Plan: Centerlines (10,4)-(38,44); raised hanger tab, rounded bag, two level ticks, and coherent J tube. Omit separate outlet sleeve.
References: supplied original source; no useful direct Lucide IV match; rounded container and attached tube construction.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a21dc47-55d9-5329-bbb6-6a7568f0645c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/transfusion blood_8a21dc47-55d9-5329-bbb6-6a7568f0645c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'iv-drip-bag-8a21dc47'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('iv-drip-bag',)
    keywords = ('iv', 'drip', 'bag')

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
        stroke("bag",(20,8),[((20,4),),((28,4),),((28,8),),((30,8),),
            ((34,12),4,4,True),((34,28),),((30,32),4,4,True),((24,32),),
            ((14,32),),((10,28),4,4,True),((10,24),),((10,16),),((10,12),),
            ((14,8),4,4,True),((20,8),)],True)
        stroke("tube",(24,32),[((24,36),),((32,44),8,8,False),((38,38),6,6,False)])
        self.relate("connect","bag","tube")
        self.add_line("tick-18",(10,16),(18,16));self.relate("connect","bag","tick-18")
        self.add_line("tick-26",(10,24),(18,24));self.relate("connect","bag","tick-26")

