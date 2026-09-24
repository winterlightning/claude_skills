"""A diagonal two-part medicine capsule sits inside a magnifier.
Plan: semantic components use coherent contours, shared nodes, and mirrored or repeated definitions.
Keyshape SQUARE; full composition retained on SOLO48. Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='15fc1905-26f1-420c-9167-f58df5f29604'
SOURCE_PATH='icon_set/work/todo-references/magnifying glass pill_15fc1905-26f1-420c-9167-f58df5f29604.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='magnifying-glass-pill'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('magnifying', 'glass', 'pill')

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
        self.add_line('pill-upper',(15,21),(21,15))
        self.add_bezier('pill-cap-right',(21,15),((26,10),(32,16),(27,21)))
        self.add_line('pill-lower',(27,21),(21,27))
        self.add_bezier('pill-cap-left',(21,27),((16,32),(10,26),(15,21)))
        self.add_contour('pill','pill-upper','pill-cap-right','pill-lower','pill-cap-left',closed=True)
        self.add_line('pill-seam',(18,18),(24,24));self.relate('connect','pill','pill-seam')

# Final review record: Pill and divider recognizable but crowd the lens. MIC failure retained; not approved.
# Visible keyshape bounds: (4, 4, 44, 44)
# Construction: Circular lens with a shared, analytically exact handle attachment.
