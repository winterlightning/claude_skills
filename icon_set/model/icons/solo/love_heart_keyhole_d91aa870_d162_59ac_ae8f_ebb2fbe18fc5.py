"""A heart encloses a classic round-topped keyhole.
Plan: semantic components use coherent contours, shared nodes, and mirrored or repeated definitions.
Keyshape SQUARE; full composition retained on SOLO48. Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d91aa870-d162-59ac-ae8f-ebb2fbe18fc5'
SOURCE_PATH='icon_set/work/todo-references/love heart keyhole_d91aa870-d162-59ac-ae8f-ebb2fbe18fc5.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='love-heart-keyhole'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('love', 'heart', 'keyhole')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def heart(self):
        # Shallow notch and broad lobes keep room for the complete inner symbol.
        self.add_bezier('left-top',(24,10),((21,7),(18,6),(15,6)),((9,6),(6,12),(6,20)))
        self.add_bezier('left-bottom',(6,20),((6,30),(16,38),(24,42)))
        self.add_bezier('right-bottom',(24,42),((32,38),(42,30),(42,20)))
        self.add_bezier('right-top',(42,20),((42,12),(39,6),(33,6)),((30,6),(27,7),(24,10)))
        self.add_contour('heart','left-top','left-bottom','right-bottom','right-top',closed=True)

    def lens(self):
        # Circle at (21,21), radius 15. Shared handle node (30,33): 9²+12²=15².
        self.add_arc('lens-a',(30,33),(12,9),radius_x=15)
        self.add_arc('lens-b',(12,9),(30,33),radius_x=15)
        self.add_contour('lens','lens-a','lens-b',closed=True)
        self.add_line('handle',(30,33),(42,42))
        self.relate('connect','lens','handle')

    def envelope(self):
        # Complete card protruding from an open envelope; bilateral fold nodes.
        self.add_polyline('body',(6,24),(6,42),(42,42),(42,24))
        self.add_polyline('fold',(6,24),(12,28),(18,32),(30,32),(36,28),(42,24))
        self.relate('connect','body','fold')
        self.add_polyline('card',(12,28),(12,6),(36,6),(36,28))
        self.relate('connect','card','fold')
        self.add_line('seam-left',(18,32),(13,37))
        self.add_line('seam-right',(30,32),(35,37))
        self.relate('connect','seam-left','fold')
        self.relate('connect','seam-right','fold')

    def build(self):

        self.heart()
        self.add_arc('keyhole-top',(21,23),(27,23),radius_x=3)
        self.add_bezier('keyhole-right',(27,23),((27,24),(26,25),(25,25)))
        self.add_line('keyhole-base-1',(25,25),(27,30))
        self.add_line('keyhole-base-2',(27,30),(21,30))
        self.add_line('keyhole-base-3',(21,30),(23,25))
        self.add_bezier('keyhole-left',(23,25),((22,25),(21,24),(21,23)))
        # One contour, shared endpoints preserve the keyhole topology.
        self.add_contour('keyhole','keyhole-top','keyhole-right','keyhole-base-1','keyhole-base-2','keyhole-base-3','keyhole-left',closed=True)

# Final review record: Recognizable heart/keyhole, but the keyhole interior closes at native size. Numeric pass; visual approval withheld.
# Visible keyshape bounds: (4, 4, 44, 44)
# Construction: Paired lobes and coherent contour construction.
