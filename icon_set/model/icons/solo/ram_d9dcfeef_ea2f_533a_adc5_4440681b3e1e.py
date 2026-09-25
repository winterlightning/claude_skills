"""Front-facing ram with paired curled horns and tapered face. Extrema (6,6)-(42,42). Mirrored geometry about x=24; tiny ears and mouth fork omitted for clear horn openings."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9dcfeef-ea2f-533a-adc5-4440681b3e1e'
SOURCE_PATH = 'pictographic-primitives/animals/ram_d9dcfeef-ea2f-533a-adc5-4440681b3e1e.svg'
AUTHOR = 'gpt-6'


class RamHead(Solo48):
    icon_id = 'ram-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    aliases = ()
    keywords = ('ram', 'goat', 'horns', 'head', 'face', 'aries', 'farm', 'animal')

    def build(self) -> None:
        # Front-facing ram with paired curled horns and tapered face. Extrema (6,6)-(42,42). Mirrored geometry about x=24; tiny ears and mouth fork omitted for clear horn openings.
        self.add_arc('left-outer', (6, 14), (14, 6), radius_x=12, radius_y=12, sweep=True)
        self.add_bezier('left-crown', (14, 6), *(((16.66752306, 6), (19.11368359, 8.95896372), (20, 14)),))
        self.add_arc('left-tip', (20, 14), (14, 22), radius_x=6, radius_y=8, sweep=True)
        self.add_arc('left-inner', (14, 22), (10, 14), radius_x=8, radius_y=8, sweep=True)
        self.add_line('left-lip', (10, 14), (6, 14))
        self.add_contour('horn-left', 'left-outer', 'left-crown', 'left-tip', 'left-inner', 'left-lip')
        self.add_arc('right-outer', (42, 14), (34, 6), radius_x=12, radius_y=12, sweep=False)
        self.add_bezier('right-crown', (34, 6), *(((31.33247694, 6), (28.88631641, 8.95896372), (28, 14)),))
        self.add_arc('right-tip', (28, 14), (34, 22), radius_x=6, radius_y=8, sweep=False)
        self.add_arc('right-inner', (34, 22), (38, 14), radius_x=8, radius_y=8, sweep=False)
        self.add_line('right-lip', (38, 14), (42, 14))
        self.add_contour('horn-right', 'right-outer', 'right-crown', 'right-tip', 'right-inner', 'right-lip')
        self.add_bezier('face-left', (14, 22), *(((14.82167653, 33.67367982), (19.06753381, 42), (24, 42)),))
        self.add_bezier('face-right', (24, 42), *(((28.93246619, 42), (33.17832347, 33.67367982), (34, 22)),))
        self.add_contour('face', 'face-left', 'face-right')
        self.relate("connect", 'face', 'horn-left')
        self.relate("connect", 'face', 'horn-right')
