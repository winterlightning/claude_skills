'meal-can: independent smooth-curve repair.\n\nConstruction: Food can with true elliptical rims and a centered label; front label simplified to one broad dash.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/cylinder.svg and atomic-debug/cylinder.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a9327102-c668-47fb-88c0-07e9b814ac8a'
SOURCE_PATH = 'pictographic-primitives/food/meal can_a9327102-c668-47fb-88c0-07e9b814ac8a.svg'
AUTHOR = 'gpt-6'


class MealCan(Solo48):
    icon_id = 'meal-can'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('meal', 'can', 'food')
    keyshape = Keyshape.VRECT_L

    def build(self):
        ellipse(self,'rim',24,10,16,6)
        path(self,'body',(8,10),('L',(8,38)),('A',16,6,False,(24,44)),('A',16,6,False,(40,38)),('L',(40,10)))
        line(self,'label',(17,28),(31,28))
        contacts(self)
