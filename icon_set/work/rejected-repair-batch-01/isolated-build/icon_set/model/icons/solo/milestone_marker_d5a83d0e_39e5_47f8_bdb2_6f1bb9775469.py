'A short upright milestone has a semicircular cap above a straight-sided rectangular body. A horizontal seam marks the cap, and a wider low plinth supports the base.\n\nConstruction: Semicircular cap, upright marker body and broad plinth. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd5a83d0e-39e5-47f8-bdb2-6f1bb9775469'
SOURCE_PATH = 'pictographic-primitives/wayfinding/milestone 1_d5a83d0e-39e5-47f8-bdb2-6f1bb9775469.svg'
AUTHOR = 'gpt-6'

class MilestoneMarker(Solo48):
    icon_id = 'milestone-marker'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('milestone', 'marker', 'road', 'stone', 'distance', 'wayfinding')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('cap', (12, 16), (36, 16), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('body-1', (36, 16), (36, 36))
        self.add_line('body-2', (36, 36), (12, 36))
        self.add_line('body-3', (12, 36), (12, 16))
        self.add_line('cap-seam', (12, 16), (36, 16))
        self.add_line('plinth-1', (12, 36), (8, 36))
        self.add_line('plinth-2', (8, 36), (8, 44))
        self.add_line('plinth-3', (8, 44), (40, 44))
        self.add_line('plinth-4', (40, 44), (40, 36))
        self.add_line('plinth-5', (40, 36), (36, 36))
        self.add_contour('marker', 'cap', 'body-1', 'body-2', 'body-3', closed=True)
        self.add_contour('plinth', 'plinth-1', 'plinth-2', 'plinth-3', 'plinth-4', 'plinth-5', closed=False)
        self.relate('connect', 'cap-seam', 'marker')
        self.relate('connect', 'plinth', 'marker')
