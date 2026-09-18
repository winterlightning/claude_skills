"""Independent 32px profile of wifi.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9c4f27d2-9a43-4e9d-867c-e102edd9f1b9'
SOURCE_PATH = 'pictographic-primitives/networks/wifi_9c4f27d2-9a43-4e9d-867c-e102edd9f1b9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9c4f27d2-9a43-4e9d-867c-e102edd9f1b9', 'pictographic-primitives/networks/wifi_9c4f27d2-9a43-4e9d-867c-e102edd9f1b9.svg'), ('b2468acd-4b50-4a65-911c-aee5076b1c7e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/electric waves_b2468acd-4b50-4a65-911c-aee5076b1c7e.svg'), ('f683dd0c-b161-414e-8816-ecfc56a54c18', 'pictographic-primitives/networks/wifi_f683dd0c-b161-414e-8816-ecfc56a54c18.svg'))
PROFILE_SOURCE_KEYS = ('solo/wifi', 'solo/wifi-f683dd0c')
SOLO_SOURCE_ICON_IDS = ('wifi', 'wifi-f683dd0c')
REFERENCE_EXPORT_SHA256 = '08e98cce167e74f1102bdab222a8ad6789a52d4b398fb8ced78a386741f8f524'

class Drawing(Sub32):
    icon_id = 'wifi-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'networks'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 11), ((7, 7), (10, 5), (16, 5)))
        self.add_bezier('p1-r1-2', (16, 5), ((22, 5), (25, 7), (30, 11)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (9, 18), ((11, 16), (13, 15), (16, 15)))
        self.add_bezier('p2-r1-2', (16, 15), ((19, 15), (21, 16), (23, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 27), (16, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
