"""Christmas Sleigh.

Plan: High-backed sleigh with recessed seat, raised lip, two supports and curled runner. Reduce decorative curls; runner remains tangent-continuous. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '002679b5-86e3-4c02-8bd6-d8930f4e6d89'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/sled_002679b5-86e3-4c02-8bd6-d8930f4e6d89.svg'
AUTHOR = 'gpt-6'

class ChristmasSleigh(Solo48):
    icon_id = 'christmas-sleigh'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('christmas', 'sleigh')

    def build(self):
        self.add_line('back-top',(4,8),(12,8))
        self.add_arc('back-curve',(12,8),(20,16),radius_x=8)
        self.add_polyline('seat',(20,16),(20,20),(24,20),(32,12),(32,28),(24,28),(12,28))
        self.add_arc('body-bottom',(12,28),(4,20),radius_x=8)
        self.add_line('back',(4,20),(4,8))
        self.add_contour('body','back-top','back-curve',*[f'seat-{i}' for i in range(1,7)],'body-bottom','back',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='seat']
        self.add_polyline('runner',(4,40),(8,40),(28,40),(34,40))
        self.add_arc('runner-curl',(34,40),(44,30),radius_x=10,sweep=False)
        self.add_contour('rail','runner-1','runner-2','runner-3','runner-curl')
        self.contours=[c for c in self.contours if c.contour_id!='runner']
        for name,a,b in [('support-left',(12,28),(8,40)),('support-right',(24,28),(28,40))]:
         self.add_line(name,a,b);self.relate('connect','body',name);self.relate('connect','rail',name)
