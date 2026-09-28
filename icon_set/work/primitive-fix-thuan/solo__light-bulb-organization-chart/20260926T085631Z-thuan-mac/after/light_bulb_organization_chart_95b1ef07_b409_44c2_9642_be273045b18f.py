'Light bulb organization chart: independent spacing revision.\n\nLarger triangular node, separated square and filled circle under the bulb.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "95b1ef07-b409-44c2-9642-be273045b18f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__light-bulb-organization-chart/20260926T085631Z-thuan-mac/reference/idea strategy_95b1ef07-b409-44c2-9642-be273045b18f.svg"
AUTHOR = "claude-opus-5-5"

class LightBulbOrganizationChart(Solo48):
    icon_id = 'light-bulb-organization-chart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('bulb', 'organization', 'chart', 'strategy', 'idea', 'hierarchy')

    def build(self):
        # Symbol plan (HRECT_L x4..44, y8..40). Light bulb centred on x20 above
        # the middle branch: r6 globe (14,14)-(20,8)-(26,14), cubics narrowing
        # tangent-continuously to a neck x16..24 that stands on the branch bar
        # at y24. Bar from x4 to x38, split at the neck feet and the middle drop.
        # Leaves: dot (4,40) on the left drop, square x16..24 under the middle
        # drop, triangle apex (38,30) on the right drop.
        L = self.add_line
        join = lambda a, b: self.relate('connect', a, b)
        self.add_arc('globe-left', (14, 14), (20, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('globe-right', (20, 8), (26, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_bezier('taper-right', (26, 14), ((26, 17), (24, 18), (24, 21)))
        L('neck-right', (24, 21), (24, 24))
        L('neck-left', (16, 24), (16, 21))
        self.add_bezier('taper-left', (16, 21), ((16, 18), (14, 17), (14, 14)))
        self.add_contour('bulb', 'neck-left', 'taper-left', 'globe-left', 'globe-right', 'taper-right', 'neck-right')
        L('drop-left', (4, 40), (4, 24))
        L('bar-a', (4, 24), (16, 24))
        L('bar-b', (16, 24), (20, 24))
        L('bar-c', (20, 24), (24, 24))
        L('bar-d', (24, 24), (38, 24))
        L('drop-right', (38, 24), (38, 30))
        self.add_contour('branches', 'drop-left', 'bar-a', 'bar-b', 'bar-c', 'bar-d', 'drop-right')
        L('middle', (20, 24), (20, 32))
        join('bulb', 'branches'); join('middle', 'branches')
        self.add_polyline('square', (16, 32), (20, 32), (24, 32), (24, 40), (16, 40), closed=True)
        join('square', 'middle')
        self.add_polyline('triangle', (38, 30), (44, 40), (32, 40), closed=True)
        join('triangle', 'branches')
        self.add_dot('circle', (4, 40))
        join('circle', 'branches')
