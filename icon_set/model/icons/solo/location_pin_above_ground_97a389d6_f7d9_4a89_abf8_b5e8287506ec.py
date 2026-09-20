'Map Pin Location Marker.\n\nSymbol plan: Pin above ground line, retained as one location subject.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: map-pin.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97a389d6-f7d9-4a89-abf8-b5e8287506ec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/location dot_97a389d6-f7d9-4a89-abf8-b5e8287506ec.svg'
AUTHOR = 'gpt-6'

class LocationPinAboveGround(Solo48):
    icon_id = 'location-pin-above-ground'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('location', 'pin', 'above', 'ground')

    def build(self):
        # Pin above ground line, retained as one location subject.
        axis_x = 24
        p_8_44 = (8, 44)
        p_10_17 = (10, 17)
        p_10_23 = (10, 23)
        p_20_17 = (20, 17)
        p_20_32 = (20, 32)
        p_24_35 = (24, 35)
        p_28_17 = (2 * axis_x - p_20_17[0], p_20_17[1])
        p_28_32 = (2 * axis_x - p_20_32[0], p_20_32[1])
        p_38_17 = (2 * axis_x - p_10_17[0], p_10_17[1])
        p_38_23 = (2 * axis_x - p_10_23[0], p_10_23[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_arc('pin-1', p_10_17, p_38_17, radius_x=14, radius_y=13, sweep=True)
        self.add_bezier('pin-2', p_38_17, (p_38_23, p_28_32, p_24_35))
        self.add_bezier('pin-3', p_24_35, (p_20_32, p_10_23, p_10_17))
        self.add_contour('pin', 'pin-1', 'pin-2', 'pin-3', closed=True)
        self.add_arc('opening-1', p_20_17, p_28_17, radius_x=4, radius_y=4, sweep=True)
        self.add_arc('opening-2', p_28_17, p_20_17, radius_x=4, radius_y=4, sweep=True)
        self.add_contour('opening', 'opening-1', 'opening-2', closed=True)
        self.add_line('ground-1', p_8_44, p_40_44)
        self.add_contour('ground', 'ground-1', closed=False)
