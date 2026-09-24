"""A crescent moon accompanies Shiva’s trident and circular emblem.
Plan: semantic components use coherent contours, shared nodes, and mirrored or repeated definitions.
Keyshape SQUARE; full composition retained on SOLO48. Omissions: Minor hooked tip curvature simplified; all symbolic components retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='53d72a10-e412-48cc-8f05-68600caa04a9'
SOURCE_PATH = 'pictographic-primitives/holidays/maha shivaratri_53d72a10-e412-48cc-8f05-68600caa04a9.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='maha-shivaratri'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('maha', 'shivaratri')

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

        self.add_arc('moon-outer',(16,6),(16,26),radius_x=10,radius_y=10,sweep=False)
        self.add_bezier('moon-inner',(16,26),((14,20),(14,12),(16,6)))
        self.add_contour('moon','moon-outer','moon-inner',closed=True)
        self.add_line('shaft-upper',(32,6),(32,29))
        self.circle('emblem',32,35,6)
        self.relate('connect','shaft-upper','emblem')
        self.add_line('shaft-lower',(32,41),(32,42));self.relate('connect','shaft-lower','emblem')
        self.add_polyline('trident-bowl',(24,10),(24,20),(32,20),(40,20),(40,10))
        self.relate('connect','trident-bowl','shaft-upper')
        self.add_line('left-ray',(22,35),(26,35));self.add_line('right-ray',(38,35),(42,35))
        self.relate('connect','left-ray','emblem');self.relate('connect','right-ray','emblem')

# Final review record: Crescent, trident and circular emblem remain identifiable; reference asymmetry retained.
# Visible keyshape bounds: (4, 4, 44, 44)
# Construction: No useful local Lucide match was used; geometry follows the supplied reference and shared construction guidance.
