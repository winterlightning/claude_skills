'navigation-arrows-up: independent smooth-curve repair.\n\nConstruction: Upright arrow with exactly mirrored arms and a centered shaft; upload variant retains its rounded receiving tray.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/arrow-up.svg and atomic-debug/arrow-up.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '428c508c-c9f9-43d1-90d2-74e0ffbb6354'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation arrows up_428c508c-c9f9-43d1-90d2-74e0ffbb6354.svg'
AUTHOR = 'gpt-6'


class NavigationArrowsUp(Solo48):
    icon_id = 'navigation-arrows-up'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'arrows', 'up', 'interface-essential')
    keyshape = Keyshape.VRECT_L

    def build(self):
        poly(self,'head',(8,20),(24,4),(40,20))
        line(self,'shaft',(24,4),(24,44))
        contacts(self)
