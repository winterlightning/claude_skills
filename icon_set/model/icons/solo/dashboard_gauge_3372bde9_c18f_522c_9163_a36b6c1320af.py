"""Dashboard Gauge.
Plan: A domed radius20 gauge closes on a flat lower edge; needle and one cardinal tick occupy a clear interior. Ink (2,6)-(46,42).
Reference construction: gauge.
Reduction: Keep only the top tick and reduce the hub to a compact circle, preserving room for the diagonal needle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3372bde9-c18f-522c-9163-a36b6c1320af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/gauge dashboard_3372bde9-c18f-522c-9163-a36b6c1320af.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'dashboard-gauge'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('dashboard', 'gauge')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_arc('left-dome',(4,28),(24,8),radius_x=20)
        self.add_arc('right-dome',(24,8),(44,28),radius_x=20)
        self.add_bezier('right-base',(44,28),((44,32),(43,36),(40,40)))
        self.add_line('bottom',(40,40),(8,40))
        self.add_bezier('left-base',(8,40),((5,36),(4,32),(4,28)))
        self.add_contour('dial','left-dome','right-dome','right-base','bottom','left-base',closed=True)
        self.add_line('tick',(24,8),(24,12));self.relate('connect','tick','dial')
        circle('hub',24,29,2)
        self.add_line('needle',(24,27),(31,20));self.relate('connect','needle','hub')
