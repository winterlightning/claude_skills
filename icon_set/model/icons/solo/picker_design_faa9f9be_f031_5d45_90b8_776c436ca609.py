'picker-design: independent smooth-curve repair.\n\nConstruction: Upright dropper with a rounded bulb, transverse grip and smooth tapered tip.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/pipette.svg and atomic-debug/pipette.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'faa9f9be-f031-5d45-90b8-776c436ca609'
SOURCE_PATH = 'pictographic-primitives/design/picker_faa9f9be-f031-5d45-90b8-776c436ca609.svg'
AUTHOR = 'gpt-6'


class PickerDesign(Solo48):
    icon_id = 'picker-design'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('picker', 'design')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'body',(14,16),('L',(14,10)),('C',(14,6),(18,4),(24,4)),('C',(30,4),(34,6),(34,10)),('L',(34,16)),('L',(34,31)),('C',(34,36),(28,36),(28,40)),('C',(28,45.333333333),(20,45.333333333),(20,40)),('C',(20,36),(14,36),(14,31)),('L',(14,16)),closed=True)
        line(self,'grip',(8,16),(40,16))
        contacts(self)
