"""Cricket profile; centerline extremes (2,8)-(46,40). Left-facing head follows actual reference; long wing and tall folded hind leg retained. Fine eye omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f676f8b4-b6a7-4e6b-ab0e-87feab8269f5'
SOURCE_PATH = 'pictographic-primitives/animals/insect cricket body_f676f8b4-b6a7-4e6b-ab0e-87feab8269f5.svg'
AUTHOR = 'gpt-6'


class Cricket(Solo48):
    icon_id = 'cricket'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('cricket', 'grasshopper', 'insect', 'locust', 'bug', 'jump', 'legs', 'chirp')

    def build(self) -> None:
        # Cricket profile; centerline extremes (2,8)-(46,40). Left-facing head follows actual reference; long wing and tall folded hind leg retained. Fine eye omitted.
        self.add_line('wing-front', (4, 22), (20, 25))
        self.add_line('wing-top', (20, 25), (36, 28))
        self.add_arc('wing-bottom', (36, 28), (25, 33), radius_x=11, radius_y=5, sweep=True)
        self.add_line('belly', (25, 33), (16, 33))
        self.add_arc('chest', (16, 33), (4, 22), radius_x=12, radius_y=11, sweep=True)
        self.add_contour('body', 'wing-front', 'wing-top', 'wing-bottom', 'belly', 'chest', closed=True)
        self.add_polyline('hind-leg', (20, 25), (36, 8), (43, 40), (46, 40), closed=False)
        self.relate("connect", 'body', 'hind-leg')
        self.add_polyline('front-leg', (16, 33), (9, 40), (2, 40), closed=False)
        self.relate("connect", 'body', 'front-leg')
        self.add_polyline('middle-leg', (25, 33), (22, 40), (17, 40), closed=False)
        self.relate("connect", 'body', 'middle-leg')
        self.add_polyline('antenna', (4, 22), (2, 15), (2, 8), closed=False)
        self.relate("connect", 'body', 'antenna')
