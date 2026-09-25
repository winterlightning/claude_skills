'fat-liquid-drop-drinks: independent smooth-curve repair.\n\nConstruction: Single smooth liquid drop: mirrored shoulders meet a deliberate top tip; lower bowl is tangent continuous.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/droplet.svg and atomic-debug/droplet.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'df25d2b8-d703-541d-9206-3a94b12492bc'
SOURCE_PATH = 'pictographic-primitives/drinks/fat liquid drop_df25d2b8-d703-541d-9206-3a94b12492bc.svg'
AUTHOR = 'gpt-6'


class FatLiquidDropDrinks(Solo48):
    icon_id = 'fat-liquid-drop-drinks'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    categories = ('drinks', 'primitives')
    aliases = ()
    keywords = ('fat', 'liquid', 'drop', 'drinks')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'drop',(24,4),('C',(20,12),(8,20),(8,28)),('C',(8,37),(15,44),(24,44)),('C',(33,44),(40,37),(40,28)),('C',(40,20),(28,12),(24,4)),closed=True)
        contacts(self)
