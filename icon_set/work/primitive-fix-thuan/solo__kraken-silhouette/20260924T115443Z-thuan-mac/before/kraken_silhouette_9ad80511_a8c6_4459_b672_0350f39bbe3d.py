'Minimalist Kraken Symbol.\n\nSymbol plan: Large central dome with two curling side tentacles; no invented face or additional limbs.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ad80511-a8c6-4459-b672-0350f39bbe3d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kraken_9ad80511-a8c6-4459-b672-0350f39bbe3d.svg'
AUTHOR = 'gpt-6'

class KrakenSilhouette(Solo48):
    icon_id = 'kraken-silhouette'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('kraken', 'silhouette')

    def build(self):
        # Large central dome with two curling side tentacles; no invented face or additional limbs.
        axis_x = 24
        p_4_28 = (4, 28)
        p_6_40 = (6, 40)
        p_9_28 = (9, 28)
        p_12_40 = (12, 40)
        p_14_20 = (14, 20)
        p_14_28 = (14, 28)
        p_14_33 = (14, 33)
        p_18_40 = (18, 40)
        p_24_8 = (24, 8)
        p_30_40 = (2 * axis_x - p_18_40[0], p_18_40[1])
        p_34_20 = (2 * axis_x - p_14_20[0], p_14_20[1])
        p_34_28 = (2 * axis_x - p_14_28[0], p_14_28[1])
        p_34_33 = (2 * axis_x - p_14_33[0], p_14_33[1])
        p_36_40 = (2 * axis_x - p_12_40[0], p_12_40[1])
        p_39_28 = (2 * axis_x - p_9_28[0], p_9_28[1])
        p_42_40 = (2 * axis_x - p_6_40[0], p_6_40[1])
        p_44_28 = (2 * axis_x - p_4_28[0], p_4_28[1])
        self.add_bezier('kraken-1', p_4_28, (p_9_28, p_6_40, p_12_40))
        self.add_bezier('kraken-2', p_12_40, (p_18_40, p_14_33, p_14_28))
        self.add_line('kraken-3', p_14_28, p_14_20)
        self.add_arc('kraken-4', p_14_20, p_24_8, radius_x=10, radius_y=12, sweep=True)
        self.add_arc('kraken-5', p_24_8, p_34_20, radius_x=10, radius_y=12, sweep=True)
        self.add_line('kraken-6', p_34_20, p_34_28)
        self.add_bezier('kraken-7', p_34_28, (p_34_33, p_30_40, p_36_40))
        self.add_bezier('kraken-8', p_36_40, (p_42_40, p_39_28, p_44_28))
        self.add_contour('kraken', 'kraken-1', 'kraken-2', 'kraken-3', 'kraken-4', 'kraken-5', 'kraken-6', 'kraken-7', 'kraken-8', closed=False)
