"""Connected Topic Node.
Plan: Round origin node meets a blank topic rectangle through a horizontal stem. Radial envelope22.
Reference construction: network.
Reduction: Keep the defining source features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'caf48b31-6f77-51ee-9876-7aa1b86d5f13'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/subtopic organize_caf48b31-6f77-51ee-9876-7aa1b86d5f13.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'connected-topic-node'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('connected', 'topic', 'node')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        circle('node',10,24,6)
        self.add_line('link',(16,24),(25,24))
        self.add_polyline('topic',(25,16),(40,16),(40,32),(25,32),(25,24),closed=True)
        self.relate('connect','link','node');self.relate('connect','link','topic')
