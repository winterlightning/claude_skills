"""Mountain and Sun: An angular mountain ridge descends toward the lower right, beside a detached round sun above its slope. Generate this component alone; exclude Diamond Frame.

Construction: An angular open descending mountain edge sits left of a detached circular sun.
Keyshape: SQUARE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'fb412b73-2149-4427-b06e-19f0aa825780'
SOURCE_PATH = 'pictographic-primitives/state/moutain with circle_fb412b73-2149-4427-b06e-19f0aa825780.svg'
AUTHOR = 'gpt-6'


class MountainAndSun(Sub32):
    icon_id = 'mountain-and-sun'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('mountain', 'sun', 'angular', 'ridge', 'descends', 'toward', 'lower', 'right')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        self.add_polyline('ridge',(2,2),(12,3),(14,14),(26,30))
        circle('sun',25,9,5)
