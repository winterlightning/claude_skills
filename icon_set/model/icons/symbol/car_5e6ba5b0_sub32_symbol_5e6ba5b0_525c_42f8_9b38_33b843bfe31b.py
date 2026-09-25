"""Independent 32px profile of car-5e6ba5b0.
Reauthored from the requested reference for SYMBOL32; see construction plan.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32
SOURCE_ICON_ID = '5e6ba5b0-525c-42f8-9b38-33b843bfe31b'
SOURCE_PATH = 'pictographic-primitives/transportation/car_5e6ba5b0-525c-42f8-9b38-33b843bfe31b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5e6ba5b0-525c-42f8-9b38-33b843bfe31b', 'pictographic-primitives/transportation/car_5e6ba5b0-525c-42f8-9b38-33b843bfe31b.svg'), ('796e3289-99b8-4ef8-bce0-4e8fa2bfefc8', 'pictographic-primitives/transportation/car_796e3289-99b8-4ef8-bce0-4e8fa2bfefc8.svg'), ('eaa7f06c-57de-4d21-aaa7-d89d24b33193', 'pictographic-primitives/transportation/car_eaa7f06c-57de-4d21-aaa7-d89d24b33193.svg'), ('edd4874e-4e76-4ead-a51d-24426b253623', 'pictographic-primitives/transportation/car_edd4874e-4e76-4ead-a51d-24426b253623.svg'))
PROFILE_SOURCE_KEYS = ('solo/car-5e6ba5b0', 'solo/car-796e3289', 'solo/car-eaa7f06c', 'solo/car-edd4874e')
SOLO_SOURCE_ICON_IDS = ('car-5e6ba5b0', 'car-796e3289', 'car-eaa7f06c', 'car-edd4874e')
REFERENCE_EXPORT_SHA256 = '74c0ff8439a2ad60f72d38cffa5d6783aeb36217329f66101bd7a6a604bc8cf1'

class DrawingContainerSymbol(Symbol32):
    icon_id = 'car-5e6ba5b0-sub32-symbol'
    related_origin_icon_id = 'car-5e6ba5b0-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/car-5e6ba5b0-sub32'
    counterpart_icon_id = 'car-5e6ba5b0-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Plan: one rounded sedan body and two equal detached wheel marks.
        # Lucide car informs the stepped roof/hood silhouette and wheel series.
        # Centerline bounds (2,4)-(30,28). At 32px omit window divisions and
        # hollow wheel centers, retaining a readable body-to-wheel ink gap.
        axis, wheel_y, wheel_offset = 16, 28, 8
        points = [(4, 20), (2, 18), (2, 14), (4, 12), (6, 12),
                  (10, 4), (18, 4), (24, 12), (28, 12), (30, 14),
                  (30, 18), (28, 20)]
        corners = {0, 2, 8, 10}
        members = []
        for index, start in enumerate(points):
            end = points[(index+1) % len(points)]
            name = f'body-{index}'
            if index in corners:
                self.add_arc(name, start, end, radius_x=2)
            else:
                self.add_line(name, start, end)
            members.append(name)
        self.add_contour('body', *members, closed=True)
        for side in (-1, 1):
            self.add_dot(f'wheel-{side}', (axis + side*wheel_offset, wheel_y))
