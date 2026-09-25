"""Diving Flag Buoy. Swallowtail flag over a wide float; omit stripe and pointed brace to retain clear flag opening.
Keyshape VRECT_L, visible extremes (6, 2, 42, 46); centerline envelope inset by 2.
Construction: Lucide flag: unified fabric contour with an attached pole. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '161e10ec-6a74-5089-a2aa-165d64d9bf7e'
SOURCE_PATH = 'pictographic-primitives/recreation/diving flag buoys_161e10ec-6a74-5089-a2aa-165d64d9bf7e.svg'
AUTHOR = 'gpt-6'


class DivingFlagBuoy(Solo48):
    icon_id = 'diving-flag-buoy'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    aliases = ()
    keywords = ('diving', 'flag', 'buoy')

    def build(self) -> None:
        self.add_line('flag-1', (20, 4), (40, 4))
        self.add_line('flag-2', (40, 4), (34, 13))
        self.add_line('flag-3', (34, 13), (40, 22))
        self.add_line('flag-4', (40, 22), (20, 22))
        self.add_line('flag-5', (20, 22), (20, 4))
        self.add_contour('flag', 'flag-1', 'flag-2', 'flag-3', 'flag-4', 'flag-5', closed=True)
        self.add_line('mast', (20, 22), (20, 34))
        self.relate("connect", 'flag', 'mast')
        self.add_arc('float-top', (8, 39), (40, 39), radius_x=16, radius_y=5, sweep=True)
        self.add_arc('float-bottom', (40, 39), (8, 39), radius_x=16, radius_y=5, sweep=True)
        self.add_contour('float', 'float-top', 'float-bottom', closed=True)
        self.relate("connect", 'mast', 'float')
