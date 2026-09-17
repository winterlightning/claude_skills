"""Open Book: independently authored container.

Construction plan: Two mirrored bowed page leaves sharing a central spine; preserve open book without text.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/content/book open 1_1d780c55-d1d8-4fad-9a0c-5cfd553331a0.svg. Lucide book-open original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '1d780c55-d1d8-4fad-9a0c-5cfd553331a0'
SOURCE_PATH = 'pictographic-primitives/content/book open 1_1d780c55-d1d8-4fad-9a0c-5cfd553331a0.svg'
AUTHOR = 'gpt-6'


class OpenBookContainer(Container64):
    icon_id = 'open-book-container'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ('open', 'book', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'outline',(2,6),[('A',(32,14),30,8,True),('A',(62,6),30,8,True),('L',(62,50)),('A',(32,58),30,8,False),('A',(2,50),30,8,False),('L',(2,6))],True)
        line('spine',(32,14),(32,58));join('spine','outline')
