"""Young Sprout in a Pot.
Plan: Mirrored broad pointed leaves at the same junction above a tapered pot. Extrema (8,4)-(40,44).
Reference: Lucide sprout: closed leaves meeting a single stem.
Reduction: Double rim and leaf veins omitted to keep the paired leaves open.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fbc0ef5-471b-5d8e-b31c-f121b23e0d86'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/plant pot_7fbc0ef5-471b-5d8e-b31c-f121b23e0d86.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'potted-sprout-level-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('young', 'sprout', 'in', 'a', 'pot')

    def build(self):

        self.add_bezier('left-a',(8,4),((20,4),(24,8),(24,20)))
        self.add_bezier('left-b',(24,20),((12,20),(8,16),(8,4)))
        self.add_contour('left','left-a','left-b',closed=True)

        self.add_bezier('right-a',(40,4),((28,4),(24,8),(24,20)))
        self.add_bezier('right-b',(24,20),((36,20),(40,16),(40,4)))
        self.add_contour('right','right-a','right-b',closed=True)

        self.relate('connect','left','right')
        self.add_line('stem',(24,20),(24,32))
        for n in ('left','right'):self.relate('connect','stem',n)
        self.add_polyline('pot',(10,32),(24,32),(38,32),(32,44),(16,44),(10,32));self.relate('connect','stem','pot')
