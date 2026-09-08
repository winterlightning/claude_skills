"""Right-facing leaping rabbit follows the supplied image. Lucide rabbit informs rounded ears, tail and haunch construction. Rear foot detail and second ear omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a74fdf4-e500-5569-9d8c-fa2c1fe5ad69'
SOURCE_PATH = 'pictographic-primitives/animals/rabbit running_5a74fdf4-e500-5569-9d8c-fa2c1fe5ad69.svg'
AUTHOR = 'gpt-6'


class LeapingRabbit(Solo48):
    icon_id = 'leaping-rabbit'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ('running-rabbit',)
    keywords = ('rabbit', 'bunny', 'leap', 'run', 'hop', 'fast', 'hare', 'motion')

    def build(self) -> None:
        self.add_arc('outline-1', (2, 27), (15, 17), radius_x=13, radius_y=10, sweep=True)
        self.add_line('outline-2', (15, 17), (26, 23))
        self.add_arc('outline-3', (26, 23), (30, 19), radius_x=3, radius_y=3, sweep=False)
        self.add_line('outline-4', (30, 19), (22, 10))
        self.add_arc('outline-5', (22, 10), (22, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('outline-6', (22, 2), (26, 4), radius_x=5, radius_y=5, sweep=True)
        self.add_line('outline-7', (26, 4), (43, 18))
        self.add_arc('outline-8', (43, 18), (46, 25), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('outline-9', (46, 25), (39, 32), radius_x=7, radius_y=7, sweep=True)
        self.add_line('outline-10', (39, 32), (33, 32))
        self.add_line('outline-11', (33, 32), (29, 36))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', 'outline-10', 'outline-11', closed=False)
        self.add_arc('belly-1', (2, 27), (13, 35), radius_x=11, radius_y=11, sweep=False)
        self.add_line('belly-2', (13, 35), (22, 46))
        self.add_line('belly-3', (22, 46), (35, 46))
        self.add_arc('belly-4', (35, 46), (35, 40), radius_x=3, radius_y=3, sweep=False)
        self.add_line('belly-5', (35, 40), (26, 40))
        self.add_line('belly-6', (26, 40), (20, 29))
        self.add_contour('belly', 'belly-1', 'belly-2', 'belly-3', 'belly-4', 'belly-5', 'belly-6', closed=False)
        self.add_line('tail-1', (2, 27), (2, 18))
        self.add_arc('tail-2', (2, 18), (8, 12), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('tail-3', (8, 12), (13, 17), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('tail', 'tail-1', 'tail-2', 'tail-3', closed=False)
        self.relate("connect", 'outline', 'belly')
        self.relate("connect", 'outline', 'tail')
        self.relate("connect", 'belly', 'tail')
