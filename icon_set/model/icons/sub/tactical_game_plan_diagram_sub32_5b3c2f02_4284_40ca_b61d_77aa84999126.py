"""Tactical Game Plan Diagram: user-requested grid-fitted 32px version of tactical-game-plan-diagram-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='5b3c2f02-4284-40ca-b61d-77aa84999126'
SOURCE_PATH='pictographic-primitives/state/strategy_5b3c2f02-4284-40ca-b61d-77aa84999126.svg'
SOLO_SOURCE_ICON_ID='tactical-game-plan-diagram-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='tactical-game-plan-diagram-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'tactical game plan diagram')
    def build(self):
        self.add_line('outline-0', (6, 2), (26, 2))
        self.add_arc('outline-1', (26, 2), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-2', (30, 6), (30, 26))
        self.add_arc('outline-3', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-4', (26, 30), (6, 30))
        self.add_arc('outline-5', (6, 30), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-6', (2, 26), (2, 6))
        self.add_arc('outline-7', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('start-top', (9, 21), (14, 21), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('start-bottom', (14, 21), (9, 21), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_bezier('route', (11, 18), ((11, 18), (21, 19), (21, 11)))
        self.add_line('head-1', (18, 14), (21, 11))
        self.add_line('head-2', (21, 11), (23, 14))
        self.add_line('cross-a', (9, 9), (12, 12))
        self.add_line('cross-b', (9, 12), (12, 9))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.add_contour('start', 'start-top', 'start-bottom', closed=True)
        self.add_contour('head', 'head-1', 'head-2', closed=False)
        self.relate('connect', 'start', 'route')
        self.relate('connect', 'route', 'head')
        self.relate('connect', 'cross-a', 'cross-b')
        self.add_anchor('center',(16, 16))
