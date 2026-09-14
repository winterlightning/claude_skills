"""Two opposite direction arrows stand on the curved top of a globe.

Construction: signpost: opposite directional boards on a shared pole; globe construction uses mirrored elliptical meridians.
Reduction: Reduced enclosed boards to directional strokes and replaced continents with meridians so the globe remains recognizable. The pole and globe share x24.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4fee1482-35b4-4084-bf71-6f139c6fb799'
SOURCE_PATH = 'pictographic-primitives/travel/travel crossroad direction board_4fee1482-35b4-4084-bf71-6f139c6fb799.svg'
AUTHOR = 'gpt-6'

class SignpostOnGlobeVariant2(Solo48):
    icon_id = 'signpost-on-globe-v2'
    variant_of = 'signpost-on-globe'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/travel'
    aliases = ()
    keywords = ('signpost', 'direction', 'globe', 'crossroad', 'travel', 'world', 'wayfinding', 'destination')

    def build(self) -> None:
        self.add_polyline('post', (24, 8), (24, 20), (24, 32))
        self.add_polyline('right-shaft', (18, 8), (24, 8), (38, 8))
        self.add_polyline('right-head', (32, 4), (38, 8), (32, 12))
        self.add_polyline('left-shaft', (10, 20), (24, 20), (30, 20))
        self.add_polyline('left-head', (16, 16), (10, 20), (16, 24))
        self.relate('connect', 'right-shaft', 'right-head')
        self.relate('connect', 'left-shaft', 'left-head')
        self.relate('connect', 'post', 'right-shaft')
        self.relate('connect', 'post', 'left-shaft')
        self.add_arc('globe-left', (8, 44), (24, 32), radius_x=16, radius_y=12)
        self.add_arc('globe-right', (24, 32), (40, 44), radius_x=16, radius_y=12)
        self.add_contour('globe', 'globe-left', 'globe-right')
        self.add_arc('meridian-left', (24, 32), (18, 44), radius_x=6, radius_y=12, sweep=False)
        self.add_arc('meridian-right', (24, 32), (30, 44), radius_x=6, radius_y=12)
        for part in ('globe', 'meridian-left', 'meridian-right'):
            self.relate('connect', 'post', part)
        self.relate('connect', 'globe', 'meridian-left')
        self.relate('connect', 'globe', 'meridian-right')
        self.relate('connect', 'meridian-left', 'meridian-right')
