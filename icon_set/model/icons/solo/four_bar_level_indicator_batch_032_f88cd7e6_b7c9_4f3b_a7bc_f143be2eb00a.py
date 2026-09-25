"""A tall rounded rectangular indicator contains four short horizontal level marks. The marks are equally spaced down the center, with matching lengths and broad margins on both sides."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f88cd7e6-b7c9-4f3b-a7bc-f143be2eb00a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/rectangle uv high 1_f88cd7e6-b7c9-4f3b-a7bc-f143be2eb00a.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'four-bar-level-indicator-batch-032'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ('four-bar-level-indicator',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: Rounded enclosure plus four equal bars with 8-unit pitch; extrema (10,4)-(38,44).

        def rect(name, x0, y0, x1, y1, r=4):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            ids=[]
            for i,p in enumerate(pts):
                q=pts[(i+1)%8]; eid=f"{name}-{i}"; ids.append(eid)
                if i%2: self.add_arc(eid,p,q,radius_x=r)
                else: self.add_line(eid,p,q)
            self.add_contour(name,*ids,closed=True)

        rect('body',10,4,38,44)
        self.contours.clear()
        self.add_contour('body-right','body-1','body-2','body-3')
        self.add_contour('body-left','body-5','body-6','body-7')
        for side in ('body-right','body-left'):
            for edge in ('body-0','body-4'): self.relate('connect',side,edge)
        for i in range(4):
            y=12+i*8
            self.add_line(f'level-{i}',(19,y),(29,y))
