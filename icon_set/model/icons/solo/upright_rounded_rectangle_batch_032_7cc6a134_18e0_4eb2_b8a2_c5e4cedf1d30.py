"""A plain upright rectangle has smoothly rounded corners and straight side edges. Its outline encloses an entirely empty interior, with no borders, marks, handles, or other attached parts."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7cc6a134-18e0-4eb2-b8a2-c5e4cedf1d30'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/vertical rectangle_7cc6a134-18e0-4eb2-b8a2-c5e4cedf1d30.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'upright-rounded-rectangle-batch-032'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ('upright-rounded-rectangle',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: One empty rounded rectangle with repeated radius; extrema (10,4)-(38,44).

        def rect(name, x0, y0, x1, y1, r=4):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            ids=[]
            for i,p in enumerate(pts):
                q=pts[(i+1)%8]; eid=f"{name}-{i}"; ids.append(eid)
                if i%2: self.add_arc(eid,p,q,radius_x=r)
                else: self.add_line(eid,p,q)
            self.add_contour(name,*ids,closed=True)

        rect('outline',10,4,38,44)
