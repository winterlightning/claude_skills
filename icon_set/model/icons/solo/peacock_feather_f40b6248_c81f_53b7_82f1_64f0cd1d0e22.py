"""Diagonal peacock feather with circular eye and bare quill. Lucide feather informs single vane and diagonal shaft; no barbs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f40b6248-c81f-53b7-82f1-64f0cd1d0e22'
SOURCE_PATH = 'pictographic-primitives/animals/peacock feather_f40b6248-c81f-53b7-82f1-64f0cd1d0e22.svg'
AUTHOR = 'gpt-6'


class PeacockFeather(Solo48):
    icon_id = 'peacock-feather'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('peacock', 'feather')

    def build(self) -> None:
        # Centerline extremes from VRECT_L: (6, 0, 42, 48)
        self.add_arc('vane-left', (40, 2), (12, 30), radius_x=28, radius_y=28, sweep=False, large_arc=False)
        self.add_line('vane-base', (12, 30), (12, 38))
        self.add_arc('vane-right', (12, 38), (40, 10), radius_x=28, radius_y=28, sweep=False, large_arc=False)
        self.add_line('vane-tip', (40, 10), (40, 2))
        self.add_contour('vane', 'vane-left', 'vane-base', 'vane-right', 'vane-tip', closed=True)
        self.add_line('quill', (12, 38), (8, 46))
        self.relate("connect", 'vane', 'quill')
        self.add_arc('eye-top', (22, 20), (28, 20), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('eye-bottom', (28, 20), (22, 20), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('eye', 'eye-top', 'eye-bottom', closed=True)
