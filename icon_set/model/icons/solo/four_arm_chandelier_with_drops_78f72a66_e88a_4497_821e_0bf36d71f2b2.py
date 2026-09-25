"""Four-arm chandelier with paired tiered lights. Mirror shared curves about x=24. Reference supplies two tiers; no useful Lucide match. Reduce three hanging drops to one central drop and omit the ceiling cup."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '78f72a66-e88a-4497-821e-0bf36d71f2b2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/ceiling ball chandelier retro_78f72a66-e88a-4497-821e-0bf36d71f2b2.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'four-arm-chandelier-with-drops'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ['Four Arm Chandelier with Drops']
    keywords = ['chandelier', 'lights', 'drops', 'ceiling', 'decorative', 'fixture', 'arms']
    def build(self):
        self.add_polyline("stem",(24,8),(24,16),(24,28))
        for side in (-1,1):
            for tier,dx,cy in [("inner",12,10),("outer",18,28)]:
                x=24+side*dx;name=f"{tier}{side}"
                nodes = [(x-2,cy),(x,cy-2),(x+2,cy),(x,cy+2),(x-2,cy)]
                members = []
                for j,(a,b) in enumerate(zip(nodes,nodes[1:])):
                    member = f"{name}-{j}"
                    self.add_arc(member,a,b,radius_x=2)
                    members.append(member)
                self.add_contour(name,*members,closed=True)
            self.add_bezier(f"innerarm{side}",(24+side*12,12),((24+side*12,24),(24+side*4,24),(24,16)))
            self.add_bezier(f"outerarm{side}",(24+side*18,30),((24+side*18,38),(24+side*8,38),(24,28)))
            self.relate("connect",f"inner{side}",f"innerarm{side}")
            self.relate("connect",f"outer{side}",f"outerarm{side}")
            self.relate("connect","stem",f"innerarm{side}")
            self.relate("connect","stem",f"outerarm{side}")
        self.relate("connect","innerarm-1","innerarm1")
        self.relate("connect","outerarm-1","outerarm1")
        self.add_dot("drop",(24,40))
