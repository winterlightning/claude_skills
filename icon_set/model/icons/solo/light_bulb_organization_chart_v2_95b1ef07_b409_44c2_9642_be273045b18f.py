# Variant of light-bulb-organization-chart; parent file remains unchanged.
'Light bulb organization chart: independent spacing revision.\n\nLarger triangular node, separated square and filled circle under the bulb.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '95b1ef07-b409-44c2-9642-be273045b18f'
SOURCE_PATH = 'pictographic-primitives/work/idea strategy_95b1ef07-b409-44c2-9642-be273045b18f.svg'
AUTHOR = 'gpt-6'

class LightBulbOrganizationChartVariant2(Solo48):
    icon_id = 'light-bulb-organization-chart-v2'
    variant_of = 'light-bulb-organization-chart'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('bulb', 'organization', 'chart', 'strategy', 'idea', 'hierarchy')

    def build(self):
        self.add_arc('bulba',(20, 12),(28, 12),radius_x=4,radius_y=4)
        self.add_arc('bulbb',(28, 12),(20, 12),radius_x=4,radius_y=4)
        self.add_contour('bulb','bulba','bulbb',closed=True)
        self.add_line('stem',(24, 16),(24, 24))
        self.add_polyline('branches',(4, 40),(4, 24),(20, 24),(24, 24),(38, 24),(38, 30),closed=False)
        self.add_line('middle',(20, 24),(20, 32))
        self.relate('connect','bulb','stem')
        self.relate('connect','stem','branches')
        self.relate('connect','middle','branches')
        self.add_polyline('square',(16, 32),(20, 32),(24, 32),(24, 40),(16, 40),closed=True)
        self.relate('connect','square','middle')
        self.add_polyline('triangle',(38, 30),(44, 40),(32, 40),closed=True)
        self.relate('connect','triangle','branches')
        self.add_dot('circle',(4, 40))
        self.relate('connect','circle','branches')
