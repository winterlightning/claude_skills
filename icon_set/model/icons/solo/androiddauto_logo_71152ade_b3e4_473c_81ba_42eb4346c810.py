'androiddauto-logo: independent smooth-curve repair.\n\nConstruction: Upright navigation badge with a centered tail notch; preserve directional corners and soften the lower lobes.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/navigation.svg and atomic-debug/navigation.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '71152ade-b3e4-473c-81ba-42eb4346c810'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/androiddauto logo_71152ade-b3e4-473c-81ba-42eb4346c810.svg'
AUTHOR = 'gpt-6'


class AndroiddautoLogo(Solo48):
    icon_id = 'androiddauto-logo'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('androiddauto', 'logo', '_uncategorized_03')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'outline',(24,4),('L',(40,30)),('C',(40,33),(33,31),(30,31)),('L',(34,39)),('C',(35,42),(33,44),(30,44)),('L',(18,44)),('C',(15,44),(13,42),(14,39)),('L',(18,31)),('C',(15,31),(8,33),(8,30)),('L',(24,4)),closed=True)
        contacts(self)
