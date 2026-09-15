'ice-cream: independent smooth-curve repair.\n\nConstruction: One smooth scoop over a tapered cone; shared rim ends preserve the physical join.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/ice-cream-cone.svg and atomic-debug/ice-cream-cone.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e002aa9b-6ff7-5580-b41d-36d43d054654'
SOURCE_PATH = 'pictographic-primitives/food/ice cream_e002aa9b-6ff7-5580-b41d-36d43d054654.svg'
AUTHOR = 'gpt-6'


class IceCreamVariant2(Solo48):
    icon_id = 'ice-cream-v2'
    variant_of = 'ice-cream'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ice', 'cream', 'food')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'scoop',(12,25),('C',(9,25),(8,23),(8,21)),('C',(8,12),(14,4),(24,4)),('C',(34,4),(40,12),(40,21)),('C',(40,23),(39,25),(36,25)),('L',(12,25)),closed=True)
        path(self,'cone',(12,25),('L',(21,42)),('C',(22,44.666666667),(26,44.666666667),(27,42)),('L',(36,25)))
        contacts(self)
