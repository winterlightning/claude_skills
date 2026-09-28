"""Pull Down Projection Screen: independently authored container.

Construction plan: A hanging rectangular screen with extended top rail and central pull ring. Calendar informs straight header construction.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/office/presentation_17f53de2-7f28-4023-80ae-484c48ce0e0e.svg. Lucide calendar original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '17f53de2-7f28-4023-80ae-484c48ce0e0e'
SOURCE_PATH = 'pictographic-primitives/office/presentation_17f53de2-7f28-4023-80ae-484c48ce0e0e.svg'
AUTHOR = 'gpt-6'


class PullDownProjectionScreen(Container64):
    icon_id = 'pull-down-projection-screen'
    category = 'office'
    categories = ('office', 'other', 'primitives-generate')
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('pull', 'down', 'projection', 'screen')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'screen',(6,2),[('L',(6,44)),('A',(10,48),4,4,False),('L',(54,48)),('A',(58,44),4,4,False),('L',(58,2))])
        line('rail',(2,2),(62,2));join('screen','rail')
        line('pull',(32,48),(32,54));join('pull','screen')
        ellipse(self,'ring',32,58,4);join('pull','ring')
