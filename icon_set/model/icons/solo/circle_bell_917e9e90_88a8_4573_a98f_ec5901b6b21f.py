"""A dome bell within a circular button.
Construction: All defining parts retained.
Lucide construction reference: bell; coherent arcs and independent enclosed content.
Keyshape CIRCLE: radial ink radius 22, centre (24,24).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '917e9e90-88a8-4573-a98f-ec5901b6b21f'
SOURCE_PATH = 'icon_set/work/todo-references/circle bell_917e9e90-88a8-4573-a98f-ec5901b6b21f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-bell'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('circle', 'bell')

    def build(self):
        # Circle symbol owns its centre and radius; independent inner content.
        cx, cy, r = 24, 24, 20
        self.add_arc('ring-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc('ring-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)
        # Symmetric dome with a shared top attachment and extended baseline.
        self.add_arc('dome-left',(16,24),(24,16),radius_x=8)
        self.add_arc('dome-right',(24,16),(32,24),radius_x=8)
        self.add_line('wall-right',(32,24),(32,30))
        self.add_line('base',(32,30),(16,30))
        self.add_line('wall-left',(16,30),(16,24))
        self.add_contour('bell','dome-left','dome-right','wall-right','base','wall-left',closed=True)
        self.add_line('finial',(24,13),(24,16))
        self.relate('connect','bell','finial')
        for side,x,end in [('left',16,14),('right',32,34)]:
            self.add_line('lip-'+side,(x,30),(end,30))
            self.relate('connect','bell','lip-'+side)

