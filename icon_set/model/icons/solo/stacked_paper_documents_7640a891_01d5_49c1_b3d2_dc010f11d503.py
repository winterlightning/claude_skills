"""Stacked Paper Documents: overlapping clipped-corner pages.
SQUARE envelope (6,6)-(42,42); common eight-unit stack offset.
Source supplies page arrangement; Lucide files supplies interrupted rear contour.
Omit fine edge slivers to keep the rear page separated at native size.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '7640a891-01d5-49c1-b3d2-dc010f11d503'
SOURCE_PATH = 'pictographic-primitives/files/common file stack_7640a891-01d5-49c1-b3d2-dc010f11d503.svg'
AUTHOR = "gpt-6"
class Icon(Solo48):
    icon_id = 'stacked-paper-documents'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "files"
    aliases = ['Stacked Paper Documents']
    keywords = ['stacked', 'paper', 'documents']
    def build(self):
        self.add_polyline("front", (14,6), (32,6), (42,16), (42,34), (14,34), closed=True)
        self.add_polyline("rear", (6,14), (6,42), (34,42))
