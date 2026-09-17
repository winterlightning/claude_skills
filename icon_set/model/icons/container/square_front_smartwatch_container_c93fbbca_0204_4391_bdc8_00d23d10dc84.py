"""Square Digital Smart Watch: independently authored container.

Construction plan: Front rounded-square watch face between equal strap ends; no hands absent from source.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/devices/smart watch square_c93fbbca-0204-4391-bdc8-00d23d10dc84.svg. Lucide watch original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'c93fbbca-0204-4391-bdc8-00d23d10dc84'
SOURCE_PATH = 'pictographic-primitives/devices/smart watch square_c93fbbca-0204-4391-bdc8-00d23d10dc84.svg'
AUTHOR = 'gpt-6'


class SquareFrontSmartwatchContainer(Container64):
    icon_id = 'square-front-smartwatch-container'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('square', 'front', 'smartwatch', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        rect(self,'face',10,14,54,50,6)
        poly('top-strap',(20,14),(22,2),(42,2),(44,14));join('face','top-strap')
        poly('bottom-strap',(20,50),(22,62),(42,62),(44,50));join('face','bottom-strap')
