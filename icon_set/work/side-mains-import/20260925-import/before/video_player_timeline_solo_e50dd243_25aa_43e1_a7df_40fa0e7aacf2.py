"""Video player timeline.

Construction reference: panel-top.
Preserves timeline and scrubber; excludes play triangle.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'e50dd243-25aa-43e1-a7df-40fa0e7aacf2'
SOURCE_PATH = 'pictographic-primitives/video/video player adjust_e50dd243-25aa-43e1-a7df-40fa0e7aacf2.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'video-player-timeline-solo-e50dd243'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('video-player-timeline',)
    keywords = ('video', 'player', 'timeline')

    def build(self):
        box(self,'player',4,8,44,40,4)
        self.add_polyline('timeline',(13,29),(22,29),(35,29))
        self.add_polyline('scrubber',(22,24),(22,29),(22,31))
        self.relate('connect','timeline','scrubber')
