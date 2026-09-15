'settings-on: independent smooth-curve repair.\n\nConstruction: Capsule-like rounded enclosure with equal semicircular ends; centered interior where present.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0392b574-2d42-4e72-8939-91f0c4b24d2f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/settings on_0392b574-2d42-4e72-8939-91f0c4b24d2f.svg'
AUTHOR = 'gpt-6'


class SettingsOn(Solo48):
    icon_id = 'settings-on'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('settings', 'on', 'interface-essential')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'outline',4,8,44,40,16)
        line(self,"switch",(32,18),(32,30))
        contacts(self)
