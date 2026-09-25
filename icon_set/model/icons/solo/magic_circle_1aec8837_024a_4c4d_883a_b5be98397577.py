"""Two interlocking triangles form a six-pointed star within a circle.
Plan: semantic components use coherent contours, shared nodes, and mirrored or repeated definitions.
Keyshape CIRCLE; full composition retained on SOLO48. Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1aec8837-024a-4c4d-883a-b5be98397577'
SOURCE_PATH='icon_set/work/todo-references/magic circle_1aec8837-024a-4c4d-883a-b5be98397577.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='magic-circle'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'video-games'
    aliases=()
    keywords=('magic', 'circle')

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
        # Six integer points on r20; all triangle intersections are shared nodes.
        nodes=[(24,4),(40,12),(40,36),(24,44),(8,36),(8,12)]
        members=[]
        for i,p in enumerate(nodes):
            n='ring-'+str(i);members.append(n)
            self.add_arc(n,p,nodes[(i+1)%6],radius_x=20)
        self.add_contour('circle',*members,closed=True)
        self.add_polyline('triangle-up',(24,4),(28,12),(34,24),(40,36),(28,36),(20,36),(8,36),(14,24),(20,12),closed=True)
        self.add_polyline('triangle-down',(24,44),(20,36),(14,24),(8,12),(20,12),(28,12),(40,12),(34,24),(28,36),closed=True)
        self.relate('connect','circle','triangle-up')
        self.relate('connect','circle','triangle-down')
        self.relate('connect','triangle-up','triangle-down')

# Final review record: Six-point star and ring remain distinct. Integer-grid triangles are slightly taller than equilateral; all shared contacts are exact.
# Visible keyshape bounds: (2, 2, 46, 46)
# Construction: No useful local Lucide match was used; geometry follows the supplied reference and shared construction guidance.
