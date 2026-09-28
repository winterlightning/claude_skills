"""An upright electrical outlet plate has rounded corners and two pairs of narrow vertical socket slots. The pairs are stacked with a large gap between them on the plain front surface."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b1cd37d-5708-4e57-8dac-f3311354f4bc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/plug board_4b1cd37d-5708-4e57-8dac-f3311354f4bc.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'vertical-electrical-power-outlet-batch-032'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ('vertical-electrical-power-outlet',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: Outlet plate and two mirrored pairs of slots; extrema (8,4)-(40,44).

        def rect(name, x0, y0, x1, y1, r=4):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            ids=[]
            for i,p in enumerate(pts):
                q=pts[(i+1)%8]; eid=f"{name}-{i}"; ids.append(eid)
                if i%2: self.add_arc(eid,p,q,radius_x=r)
                else: self.add_line(eid,p,q)
            self.add_contour(name,*ids,closed=True)

        rect('plate',8,4,40,44)
        for i,y in enumerate((14,30)):
            for x in (18,30): self.add_line(f'slot-{i}-{x}',(x,y),(x,y+4))
