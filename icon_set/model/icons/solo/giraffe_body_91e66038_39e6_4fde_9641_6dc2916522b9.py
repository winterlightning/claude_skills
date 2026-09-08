"""Right-facing giraffe with long neck, one ossicone and two visible legs; distant legs and tiny facial marks omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91e66038-39e6-4fde-9641-6dc2916522b9'
SOURCE_PATH = 'pictographic-primitives/animals/giraffe body_91e66038-39e6-4fde-9641-6dc2916522b9.svg'
AUTHOR = 'gpt-6'


class StandingGiraffe(Solo48):
    icon_id = 'standing-giraffe'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('giraffe', 'standing', 'neck', 'tall', 'animal', 'safari', 'zoo', 'africa')

    def build(self) -> None:
        # Keyshape ink extremes: (3, 0, 45, 48); centerlines inset by stroke radius 2.
        self.add_line('body-1', (11, 27), (23, 27))
        self.add_arc('body-2', (23, 27), (28, 22), radius_x=5, radius_y=5, sweep=False)
        self.add_line('body-3', (28, 22), (31, 9))
        self.add_line('body-4', (31, 9), (27, 7))
        self.add_line('body-5', (27, 7), (26, 2))
        self.add_line('body-6', (26, 2), (32, 5))
        self.add_line('body-7', (32, 5), (35, 9))
        self.add_line('body-8', (35, 9), (43, 15))
        self.add_line('body-9', (43, 15), (43, 18))
        self.add_line('body-10', (43, 18), (35, 18))
        self.add_line('body-11', (35, 18), (33, 31))
        self.add_line('body-12', (33, 31), (33, 46))
        self.add_line('body-13', (33, 46), (27, 46))
        self.add_line('body-14', (27, 46), (25, 36))
        self.add_line('body-15', (25, 36), (17, 36))
        self.add_line('body-16', (17, 36), (11, 46))
        self.add_line('body-17', (11, 46), (5, 46))
        self.add_line('body-18', (5, 46), (11, 27))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', 'body-12', 'body-13', 'body-14', 'body-15', 'body-16', 'body-17', 'body-18', closed=True)
        self.add_line('horn', (35, 9), (35, 2))
        self.relate("connect", 'horn', 'body')
        self.add_line('tail', (11, 27), (5, 33))
        self.relate("connect", 'tail', 'body')
