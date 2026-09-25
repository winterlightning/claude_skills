'Modern Doorbell Button.\n\nSymbol plan: Tall pill-shaped mounting plate with one central circular doorbell button.\nKeyshape: VRECT_M; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98f12741-22af-40d9-ac63-b267d9991649'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/doorbell_98f12741-22af-40d9-ac63-b267d9991649.svg'
AUTHOR = 'gpt-6'

class ModernDoorbellButton(Solo48):
    icon_id = 'modern-doorbell-button'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('modern', 'doorbell', 'button')

    def build(self):
        # Tall pill-shaped mounting plate with one central circular doorbell button.
        axis_x = 24
        p_10_16 = (10, 16)
        p_10_32 = (10, 32)
        p_19_24 = (19, 24)
        p_22_4 = (22, 4)
        p_22_44 = (22, 44)
        p_26_4 = (2 * axis_x - p_22_4[0], p_22_4[1])
        p_26_44 = (2 * axis_x - p_22_44[0], p_22_44[1])
        p_29_24 = (2 * axis_x - p_19_24[0], p_19_24[1])
        p_38_16 = (2 * axis_x - p_10_16[0], p_10_16[1])
        p_38_32 = (2 * axis_x - p_10_32[0], p_10_32[1])
        self.add_line('plate-1', p_22_4, p_26_4)
        self.add_arc('plate-2', p_26_4, p_38_16, radius_x=12, radius_y=12, sweep=True)
        self.add_line('plate-3', p_38_16, p_38_32)
        self.add_arc('plate-4', p_38_32, p_26_44, radius_x=12, radius_y=12, sweep=True)
        self.add_line('plate-5', p_26_44, p_22_44)
        self.add_arc('plate-6', p_22_44, p_10_32, radius_x=12, radius_y=12, sweep=True)
        self.add_line('plate-7', p_10_32, p_10_16)
        self.add_arc('plate-8', p_10_16, p_22_4, radius_x=12, radius_y=12, sweep=True)
        self.add_contour('plate', 'plate-1', 'plate-2', 'plate-3', 'plate-4', 'plate-5', 'plate-6', 'plate-7', 'plate-8', closed=True)
        self.add_arc('button-1', p_19_24, p_29_24, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('button-2', p_29_24, p_19_24, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('button', 'button-1', 'button-2', closed=True)
