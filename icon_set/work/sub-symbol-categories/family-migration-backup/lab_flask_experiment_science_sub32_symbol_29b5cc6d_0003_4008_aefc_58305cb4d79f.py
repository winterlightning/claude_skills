# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of lab-flask-experiment-science.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '29b5cc6d-0003-4008-aefc-58305cb4d79f'
SOURCE_PATH = 'pictographic-primitives/science/lab flask experiment_29b5cc6d-0003-4008-aefc-58305cb4d79f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('29b5cc6d-0003-4008-aefc-58305cb4d79f', 'pictographic-primitives/science/lab flask experiment_29b5cc6d-0003-4008-aefc-58305cb4d79f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/lab-flask-experiment-science',)
SOLO_SOURCE_ICON_IDS = ('lab-flask-experiment-science',)
REFERENCE_EXPORT_SHA256 = 'a7804f8928e3355216fab37ef608b0b62b7975848ef0d27e353d308545abd057'

class DrawingContainerSymbol(Sub32):
    icon_id = 'lab-flask-experiment-science-sub32-symbol'
    variant_of = 'lab-flask-experiment-science-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/lab-flask-experiment-science-sub32'
    counterpart_icon_id = 'lab-flask-experiment-science-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'science'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (20, 2))
        self.add_line('p1-r1-2', (20, 2), (20, 13))
        self.add_bezier('p1-r1-3', (20, 13), ((20, 15), (27, 15), (27, 22)))
        self.add_arc('p1-r1-4', (27, 22), (19, 30), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (19, 30), (13, 30))
        self.add_arc('p1-r1-6', (13, 30), (5, 22), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-7', (5, 22), ((5, 15), (12, 15), (12, 13)))
        self.add_line('p1-r1-8', (12, 13), (12, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_bezier('p2-r1-1', (5, 22), ((6, 21), (7, 20), (8, 20)))
        self.add_bezier('p2-r1-2', (8, 20), ((10, 20), (11, 23), (13, 23)))
        self.add_bezier('p2-r1-3', (13, 23), ((14, 23), (15, 22), (16, 22)))
        self.add_bezier('p2-r1-4', (16, 22), ((17, 21), (18, 20), (19, 20)))
        self.add_bezier('p2-r1-5', (19, 20), ((21, 20), (22, 23), (24, 23)))
        self.add_bezier('p2-r1-6', (24, 23), ((25, 23), (26, 22), (27, 22)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-6')
        self.relate('connect', 'p1-r1-4', 'p2-r1-6')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
