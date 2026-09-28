"""A broad ski goggle with a brow band and a central nose notch."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a177b70f-0c0f-5d94-9d0e-e53300456681'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/glasses ski_a177b70f-0c0f-5d94-9d0e-e53300456681.svg'
AUTHOR = 'gpt-6'


class SkiGogglesWithBrowBand(Solo48):
    icon_id = 'ski-goggles-with-brow-band'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "accessories"
    categories = ("primitives", "accessories")
    aliases = ()
    keywords = ('goggles', 'ski goggles', 'snow', 'ski', 'eyewear', 'winter', 'sports', 'snowboard')

    def build(self) -> None:
        # HRECT_L: authored directly to its SOLO48 centerline extremes.
        self.add_line('top', (8, 8), (40, 8))
        self.add_arc('tr', (40, 8), (44, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('r-upper', (44, 12), (44, 17))
        self.add_line('r-lower', (44, 17), (44, 32))
        self.add_arc('br', (44, 32), (38, 40), radius_x=6, radius_y=8, sweep=True)
        self.add_line('r-base', (38, 40), (34, 40))
        self.add_arc('nose-r', (34, 40), (28, 34), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('nose', (28, 34), (20, 34), radius_x=4, radius_y=4, sweep=False)
        self.add_arc('nose-l', (20, 34), (14, 40), radius_x=6, radius_y=6, sweep=True)
        self.add_line('l-base', (14, 40), (10, 40))
        self.add_arc('bl', (10, 40), (4, 32), radius_x=6, radius_y=8, sweep=True)
        self.add_line('l-lower', (4, 32), (4, 17))
        self.add_line('l-upper', (4, 17), (4, 12))
        self.add_arc('tl', (4, 12), (8, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('outline', 'top', 'tr', 'r-upper', 'r-lower', 'br', 'r-base', 'nose-r', 'nose', 'nose-l', 'l-base', 'bl', 'l-lower', 'l-upper', 'tl', closed=True)
        self.add_line('brow', (4, 17), (44, 17))
        self.relate("connect", 'brow', 'outline')
