"""A tall rounded rectangular level indicator contains three horizontal bars in its lower half. The bars are equal in length and evenly spaced, leaving the upper section blank."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb43ab14-fd5f-484f-84c3-10dcc97db754'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/rectangle uv medium 1_cb43ab14-fd5f-484f-84c3-10dcc97db754.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'vertical-level-indicator-batch-032'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ('vertical-level-indicator',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: Three equal bars anchored low; shared 8-unit pitch; extrema (10,4)-(38,44).

        def rect(name, x0, y0, x1, y1, r=4):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            ids=[]
            for i,p in enumerate(pts):
                q=pts[(i+1)%8]; eid=f"{name}-{i}"; ids.append(eid)
                if i%2: self.add_arc(eid,p,q,radius_x=r)
                else: self.add_line(eid,p,q)
            self.add_contour(name,*ids,closed=True)

        rect('body',10,4,38,44)
        for i in range(3):
            y=19+i*8
            self.add_line(f'level-{i}',(19,y),(29,y))
