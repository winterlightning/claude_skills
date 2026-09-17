"""Horizontal Slider; standalone reconstruction of the supplied reference.
Construction: Lucide sliders-horizontal informed coherent contours and structural joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '941fbf6b-a6f1-56d2-9eab-84199e3fb40c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/setting slider horizontal_941fbf6b-a6f1-56d2-9eab-84199e3fb40c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-slider'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('slider', 'control', 'setting', 'adjust', 'horizontal', 'knob')

    def build(self):
        # Plan: capsule owns x=20, radius=4, extrema y=10/38; asymmetric track.
        self.add_arc("knob-top", (16,14), (24,14), radius_x=4)
        self.add_line("knob-right", (24,14), (24,34))
        self.add_arc("knob-bottom", (24,34), (16,34), radius_x=4)
        self.add_line("knob-left", (16,34), (16,14))
        self.add_contour("knob", "knob-top", "knob-right", "knob-bottom", "knob-left", closed=True)
        self.add_line("track-left", (4,24), (8,24))
        self.add_line("track-right", (32,24), (44,24))
