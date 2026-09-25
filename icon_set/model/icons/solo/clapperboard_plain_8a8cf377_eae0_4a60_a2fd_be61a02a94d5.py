"""Clapperboard. Retains the identifying silhouette and visible features.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide clapperboard: rounded slate and diagonal band dividers; supplied source specifies a closed level band and one text line.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a8cf377-eae0-4a60-a2fd-be61a02a94d5'
SOURCE_PATH = 'pictographic-primitives/symbol/clapper_8a8cf377-eae0-4a60-a2fd-be61a02a94d5.svg'
AUTHOR = 'gpt-6'


class ClapperboardPlain(Solo48):
    icon_id = 'clapperboard-plain'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('clapperboard', 'film', 'movie', 'cinema', 'video', 'production', 'slate', 'scene')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        self.add_line('top-1', (8, 8), (28, 8))
        self.add_line('top-2', (28, 8), (40, 8))
        self.add_arc('ne', (40, 8), (44, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('right-1', (44, 12), (44, 18))
        self.add_line('right-2', (44, 18), (44, 36))
        self.add_arc('se', (44, 36), (40, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom', (40, 40), (8, 40))
        self.add_arc('sw', (8, 40), (4, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left-1', (4, 36), (4, 18))
        self.add_line('left-2', (4, 18), (4, 12))
        self.add_arc('nw', (4, 12), (8, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('board', 'top-1', 'top-2', 'ne', 'right-1', 'right-2', 'se', 'bottom', 'sw', 'left-1', 'left-2', 'nw', closed=True)
        self.add_polyline('band', (4, 18), (20, 18), (44, 18))
        self.add_line('stripe', (20, 18), (28, 8))
        self.relate("connect", 'board', 'band')
        self.relate("connect", 'board', 'stripe')
        self.relate("connect", 'band', 'stripe')
        self.add_line('text', (14, 29), (34, 29))
