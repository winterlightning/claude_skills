"""Portrait Handheld Tablet: standalone SOLO48 reconstruction.
Source render supplies essential parts and arrangement. Lucide construction
reference and ownership plan are recorded in build. Original artwork preserved.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from ._symmetry_curves import path, ellipse, box, contacts
SOURCE_ICON_ID = '56184363-0fa8-5bb5-bae5-239ae516f66d'
SOURCE_PATH = 'pictographic-primitives/devices/tablet_56184363-0fa8-5bb5-bae5-239ae516f66d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'portrait-handheld-tablet-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ('Portrait Handheld Tablet',)
    keywords = ('portrait', 'handheld', 'tablet')
    def build(self):
        # Wider VRECT_L shell distinguishes tablet from phone; no home mark in source.
        # Lucide smartphone provides tangent quarter-circle corner construction.
        box(self,'shell',8,4,40,44,4,ys=(34,))
        self.add_line('bezel',(8,34),(40,34))
        self.relate('connect','shell','bezel')
