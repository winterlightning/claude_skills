# Variant of eye; parent file remains unchanged.
"""Eye: Two broad curved eyelids meet at pointed left and right corners to form a horizontal almond outline. A tiny central dot appears inside, without a visible iris ring.

Construction: Eye envelope is two mirrored shallow elliptical arcs meeting at pointed canthi; centre dot preserves the source pupil.
Keyshape: HRECT_L; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4fe0ffe1-6a10-4f5e-96f8-3d6033f13623'
SOURCE_PATH = 'pictographic-primitives/state/eye 1_4fe0ffe1-6a10-4f5e-96f8-3d6033f13623.svg'
AUTHOR = 'gpt-6'

class EyeVariant2(Sub32):
    icon_id = 'eye-v2'
    variant_of = 'eye'
    variant_label = 'Almond outline'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('eye', 'broad', 'curved', 'eyelids', 'meet', 'pointed', 'left', 'right')

    def build(self):
        self.add_arc('upper', (2, 16), (30, 16), radius_x=50, radius_y=250)
        self.add_arc('lower', (30, 16), (2, 16), radius_x=50, radius_y=250)
        self.add_contour('outline', 'upper', 'lower', closed=True)
        self.add_dot('pupil', (16, 16))
