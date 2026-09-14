"""Diver Beside Marker Buoy. Diver reaches toward a flagged marker; retain the water cue and trailing line, omit the second arm and extra waves.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05eae23b-b81d-5ba9-a08b-414daf65ebe4'
SOURCE_PATH = 'pictographic-primitives/recreation/diving scuba free diving buoy flag hold_05eae23b-b81d-5ba9-a08b-414daf65ebe4.svg'
AUTHOR = 'gpt-6'


class DiverBesideMarkerBuoy(Solo48):
    icon_id = 'diver-beside-marker-buoy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('diver', 'beside', 'marker', 'buoy')

    def build(self) -> None:
        self.add_line('flag-1', (28, 6), (42, 6))
        self.add_line('flag-2', (42, 6), (42, 16))
        self.add_line('flag-3', (42, 16), (28, 16))
        self.add_line('flag-4', (28, 16), (28, 6))
        self.add_contour('flag', 'flag-1', 'flag-2', 'flag-3', 'flag-4', closed=True)
        self.add_line('mast-top', (28, 16), (28, 22))
        self.relate("connect", 'flag', 'mast-top')
        self.add_arc('float-top', (23, 27), (33, 27), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('float-bottom', (33, 27), (23, 27), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('float', 'float-top', 'float-bottom', closed=True)
        self.relate("connect", 'float', 'mast-top')
        self.add_line('rope', (28, 32), (28, 42))
        self.relate("connect", 'float', 'rope')
        self.add_arc('head-top', (8, 27), (12, 27), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('head-bottom', (12, 27), (8, 27), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('diver-1', (6, 42), (11, 37))
        self.add_line('diver-2', (11, 37), (19, 37))
        self.add_contour('diver', 'diver-1', 'diver-2', closed=False)
        self.add_line('water', (6, 15), (16, 15))
