"""circle button previous. Standalone reconstruction of supplied reference.
Plan: preserve the whole composition; CIRCLE bounds (2, 2, 46, 46).
Construction reference: Lucide skip-back, round joins and coherent symbol contours.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '20ae5ca1-a8f1-4814-bf9a-56405dc59ca4'
SOURCE_PATH = 'icon_set/work/todo-references/circle button previous_20ae5ca1-a8f1-4814-bf9a-56405dc59ca4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-button-previous'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('circle', 'button', 'previous')

    def build(self):

        # A circular enclosure owns the centre and radius; two tangent semicircles.
        cx = cy = 24
        radius = 20
        self.add_arc('ring-top', (cx-radius,cy), (cx+radius,cy), radius_x=radius)
        self.add_arc('ring-bottom', (cx+radius,cy), (cx-radius,cy), radius_x=radius)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)

        # The previous symbol is a left stop bar and left-pointing closed triangle.
        self.add_line('stop',(14,18),(14,30))
        self.add_polyline('triangle',(22,24),(32,16),(32,32),closed=True)

