"""Camper Van. Right-facing vehicle; retain two wheels and the side-window mark, omit its frame and trim.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide caravan: tangent roof corners, structural windows and circular wheels. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '67545933-613d-5320-bb66-9887235b5423'
SOURCE_PATH = 'pictographic-primitives/recreation/camping rv_67545933-613d-5320-bb66-9887235b5423.svg'
AUTHOR = 'gpt-6'


class CamperVan(Solo48):
    icon_id = 'camper-van'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('camper', 'van')

    def build(self) -> None:
        self.add_line('body-1', (9, 35), (4, 35))
        self.add_line('body-2', (4, 35), (4, 12))
        self.add_arc('roof-turn', (4, 12), (8, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_line('roof-1', (8, 8), (31, 8))
        self.add_line('roof-2', (31, 8), (44, 24))
        self.add_line('roof-3', (44, 24), (44, 35))
        self.add_line('roof-4', (44, 35), (39, 35))
        self.add_contour('shell', 'body-1', 'body-2', 'roof-turn', 'roof-1', 'roof-2', 'roof-3', 'roof-4', closed=False)
        self.add_arc('wheel-left-top', (9, 35), (19, 35), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('wheel-left-bottom', (19, 35), (9, 35), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('wheel-left', 'wheel-left-top', 'wheel-left-bottom', closed=True)
        self.add_arc('wheel-right-top', (29, 35), (39, 35), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('wheel-right-bottom', (39, 35), (29, 35), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('wheel-right', 'wheel-right-top', 'wheel-right-bottom', closed=True)
        self.relate("connect", 'shell', 'wheel-left')
        self.relate("connect", 'shell', 'wheel-right')
        self.add_line('sill', (19, 35), (29, 35))
        self.relate("connect", 'sill', 'wheel-left')
        self.relate("connect", 'sill', 'wheel-right')
        self.add_line('window', (13, 20), (22, 20))
        self.add_line('windscreen-1', (31, 8), (31, 24))
        self.add_line('windscreen-2', (31, 24), (44, 24))
        self.add_contour('windscreen', 'windscreen-1', 'windscreen-2', closed=False)
        self.relate("connect", 'windscreen', 'shell')
