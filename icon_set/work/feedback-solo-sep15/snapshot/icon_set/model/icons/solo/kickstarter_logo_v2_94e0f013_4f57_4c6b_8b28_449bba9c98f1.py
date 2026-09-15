'kickstarter-logo: independent smooth-curve repair.\n\nConstruction: Kickstarter K outline: flowing paired lobes and a straight stem; intentional letter notches remain.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/braces.svg and atomic-debug/braces.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '94e0f013-4f57-4c6b-8b28-449bba9c98f1'
SOURCE_PATH = 'pictographic-primitives/logos/kickstarter logo_94e0f013-4f57-4c6b-8b28-449bba9c98f1.svg'
AUTHOR = 'gpt-6'


class KickstarterLogoVariant2(Solo48):
    icon_id = 'kickstarter-logo-v2'
    variant_of = 'kickstarter-logo'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('kickstarter', 'logo', 'logos')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'letter',(8,10),('C',(8,6),(10,4),(14,4)),('C',(18,4),(20,7),(20,12)),('L',(20,15)),('L',(29,6)),('C',(31,4),(32,4),(34,4)),('A',6,6,True,(40,10)),('L',(40,12)),('C',(40,16),(34,20),(30,24)),('C',(34,28),(40,32),(40,36)),('L',(40,38)),('A',6,6,True,(34,44)),('C',(32,44),(31,44),(29,42)),('L',(20,33)),('L',(20,36)),('C',(20,41),(18,44),(14,44)),('C',(10,44),(8,42),(8,38)),('L',(8,10)),closed=True)
        contacts(self)
