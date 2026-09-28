from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '145df94c-38fe-4a63-b878-f9b0d6c352db'
SOURCE_PATH = 'pictographic-primitives/babies/poo poop station waste_145df94c-38fe-4a63-b878-f9b0d6c352db.svg'
AUTHOR = 'gpt-6'

class PottyWithSteam(Solo48):
    icon_id = 'potty-with-steam'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "babies"
    categories = ("babies", "primitives")
    aliases = ()
    keywords = ('potty', 'toilet', 'poop', 'steam', 'smell', 'training', 'baby', 'bathroom')

    # Designed to centerline extremes (6, 6)–(42, 42).
    def build(self):
        # Steaming potty: symmetric bowl and flowing steam strokes with a clear gap above the seat.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('potty',(6,24),(6,42),(16,36),(32,36),(42,42),(42,24))
        a('bowl',(6,24),(42,24),18,8,sweep=False)
        link('connect','bowl','potty')
        for x in (14,34):
            a(f'steam-a-{x}',(x,6),(x,12),4,3)
            a(f'steam-b-{x}',(x,12),(x,18),4,3,sweep=False)
            self.add_contour(f'steam-{x}',f'steam-a-{x}',f'steam-b-{x}')
