"""Rear view of a car with its luggage compartment symbol centered.
Plan: semantic components use coherent contours, shared nodes, and mirrored or repeated definitions.
Keyshape HRECT_L; full composition retained on SOLO48. Omissions: Short bumper ticks omitted; wheels remain paired.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5f2c92bb-8547-4bda-9a89-b7724021c337'
SOURCE_PATH = 'pictographic-primitives/transportation/luggage compartment release_5f2c92bb-8547-4bda-9a89-b7724021c337.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id='luggage-compartment-release'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'transportation'
    aliases=()
    keywords=('luggage', 'compartment', 'release')

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

        self.add_polyline('car',(6,32),(6,22),(12,6),(36,6),(42,22),(42,32),(42,32),(34,32),(33,32),(15,32),(14,32),(6,32),(6,32))
        for n,x in [('left',10),('right',38)]:
            self.add_line(n+'-wheel-side',(x-4,32),(x-4,38))
            self.add_arc(n+'-wheel-round',(x-4,38),(x+4,38),radius_x=4,sweep=False)
            self.add_line(n+'-wheel-end',(x+4,38),(x+4,32))
            self.add_contour(n+'-wheel',n+'-wheel-side',n+'-wheel-round',n+'-wheel-end');self.relate('connect',n+'-wheel','car')
        self.add_polyline('luggage',(15,32),(15,24),(17,24),(31,24),(33,24),(33,32))
        self.relate('connect','luggage','car')
        self.add_arc('luggage-handle',(17,24),(31,24),radius_x=7)
        self.relate('connect','luggage-handle','luggage')

# Final review record: Car, paired wheels and luggage symbol remain distinct. Wheel bends use matched radius4.
# Visible keyshape bounds: (2, 6, 46, 42)
# Construction: No useful local Lucide match was used; geometry follows the supplied reference and shared construction guidance.

# Final repair review: A car-shaped compartment release sign enclosing luggage.
# SQUARE adds vertical room for the wheels and handle.
# Changes: Enlarged luggage handle and deepened wheel openings; omitted tiny side ticks.
# validate_icon: valid; build gate: pass with zero errors and zero warnings.
