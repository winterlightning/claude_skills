'Three-node hierarchy: equal circular nodes and a single shared convergence point for the links.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '898ebb55-2ee9-5526-bfd8-23179486bc8d'
SOURCE_PATH = 'icons-json/programing/hierarchy_898ebb55-2ee9-5526-bfd8-23179486bc8d.json'
AUTHOR = 'gpt-6'

class Hierarchy898ebb55(Solo48):
    icon_id = 'hierarchy-898ebb55'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('hierarchy', 'programing')

    def build(self) -> None:
        self.add_arc('top-top', (4,14), (16,14), radius_x=6, radius_y=6)
        self.add_arc('top-bottom', (16,14), (4,14), radius_x=6, radius_y=6)
        self.add_contour('top', 'top-top', 'top-bottom', closed=True)

        self.add_arc('bottom-top', (4,34), (16,34), radius_x=6, radius_y=6)
        self.add_arc('bottom-bottom', (16,34), (4,34), radius_x=6, radius_y=6)
        self.add_contour('bottom', 'bottom-top', 'bottom-bottom', closed=True)

        self.add_arc('right-top', (32,24), (44,24), radius_x=6, radius_y=6)
        self.add_arc('right-bottom', (44,24), (32,24), radius_x=6, radius_y=6)
        self.add_contour('right', 'right-top', 'right-bottom', closed=True)

        self.add_line('upper-link',(16,14),(32,24))
        self.add_line('lower-link',(16,34),(32,24))
        for a,b in (('upper-link','top'),('upper-link','right'),('lower-link','bottom'),('lower-link','right'),('upper-link','lower-link')):self.relate('connect',a,b)
