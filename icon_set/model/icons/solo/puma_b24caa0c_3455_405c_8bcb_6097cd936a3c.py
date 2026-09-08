"""Low left-facing cat follows the supplied image. Lucide bird provides only general coherent contour construction; no useful local puma match. Far legs and facial detail omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b24caa0c-3455-405c-8bcb-6097cd936a3c'
SOURCE_PATH = 'pictographic-primitives/animals/puma_b24caa0c-3455-405c-8bcb-6097cd936a3c.svg'
AUTHOR = 'gpt-6'


class ProwlingPuma(Solo48):
    icon_id = 'prowling-puma'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ('cougar', 'mountain-lion')
    keywords = ('puma', 'cougar', 'mountain lion', 'prowl', 'big cat', 'feline', 'stalk', 'wildlife')

    def build(self) -> None:
        self.add_line('outline-1', (2, 20), (5, 17))
        self.add_line('outline-2', (5, 17), (8, 8))
        self.add_line('outline-3', (8, 8), (13, 13))
        self.add_line('outline-4', (13, 13), (30, 13))
        self.add_arc('outline-5', (30, 13), (40, 19), radius_x=14, radius_y=14, sweep=True)
        self.add_line('outline-6', (40, 19), (46, 25))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', closed=False)
        self.add_arc('underside-1', (2, 20), (8, 24), radius_x=6, radius_y=4, sweep=False)
        self.add_line('underside-2', (8, 24), (13, 24))
        self.add_line('underside-3', (13, 24), (8, 33))
        self.add_arc('underside-4', (8, 33), (11, 40), radius_x=4, radius_y=5, sweep=False)
        self.add_line('underside-5', (11, 40), (19, 29))
        self.add_line('underside-6', (19, 29), (29, 29))
        self.add_arc('underside-7', (29, 29), (36, 34), radius_x=7, radius_y=5, sweep=False)
        self.add_line('underside-8', (36, 34), (36, 40))
        self.add_line('underside-9', (36, 40), (42, 40))
        self.add_line('underside-10', (42, 40), (42, 31))
        self.add_arc('underside-11', (42, 31), (36, 22), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('underside', 'underside-1', 'underside-2', 'underside-3', 'underside-4', 'underside-5', 'underside-6', 'underside-7', 'underside-8', 'underside-9', 'underside-10', 'underside-11', closed=False)
        self.relate("connect", 'outline', 'underside')
