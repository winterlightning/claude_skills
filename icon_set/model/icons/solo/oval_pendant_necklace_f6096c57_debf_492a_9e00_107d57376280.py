'Necklace with Pendant.\n\nSymbol plan: Rounded necklace loop, straight connecting bail and oval pendant; remove tiny loop walls from bail.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6096c57-debf-492a-9e00-107d57376280'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jewellery_f6096c57-debf-492a-9e00-107d57376280.svg'
AUTHOR = 'gpt-6'

class OvalPendantNecklace(Solo48):
    icon_id = 'oval-pendant-necklace'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('oval', 'pendant', 'necklace')

    def build(self):
        # Rounded necklace loop, straight connecting bail and oval pendant; remove tiny loop walls from bail.
        axis_x = 24
        p_8_14 = (8, 14)
        p_18_39 = (18, 39)
        p_24_4 = (24, 4)
        p_24_24 = (24, 24)
        p_24_34 = (24, 34)
        p_24_44 = (24, 44)
        p_30_39 = (2 * axis_x - p_18_39[0], p_18_39[1])
        p_40_14 = (2 * axis_x - p_8_14[0], p_8_14[1])
        self.add_arc('chain-1', p_8_14, p_24_4, radius_x=16, radius_y=10, sweep=True)
        self.add_arc('chain-2', p_24_4, p_40_14, radius_x=16, radius_y=10, sweep=True)
        self.add_arc('chain-3', p_40_14, p_24_24, radius_x=16, radius_y=10, sweep=True)
        self.add_arc('chain-4', p_24_24, p_8_14, radius_x=16, radius_y=10, sweep=True)
        self.add_contour('chain', 'chain-1', 'chain-2', 'chain-3', 'chain-4', closed=True)
        self.add_line('bail-1', p_24_24, p_24_34)
        self.add_contour('bail', 'bail-1', closed=False)
        self.relate("connect", 'chain', 'bail')
        self.add_arc('pendant-1', p_24_34, p_30_39, radius_x=6, radius_y=5, sweep=True)
        self.add_arc('pendant-2', p_30_39, p_24_44, radius_x=6, radius_y=5, sweep=True)
        self.add_arc('pendant-3', p_24_44, p_18_39, radius_x=6, radius_y=5, sweep=True)
        self.add_arc('pendant-4', p_18_39, p_24_34, radius_x=6, radius_y=5, sweep=True)
        self.add_contour('pendant', 'pendant-1', 'pendant-2', 'pendant-3', 'pendant-4', closed=True)
        self.relate("connect", 'bail', 'pendant')
