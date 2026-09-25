"""Wood Carving Chisel.

Plan: Rounded diagonal chisel handle, blade entering wood depression, and upright curled shaving. Remove grain and tight curl tip. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00b49465-7cd7-565b-aef6-2228eb47bc3c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/wood carving_00b49465-7cd7-565b-aef6-2228eb47bc3c.svg'
AUTHOR = 'gpt-6'

class WoodCarvingChisel(Solo48):
    icon_id = 'wood-carving-chisel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hobbies'
    aliases = ()
    keywords = ('wood', 'carving', 'chisel')

    def build(self):
        self.add_arc('handle-top',(7,14),(15,8),radius_x=5)
        self.add_line('handle-r',(15,8),(18,12))
        self.add_arc('handle-br',(18,12),(17,19),radius_x=5)
        self.add_arc('handle-bl',(17,19),(10,18),radius_x=5)
        self.add_line('handle-l',(10,18),(7,14))
        self.add_contour('handle','handle-top','handle-r','handle-br','handle-bl','handle-l',closed=True)
        self.add_line('shaft',(17,19),(26,34))
        self.add_line('wood-top',(6,30),(18,30))
        self.add_arc('cut-left',(18,30),(26,34),radius_x=8,radius_y=4,sweep=False)
        self.add_arc('cut-right',(26,34),(34,30),radius_x=8,radius_y=4,sweep=False)
        self.add_polyline('wood-sides',(34,30),(42,30),(42,42),(6,42),(6,30))
        self.add_contour('wood','wood-top','cut-left','cut-right',*[f'wood-sides-{i}' for i in range(1,5)],closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='wood-sides']
        self.add_line('shaving-stem',(34,30),(34,22))
        self.add_arc('shaving-top',(34,22),(42,14),radius_x=8)
        self.add_contour('shaving','shaving-stem','shaving-top')
        for a,b in [('handle','shaft'),('shaft','wood'),('wood','shaving')]:self.relate('connect',a,b)
