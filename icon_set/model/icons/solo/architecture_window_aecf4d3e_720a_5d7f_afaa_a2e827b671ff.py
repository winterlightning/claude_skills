'architecture-window: independent smooth-curve repair.\n\nConstruction: Arched window: a true semicircular crown, straight jambs and shared central mullion.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/house.svg and atomic-debug/house.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'aecf4d3e-720a-5d7f-afaa-a2e827b671ff'
SOURCE_PATH = 'pictographic-primitives/building/architecture window_aecf4d3e-720a-5d7f-afaa-a2e827b671ff.svg'
AUTHOR = 'gpt-6'


class ArchitectureWindow(Solo48):
    icon_id = 'architecture-window'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('architecture', 'window', 'building')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'frame',(8,44),('L',(8,20)),('A',16,16,True,(24,4)),('A',16,16,True,(40,20)),('L',(40,44)),('L',(24,44)),('L',(8,44)),closed=True)
        line(self,'mullion',(24,4),(24,44))
        line(self,'crossbar',(8,28),(40,28))
        contacts(self)
