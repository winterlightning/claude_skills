"""Circular Arrows. Retains the identifying silhouette and visible features.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide refresh-cw: two opposing curved arrows; source determines the open chevron heads.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05c80477-9896-4d21-a898-62918b362b22'
SOURCE_PATH = 'pictographic-primitives/symbol/circular arrows_05c80477-9896-4d21-a898-62918b362b22.svg'
AUTHOR = 'gpt-6'


class ArrowsCircularChevron(Solo48):
    icon_id = 'arrows-circular-chevron'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('sync', 'refresh', 'repeat', 'loop', 'circular', 'arrows', 'reload', 'exchange')

    def build(self) -> None:
        self.add_arc('upper-curve', (6, 28), (22, 12), radius_x=16, radius_y=16, sweep=True)
        self.add_line('upper-tip', (22, 12), (30, 12))
        self.add_contour('upper-shaft', 'upper-curve', 'upper-tip')
        self.add_polyline('upper-head', (24, 6), (30, 12), (24, 18))
        self.relate("connect", 'upper-shaft', 'upper-head')
        self.add_arc('lower-curve', (42, 20), (26, 36), radius_x=16, radius_y=16, sweep=True)
        self.add_line('lower-tip', (26, 36), (18, 36))
        self.add_contour('lower-shaft', 'lower-curve', 'lower-tip')
        self.add_polyline('lower-head', (24, 30), (18, 36), (24, 42))
        self.relate("connect", 'lower-shaft', 'lower-head')
