'Human Endocrine Gland.\n\nSymbol plan: Visible capsule, connecting stalk and teardrop retained without asserting a specific gland anatomy.\nKeyshape: VRECT_M; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd567ff6d-187c-4af0-9596-85dcadc8d1e2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gland_d567ff6d-187c-4af0-9596-85dcadc8d1e2.svg'
AUTHOR = 'gpt-6'

class CapsuleConnectedToTeardropForm(Solo48):
    icon_id = 'capsule-connected-to-teardrop-form'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('capsule', 'connected', 'to', 'teardrop', 'form')

    def build(self):
        # Visible capsule, connecting stalk and teardrop retained without asserting a specific gland anatomy.
        axis_x = 24
        p_10_34 = (10, 34)
        p_10_38 = (10, 38)
        p_10_42 = (10, 42)
        p_18_44 = (18, 44)
        p_20_9 = (20, 9)
        p_20_17 = (20, 17)
        p_20_32 = (20, 32)
        p_24_44 = (24, 44)
        p_25_22 = (25, 22)
        p_25_29 = (25, 29)
        p_30_9 = (30, 9)
        p_30_17 = (30, 17)
        p_30_32 = (30, 32)
        p_30_44 = (2 * axis_x - p_18_44[0], p_18_44[1])
        p_38_34 = (2 * axis_x - p_10_34[0], p_10_34[1])
        p_38_38 = (2 * axis_x - p_10_38[0], p_10_38[1])
        p_38_42 = (2 * axis_x - p_10_42[0], p_10_42[1])
        self.add_arc('capsule-1', p_20_9, p_30_9, radius_x=5, radius_y=5, sweep=True)
        self.add_line('capsule-2', p_30_9, p_30_17)
        self.add_arc('capsule-3', p_30_17, p_20_17, radius_x=5, radius_y=5, sweep=True)
        self.add_line('capsule-4', p_20_17, p_20_9)
        self.add_contour('capsule', 'capsule-1', 'capsule-2', 'capsule-3', 'capsule-4', closed=True)
        self.add_line('stalk-1', p_25_22, p_25_29)
        self.add_contour('stalk', 'stalk-1', closed=False)
        self.relate("connect", 'capsule', 'stalk')
        self.add_bezier('drop-1', p_25_29, (p_30_32, p_38_34, p_38_38))
        self.add_bezier('drop-2', p_38_38, (p_38_42, p_30_44, p_24_44))
        self.add_bezier('drop-3', p_24_44, (p_18_44, p_10_42, p_10_38))
        self.add_bezier('drop-4', p_10_38, (p_10_34, p_20_32, p_25_29))
        self.add_contour('drop', 'drop-1', 'drop-2', 'drop-3', 'drop-4', closed=True)
        self.relate("connect", 'stalk', 'drop')
