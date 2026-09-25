"""Decision Flowchart.
Plan: Two equal process boxes repeat vertically; connectors attach to separate diamond vertices. Ink (2,6)-(46,42).
Reference construction: workflow.
Reduction: Use compact rectangular process boxes and a short exit bend.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '508c3764-36f1-4a78-b476-81ce4a08ec31'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/workflow gantt chart_508c3764-36f1-4a78-b476-81ce4a08ec31.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'decision-flowchart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('decision', 'flowchart')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for j,y in enumerate((8,26)):
         self.add_polyline(f'process-{j}',(4,y),(16,y),(16,y+5),(16,y+10),(4,y+10),closed=True)
        self.add_polyline('decision',(34,18),(44,28),(34,38),(24,28),closed=True)
        self.add_polyline('top-link',(16,13),(34,13),(34,18))
        self.add_line('lower-link',(16,31),(24,28))
        self.relate('connect','top-link','process-0');self.relate('connect','top-link','decision')
        self.relate('connect','lower-link','process-1');self.relate('connect','lower-link','decision')
        self.add_polyline('exit',(34,38),(34,40),(44,40));self.relate('connect','exit','decision')
