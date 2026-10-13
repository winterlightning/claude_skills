"""Independent 32px profile of lab-flask-experiment-science.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '29b5cc6d-0003-4008-aefc-58305cb4d79f'
SOURCE_PATH = 'pictographic-primitives/science/lab flask experiment_29b5cc6d-0003-4008-aefc-58305cb4d79f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('29b5cc6d-0003-4008-aefc-58305cb4d79f', 'pictographic-primitives/science/lab flask experiment_29b5cc6d-0003-4008-aefc-58305cb4d79f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/lab-flask-experiment-science',)
SOLO_SOURCE_ICON_IDS = ('lab-flask-experiment-science',)
REFERENCE_EXPORT_SHA256 = 'a7804f8928e3355216fab37ef608b0b62b7975848ef0d27e353d308545abd057'

class DrawingContainerSymbol(Sub32):
    icon_id = 'lab-flask-experiment-science-sub32-symbol'
    related_origin_icon_id = 'lab-flask-experiment-science-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/lab-flask-experiment-science-sub32'
    counterpart_icon_id = 'lab-flask-experiment-science-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'science'
    categories = ('science', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Lab flask: neck widening to a flat-bottomed body, a straight liquid line.
        self.add_polyline('flask', (12, 2), (12, 12), (4, 28), (4, 30), (28, 30), (28, 28), (20, 12), (20, 2), closed=True)
        self.add_line('liquid', (8, 20), (24, 20))
        self.relate('connect', 'flask', 'liquid')
