"""Front-facing ram with paired curled horns and tapered face. Extrema (2,2)-(46,46). Mirrored geometry about x=24; tiny ears and mouth fork omitted for clear horn openings."""
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
    category = 'animals/wildlife'
    aliases = ()
    keywords = ('ram', 'goat', 'horns', 'head', 'face', 'aries', 'farm', 'animal')

    def build(self) -> None:
        # Front-facing ram with paired curled horns and tapered face. Extrema (2,2)-(46,46). Mirrored geometry about x=24; tiny ears and mouth fork omitted for clear horn openings.
        self.add_arc('left-outer', (2, 14), (14, 2), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('left-crown', (14, 2), (20, 14), radius_x=6, radius_y=12, sweep=True)
        self.add_arc('left-tip', (20, 14), (14, 22), radius_x=6, radius_y=8, sweep=True)
        self.add_arc('left-inner', (14, 22), (10, 14), radius_x=8, radius_y=8, sweep=True)
        self.add_line('left-lip', (10, 14), (2, 14))
        self.add_contour('horn-left', 'left-outer', 'left-crown', 'left-tip', 'left-inner', 'left-lip')
        self.add_arc('right-outer', (46, 14), (34, 2), radius_x=12, radius_y=12, sweep=False)
        self.add_arc('right-crown', (34, 2), (28, 14), radius_x=6, radius_y=12, sweep=False)
        self.add_arc('right-tip', (28, 14), (34, 22), radius_x=6, radius_y=8, sweep=False)
        self.add_arc('right-inner', (34, 22), (38, 14), radius_x=8, radius_y=8, sweep=False)
        self.add_line('right-lip', (38, 14), (46, 14))
        self.add_contour('horn-right', 'right-outer', 'right-crown', 'right-tip', 'right-inner', 'right-lip')
        self.add_arc('face-left', (14, 22), (24, 46), radius_x=10, radius_y=24, sweep=False)
        self.add_arc('face-right', (24, 46), (34, 22), radius_x=10, radius_y=24, sweep=False)
        self.add_contour('face', 'face-left', 'face-right')
        self.relate("connect", 'face', 'horn-left')
        self.relate("connect", 'face', 'horn-right')
