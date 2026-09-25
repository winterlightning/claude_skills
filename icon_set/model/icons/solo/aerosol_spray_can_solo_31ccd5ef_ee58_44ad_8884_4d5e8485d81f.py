"""Aerosol Spray Can. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
Preserve aerosol body and nozzle; atomized spray omitted at native size.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '31ccd5ef-ee58-44ad-8884-4d5e8485d81f'
SOURCE_PATH = 'pictographic-primitives/other/spray can_31ccd5ef-ee58-44ad-8884-4d5e8485d81f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'aerosol-spray-can-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'aerosol spray can')
    def build(self):
        rounded_rect(self,'can',6,16,28,42,4)
        self.add_polyline('nozzle',(12,16),(12,6),(22,6),(22,16))
        self.relate('connect','nozzle','can')
        self.add_line('spray-top',(36,9),(42,6))
        self.add_line('spray-bottom',(36,17),(42,20))
