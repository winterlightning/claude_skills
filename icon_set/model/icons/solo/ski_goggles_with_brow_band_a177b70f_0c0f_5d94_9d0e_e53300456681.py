"""A broad ski goggle with a brow band and a central nose notch."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a177b70f-0c0f-5d94-9d0e-e53300456681'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/glasses ski_a177b70f-0c0f-5d94-9d0e-e53300456681.svg'
AUTHOR = 'astra-chatgpt'


class SkiGogglesWithBrowBand(Solo48):
    icon_id = 'ski-goggles-with-brow-band'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('goggles', 'ski goggles', 'snow', 'ski', 'eyewear', 'winter', 'sports', 'snowboard')

    def build(self) -> None:
        # HRECT_M: authored directly to its SOLO48 centerline extremes.
        self.add_line('top', (6, 11), (42, 11))
        self.add_arc('tr', (42, 11), (46, 15), radius_x=4, radius_y=4, sweep=True)
        self.add_line('r-upper', (46, 15), (46, 19))
        self.add_line('r-lower', (46, 19), (46, 29))
        self.add_arc('br', (46, 29), (38, 37), radius_x=8, radius_y=8, sweep=True)
        self.add_line('r-base', (38, 37), (34, 37))
        self.add_arc('nose-r', (34, 37), (28, 31), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('nose', (28, 31), (20, 31), radius_x=4, radius_y=4, sweep=False)
        self.add_arc('nose-l', (20, 31), (14, 37), radius_x=6, radius_y=6, sweep=True)
        self.add_line('l-base', (14, 37), (10, 37))
        self.add_arc('bl', (10, 37), (2, 29), radius_x=8, radius_y=8, sweep=True)
        self.add_line('l-lower', (2, 29), (2, 19))
        self.add_line('l-upper', (2, 19), (2, 15))
        self.add_arc('tl', (2, 15), (6, 11), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('outline', 'top', 'tr', 'r-upper', 'r-lower', 'br', 'r-base', 'nose-r', 'nose', 'nose-l', 'l-base', 'bl', 'l-lower', 'l-upper', 'tl', closed=True)
        self.add_line('brow', (2, 19), (46, 19))
        self.relate("connect", 'brow', 'outline')
