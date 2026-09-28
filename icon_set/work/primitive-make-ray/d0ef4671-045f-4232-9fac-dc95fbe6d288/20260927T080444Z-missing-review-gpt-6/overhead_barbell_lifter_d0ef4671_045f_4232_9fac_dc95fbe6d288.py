"""Revision of overhead-barbell-lifter. The rejected lifter looked like a box with a dot. Opened the head into a circle and drew raised diagonal arms beneath a barbell with end plates.
Symbol plan: redraw the original subject with one coherent SOLO48 construction.
"""
'Overhead barbell lifter: independent spacing revision.\n\nEight-unit weight/arm gaps and a filled head, retaining the overhead lifting pose.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd0ef4671-045f-4232-9fac-dc95fbe6d288'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__overhead-barbell-lifter/20260927T074149Z-thuan-mac-1/reference/weightlift_d0ef4671-045f-4232-9fac-dc95fbe6d288.svg'
AUTHOR = 'gpt-6'

class OverheadBarbellLifter(Solo48):
    icon_id = 'overhead-barbell-lifter'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('overhead', 'barbell', 'lifter', 'sport')

    def build(self):
        self.add_line('bar',(6,6),(42,6))
        self.add_line('left-plate',(6,6),(6,14))
        self.add_line('right-plate',(42,6),(42,14))
        self.relate('connect','bar','left-plate')
        self.relate('connect','bar','right-plate')
        self.add_polyline('arms',(18,6),(12,22),(18,31),(24,31),(30,31),(36,22),(30,6))
        self.relate('connect','bar','arms')
        self.add_arc('head-a',(21,20),(27,20),radius_x=3)
        self.add_arc('head-b',(27,20),(21,20),radius_x=3)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_line('torso',(24,31),(24,34))
        self.relate('connect','torso','arms')
        self.add_polyline('legs',(18,42),(24,34),(30,42))
        self.relate('connect','torso','legs')
        self.mark_human_figure('lifter',head='head',torso='torso',torso_junction='start')
