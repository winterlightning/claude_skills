"""Dog in Wheelchair Cart.

Plan: Right-facing dog on one foreleg with hindquarters on a large cart wheel. Wheel joins a short support shaft, not the body contour.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '437c8843-3f37-4c2f-adf8-fc4be5c729ca'
SOURCE_PATH = 'pictographic-primitives/pets/disabled pet_437c8843-3f37-4c2f-adf8-fc4be5c729ca.svg'
AUTHOR = 'gpt-6'

class DogInWheelchairCart(Solo48):
    icon_id = 'dog-in-wheelchair-cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'wheelchair', 'disabled', 'mobility', 'cart', 'pet', 'care', 'accessibility')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis = 24
        def mirror(p): return (2 * axis - p[0], p[1])
        # A rounded forehead and a projecting snout make the profile read as a dog.
        line('back',(14,16),(26,16))
        arc('neck-crown',(26,16),(34,8),8)
        arc('forehead',(34,8),(40,14),6)
        line('snout-top',(40,14),(44,14))
        arc('snout',(44,14),(36,22),8)
        line('chest',(36,22),(34,40))
        line('paw',(34,40),(42,40))
        contour('dog','back','neck-crown','forehead','snout-top','snout','chest','paw')
        arc('wheel-right',(14,24),(14,40),8)
        arc('wheel-left',(14,40),(14,24),8)
        contour('wheel','wheel-right','wheel-left',closed=True)
        line('support',(14,16),(14,24))
        self.relate('connect','support','wheel')
        self.relate('connect','support','dog')
        arc('tail',(14,16),(4,8),10,8)
        self.relate('connect','tail','dog')
        self.relate('connect','tail','support')
