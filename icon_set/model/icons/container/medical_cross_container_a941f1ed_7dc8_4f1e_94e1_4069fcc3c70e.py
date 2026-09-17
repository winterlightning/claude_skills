"""Medical Cross Symbol: independently authored container.

Construction plan: Single equal-armed cross outline with arm width twenty; mirror both axes.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/health/cross_a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e.svg. Lucide cross original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e'
SOURCE_PATH = 'pictographic-primitives/health/cross_a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e.svg'
AUTHOR = 'gpt-6'


class MedicalCrossContainer(Container64):
    icon_id = 'medical-cross-container'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('medical', 'cross', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        poly('cross',(22,2),(42,2),(42,22),(62,22),(62,42),(42,42),(42,62),(22,62),(22,42),(2,42),(2,22),(22,22),closed=True)
