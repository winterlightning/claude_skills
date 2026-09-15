'dna: independent smooth-curve repair.\n\nConstruction: Two smooth helical rails cross at a shared center node; paired terminal rungs.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/dna.svg and atomic-debug/dna.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'b4ea616c-9fe4-40b2-ab7c-11c82b439358'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/dna_b4ea616c-9fe4-40b2-ab7c-11c82b439358.svg'
AUTHOR = 'gpt-6'


class Dna(Solo48):
    icon_id = 'dna'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('dna', 'artificial-intelligence')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'helix-a',(8,4),('C',(8,14),(15,19),(24,24)),('C',(33,29),(40,34),(40,44)))
        path(self,'helix-b',(40,4),('C',(40,14),(33,19),(24,24)),('C',(15,29),(8,34),(8,44)))
        line(self,'top-rung',(8,4),(40,4))
        line(self,'bottom-rung',(8,44),(40,44))
        contacts(self)
