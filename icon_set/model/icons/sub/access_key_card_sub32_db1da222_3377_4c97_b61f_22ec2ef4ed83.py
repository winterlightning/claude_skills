"""Access Key Card: user-requested grid-fitted 32px version of access-key-card-solo.
Plan: retain source primitive/contour topology and fit VRECT_L ink (4, 0, 28, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='db1da222-3377-4c97-b61f-22ec2ef4ed83'
SOURCE_PATH='pictographic-primitives/other/key vertical rectangcle_db1da222-3377-4c97-b61f-22ec2ef4ed83.svg'
SOLO_SOURCE_ICON_ID='access-key-card-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='access-key-card-sub32'
    keyshape=Keyshape.VRECT_L
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'access key card')
    def build(self):
        self.add_line('card-0', (9, 2), (23, 2))
        self.add_arc('card-1', (23, 2), (26, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('card-2', (26, 5), (26, 27))
        self.add_arc('card-3', (26, 27), (23, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('card-4', (23, 30), (9, 30))
        self.add_arc('card-5', (9, 30), (6, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('card-6', (6, 27), (6, 5))
        self.add_arc('card-7', (6, 5), (9, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('key-bow-top', (13, 12), (19, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('key-bow-bottom', (19, 12), (13, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('key-stem-1', (16, 15), (16, 22))
        self.add_line('key-stem-2', (16, 22), (19, 22))
        self.add_contour('card', 'card-0', 'card-1', 'card-2', 'card-3', 'card-4', 'card-5', 'card-6', 'card-7', closed=True)
        self.add_contour('key-bow', 'key-bow-top', 'key-bow-bottom', closed=True)
        self.add_contour('key-stem', 'key-stem-1', 'key-stem-2', closed=False)
        self.relate('connect', 'key-bow', 'key-stem')
        self.add_anchor('center',(16, 16))
