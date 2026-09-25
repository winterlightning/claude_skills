"""Manual Coffee Grinder.

Plan: Manual grinder with broad hopper, bent crank and divided rounded body. Bounds (8,4)-(40,44). Grip simplified to a downturned crank end.
Construction reference: Lucide funnel: hopper; rounded rectangle for grinding body.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '6a654ad1-1aab-4ecf-8853-972702e20fb5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee filter_6a654ad1-1aab-4ecf-8853-972702e20fb5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'manual-coffee-grinder-with-crank-and-hopper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('manual', 'coffee', 'grinder')

    def build(self):
        poly(self,'hopper',(8,16),(24,16),(36,16),(28,28),(16,28),(8,16))
        box(self,'body',12,28,32,44,3,ys=(36,))
        line(self,'seam',(12,36),(32,36))
        poly(self,'crank',(24,16),(24,4),(40,4),(40,8))
        contacts(self)
