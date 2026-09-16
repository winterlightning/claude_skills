# Variant of tnt-detonator-plunger-v2; parent file remains unchanged.
'A detonator with a larger empty box and open cable loop.\n\nSQUARE: ink (0,0)-(64,64). Box centerlines (2,16)-(40,62),\nup from (2,24)-(38,62): clear straight interior grows from 32x34 to 34x42.\nCable-to-box centerline spacing grows from 8 to 10; loop width remains 12.\nLucide monitor original and atomic-debug informed the rounded box and centered\npost. The source supplies the T handle and asymmetric cable. The final cable\nfoot is omitted, leaving a simple round-ended descent and more room for the box.\nSymbol plan: box owns the centered plunger and wire attachment; wire turns\nshare endpoints and tangents. Parent remains unchanged.\nHosting (compose.py): plus valid; heart valid; check valid.\n'
from ...keyshapes import Keyshape
from ._base import Container64
SOURCE_ICON_ID = '2ba32171-2b1e-4619-ac1e-b8b912b7fa13'
SOURCE_PATH = 'container_icons/svg/tnt-detonator-plunger-2ba32171-2b1e-4619-ac1e-b8b912b7fa13.svg'
AUTHOR = 'gpt-6'

class TntDetonatorPlungerVariant3(Container64):
    icon_id = 'tnt-detonator-plunger-v3'
    variant_of = 'tnt-detonator-plunger-v2'
    variant_label = 'Larger box and more open cable spacing'
    keyshape = Keyshape.SQUARE
    category = 'containers'
    aliases = ()
    keywords = ('tnt', 'detonator', 'plunger', 'explosive')

    def build(self):
        left, right, top, bottom, radius, axis = (2, 40, 16, 62, 6, 21)
        self.add_line('box-top', (left + radius, top), (right - radius, top))
        self.add_arc('box-ne', (right - radius, top), (right, top + radius), radius_x=radius)
        self.add_line('box-right', (right, top + radius), (right, bottom - radius))
        self.add_arc('box-se', (right, bottom - radius), (right - radius, bottom), radius_x=radius)
        self.add_line('box-bottom', (right - radius, bottom), (left + radius, bottom))
        self.add_arc('box-sw', (left + radius, bottom), (left, bottom - radius), radius_x=radius)
        self.add_line('box-left', (left, bottom - radius), (left, top + radius))
        self.add_arc('box-nw', (left, top + radius), (left + radius, top), radius_x=radius)
        self.add_contour('box', 'box-top', 'box-ne', 'box-right', 'box-se', 'box-bottom', 'box-sw', 'box-left', 'box-nw', closed=True)
        self.add_line('plunger', (axis, 2), (axis, top))
        self.add_line('handle', (axis - 12, 2), (axis + 12, 2))
        self.relate('connect', 'handle', 'plunger')
        self.relate('connect', 'plunger', 'box')
        self.add_arc('wire-out', (right, 48), (50, 38), radius_x=10, sweep=False)
        self.add_line('wire-rise', (50, 38), (50, 34))
        self.add_arc('wire-crest', (50, 34), (62, 34), radius_x=6)
        self.add_line('wire-fall', (62, 34), (62, 62))
        self.add_contour('wire', 'wire-out', 'wire-rise', 'wire-crest', 'wire-fall')
        self.relate('connect', 'wire', 'box')
