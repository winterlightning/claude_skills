"""Goalkeeper reaching up toward a ball with a gently leaning body.

Plan: SQUARE extremes (6,6)-(42,42). Circular head, connected arm/torso
strokes and two legs; ball at the raised hand. Human full_body_ref.png
owns proportions. Head (18,11), radius5 ends at16; neck (18,24) is on
the upper torso axis with exactly 4 visible units of detached clearance.
Original supplies the reach and lowered opposite arm. No useful Lucide
construction beyond the inspected shared human reference was required.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '974f127b-6a9c-4f4e-b8b2-aaea365c16ef'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__goalkeeper-reaching-for-ball/20260929T104833Z-thuan-mac/reference/keeper_974f127b-6a9c-4f4e-b8b2-aaea365c16ef.svg'
AUTHOR = 'gpt-6'


class Goalkeeper(Solo48):
    icon_id = 'goalkeeper-reaching-for-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('goalkeeper', 'reach', 'ball', 'save', 'soccer')

    def build(self):
        self.add_arc('head-top',(13,11),(23,11),radius_x=5)
        self.add_arc('head-bottom',(23,11),(13,11),radius_x=5)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_bezier('torso',(18,24),((18,29),(16,31),(15,33)))
        self.mark_human_figure('keeper',head='head',torso='torso',torso_junction='start')
        self.add_bezier('lower-arm',(18,24),((12,24),(10,28),(6,32)))
        self.add_polyline('raised-arm',(18,24),(26,24),(36,18))
        self.relate('connect','torso','lower-arm')
        self.relate('connect','torso','raised-arm')
        self.relate('connect','lower-arm','raised-arm')
        self.add_polyline('legs',(8,42),(15,33),(23,42))
        self.relate('connect','torso','legs')
        self.add_arc('ball-left',(36,18),(36,6),radius_x=6)
        self.add_arc('ball-right',(36,6),(36,18),radius_x=6)
        self.add_contour('ball','ball-left','ball-right',closed=True)
        self.relate('connect','ball','raised-arm')
