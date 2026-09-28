"""Person in Dragon Boat.

Plan: Left dragon prow and seated passenger over deep hull; centerlines (6,6)-(42,42).
Construction: Lucide sailboat rounded hull and human_ref detached circular head.
Reduction: Omitted eye and wave decoration; silhouette retains snout and crest.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'c288b0dd-b2d8-52ee-8466-959715e29cdf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-in-dragon-boat/20260927T153747Z-thuan-mac-1/reference/dragon boat festival_c288b0dd-b2d8-52ee-8466-959715e29cdf.svg'
AUTHOR = "gpt-6"


class IconPersonInDragonBoat(Solo48):
    icon_id = 'person-in-dragon-boat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('person', 'in', 'dragon', 'boat')

    def build(self):
        # Dragon prow, shallow hull, lone passenger, and three water crests.
        self.add_polyline('boat', (6, 18), (14, 18), (18, 10), (18, 26), (35, 26), (42, 22), (40, 28), (34, 32), (18, 32), (10, 27), (6, 22), closed=True)
        self.add_arc('head-top', (27, 10), (35, 10), radius_x=4)
        self.add_arc('head-bottom', (35, 10), (27, 10), radius_x=4)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('torso', (31, 22), (31, 26))
        self.relate('connect', 'torso', 'boat')
        self.add_polyline('water', (8, 42), (13, 40), (18, 42), (23, 40), (28, 42), (33, 40), (38, 42))
        self.mark_human_figure('passenger', head='head', torso='torso', torso_junction='start')
