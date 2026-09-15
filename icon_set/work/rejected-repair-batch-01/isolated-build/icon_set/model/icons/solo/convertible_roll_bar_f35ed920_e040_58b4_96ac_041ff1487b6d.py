"""Convertible with Roll Bar, rebuilt from the supplied reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f35ed920-e040-58b4-96ac-041ff1487b6d'
SOURCE_PATH = 'pictographic-primitives/transportation/convertible_f35ed920-e040-58b4-96ac-041ff1487b6d.svg'
AUTHOR = 'gpt-6'

class ConvertibleRollBar(Solo48):
    icon_id = 'convertible-roll-bar'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('convertible', 'sports car', 'roadster', 'cabriolet', 'car', 'open top', 'vehicle', 'side view')

    def build(self) -> None:
        """Raise the body shoulder above both wheels and move its attached windscreen and roll bar with it."""
        for i, x in enumerate((14, 34)):
            self.add_arc(f'wheel-{i}-a', (x - 6, 34), (x + 6, 34), radius_x=6)
            self.add_arc(f'wheel-{i}-b', (x + 6, 34), (x - 6, 34), radius_x=6)
            self.add_contour(f'wheel-{i}', f'wheel-{i}-a', f'wheel-{i}-b', closed=True)
        self.add_polyline('body', (8, 34), (4, 34), (4, 22), (18, 22), (34, 22), (40, 22), (44, 26), (44, 34), (40, 34))
        self.add_line('sill', (20, 34), (28, 34))
        for w in ('wheel-0', 'wheel-1'):
            self.relate('connect', 'body', w)
            self.relate('connect', 'sill', w)
        self.add_line('windscreen', (26, 8), (34, 22))
        self.add_line('roll-bar', (18, 14), (18, 22))
        self.relate('connect', 'windscreen', 'body')
        self.relate('connect', 'roll-bar', 'body')
