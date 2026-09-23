"""circle bell. Standalone reconstruction of supplied reference.
Plan: preserve the whole composition; CIRCLE bounds (2, 2, 46, 46).
Construction reference: Lucide bell, round joins and coherent symbol contours.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '917e9e90-88a8-4573-a98f-ec5901b6b21f'
SOURCE_PATH = 'icon_set/work/todo-references/circle bell_917e9e90-88a8-4573-a98f-ec5901b6b21f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-bell'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('circle', 'bell')

    def build(self):

        # A circular enclosure owns the centre and radius; two tangent semicircles.
        cx = cy = 24
        radius = 20
        self.add_arc('ring-top', (cx-radius,cy), (cx+radius,cy), radius_x=radius)
        self.add_arc('ring-bottom', (cx+radius,cy), (cx-radius,cy), radius_x=radius)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)

        # Symmetric dome with straight skirts and a joined crown stalk.
        self.add_arc('dome-left',(17,23),(24,16),radius_x=7)
        self.add_arc('dome-right',(24,16),(31,23),radius_x=7)
        self.add_line('skirt-1',(31,23),(31,30))
        self.add_line('skirt-2',(31,30),(17,30))
        self.add_line('skirt-3',(17,30),(17,23))
        self.add_contour('bell','dome-left','dome-right','skirt-1','skirt-2','skirt-3',closed=True)
        self.add_line('crown',(24,13),(24,16))
        self.relate('connect','dome-left','crown')
        self.relate('connect','dome-right','crown')

        self.add_line('lip-left',(15,30),(17,30))
        self.add_line('lip-right',(31,30),(33,30))
        self.relate('connect','bell','lip-left')
        self.relate('connect','bell','lip-right')
