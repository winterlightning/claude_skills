"""Independent 32px profile of mail.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '75ad5383-92bd-435c-984f-c475f5f845c1'
SOURCE_PATH = 'pictographic-primitives/symbol/mail_75ad5383-92bd-435c-984f-c475f5f845c1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('75ad5383-92bd-435c-984f-c475f5f845c1', 'pictographic-primitives/symbol/mail_75ad5383-92bd-435c-984f-c475f5f845c1.svg'), ('19aca772-9076-4cc0-8470-0cdffef95def', 'pictographic-primitives/symbol/e mail_19aca772-9076-4cc0-8470-0cdffef95def.svg'), ('a6d5c36b-5f72-4bbf-a205-b2d56aaf29a5', 'pictographic-primitives/symbol/mail_a6d5c36b-5f72-4bbf-a205-b2d56aaf29a5.svg'), ('2a98051e-e248-4ae8-8a84-a56070dcb2ad', 'pictographic-primitives/symbol/page mail_2a98051e-e248-4ae8-8a84-a56070dcb2ad.svg'))
PROFILE_SOURCE_KEYS = ('solo/mail', 'solo/e-mail', 'solo/mail-symbol', 'solo/page-mail')
SOLO_SOURCE_ICON_IDS = ('mail', 'e-mail', 'mail-symbol', 'page-mail')
REFERENCE_EXPORT_SHA256 = '9e2c67811a8f83e9c1036555c0f9612b42e7aa6d06c6eab13201a553c08ff94d'

class DrawingContainerSymbol(Sub32):
    icon_id = 'mail-sub32-symbol'
    related_origin_icon_id = 'mail-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/mail-sub32'
    counterpart_icon_id = 'mail-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Mail: envelope with a V flap from the top corners.
        self.add_polyline('envelope', (2, 4), (30, 4), (30, 28), (2, 28), closed=True)
        self.add_polyline('flap', (2, 4), (16, 16), (30, 4))
        self.relate('connect', 'envelope', 'flap')
