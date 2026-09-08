"""Front peacock with symmetric tail fan and centered body, directional beak; short fan strokes and feet simplified."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e421611-5f19-400d-8a51-23357e8cb95c'
SOURCE_PATH = 'pictographic-primitives/animals/peacock feathers up_9e421611-5f19-400d-8a51-23357e8cb95c.svg'
AUTHOR = 'gpt-6'


class PeacockWithSpreadTail(Solo48):
    icon_id = 'peacock-with-spread-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('peacock', 'with', 'spread', 'tail')

    def build(self) -> None:
        # Centerline extremes from SQUARE: (0, 0, 48, 48)
        self.add_arc('fan-left', (2, 24), (24, 2), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('fan-right', (24, 2), (46, 24), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('fan-lower-right', (46, 24), (42, 38), radius_x=30, radius_y=30, sweep=True, large_arc=False)
        self.add_line('fan-right-base', (42, 38), (39, 38))
        self.add_contour('fan', 'fan-left', 'fan-right', 'fan-lower-right', 'fan-right-base', closed=False)
        self.add_arc('fan-lower-left', (2, 24), (6, 38), radius_x=30, radius_y=30, sweep=False, large_arc=False)
        self.add_line('fan-left-base', (6, 38), (9, 38))
        self.add_contour('fan-left-side', 'fan-lower-left', 'fan-left-base', closed=False)
        self.relate("connect", 'fan', 'fan-left-side')
        self.add_arc('head', (20, 22), (28, 14), radius_x=6, radius_y=6, sweep=True, large_arc=True)
        self.add_line('beak', (28, 14), (33, 20))
        self.add_line('throat', (33, 20), (27, 22))
        self.add_line('body-right', (27, 22), (31, 33))
        self.add_arc('belly', (31, 33), (24, 41), radius_x=7, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('belly-left', (24, 41), (17, 33), radius_x=7, radius_y=8, sweep=True, large_arc=False)
        self.add_line('body-left', (17, 33), (20, 22))
        self.add_contour('bird', 'head', 'beak', 'throat', 'body-right', 'belly', 'belly-left', 'body-left', closed=True)
        self.add_line('leg-left', (24, 41), (18, 46))
        self.add_line('leg-right', (24, 41), (30, 46))
        self.relate("connect", 'bird', 'leg-left')
        self.relate("connect", 'bird', 'leg-right')
        self.relate("connect", 'leg-left', 'leg-right')
