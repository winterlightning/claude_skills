"""Column Summary Diagram.
Plan: Three left cells share divider endpoints; conversion arrow occupies the central eight-unit band. Ink (2,6)-(46,42).
Reference construction: network; shuffle.
Reduction: Keep three source cells. Reduce the two summary text marks to one short vertical mark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b80d2397-d3ce-4283-b474-0314b0feda45'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/column summary_b80d2397-d3ce-4283-b474-0314b0feda45.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'column-summary-diagram'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('column', 'summary', 'diagram')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('column',(4,8),(12,8),(12,18),(12,30),(12,40),(4,40),(4,30),(4,18),closed=True)
        for y in (18,30):
         self.add_line(f'divider-{y}',(4,y),(12,y));self.relate('connect',f'divider-{y}','column')
        self.add_line('shaft',(20,24),(28,24))
        self.add_polyline('head',(22,18),(28,24),(22,30))
        self.relate('connect','shaft','head')
        self.add_polyline('summary',(44,8),(36,8),(36,18),(36,40),(44,40))
        self.add_line('summary-divider',(36,18),(44,18))
        self.relate('connect','summary','summary-divider')
        self.add_line('summary-mark',(44,29),(44,30))
