"""Completed Task Checklist: user-requested grid-fitted 32px version of completed-task-checklist-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='7cfb0a8d-3a06-46ff-b6d2-3ff796fbca84'
SOURCE_PATH='pictographic-primitives/content/list_7cfb0a8d-3a06-46ff-b6d2-3ff796fbca84.svg'
SOLO_SOURCE_ICON_ID='completed-task-checklist-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='completed-task-checklist-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'content'
    categories = ('content', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'completed task checklist')
    def build(self):
        self.add_line('outline-0', (6, 2), (26, 2))
        self.add_arc('outline-1', (26, 2), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-2', (30, 6), (30, 26))
        self.add_arc('outline-3', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-4', (26, 30), (6, 30))
        self.add_arc('outline-5', (6, 30), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-6', (2, 26), (2, 6))
        self.add_arc('outline-7', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('check-16-1', (9, 10), (12, 12))
        self.add_line('check-16-2', (12, 12), (16, 9))
        self.add_line('text-16', (23, 10), (23, 10))
        self.add_line('check-30-1', (9, 21), (12, 23))
        self.add_line('check-30-2', (12, 23), (16, 20))
        self.add_line('text-30', (23, 21), (23, 21))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.add_contour('check-16', 'check-16-1', 'check-16-2', closed=False)
        self.add_contour('check-30', 'check-30-1', 'check-30-2', closed=False)
        self.add_anchor('center',(16, 16))
