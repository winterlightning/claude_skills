"""Independent 32px profile of shield.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0fa98a0f-6de4-4ade-b905-178ec453bc23'
SOURCE_PATH = 'pictographic-primitives/protection/shield_0fa98a0f-6de4-4ade-b905-178ec453bc23.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0fa98a0f-6de4-4ade-b905-178ec453bc23', 'pictographic-primitives/protection/shield_0fa98a0f-6de4-4ade-b905-178ec453bc23.svg'), ('8e1100ca-39fe-4e71-b978-93997ec5e7d8', 'pictographic-primitives/protection/shield_8e1100ca-39fe-4e71-b978-93997ec5e7d8.svg'), ('ba7b0c51-fe87-48cd-a5c0-eea81086a3a9', 'pictographic-primitives/protection/shield_ba7b0c51-fe87-48cd-a5c0-eea81086a3a9.svg'), ('ee28756e-a560-4166-b776-2aebcbfcabaa', 'pictographic-primitives/protection/shield_ee28756e-a560-4166-b776-2aebcbfcabaa.svg'))
PROFILE_SOURCE_KEYS = ('solo/shield', 'solo/shield-8e1100ca', 'solo/shield-ba7b0c51', 'solo/shield-ee28756e')
SOLO_SOURCE_ICON_IDS = ('shield', 'shield-8e1100ca', 'shield-ba7b0c51', 'shield-ee28756e')
REFERENCE_EXPORT_SHA256 = '764b4ffc339d83132ae16c761a39500cf8cd920b49f9ed3a98e90510c1b8d4d8'

class DrawingContainerSymbol(Sub32):
    icon_id = 'shield-sub32-symbol'
    related_origin_icon_id = 'shield-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/shield-sub32'
    counterpart_icon_id = 'shield-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 6), (27, 6), radius_x=11, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (27, 6), (27, 13))
        self.add_arc('p1-r1-3', (27, 13), (16, 30), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 30), (5, 13), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (5, 13), (5, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
