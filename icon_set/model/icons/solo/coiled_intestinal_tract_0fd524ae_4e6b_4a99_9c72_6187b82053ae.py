'Human Digestive Intestines.\n\nSymbol plan: Continuous three-bend intestinal meander with inlet and outlet; doubled walls reduced to one round-ended tubular stroke.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fd524ae-4e6b-4a99-9c72-6187b82053ae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/intestine_0fd524ae-4e6b-4a99-9c72-6187b82053ae.svg'
AUTHOR = 'gpt-6'

class CoiledIntestinalTract(Solo48):
    icon_id = 'coiled-intestinal-tract'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('coiled', 'intestinal', 'tract')

    def build(self):
        # Continuous three-bend intestinal meander with inlet and outlet; doubled walls reduced to one round-ended tubular stroke.
        axis_x = 24
        p_14_10 = (14, 10)
        p_14_22 = (14, 22)
        p_14_40 = (14, 40)
        p_14_44 = (14, 44)
        p_20_34 = (20, 34)
        p_24_4 = (24, 4)
        p_24_10 = (24, 10)
        p_34_22 = (2 * axis_x - p_14_22[0], p_14_22[1])
        p_34_34 = (34, 34)
        self.add_line('intestine-1', p_24_4, p_24_10)
        self.add_line('intestine-2', p_24_10, p_14_10)
        self.add_arc('intestine-3', p_14_10, p_14_22, radius_x=6, radius_y=6, sweep=False)
        self.add_line('intestine-4', p_14_22, p_34_22)
        self.add_arc('intestine-5', p_34_22, p_34_34, radius_x=6, radius_y=6, sweep=True)
        self.add_line('intestine-6', p_34_34, p_20_34)
        self.add_arc('intestine-7', p_20_34, p_14_40, radius_x=6, radius_y=6, sweep=False)
        self.add_line('intestine-8', p_14_40, p_14_44)
        self.add_contour('intestine', 'intestine-1', 'intestine-2', 'intestine-3', 'intestine-4', 'intestine-5', 'intestine-6', 'intestine-7', 'intestine-8', closed=False)
