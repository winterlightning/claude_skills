"""Independent 32px profile of chart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e6769cc6-7edd-4638-9a68-d793ea0c3ccc'
SOURCE_PATH = 'pictographic-primitives/symbol/chart_e6769cc6-7edd-4638-9a68-d793ea0c3ccc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e6769cc6-7edd-4638-9a68-d793ea0c3ccc', 'pictographic-primitives/symbol/chart_e6769cc6-7edd-4638-9a68-d793ea0c3ccc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chart',)
SOLO_SOURCE_ICON_IDS = ('chart',)
REFERENCE_EXPORT_SHA256 = '6b4b517380ad3f8457c9b855151dcd5b641a872d0739fb5e778502b6bf0c99e4'

class Drawing(Sub32):
    icon_id = 'chart-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 24), ((6, 24), (4, 6), (8, 6)))
        self.add_bezier('p1-r1-2', (8, 6), ((12, 6), (10, 27), (15, 27)))
        self.add_bezier('p1-r1-3', (15, 27), ((19, 27), (17, 5), (22, 5)))
        self.add_bezier('p1-r1-4', (22, 5), ((26, 5), (24, 26), (30, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
