"""HDR Text. Retains the complete text and original case with monoline construction.

HRECT_L visible extremes (2, 6, 46, 42), centerlines (4, 8, 44, 40).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5580b474-3597-486f-9212-1e7b6c337f96'
SOURCE_PATH = 'pictographic-primitives/symbol/HDR_5580b474-3597-486f-9212-1e7b6c337f96.svg'
AUTHOR = 'gpt-6'


class HdrText(Solo48):
    icon_id = 'hdr-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('hdr', 'high-dynamic-range', 'photo', 'video', 'display', 'camera', 'text')

    def build(self) -> None:
        self.add_polyline('h-left', (6, 8), (6, 24), (6, 40))
        self.add_polyline('h-right', (12, 8), (12, 24), (12, 40))
        self.add_line('h-bar', (6, 24), (12, 24))
        self.relate("connect", 'h-left', 'h-bar')
        self.relate("connect", 'h-right', 'h-bar')
        self.add_arc('d-curve', (21, 8), (21, 40), radius_x=6, radius_y=16, sweep=True)
        self.add_line('d-back', (21, 40), (21, 8))
        self.add_contour('d', 'd-curve', 'd-back', closed=True)
        self.add_polyline('r-stem', (36, 40), (36, 24), (36, 8))
        self.add_arc('r-bowl', (36, 8), (36, 24), radius_x=8, radius_y=8, sweep=True)
        self.add_line('r-leg', (36, 24), (42, 40))
        self.relate("connect", 'r-stem', 'r-bowl')
        self.relate("connect", 'r-stem', 'r-leg')
        self.relate("connect", 'r-bowl', 'r-leg')
