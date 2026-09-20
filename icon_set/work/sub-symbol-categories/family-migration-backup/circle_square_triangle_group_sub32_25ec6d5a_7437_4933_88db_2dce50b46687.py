"""Independent 32px profile of circle-square-triangle-group.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '25ec6d5a-7437-4933-88db-2dce50b46687'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/shapes_25ec6d5a-7437-4933-88db-2dce50b46687.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('25ec6d5a-7437-4933-88db-2dce50b46687', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/shapes_25ec6d5a-7437-4933-88db-2dce50b46687.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-square-triangle-group',)
SOLO_SOURCE_ICON_IDS = ('circle-square-triangle-group',)
REFERENCE_EXPORT_SHA256 = 'b257f798e94f3c1ea1d428169fc7e4c6685b6709689bdf1268000e79525568ce'

class Drawing(Sub32):
    icon_id = 'circle-square-triangle-group-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 9), (30, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 9), (16, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 16), (11, 16))
        self.add_line('p2-r1-2', (11, 16), (11, 25))
        self.add_line('p2-r1-3', (11, 25), (2, 25))
        self.add_line('p2-r1-4', (2, 25), (2, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (23, 22), (30, 30))
        self.add_line('p3-r1-2', (30, 30), (16, 30))
        self.add_line('p3-r1-3', (16, 30), (23, 22))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
