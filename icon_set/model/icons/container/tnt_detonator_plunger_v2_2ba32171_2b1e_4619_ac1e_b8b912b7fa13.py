"""A T-handle detonator box with an attached looping cable.

SQUARE: ink (0,0)-(64,64), centerlines (2,2)-(62,62).
Lucide monitor original and atomic-debug informed consistent quarter-circle
box corners and a centered post. No direct detonator reference was found.
The source's T plunger, box and cable remain. The wider cable loop has tangent
joins; intentional right-side asymmetry follows the source.
Hosting (compose.py): plus blocked; heart valid; check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '2ba32171-2b1e-4619-ac1e-b8b912b7fa13'
SOURCE_PATH = 'container_icons/svg/tnt-detonator-plunger-2ba32171-2b1e-4619-ac1e-b8b912b7fa13.svg'
AUTHOR = 'gpt-6'


class TntDetonatorPlungerVariant2(Container64):
    icon_id = 'tnt-detonator-plunger-v2'
    variant_of = 'tnt-detonator-plunger'
    variant_label = 'Wider cable loop and balanced plunger'
    keyshape = Keyshape.SQUARE
    category = 'containers'
    aliases = ()
    keywords = ('tnt', 'detonator', 'plunger', 'explosive')

    def build(self):
        # Plan: rounded box owns its centered plunger and cable attachment;
        # one continuous cable has quarter turns and one semicircular crest.
        left, right, top, bottom, radius, axis = 2, 38, 24, 62, 6, 20
        self.add_line('box-top', (left+radius,top), (right-radius,top))
        self.add_arc('box-ne', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('box-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('box-se', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('box-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('box-sw', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('box-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('box-nw', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('box', 'box-top', 'box-ne', 'box-right', 'box-se',
                         'box-bottom', 'box-sw', 'box-left', 'box-nw', closed=True)
        self.add_line('plunger', (axis,2), (axis,top))
        self.add_line('handle', (axis-12,2), (axis+12,2))
        self.relate('connect', 'handle', 'plunger')
        self.relate('connect', 'plunger', 'box')
        self.add_arc('wire-out', (right,50), (46,42), radius_x=8, sweep=False)
        self.add_line('wire-rise', (46,42), (46,36))
        self.add_arc('wire-crest', (46,36), (58,36), radius_x=6)
        self.add_line('wire-fall', (58,36), (58,58))
        self.add_arc('wire-foot', (58,58), (62,62), radius_x=4, sweep=False)
        self.add_contour('wire', 'wire-out', 'wire-rise', 'wire-crest', 'wire-fall', 'wire-foot')
        self.relate('connect', 'wire', 'box')
