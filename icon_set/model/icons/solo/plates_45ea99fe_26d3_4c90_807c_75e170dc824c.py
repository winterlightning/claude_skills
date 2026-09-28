'plates: independent smooth-curve repair.\n\nConstruction: Two stacked bowls with identical smooth half-ellipse silhouettes and clear vertical spacing.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/cup-soda.svg and atomic-debug/cup-soda.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '45ea99fe-26d3-4c90-807c-75e170dc824c'
SOURCE_PATH = 'pictographic-primitives/hotels/plates_45ea99fe-26d3-4c90-807c-75e170dc824c.svg'
AUTHOR = 'gpt-6'


class Plates(Solo48):
    icon_id = 'plates'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hotels'
    categories = ('hotels', 'primitives')
    aliases = ()
    keywords = ('plates', 'hotels')
    keyshape = Keyshape.HRECT_L

    def build(self):
        for name,cy in (('top',8),('bottom',30)):
            path(self,name,(4,cy),('L',(44,cy)),('A',20,10,True,(24,cy+10)),('A',20,10,True,(4,cy)),closed=True)
        contacts(self)
