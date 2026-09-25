'psychiatry: independent smooth-curve repair.\n\nConstruction: Psi symbol for psychiatry: coherent symmetric bowl, central stem, separated top serifs and base serif preserve the letter identity.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/utensils.svg and atomic-debug/utensils.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f0d4e8d8-2e3e-47b4-82f6-85f8457f25af'
SOURCE_PATH = 'pictographic-primitives/health/psychiatry_f0d4e8d8-2e3e-47b4-82f6-85f8457f25af.svg'
AUTHOR = 'gpt-6'


class Psychiatry(Solo48):
    icon_id = 'psychiatry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('psychiatry', 'health')
    keyshape = Keyshape.SQUARE

    def build(self):
        path(self,'bowl',(10,6),('L',(10,16)),('C',(10,22),(16,24),(24,24)),('C',(32,24),(38,22),(38,16)),('L',(38,6)))
        line(self,'stem',(24,6),(24,24))
        line(self,'handle',(24,24),(24,42))
        line(self,'left-serif',(6,6),(10,6))
        line(self,'right-serif',(38,6),(42,6))
        line(self,'top-serif',(22,6),(26,6))
        line(self,'foot',(18,42),(30,42))
        contacts(self)
