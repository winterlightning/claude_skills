"""A lion face with rounded inner muzzle inside a heart-shaped mane.
Plan: semantic components use coherent contours, shared nodes, and mirrored or repeated definitions.
Keyshape SQUARE; full composition retained on SOLO48. Omissions: Fine facial marks omitted, as the reference has no separate eyes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9b6a2c4c-3b0c-4b0c-a13c-c9c39f1f1cad'
SOURCE_PATH='icon_set/work/todo-references/lion_9b6a2c4c-3b0c-4b0c-a13c-c9c39f1f1cad.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='lion'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('lion',)

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
        self.add_bezier('face',(24,23),((21,15),(14,17),(17,23)),((19,25),(18,27),(19,28)),((20,31),(23,29),(24,27)),((25,30),(28,30),(28,28)),((30,26),(29,25),(31,23)),((34,17),(27,15),(24,23)))
        self.add_contour('muzzle','face',closed=True)

# Final review record: Mane and butterfly-like muzzle preserve the unusual reference; muzzle lobes are reduced. No separate eyes added.
# Visible keyshape bounds: (4, 4, 44, 44)
# Construction: Paired lobes and coherent contour construction.
