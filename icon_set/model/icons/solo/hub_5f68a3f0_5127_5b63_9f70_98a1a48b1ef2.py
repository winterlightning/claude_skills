'Hub network: three round nodes, outer links and central spokes share exact attachment points; omit the crowded centre ring.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f68a3f0-5127-5b63-9f70-98a1a48b1ef2'
SOURCE_PATH = 'icons-json/programing/hub_5f68a3f0-5127-5b63-9f70-98a1a48b1ef2.json'
AUTHOR = 'gpt-6'

class Hub(Solo48):
    icon_id = 'hub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('hub', 'programing')

    def build(self) -> None:
        self.add_arc('top-node-top', (20,10), (28,10), radius_x=4, radius_y=4)
        self.add_arc('top-node-bottom', (28,10), (20,10), radius_x=4, radius_y=4)
        self.add_contour('top-node', 'top-node-top', 'top-node-bottom', closed=True)

        self.add_arc('left-node-top', (6,34), (14,34), radius_x=4, radius_y=4)
        self.add_arc('left-node-bottom', (14,34), (6,34), radius_x=4, radius_y=4)
        self.add_contour('left-node', 'left-node-top', 'left-node-bottom', closed=True)

        self.add_arc('right-node-top', (34,34), (42,34), radius_x=4, radius_y=4)
        self.add_arc('right-node-bottom', (42,34), (34,34), radius_x=4, radius_y=4)
        self.add_contour('right-node', 'right-node-top', 'right-node-bottom', closed=True)

        self.add_polyline('outer-left',(20,10),(10,18),(10,30))
        self.add_polyline('outer-right',(28,10),(38,18),(38,30))
        self.add_polyline('outer-bottom',(10,38),(24,42),(38,38))
        self.relate('connect','outer-left','top-node');self.relate('connect','outer-left','left-node')
        self.relate('connect','outer-right','top-node');self.relate('connect','outer-right','right-node')
        self.relate('connect','outer-bottom','left-node');self.relate('connect','outer-bottom','right-node')
        self.add_line('top-link',(24,14),(24,24))
        self.add_line('left-link',(14,34),(24,24));self.add_line('right-link',(34,34),(24,24))
        for a,b in (('top-link','top-node'),('left-link','left-node'),('right-link','right-node'),('top-link','left-link'),('top-link','right-link'),('left-link','right-link')):self.relate('connect',a,b)
