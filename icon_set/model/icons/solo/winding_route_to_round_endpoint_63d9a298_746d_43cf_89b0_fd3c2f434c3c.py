"""A winding route ends at a round destination. SQUARE: (6,6)-(42,42).
Reference supplies the rising S route and one endpoint; Lucide route supplies
continuous tangent turns and shared endpoint construction. Natural asymmetry.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '63d9a298-746d-43cf-89b0-fd3c2f434c3c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/route_63d9a298-746d-43cf-89b0-fd3c2f434c3c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'winding-route-to-round-endpoint'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Curved Route to Destination']
    keywords = ['route', 'path', 'endpoint', 'journey', 'curve', 'navigation']
    def build(self):
        self.add_arc('destination-right',(36,6),(36,18),radius_x=6)
        self.add_arc('destination-left',(36,18),(36,6),radius_x=6)
        self.add_contour('destination','destination-right','destination-left',closed=True)
        self.add_bezier('route',(6,42),((20,42),(10,24),(24,24)),((32,24),(36,24),(36,18)))
        self.relate('connect','destination-right','route')
        self.relate('connect','destination-left','route')
