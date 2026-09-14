'A person kneels facing right and bends over an open toilet bowl. Both arms reach onto the rim, while the head hangs over the bowl beside its tall rear tank.\n\nConstruction: Person bends toward a toilet bowl, one hand touching the rim. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2a8bbde-27d6-42cd-96b8-9da81e48b075'
SOURCE_PATH = 'pictographic-primitives/wayfinding/vomit toilet_a2a8bbde-27d6-42cd-96b8-9da81e48b075.svg'
AUTHOR = 'gpt-6'

class PersonLeaningOverToilet(Solo48):
    icon_id = 'person-leaning-over-toilet'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'toilet', 'vomiting', 'kneeling', 'bathroom', 'illness')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (20, 11), (26, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (26, 11), (20, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-back-1', (16, 23), (10, 29))
        self.add_line('person-back-2', (10, 29), (16, 40))
        self.add_line('person-back-3', (16, 40), (4, 40))
        self.add_line('person-arm-1', (16, 23), (24, 28))
        self.add_line('person-arm-2', (24, 28), (30, 28))
        self.add_line('toilet-1', (30, 28), (34, 28))
        self.add_line('toilet-2', (34, 28), (34, 18))
        self.add_line('toilet-3', (34, 18), (44, 18))
        self.add_line('toilet-4', (44, 18), (44, 40))
        self.add_arc('bowl', (30, 28), (38, 36), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-back', 'person-back-1', 'person-back-2', 'person-back-3', closed=False)
        self.add_contour('person-arm', 'person-arm-1', 'person-arm-2', closed=False)
        self.add_contour('toilet', 'toilet-1', 'toilet-2', 'toilet-3', 'toilet-4', closed=False)
        self.relate('connect', 'person-back', 'person-arm')
        self.relate('connect', 'bowl', 'toilet')
        self.relate('connect', 'person-arm', 'toilet')
