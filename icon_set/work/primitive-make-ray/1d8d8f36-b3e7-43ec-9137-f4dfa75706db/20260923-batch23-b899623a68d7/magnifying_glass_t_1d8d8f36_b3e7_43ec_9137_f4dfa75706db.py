"""A serif capital T sits inside a magnifier.
Plan: semantic components use coherent contours, shared nodes, and mirrored or repeated definitions.
Keyshape SQUARE; full composition retained on SOLO48. Omissions: Short top serifs reduced to three-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1d8d8f36-b3e7-43ec-9137-f4dfa75706db'
SOURCE_PATH='icon_set/work/todo-references/magnifying glass t_1d8d8f36-b3e7-43ec-9137-f4dfa75706db.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='magnifying-glass-t'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('magnifying', 'glass', 't')

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
        self.lens()
        # Retain top bar and bottom serif; tiny drop-serifs are omitted for clearance.
        self.add_polyline('t-top',(16,17),(21,17),(26,17))
        self.add_line('t-stem',(21,17),(21,27))
        self.add_polyline('t-base',(18,27),(21,27),(24,27))
        self.relate('connect','t-top','t-stem');self.relate('connect','t-stem','t-base')

# Final review record: T remains legible with top bar, stem and bottom serif. Tiny downward top serifs omitted for clearance.
# Visible keyshape bounds: (4, 4, 44, 44)
# Construction: Circular lens with a shared, analytically exact handle attachment.
