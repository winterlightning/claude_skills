'Three repeated binder spines. HRECT_L uses all 40 horizontal centerline units: three 8-wide spines separated by 8. Lucide library teaches repeated upright book contours. Labels and finger holes cannot fit: even a dot needs 16-wide spine, circle hole needs 20; three require 64 or 76 units including gaps, exceeding upright and diagonal span. Candidate is pending visual identity review.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '42cdb953-b64a-446a-9e2f-0a5e1116e601'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/archive books_42cdb953-b64a-446a-9e2f-0a5e1116e601.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'three-labeled-ring-binders'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ['Three Office Ring Binders']
    keywords = ['binders', 'spines', 'labels', 'holes', 'office', 'archive', 'files']
    def build(self):
        for j in range(3):
            left=4+16*j
            self.add_polyline(f'spine-{j}',(left,8),(left+8,8),(left+8,40),(left,40),closed=True)
