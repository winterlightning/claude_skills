"""Enlarge the upper tail lobe by six units while preserving the broad lower lobe and geometric hammer-shaped head. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bdd1577c-6f14-5bee-a41f-fac2b80017a7'
SOURCE_PATH = 'pictographic-primitives/animals/shark hammer_bdd1577c-6f14-5bee-a41f-fac2b80017a7.svg'
AUTHOR = 'gpt-6'

class HammerheadShark(Solo48):
    icon_id = 'hammerhead-shark'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('hammerhead', 'shark', 'head', 'fins', 'sea', 'ocean', 'fish', 'predator')

    def build(self):
        """Symbol plan: Enlarge the upper tail lobe by six units while preserving the broad lower lobe and geometric hammer-shaped head. Reference: inspected current parent; no useful exact Lucide match selected."""
        points = [(6, 6), (34, 6), (34, 14), (24, 14), (24, 18), (28, 22), (24, 26)]
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'head-{i}', a, b)
        self.add_arc('inner-body', (24, 26), (34, 32), radius_x=10, radius_y=6, sweep=False)
        self.add_line('tail-upper', (34, 32), (42, 16))
        self.add_line('tail-end', (42, 16), (42, 42))
        self.add_line('tail-bottom', (42, 42), (30, 42))
        self.add_arc('outer-body', (30, 42), (14, 26), radius_x=16, sweep=True)
        points = [(14, 26), (6, 26), (14, 18), (14, 14), (6, 14), (6, 6)]
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'left-{i}', a, b)
        self.add_contour('body', *[f'head-{i}' for i in range(1, 7)], 'inner-body', 'tail-upper', 'tail-end', 'tail-bottom', 'outer-body', *[f'left-{i}' for i in range(1, 6)], closed=True)
