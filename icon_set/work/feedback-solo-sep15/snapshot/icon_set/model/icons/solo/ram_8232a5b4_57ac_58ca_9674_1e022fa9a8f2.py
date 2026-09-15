"""Stylized ram profile with hooked horn, open neck and stacked jaw lobes. Extrema (6,6)-(42,42). Lucide snail informs the open curl. Tiny inner creases omitted; source asymmetry retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8232a5b4-57ac-58ca-9674-1e022fa9a8f2'
SOURCE_PATH = 'pictographic-primitives/animals/ram_8232a5b4-57ac-58ca-9674-1e022fa9a8f2.svg'
AUTHOR = 'gpt-6'


class StylizedRamHead(Solo48):
    icon_id = 'stylized-ram-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/wildlife'
    aliases = ()
    keywords = ('ram', 'sheep', 'horn', 'curl', 'head', 'profile', 'abstract', 'animal')

    def build(self) -> None:
        # Stylized ram profile with hooked horn, open neck and stacked jaw lobes. Extrema (6,6)-(42,42). Lucide snail informs the open curl. Tiny inner creases omitted; source asymmetry retained.
        self.add_arc('curl', (24, 14), (22, 22), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('horn-left', (22, 22), (12, 12), radius_x=10, radius_y=10, sweep=True)
        self.add_bezier('crown', (12, 12), *(((13.70141156, 8.06218191), (17.72479037, 6), (22, 6)),))
        self.add_arc('forehead', (22, 6), (42, 20), radius_x=28, radius_y=28, sweep=True)
        self.add_bezier('nose', (42, 20), *(((42, 21.9528534), (42, 24.0471466), (42, 26)),))
        self.add_bezier('muzzle-round', (42, 26), *(((42, 28.21753356), (41.75220913, 30.5422399), (40, 32)),))
        self.add_line('muzzle-bottom', (40, 32), (34, 32))
        self.add_line('muzzle-bottom-inner', (34, 32), (28, 32))
        self.add_arc('muzzle-inner', (28, 32), (22, 26), radius_x=6, radius_y=6, sweep=True)
        self.add_line('bridge', (22, 26), (22, 22))
        self.add_contour('head', 'curl', 'horn-left', 'crown', 'forehead', 'nose', 'muzzle-round', 'muzzle-bottom', 'muzzle-bottom-inner', 'muzzle-inner', 'bridge')
        self.add_bezier('neck-top', (6, 20), *(((6, 16.57983229), (8.06218191, 13.36112925), (12, 12)),))
        self.relate("connect", 'head', 'neck-top')
        self.add_arc('jaw-upper', (34, 32), (26, 40), radius_x=8, radius_y=8, sweep=True)
        self.add_bezier('jaw-lower', (26, 40), *(((23.57039983, 41.75220913), (19.69588927, 42), (16, 42)),))
        self.add_bezier('neck-base', (16, 42), *(((14.14359354, 42), (11.85640646, 42), (10, 42)),))
        self.add_contour('lower', 'jaw-upper', 'jaw-lower', 'neck-base')
        self.relate("connect", 'head', 'lower')
