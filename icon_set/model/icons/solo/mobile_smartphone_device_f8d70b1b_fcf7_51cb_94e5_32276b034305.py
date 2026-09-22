"""Mobile Smartphone Device: standalone SOLO48 reconstruction.
Source render supplies essential parts and arrangement. Lucide construction
reference and ownership plan are recorded in build. Original artwork preserved.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from ._symmetry_curves import path, ellipse, box, contacts
SOURCE_ICON_ID = 'f8d70b1b-fcf7-51cb-94e5-32276b034305'
SOURCE_PATH = 'pictographic-primitives/devices/screen_f8d70b1b-fcf7-51cb-94e5-32276b034305.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-smartphone-device-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ('Mobile Smartphone Device',)
    keywords = ('mobile', 'smartphone', 'device')
    def build(self):
        # Symmetric rounded shell owns divider and centered home mark.
        # VRECT_M supplies phone proportions; Lucide smartphone teaches corner flow.
        box(self,'shell',10,4,38,44,4,ys=(26,))
        self.add_line('bezel',(10,26),(38,26))
        self.relate('connect','shell','bezel')
        self.add_line('home',(22,35),(26,35))
