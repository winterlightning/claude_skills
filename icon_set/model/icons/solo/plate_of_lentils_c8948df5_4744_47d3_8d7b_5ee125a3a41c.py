'Lentils in a Bowl.\n\nSymbol plan: Plate with four lentils in a repeated grid; reduce seven scattered lentils to maintain clearance.\nKeyshape: CIRCLE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8948df5-4744-47d3-8d7b-5ee125a3a41c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/lentil_c8948df5-4744-47d3-8d7b-5ee125a3a41c.svg'
AUTHOR = 'gpt-6'

class PlateOfLentils(Solo48):
    icon_id = 'plate-of-lentils'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('plate', 'of', 'lentils')

    def build(self):
        # Plate with four lentils in a repeated grid; reduce seven scattered lentils to maintain clearance.
        axis_x = 24
        p_4_24 = (4, 24)
        p_16_18 = (16, 18)
        p_16_30 = (16, 30)
        p_20_18 = (20, 18)
        p_20_30 = (20, 30)
        p_28_18 = (2 * axis_x - p_20_18[0], p_20_18[1])
        p_28_30 = (2 * axis_x - p_20_30[0], p_20_30[1])
        p_32_18 = (2 * axis_x - p_16_18[0], p_16_18[1])
        p_32_30 = (2 * axis_x - p_16_30[0], p_16_30[1])
        p_44_24 = (2 * axis_x - p_4_24[0], p_4_24[1])
        self.add_arc('plate-1', p_4_24, p_44_24, radius_x=20, radius_y=20, sweep=True)
        self.add_arc('plate-2', p_44_24, p_4_24, radius_x=20, radius_y=20, sweep=True)
        self.add_contour('plate', 'plate-1', 'plate-2', closed=True)
        self.add_arc('lentil-18-18-1', p_16_18, p_20_18, radius_x=2, radius_y=2, sweep=True)
        self.add_arc('lentil-18-18-2', p_20_18, p_16_18, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('lentil-18-18', 'lentil-18-18-1', 'lentil-18-18-2', closed=True)
        self.add_arc('lentil-18-30-1', p_16_30, p_20_30, radius_x=2, radius_y=2, sweep=True)
        self.add_arc('lentil-18-30-2', p_20_30, p_16_30, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('lentil-18-30', 'lentil-18-30-1', 'lentil-18-30-2', closed=True)
        self.add_arc('lentil-30-18-1', p_28_18, p_32_18, radius_x=2, radius_y=2, sweep=True)
        self.add_arc('lentil-30-18-2', p_32_18, p_28_18, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('lentil-30-18', 'lentil-30-18-1', 'lentil-30-18-2', closed=True)
        self.add_arc('lentil-30-30-1', p_28_30, p_32_30, radius_x=2, radius_y=2, sweep=True)
        self.add_arc('lentil-30-30-2', p_32_30, p_28_30, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('lentil-30-30', 'lentil-30-30-1', 'lentil-30-30-2', closed=True)
