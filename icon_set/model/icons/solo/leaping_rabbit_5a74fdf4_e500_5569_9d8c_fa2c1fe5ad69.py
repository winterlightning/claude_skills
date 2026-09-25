"""Round the rabbit head and muzzle while retaining the leaping body and long ear. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5a74fdf4-e500-5569-9d8c-fa2c1fe5ad69'
SOURCE_PATH = 'pictographic-primitives/animals/rabbit running_5a74fdf4-e500-5569-9d8c-fa2c1fe5ad69.svg'
AUTHOR = 'gpt-6'

class LeapingRabbit(Solo48):
    icon_id = 'leaping-rabbit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ('running-rabbit',)
    keywords = ('rabbit', 'bunny', 'leap', 'run', 'hop', 'fast', 'hare', 'motion')

    def build(self):
        """Symbol plan: Round the rabbit head and muzzle while retaining the leaping body and long ear. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_arc('rump', (6, 28), (16, 18), radius_x=10, radius_y=10, sweep=True)
        self.add_line('back', (16, 18), (26, 24))
        self.add_arc('shoulder', (26, 24), (32, 18), radius_x=6, radius_y=6, sweep=False)
        self.add_line('head-1', (32, 18), (36, 18))
        self.add_arc('head-2', (36, 18), (42, 24), radius_x=6)
        self.add_arc('head-3', (42, 24), (36, 30), radius_x=6)
        self.add_line('head-4', (36, 30), (30, 34))
        self.contours = [c for c in self.contours if c.contour_id != 'head']
        self.add_contour('outline', 'rump', 'back', 'shoulder', 'head-1', 'head-2', 'head-3', 'head-4', closed=False)
        self.add_line('ear', (32, 18), (22, 6))
        self.relate('connect', 'ear', 'outline')
        self.add_arc('belly', (6, 28), (14, 36), radius_x=8, radius_y=8, sweep=False)
        self.add_polyline('foot', (14, 36), (22, 42), (36, 42), closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'foot']
        self.add_contour('lower', 'belly', 'foot-1', 'foot-2', closed=False)
        self.relate('connect', 'lower', 'outline')
        self.add_dot('tail', (6, 12))
