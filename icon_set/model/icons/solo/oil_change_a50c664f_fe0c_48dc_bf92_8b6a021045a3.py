'oil-change: independent smooth-curve repair.\n\nConstruction: Oil drop above a broad receiving tray; rounded drop bowl and tray corners.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/droplet.svg and atomic-debug/droplet.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a50c664f-fe0c-48dc-bf92-8b6a021045a3'
SOURCE_PATH = 'pictographic-primitives/transportation/oil change_a50c664f-fe0c-48dc-bf92-8b6a021045a3.svg'
AUTHOR = 'gpt-6'


class OilChange(Solo48):
    icon_id = 'oil-change'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('oil', 'change', 'transportation')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'drop',(24,4),('C',(21,10),(15,15),(15,21)),('A',9,9,False,(24,30)),('A',9,9,False,(33,21)),('C',(33,15),(27,10),(24,4)),closed=True)
        path(self,'tray',(8,31),('L',(11,41)),('C',(11.5,43),(13,44),(16,44)),('L',(32,44)),('C',(35,44),(36.5,43),(37,41)),('L',(40,31)))
        contacts(self)
