'Automatic scaling: four equal outward arrows attach to the central rounded box at real cardinal points.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44752e4f-d0f1-4401-8bb4-351d9cd71f62'
SOURCE_PATH = 'icons-json/programing/scaling auto_44752e4f-d0f1-4401-8bb4-351d9cd71f62.json'
AUTHOR = 'gpt-6'

class ScalingAuto(Solo48):
    icon_id = 'scaling-auto'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('scaling', 'auto', 'programing')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 17, 17, 31, 31, 3
        self.add_line('box-top', (left+radius,top), (right-radius,top))
        self.add_arc('box-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('box-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('box-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('box-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('box-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('box-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('box-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('box', *('box-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        for i,(dx,dy) in enumerate(((0,-1),(1,0),(0,1),(-1,0))):
            def p(a,b):return (24+dx*a-dy*b,24+dy*a+dx*b)
            self.add_line(f'shaft-{i}',p(7,0),p(18,0))
            self.add_polyline(f'head-{i}',p(14,-4),p(18,0),p(14,4))
            self.relate('connect','box',f'shaft-{i}');self.relate('connect',f'head-{i}',f'shaft-{i}')
