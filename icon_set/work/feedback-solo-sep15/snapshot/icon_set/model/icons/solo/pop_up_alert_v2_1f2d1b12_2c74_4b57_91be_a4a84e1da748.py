'pop-up-alert: independent smooth-curve repair.\n\nConstruction: Question panel with a larger readable question hook and separate dot; retain its meaningful asymmetry. Three alert dots replace cramped short rays above the panel.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/circle.svg and atomic-debug/circle.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '1f2d1b12-2c74-4b57-91be-a4a84e1da748'
SOURCE_PATH = 'pictographic-primitives/apps/pop up alert_1f2d1b12-2c74-4b57-91be-a4a84e1da748.svg'
AUTHOR = 'gpt-6'


class PopUpAlertVariant2(Solo48):
    icon_id = 'pop-up-alert-v2'
    variant_of = 'pop-up-alert'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('pop', 'up', 'alert', 'apps')
    keyshape = Keyshape.VRECT_L

    def build(self):
        box(self,'panel',8,12,40,44,4)
        path(self,'question',(18,26),('C',(18,19.333333333),(30,19.333333333),(30,26)),('C',(30,27),(24,27),(24,27)))
        self.add_dot('question-dot',(24,35))
        for name,x in (('left',8),('center',24),('right',40)): self.add_dot('alert-'+name,(x,4))
        contacts(self)
