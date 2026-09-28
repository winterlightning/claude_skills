'house-entrance: independent smooth-curve repair.\n\nConstruction: House silhouette with an integrated arched doorway and symmetrical eaves.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/house.svg and atomic-debug/house.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a8ff6223-9707-5e5b-9f2e-83b33b38b733'
SOURCE_PATH = 'pictographic-primitives/interface-essential/house entrance_a8ff6223-9707-5e5b-9f2e-83b33b38b733.svg'
AUTHOR = 'gpt-6'


class HouseEntrance(Solo48):
    icon_id = 'house-entrance'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('house', 'entrance', 'interface-essential')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'house',(4,40),('L',(4,21)),('L',(24,8)),('L',(44,21)),('L',(44,40)),('L',(31,40)),('L',(31,32)),('A',7,7,False,(24,25)),('A',7,7,False,(17,32)),('L',(17,40)),('L',(4,40)),closed=True)
        contacts(self)
