"""Stylized ram profile with hooked horn, open neck and stacked jaw lobes. Extrema (2,2)-(46,46). Lucide snail informs the open curl. Tiny inner creases omitted; source asymmetry retained."""
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
        # Stylized ram profile with hooked horn, open neck and stacked jaw lobes. Extrema (2,2)-(46,46). Lucide snail informs the open curl. Tiny inner creases omitted; source asymmetry retained.
        self.add_arc('curl', (24, 14), (22, 22), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('horn-left', (22, 22), (12, 12), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('crown', (12, 12), (22, 2), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('forehead', (22, 2), (42, 20), radius_x=28, radius_y=28, sweep=True)
        self.add_arc('nose', (42, 20), (46, 26), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('muzzle-round', (46, 26), (40, 32), radius_x=6, radius_y=6, sweep=True)
        self.add_line('muzzle-bottom', (40, 32), (34, 32))
        self.add_line('muzzle-bottom-inner', (34, 32), (28, 32))
        self.add_arc('muzzle-inner', (28, 32), (22, 26), radius_x=6, radius_y=6, sweep=True)
        self.add_line('bridge', (22, 26), (22, 22))
        self.add_contour('head', 'curl', 'horn-left', 'crown', 'forehead', 'nose', 'muzzle-round', 'muzzle-bottom', 'muzzle-bottom-inner', 'muzzle-inner', 'bridge')
        self.add_arc('neck-top', (2, 20), (12, 12), radius_x=10, radius_y=8, sweep=True)
        self.relate("connect", 'head', 'neck-top')
        self.add_arc('jaw-upper', (34, 32), (26, 40), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('jaw-lower', (26, 40), (16, 46), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('neck-base', (16, 46), (10, 43), radius_x=6, radius_y=3, sweep=True)
        self.add_contour('lower', 'jaw-upper', 'jaw-lower', 'neck-base')
        self.relate("connect", 'head', 'lower')
