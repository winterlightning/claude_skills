'Multi-Story Apartment Building.\n\nSymbol plan: Four windows in an equal two-by-two series above a central arched entrance; windows reduced to solid marks.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1bd1e63-3299-43d7-a4b6-d4973b2cff06'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tenement_e1bd1e63-3299-43d7-a4b6-d4973b2cff06.svg'
AUTHOR = 'gpt-6'

class FourWindowApartmentBuilding(Solo48):
    icon_id = 'four-window-apartment-building'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('four', 'window', 'apartment', 'building')

    def build(self):
        # Four windows in an equal two-by-two series above a central arched entrance; windows reduced to solid marks.
        axis_x = 24
        p_8_4 = (8, 4)
        p_8_44 = (8, 44)
        p_18_14 = (18, 14)
        p_18_23 = (18, 23)
        p_19_35 = (19, 35)
        p_19_44 = (19, 44)
        p_29_35 = (2 * axis_x - p_19_35[0], p_19_35[1])
        p_29_44 = (2 * axis_x - p_19_44[0], p_19_44[1])
        p_30_14 = (2 * axis_x - p_18_14[0], p_18_14[1])
        p_30_23 = (2 * axis_x - p_18_23[0], p_18_23[1])
        p_40_4 = (2 * axis_x - p_8_4[0], p_8_4[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_line('building-1', p_8_4, p_40_4)
        self.add_line('building-2', p_40_4, p_40_44)
        self.add_line('building-3', p_40_44, p_8_44)
        self.add_line('building-4', p_8_44, p_8_4)
        self.add_contour('building', 'building-1', 'building-2', 'building-3', 'building-4', closed=True)
        self.add_line('door-1', p_19_44, p_19_35)
        self.add_arc('door-2', p_19_35, p_29_35, radius_x=5, radius_y=5, sweep=True)
        self.add_line('door-3', p_29_35, p_29_44)
        self.add_contour('door', 'door-1', 'door-2', 'door-3', closed=False)
        self.relate("connect", 'building', 'door')
        self.add_line('window-18-14-1', p_18_14, p_18_14)
        self.add_contour('window-18-14', 'window-18-14-1', closed=False)
        self.add_line('window-18-23-1', p_18_23, p_18_23)
        self.add_contour('window-18-23', 'window-18-23-1', closed=False)
        self.add_line('window-30-14-1', p_30_14, p_30_14)
        self.add_contour('window-30-14', 'window-30-14-1', closed=False)
        self.add_line('window-30-23-1', p_30_23, p_30_23)
        self.add_contour('window-30-23', 'window-30-23-1', closed=False)
