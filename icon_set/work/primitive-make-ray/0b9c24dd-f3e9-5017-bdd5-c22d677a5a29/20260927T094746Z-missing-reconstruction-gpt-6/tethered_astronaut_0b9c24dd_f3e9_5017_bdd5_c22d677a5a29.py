"""An astronaut floats diagonally with a round helmet at upper right and two extended legs toward lower left. Bent arms flank the torso, a backpack sits behind the shoulders, and a tether curves out to the right.

SQUARE visible extremes (4,4)-(44,44); diagonal helmet, bent arms, two legs and tether. Suit seams and separate backpack outline dropped for native clarity. No useful Lucide astronaut match; floating pose deliberately asymmetric.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0b9c24dd-f3e9-5017-bdd5-c22d677a5a29'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tethered-astronaut/20260927T094425Z-thuan-mac-1/reference/astronaut_0b9c24dd-f3e9-5017-bdd5-c22d677a5a29.svg'
AUTHOR = 'gpt-6'
REVISION_COMPARISON = 'The rejected limbs crossed the helmet and tether, obscuring the floating person.'
REVISION_CHANGE = 'Rebuilt an open diagonal suit pose with aligned helmet, backpack, two legs, and a separate tether.'


class TetheredAstronaut(Solo48):
    icon_id = 'tethered-astronaut'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('astronaut', 'spacesuit', 'tether', 'space', 'helmet', 'orbit')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        # Floating suit: aligned helmet, diagonal torso, two arms and two legs.
        self.circle('helmet',32,12,6)
        self.add_line('torso-top',(32,26),(24,30))
        self.add_line('torso-bottom',(24,30),(18,34))
        self.add_polyline('arm-left',(24,30),(14,20),(6,28))
        self.add_polyline('arm-right',(24,30),(36,36),(42,30))
        self.add_line('backpack',(14,20),(18,10))
        self.relate('connect','backpack','arm-left')
        self.add_line('leg-left',(18,34),(8,42))
        self.add_line('leg-right',(18,34),(24,42))
        self.add_line('tether',(42,30),(42,42))
        for a,b in [('torso-top','torso-bottom'),('torso-bottom','arm-left'),
                    ('torso-bottom','arm-right'),('torso-bottom','leg-left'),
                    ('torso-bottom','leg-right'),('arm-right','tether')]:
            self.relate('connect',a,b)
        self.mark_human_figure('astronaut', head='helmet', torso='torso-top', torso_junction='start')
