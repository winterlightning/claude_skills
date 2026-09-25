# Variant of prohibition-sign-sub32; parent file remains unchanged.
"""Independent 32px profile of prohibition-sign-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9d7e100f-bbce-49f1-a485-175de3295e3d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/cancel_9d7e100f-bbce-49f1-a485-175de3295e3d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ea16df49-fc08-4bf0-8bb3-41d6a1fb33cf', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/prohitbition_ea16df49-fc08-4bf0-8bb3-41d6a1fb33cf.svg'), ('9d7e100f-bbce-49f1-a485-175de3295e3d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/cancel_9d7e100f-bbce-49f1-a485-175de3295e3d.svg'))
PROFILE_SOURCE_KEYS = ('solo/prohibition-sign-solo',)
SOLO_SOURCE_ICON_IDS = ('prohibition-sign-solo',)
REFERENCE_EXPORT_SHA256 = '23c54c8a7a1e6e82d73a8021292de19b8e794ebb3f94431efc854dd701fcc733'

class DrawingVariant2(Sub32):
    icon_id = 'prohibition-sign-sub32-v2'
    variant_of = 'prohibition-sign-sub32'
    variant_label = 'True circular outline'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # True circle centered (16,16), radius14; exact 45-degree rising slash.
        # Slash ends overlap the circle's painted band, without distorting it.
        self.add_arc('circle-top',(2,16),(30,16),radius_x=14)
        self.add_arc('circle-bottom',(30,16),(2,16),radius_x=14)
        self.add_contour('circle','circle-top','circle-bottom',closed=True)
        self.add_line('slash',(7,25),(25,7))
        self.relate('connect','circle','slash')
