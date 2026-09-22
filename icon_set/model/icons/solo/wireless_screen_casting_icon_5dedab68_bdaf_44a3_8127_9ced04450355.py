"""Screen with a casting triangle below its open lower edge.

HRECT_L gives the screen a wide silhouette. The screen owns one open,
rounded contour; the centered triangle is a closed contour. Mirror all
screen turns about x=24. Source supplies arrangement; Lucide airplay
supplies the uninterrupted rounded screen contour principle. Omit no
identity-bearing parts, simplify the triangle to three straight strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5dedab68-bdaf-44a3-8127-9ced04450355'
SOURCE_PATH = 'pictographic-primitives/devices/sharing screen media_5dedab68-bdaf-44a3-8127-9ced04450355.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wireless-screen-casting-icon'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ('airplay', 'screen mirroring')
    keywords = ('wireless', 'screen', 'casting', 'icon')

    def build(self):
        axis, left, top, bottom, radius = 24, 4, 8, 30, 4
        right = 2*axis-left
        self.add_arc('lower-left', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('left', (left,bottom-radius), (left,top+radius))
        self.add_arc('upper-left', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_line('top', (left+radius,top), (right-radius,top))
        self.add_arc('upper-right', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('right', (right,top+radius), (right,bottom-radius))
        self.add_arc('lower-right', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_contour('screen', 'lower-left','left','upper-left','top','upper-right','right','lower-right')
        self.add_polyline('casting', (axis,26), (34,40), (14,40), closed=True)
