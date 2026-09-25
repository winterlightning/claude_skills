"""The word LOVE in a two-by-two layout, with a heart as the O.
Plan: semantic components use coherent contours, shared nodes, and mirrored or repeated definitions.
Keyshape SQUARE; full composition retained on SOLO48. Omissions: Rounded V bottom reduced to a round joined vertex.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='223c2cf3-707e-5588-bcee-3eb48df2972c'
SOURCE_PATH='icon_set/work/todo-references/lgbt love_223c2cf3-707e-5588-bcee-3eb48df2972c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='lgbt-love'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'romance'
    aliases=()
    keywords=('lgbt', 'love')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def heart(self):
        # Shared bilateral lobe radius and mirrored flanks; exact square extremes.
        self.add_arc('lobe-left',(24,15),(6,15),radius_x=9,sweep=False)
        self.add_bezier('flank-left',(6,15),((6,28),(16,37),(24,42)))
        self.add_bezier('flank-right',(24,42),((32,37),(42,28),(42,15)))
        self.add_arc('lobe-right',(42,15),(24,15),radius_x=9,sweep=False)
        self.add_contour('heart','lobe-left','flank-left','flank-right','lobe-right',closed=True)

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

        self.add_polyline('l',(6,6),(6,18),(18,18))
        self.add_arc('heart-left',(34,10),(26,10),radius_x=4,sweep=False)
        self.add_bezier('heart-bottom',(26,10),((26,13),(30,16),(34,18)),((38,16),(42,13),(42,10)))
        self.add_arc('heart-right',(42,10),(34,10),radius_x=4,sweep=False)
        self.add_contour('o-heart','heart-left','heart-bottom','heart-right',closed=True)
        self.add_polyline('v',(6,26),(12,42),(18,26))
        self.add_polyline('e',(42,26),(28,26),(28,34),(28,42),(42,42))
        self.add_line('e-middle',(28,34),(40,34));self.relate('connect','e','e-middle')

# Keyshape visible bounds: (4, 4, 44, 44)
# Construction: Paired heart lobes and coherent contour construction informed the drawing; proportions were authored afresh for the complete composition.
# Final reductions: Rounded V bottom reduced to a round joined vertex.
# Visual review: Two-by-two LOVE lettering reads clearly; the heart replaces O, with balanced rows and adequate separation.

# Final review record: LOVE lettering and heart read clearly in the two-by-two arrangement.
# Visible keyshape bounds: (4, 4, 44, 44)
# Construction: Paired lobes and coherent contour construction.
