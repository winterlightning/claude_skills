"""Chevron Marker Board, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '88cc82e8-6bf8-4a2c-bd7b-cc0bddf04d43'
SOURCE_PATH = 'pictographic-primitives/transportation/light guide_88cc82e8-6bf8-4a2c-bd7b-cc0bddf04d43.svg'
AUTHOR = 'gpt-6'

class ChevronMarkerBoard(Solo48):
    icon_id = 'chevron-marker-board'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('chevron', 'marker', 'guide', 'road marker', 'reflector', 'direction', 'sign', 'light guide')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        # Current contract centerline extremes: (8,6)-(40,42).
        self.add_line('top',(12, 4),(36, 4))
        self.add_arc('tr',(36, 4),(40,8),radius_x=4)
        self.add_polyline('right',(40,8),(40,24),(40,38),(40,40))
        self.add_arc('br',(40,40),(36, 44),radius_x=4)
        self.add_line('bottom',(36, 44),(12, 44))
        self.add_arc('bl',(12, 44),(8,40),radius_x=4)
        self.add_polyline('left',(8,40),(8,38),(8,24),(8,8))
        self.add_arc('tl',(8,8),(12, 4),radius_x=4)
        self.relate('connect','top','tr')
        self.relate('connect','tr','right')
        self.relate('connect','right','br')
        self.relate('connect','br','bottom')
        self.relate('connect','bottom','bl')
        self.relate('connect','bl','left')
        self.relate('connect','left','tl')
        self.relate('connect','tl','top')
        for i,y in enumerate((24,38)):
            self.add_polyline(f'chevron-{i}',(8,y),(24,y-12),(40,y))
            self.relate('connect',f'chevron-{i}','left')
            self.relate('connect',f'chevron-{i}','right')
