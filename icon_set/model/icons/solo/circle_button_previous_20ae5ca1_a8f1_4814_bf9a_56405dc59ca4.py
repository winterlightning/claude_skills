"""A circular previous-track control with bar and left triangle.
Construction: All defining parts retained.
Lucide construction reference: circle-play; coherent arcs and independent enclosed content.
Keyshape CIRCLE: radial ink radius 22, centre (24,24).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20ae5ca1-a8f1-4814-bf9a-56405dc59ca4'
SOURCE_PATH = 'icon_set/work/todo-references/circle button previous_20ae5ca1-a8f1-4814-bf9a-56405dc59ca4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-button-previous'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('circle', 'button', 'previous')

    def build(self):
        # Circle symbol owns its centre and radius; independent inner content.
        cx, cy, r = 24, 24, 20
        self.add_arc('ring-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc('ring-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)
        # Previous-track control: separate stop bar and left-pointing triangle.
        self.add_line('stop-bar',(14,18),(14,30))
        self.add_polyline('previous',(22,24),(31,16),(31,32),closed=True)

