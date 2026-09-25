"""Symmetric two-arm chandelier. Tall envelope preserves hanging stem and diamond drop. Shared bulb radii and mirrored arms. Reference gives arrangement; no Lucide chandelier match. Omit saucer bars and simplify flame bulbs to circles."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '53a2db53-1b8f-480f-8587-7d742044c811'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/ceiling ball chandelier retro 1_53a2db53-1b8f-480f-8587-7d742044c811.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'two-arm-pendant-chandelier'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ['Two Arm Pendant Chandelier']
    keywords = ['chandelier', 'lighting', 'bulbs', 'pendant', 'ceiling', 'arms', 'fixture']
    def build(self):
        self.add_polyline("ceiling",(16,4),(24,4),(32,4))
        self.add_polyline("stem",(24,4),(24,20),(24,32))
        self.relate("connect","ceiling","stem")
        self.add_polyline("pendant",(24,32),(30,38),(24,44),(18,38),closed=True)
        self.relate("connect","stem","pendant")
        for side in (-1,1):
            x=24+side*12;name=f"bulb{side}"
            self.add_arc(name+"a",(x,10),(x,18),radius_x=4)
            self.add_arc(name+"b",(x,18),(x,10),radius_x=4)
            self.add_contour(name,name+"a",name+"b",closed=True)
            self.add_bezier(f"arm{side}",(x,18),((x,24),(24+side*8,24),(24,20)))
            self.relate("connect",name,f"arm{side}")
            self.relate("connect","stem",f"arm{side}")
        self.relate("connect","arm-1","arm1")
