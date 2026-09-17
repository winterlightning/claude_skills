"""Dental Floss Container: independently authored container.

Construction plan: Rounded floss case plus a continuous trailing thread on the right; folder informs rounded casing only.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/health/dental floss_2c0bb5cc-c4fc-42a3-9d62-745c7c7e25dc.svg. Lucide folder original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus passes, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '2c0bb5cc-c4fc-42a3-9d62-745c7c7e25dc'
SOURCE_PATH = 'pictographic-primitives/health/dental floss_2c0bb5cc-c4fc-42a3-9d62-745c7c7e25dc.svg'
AUTHOR = 'gpt-6'


class DentalFlossContainerMain(Container64):
    icon_id = 'dental-floss-container-main'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ('dental', 'floss', 'container', 'main')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        rect(self,'case',2,6,44,58,8)
        path(self,'thread',(44,22),[('L',(48,22)),('A',(54,28),6,6,True),('L',(54,54)),('A',(62,54),4,4,False)])
        join('case','thread')
