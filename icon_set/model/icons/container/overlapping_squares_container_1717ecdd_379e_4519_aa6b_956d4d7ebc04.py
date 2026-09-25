"""Overlapping Rounded Squares: independently authored container.

Construction plan: Front rounded square occludes the rear outline; retain offset and equal proportions.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/interface-essential/duplicate_1717ecdd-379e-4519-aa6b-956d4d7ebc04.svg. Lucide squares-exclude original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '1717ecdd-379e-4519-aa6b-956d4d7ebc04'
SOURCE_PATH = 'pictographic-primitives/interface-essential/duplicate_1717ecdd-379e-4519-aa6b-956d4d7ebc04.svg'
AUTHOR = 'gpt-6'


class OverlappingSquaresContainer(Container64):
    icon_id = 'overlapping-squares-container'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('overlapping', 'squares', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        rect(self,'front',2,2,46,46,4)
        path(self,'rear',(46,18),[('L',(58,18)),('A',(62,22),4,4,True),('L',(62,58)),('A',(58,62),4,4,True),('L',(22,62)),('A',(18,58),4,4,True),('L',(18,46))])
        join('front','rear')
