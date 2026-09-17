"""Test Tubes in Rack.

Plan: Two repeated U tubes on rack rails. Lucide test-tubes informs round bottoms; remove top flanges and liquid lines for clear tube interiors. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2080ea7e-3a5a-477c-adab-bbd27c3ad56a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/test tubes hang_2080ea7e-3a5a-477c-adab-bbd27c3ad56a.svg'
AUTHOR = 'gpt-6'


class TestTubesInRack(Solo48):
    icon_id = 'test-tubes-in-rack'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('test', 'tubes', 'in', 'rack')

    def build(self):
        for i in range(2):
            x=6+24*i;p=f'tube-{i}'
            self.add_line(p+'-left',(x,6),(x,26))
            self.add_arc(p+'-bottom-left',(x,26),(x+6,32),radius_x=6,sweep=False)
            self.add_arc(p+'-bottom-right',(x+6,32),(x+12,26),radius_x=6,sweep=False)
            self.add_line(p+'-right',(x+12,26),(x+12,6))
            self.add_contour(p,p+'-left',p+'-bottom-left',p+'-bottom-right',p+'-right')
        self.add_polyline('rack-top',(6,6),(18,6),(30,6),(42,6))
        self.add_polyline('rack-base',(6,42),(12,42),(36,42),(42,42))
        for i in range(2):
            x=12+24*i
            self.add_line(f'support-{i}',(x,32),(x,42))
            self.relate('connect','rack-top',f'tube-{i}')
            self.relate('connect',f'support-{i}',f'tube-{i}')
            self.relate('connect',f'support-{i}','rack-base')
