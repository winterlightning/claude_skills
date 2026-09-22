'A funnel feeds three terminal nodes through a shared branch. Natural connected distribution diagram. HRECT_L fits broad inlet and node row. Lucide funnel provides taper construction. Shared branch center and reflected side arms; smaller terminal circles preserve the three-node count.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b7d69bd-8caa-4c24-8a98-8203b4634aff'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon sns filtered notification_5b7d69bd-8caa-4c24-8a98-8203b4634aff.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'funnel-feeding-three-network-nodes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ['Funnel and Branching Network Nodes']
    keywords = ['funnel', 'filter', 'network', 'nodes', 'branch', 'data', 'distribution']
    def build(self):
        self.add_polyline('funnel',(4,8),(44,8),(28,16),(28,19),(24,19),(20,19),(20,16),closed=True)
        self.add_line('feed',(24,19),(24,27))
        self.relate('connect','feed','funnel')
        self.add_polyline('left-arm',(8,36),(8,27),(24,27))
        self.add_polyline('right-arm',(24,27),(40,27),(40,36))
        self.add_line('middle-arm',(24,27),(24,36))
        self.relate('connect','feed','left-arm','right-arm','middle-arm')
        for j,x in enumerate((8,24,40)):
            self.add_arc(f'node-{j}-a',(x,36),(x,40),radius_x=2)
            self.add_arc(f'node-{j}-b',(x,40),(x,36),radius_x=2)
            self.add_contour(f'node-{j}',f'node-{j}-a',f'node-{j}-b',closed=True)
            self.relate('connect',f'node-{j}',('left-arm','middle-arm','right-arm')[j])
