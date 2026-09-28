"""Person in Flagged Dragon Boat.

Plan: Dragon prow, passenger, flag and deep hull; centerlines (4,8)-(44,40).
Construction: Lucide sailboat rounded hull and human_ref detached circular head.
Reduction: Omitted eye and repeated waves; widened flag and hull openings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '1876597a-539e-43bb-87c0-8c28c478f11a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-in-flagged-dragon-boat/20260927T153747Z-thuan-mac-1/reference/dragon boat festival person_1876597a-539e-43bb-87c0-8c28c478f11a.svg'
AUTHOR = "gpt-6"


class IconPersonInFlaggedDragonBoat(Solo48):
    icon_id = 'person-in-flagged-dragon-boat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('person', 'in', 'flagged', 'dragon', 'boat')

    def build(self):
        # Dragon bow, passenger, square flag and wave line.
        self.add_polyline('boat', (4, 20), (10, 20), (12, 14), (14, 24), (36, 24), (44, 26), (40, 30), (20, 30), (8, 26), closed=True)
        self.add_arc('head-top', (21, 12), (27, 12), radius_x=3)
        self.add_arc('head-bottom', (27, 12), (21, 12), radius_x=3)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('torso', (24, 23), (24, 24))
        self.relate('connect', 'torso', 'boat')
        self.add_polyline('flag', (36, 24), (36, 8), (44, 8), (44, 16), (36, 16))
        self.relate('connect', 'flag', 'boat')
        self.add_polyline('water', (6, 40), (12, 39), (18, 40), (24, 39), (30, 40), (36, 39), (42, 40))
        self.mark_human_figure('passenger', head='head', torso='torso', torso_junction='start')
