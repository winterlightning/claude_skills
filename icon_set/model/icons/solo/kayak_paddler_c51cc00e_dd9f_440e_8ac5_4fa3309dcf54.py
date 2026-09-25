"""Kayak Paddler. Seated paddler above a long pointed kayak; retain the head and arm gesture, with the lower torso omitted behind the boat. Diagonal paddle ends are solid strokes and its middle is occluded by the hull.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide sailboat: a simple hull with sparse figure detail. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c51cc00e-dd9f-440e-8ac5-4fa3309dcf54'
SOURCE_PATH = 'pictographic-primitives/recreation/sport kayaking_c51cc00e-dd9f-440e-8ac5-4fa3309dcf54.svg'
AUTHOR = 'gpt-6'


class KayakPaddler(Solo48):
    icon_id = 'kayak-paddler'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ('kayak', 'paddler')

    def build(self) -> None:
        self.add_arc('head-top', (18, 10), (22, 10), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('head-bottom', (22, 10), (18, 10), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('person-1', (14, 21), (28, 21))
        self.add_line('person-2', (28, 21), (32, 15))
        self.add_contour('person', 'person-1', 'person-2', closed=False)
        self.add_line('paddle-1', (38, 8), (32, 15))
        self.add_line('paddle-2', (32, 15), (28, 21))
        self.add_line('paddle-3', (28, 21), (24, 30))
        self.add_contour('paddle', 'paddle-1', 'paddle-2', 'paddle-3', closed=False)
        self.relate("connect", 'paddle', 'person')
        self.add_arc('hull-top-left', (4, 34), (24, 30), radius_x=20, radius_y=4, sweep=True)
        self.add_arc('hull-top-right', (24, 30), (44, 34), radius_x=20, radius_y=4, sweep=True)
        self.add_arc('hull-bottom-right', (44, 34), (24, 38), radius_x=20, radius_y=4, sweep=True)
        self.add_arc('hull-bottom-left', (24, 38), (4, 34), radius_x=20, radius_y=4, sweep=True)
        self.add_contour('kayak', 'hull-top-left', 'hull-top-right', 'hull-bottom-right', 'hull-bottom-left', closed=True)
        self.relate("connect", 'paddle', 'kayak')
        self.add_line('lower-paddle', (24, 38), (18, 40))
        self.relate("connect", 'lower-paddle', 'kayak')
