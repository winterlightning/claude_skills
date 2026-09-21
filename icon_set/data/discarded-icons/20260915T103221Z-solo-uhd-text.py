"""UHD Text. Retains the complete text and original case with monoline construction.

HRECT_L visible extremes (2, 6, 46, 42), centerlines (4, 8, 44, 40).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0cda311-e543-4320-895b-b795fcc497b0'
SOURCE_PATH = 'pictographic-primitives/symbol/UHD (text)_b0cda311-e543-4320-895b-b795fcc497b0.svg'
AUTHOR = 'gpt-6'


class UhdText(Solo48):
    icon_id = 'uhd-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('uhd', '4k', 'ultra-hd', 'resolution', 'video', 'display', 'screen', 'text')

    def build(self) -> None:
        self.add_line('u-left', (4, 8), (4, 36))
        self.add_arc('u-bottom', (4, 36), (12, 36), radius_x=4, radius_y=4, sweep=False)
        self.add_line('u-right', (12, 36), (12, 8))
        self.add_contour('u', 'u-left', 'u-bottom', 'u-right')
        self.add_polyline('h-left', (21, 8), (21, 24), (21, 40))
        self.add_polyline('h-right', (29, 8), (29, 24), (29, 40))
        self.add_line('h-bar', (21, 24), (29, 24))
        self.relate("connect", 'h-left', 'h-bar')
        self.relate("connect", 'h-right', 'h-bar')
        self.add_arc('d-curve', (38, 8), (38, 40), radius_x=6, radius_y=16, sweep=True)
        self.add_line('d-back', (38, 40), (38, 8))
        self.add_contour('d', 'd-curve', 'd-back', closed=True)
