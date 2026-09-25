"""Braille Alphabet Dot Pattern.
Symbol plan: Two columns of three dots on shared row positions; visible bounds (8,2)-(40,46).
Construction: Lucide battery for tangent rounded rectangles; shared human reference for people.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import rounded_rect, circle
SOURCE_ICON_ID = '9a878067-c24e-4478-bd0a-a0a8e12afcc0'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/9a878067-c24e-4478-bd0a-a0a8e12afcc0.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'braille-six-dot-cell'
    keyshape = Keyshape.VRECT_M
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('braille alphabet dot pattern',)
    def build(self):
        for column,x in enumerate((10,38)):
            for row,y in enumerate((4,24,44)):
                self.add_dot(f'dot-{column}-{row}',(x,y))
