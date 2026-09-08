"""Seahorse with blunt snout, S body and hooked tail; original orientation retained. Centerline (11,2)-(37,46)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f6a3c15-cfca-5d3d-83d6-1c6bddf42ba8'
SOURCE_PATH = 'pictographic-primitives/animals/seahorse_2f6a3c15-cfca-5d3d-83d6-1c6bddf42ba8.svg'
AUTHOR = 'gpt-6'


class Seahorse(Solo48):
    icon_id = 'seahorse'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('seahorse', 'sea', 'ocean', 'marine', 'fish', 'curl', 'tail', 'aquarium')

    def build(self) -> None:
        self.add_arc('outline-1', (15, 37), (11, 41), radius_x=5, radius_y=5, sweep=False)
        self.add_arc('outline-2', (11, 41), (20, 46), radius_x=9, radius_y=5, sweep=False)
        self.add_arc('outline-3', (20, 46), (31, 35), radius_x=11, radius_y=11, sweep=False)
        self.add_line('outline-4', (31, 35), (31, 19))
        self.add_arc('outline-5', (31, 19), (37, 5), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('outline-6', (37, 5), (30, 2), radius_x=7, radius_y=3, sweep=False)
        self.add_arc('outline-7', (30, 2), (24, 5), radius_x=6, radius_y=3, sweep=False)
        self.add_arc('outline-8', (24, 5), (11, 10), radius_x=15, radius_y=10, sweep=True)
        self.add_line('outline-9', (11, 10), (11, 16))
        self.add_line('outline-10', (11, 16), (20, 16))
        self.add_arc('outline-11', (20, 16), (23, 20), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('outline-12', (23, 20), (20, 30), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('outline-13', (20, 30), (23, 37), radius_x=12, radius_y=12, sweep=False)
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', 'outline-10', 'outline-11', 'outline-12', 'outline-13', closed=False)
        self.add_line('fin-1', (31, 22), (37, 20))
        self.add_line('fin-2', (37, 20), (37, 30))
        self.add_line('fin-3', (37, 30), (31, 28))
        self.add_contour('fin', 'fin-1', 'fin-2', 'fin-3', closed=False)
        self.relate("connect", 'outline', 'fin')
