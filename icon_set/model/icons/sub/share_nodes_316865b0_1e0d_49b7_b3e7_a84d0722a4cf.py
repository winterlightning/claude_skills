"""Share Nodes: A left circular node connects by two sloping links to smaller circular nodes at upper right and lower right. Generate this component alone; exclude Circle Frame.

Construction: Three circular nodes connect through two diagonal links at shared cardinal points.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '316865b0-1e0d-49b7-b3e7-a84d0722a4cf'
SOURCE_PATH = 'pictographic-primitives/state/circle share_316865b0-1e0d-49b7-b3e7-a84d0722a4cf.svg'
AUTHOR = 'gpt-6'


class ShareNodes(Sub32):
    icon_id = 'share-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('share', 'nodes', 'left', 'circular', 'node', 'connects', 'sloping', 'links')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle('left',8,16,6)
        circle('upper',26,6,4)
        circle('lower',26,26,4)
        self.add_line('link-upper',(14,16),(22,6))
        self.add_line('link-lower',(14,16),(22,26))
        for link,node in (('link-upper','upper'),('link-lower','lower')):
            self.relate('connect','left',link)
            self.relate('connect',node,link)
        self.relate('connect','link-upper','link-lower')
