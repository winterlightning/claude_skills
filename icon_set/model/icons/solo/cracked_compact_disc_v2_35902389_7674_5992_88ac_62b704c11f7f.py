# Variant of cracked-compact-disc; parent file remains unchanged.
'Wider crack opening. Independent feedback revision; preserve source subject.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '35902389-7674-5992-88ac-62b704c11f7f'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/cd broken_35902389-7674-5992-88ac-62b704c11f7f.svg'
AUTHOR = 'gpt-6'

class CrackedCompactDiscVariant2(Solo48):
    icon_id = 'cracked-compact-disc-v2'
    variant_of = 'cracked-compact-disc'
    variant_label = 'Wider crack opening'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('cd', 'disc', 'broken', 'cracked', 'damaged', 'media', 'storage', 'error', 'disk')

    def build(self) -> None:
        self.add_arc('rim-upper-left', (12, 10), (2, 24), radius_x=10, radius_y=14, sweep=False, large_arc=False)
        self.add_arc('rim-lower-left', (2, 24), (24, 46), radius_x=22, radius_y=22, sweep=False, large_arc=False)
        self.add_arc('rim-lower-right', (24, 46), (46, 24), radius_x=22, radius_y=22, sweep=False, large_arc=False)
        self.add_arc('rim-upper-right', (46, 24), (24, 2), radius_x=22, radius_y=22, sweep=False, large_arc=False)
        self.add_contour('rim', 'rim-upper-left', 'rim-lower-left', 'rim-lower-right', 'rim-upper-right', closed=False)
        self.add_polyline('crack', (24, 2), (16, 18), (29, 18), (18, 34), closed=False)
        self.relate('connect', 'rim', 'crack')
