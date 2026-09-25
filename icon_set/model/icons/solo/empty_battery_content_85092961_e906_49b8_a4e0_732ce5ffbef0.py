"""Empty Battery Symbol.
Symbol plan: Rounded body and detached terminal; visible bounds (2,8)-(46,40). Terminal shape simplified to Lucide-style stroke.
Construction: Lucide battery for tangent rounded rectangles; shared human reference for people.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import rounded_rect, circle
SOURCE_ICON_ID = '85092961-e906-49b8-a4e0-732ce5ffbef0'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/85092961-e906-49b8-a4e0-732ce5ffbef0.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'empty-battery-content'
    keyshape = Keyshape.HRECT_M
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('empty battery symbol',)
    def build(self):
        rounded_rect(self,'body',4,10,35,38,4)
        self.add_line('terminal',(44,18),(44,30))
