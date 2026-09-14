"""Flagged Diving Buoy. Round float with flag and trailing rope; reduce flanking waves to short water marks. Flag gives deliberate asymmetry.
Keyshape VRECT_L, visible extremes (6, 2, 42, 46); centerline envelope inset by 2.
Construction: Lucide flag: a simple attached fabric contour and pole. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57a87afc-6af8-4647-a7c2-7bb5c5bffccf'
SOURCE_PATH = 'pictographic-primitives/recreation/diving scuba free diving buoy flag_57a87afc-6af8-4647-a7c2-7bb5c5bffccf.svg'
AUTHOR = 'gpt-6'


class FlaggedDivingBuoy(Solo48):
    icon_id = 'flagged-diving-buoy'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('flagged', 'diving', 'buoy')

    def build(self) -> None:
        self.add_line('flag-1', (24, 4), (40, 4))
        self.add_line('flag-2', (40, 4), (40, 14))
        self.add_line('flag-3', (40, 14), (24, 14))
        self.add_line('flag-4', (24, 14), (24, 4))
        self.add_contour('flag', 'flag-1', 'flag-2', 'flag-3', 'flag-4', closed=True)
        self.add_line('mast', (24, 14), (24, 21))
        self.relate("connect", 'flag', 'mast')
        self.add_arc('float-top', (18, 27), (30, 27), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('float-bottom', (30, 27), (18, 27), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('float', 'float-top', 'float-bottom', closed=True)
        self.relate("connect", 'mast', 'float')
        self.add_line('rope', (24, 33), (24, 44))
        self.relate("connect", 'float', 'rope')
        self.add_line('water-left', (8, 28), (10, 28))
        self.add_line('water-right', (38, 28), (40, 28))
