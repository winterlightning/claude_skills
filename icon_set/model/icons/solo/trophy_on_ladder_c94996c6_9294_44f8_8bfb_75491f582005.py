"""A handled trophy cup stands directly atop a tall ladder. The cup's narrow stem meets the converging ladder rails, with horizontal rungs descending between the splayed legs.
Lucide trophy cup and handle construction. Cup stem meets the splayed ladder with two rung levels. Symmetric about x=24; extra rungs omitted for spacing.
VRECT_L: centerline extremes (8,6)-(40,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c94996c6-9294-44f8-8bfb-75491f582005'
SOURCE_PATH = 'pictographic-primitives/work/workflow coaching ladder trophy_c94996c6-9294-44f8-8bfb-75491f582005.svg'
AUTHOR = 'gpt-6'

class TrophyOnLadder(Solo48):
    icon_id = 'trophy-on-ladder'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('trophy', 'ladder', 'cup', 'achievement', 'climbing', 'award')

    def build(self) -> None:
        """Opening repair: Deepened the cup handles and bowl together to enlarge both handle openings."""
        self.add_line('stem', (24, 24), (24, 22))
        self.add_arc('cup-left', (24, 22), (16, 14), sweep=True, large_arc=False, radius_x=8, radius_y=8)
        self.add_line('cup-wall-left', (16, 14), (16, 6))
        self.add_line('cup-rim', (16, 6), (32, 6))
        self.add_line('cup-wall-right', (32, 6), (32, 14))
        self.add_arc('cup-right', (32, 14), (24, 22), sweep=True, large_arc=False, radius_x=8, radius_y=8)
        self.add_contour('cup', 'stem', 'cup-left', 'cup-wall-left', 'cup-rim', 'cup-wall-right', 'cup-right', closed=False)
        self.add_line('handle-left-top', (16, 6), (8, 6))
        self.add_arc('handle-left', (8, 6), (16, 14), large_arc=False, radius_x=8, radius_y=10, sweep=False)
        self.add_contour('left-handle', 'handle-left-top', 'handle-left', closed=False)
        self.relate('connect', 'left-handle', 'cup')
        self.add_line('handle-right-top', (32, 6), (40, 6))
        self.add_arc('handle-right', (40, 6), (32, 14), large_arc=False, radius_x=8, radius_y=10, sweep=True)
        self.add_contour('right-handle', 'handle-right-top', 'handle-right', closed=False)
        self.relate('connect', 'right-handle', 'cup')
        self.add_polyline('ladder', (16, 42), (18, 34), (20, 24), (24, 24), (28, 24), (30, 34), (32, 42), closed=False)
        self.relate('connect', 'ladder', 'cup')
        self.add_line('rung', (18, 34), (30, 34))
        self.relate('connect', 'rung', 'ladder')
