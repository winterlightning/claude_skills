"""Circular Terminal Connector.

Symbol plan: Horizontal connector and circular endpoint. One circle of radius 14; stem meets its leftmost cardinal node. Circle enlarged to fit the horizontal keyshape.
Keyshape HRECT_M; exact visible bounds (2, 8, 46, 40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21c08633-e9cf-5572-ad79-4e6989fc08b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/end point circle_21c08633-e9cf-5572-ad79-4e6989fc08b9.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'horizontal-connector-ending-in-circle'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ()
    keywords = ('circular', 'terminal', 'connector')

    def build(self):
        self.circle('terminal',30,24,14)
        self.add_line('connector',(4,24),(16,24));self.relate('connect','terminal','connector')

    def circle(self,name,cx,cy,r):
        points=[(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        names=[]
        for i,start in enumerate(points):
            part=f'{name}-{i}';self.add_arc(part,start,points[(i+1)%4],radius_x=r);names.append(part)
        self.add_contour(name,*names,closed=True)
