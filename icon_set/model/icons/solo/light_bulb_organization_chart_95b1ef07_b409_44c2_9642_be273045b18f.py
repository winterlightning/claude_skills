"""A glowing light bulb sits atop a branching organization chart. A central stem joins a horizontal crossbar whose three descending branches end in a circle, square and triangle.
Lucide lightbulb and network construction. Three distinct nodes retain circle, square, and triangle identity. Rays and socket threads omitted; node widths and spacing are balanced.
HRECT_L: centerline extremes (6,8)-(42,40); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95b1ef07-b409-44c2-9642-be273045b18f'
SOURCE_PATH = 'pictographic-primitives/work/idea strategy_95b1ef07-b409-44c2-9642-be273045b18f.svg'
AUTHOR = 'gpt-6'


class LightBulbOrganizationChart(Solo48):
    icon_id = 'light-bulb-organization-chart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('bulb', 'organization', 'chart', 'strategy', 'idea', 'hierarchy')

    def build(self) -> None:
        self.add_line('stem', (20, 23), (20, 20))
        self.add_line('base-right', (20, 20), (24, 20))
        self.add_arc('bulb-right', (24, 20), (26, 14), radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('bulb-top', (26, 14), (14, 14), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('bulb-left', (14, 14), (16, 20), radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_line('base-left', (16, 20), (20, 20))
        self.add_contour('bulb', 'stem', 'base-right', 'bulb-right', 'bulb-top', 'bulb-left', 'base-left', closed=False)
        self.add_polyline('branches', (6, 36), (6, 23), (20, 23), (38, 23), (38, 28), closed=False)
        self.relate("connect", 'bulb', 'branches')
        self.add_line('middle-branch', (20, 23), (20, 29))
        self.relate("connect", 'branches', 'middle-branch')
        self.relate("connect", 'bulb', 'middle-branch')
        self.add_arc('circle-node-top', (6, 38), (8, 38), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('circle-node-bottom', (8, 38), (6, 38), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('circle-node', 'circle-node-top', 'circle-node-bottom', closed=True)
        self.relate("connect", 'circle-node', 'branches')
        self.add_polyline('square-node', (16, 29), (24, 29), (24, 37), (16, 37), closed=True)
        self.relate("connect", 'square-node', 'middle-branch')
        self.add_polyline('triangle-node', (38, 28), (42, 40), (32, 40), closed=True)
        self.relate("connect", 'triangle-node', 'branches')
