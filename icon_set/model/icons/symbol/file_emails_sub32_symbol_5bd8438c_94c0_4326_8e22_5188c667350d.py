"""Independent 32px profile of file-emails.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5bd8438c-94c0-4326-8e22-5188c667350d'
SOURCE_PATH = 'pictographic-primitives/emails/file_5bd8438c-94c0-4326-8e22-5188c667350d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5bd8438c-94c0-4326-8e22-5188c667350d', 'pictographic-primitives/emails/file_5bd8438c-94c0-4326-8e22-5188c667350d.svg'), ('ee647811-20d2-4d87-9000-0d11db8aa255', 'pictographic-primitives/files/document_ee647811-20d2-4d87-9000-0d11db8aa255.svg'))
PROFILE_SOURCE_KEYS = ('solo/file-emails', 'solo/document-files')
SOLO_SOURCE_ICON_IDS = ('file-emails', 'document-files')
REFERENCE_EXPORT_SHA256 = '69667b7d09f1c2eb89fdde47e5fed35df35e783a156002aaee93d6d92a54cf6e'

class DrawingContainerSymbol(Sub32):
    icon_id = 'file-emails-sub32-symbol'
    related_origin_icon_id = 'file-emails-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/file-emails-sub32'
    counterpart_icon_id = 'file-emails-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'emails'
    categories = ('emails', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 13), (21, 13))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (11, 20), (21, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 2), (22, 2))
        self.add_line('p3-r1-2', (22, 2), (27, 8))
        self.add_line('p3-r1-3', (27, 8), (27, 30))
        self.add_line('p3-r1-4', (27, 30), (5, 30))
        self.add_line('p3-r1-5', (5, 30), (5, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
