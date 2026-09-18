"""Checklist Document for Tasks: user-requested grid-fitted 32px version of checklist-document-for-tasks-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3b7aa072-22e2-420b-a990-9a6447b66ea3'
SOURCE_PATH = 'pictographic-primitives/symbol/task list_3b7aa072-22e2-420b-a990-9a6447b66ea3.svg'
SOLO_SOURCE_ICON_ID = 'checklist-document-for-tasks-solo'
AUTHOR = 'gpt-6'

class Drawing(Sub32):
    icon_id = 'checklist-document-for-tasks-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'grid fitted', 'checklist document for tasks')

    def build(self):
        self.add_line('page-1', (4, 2), (20, 2))
        self.add_line('page-2', (20, 2), (28, 9))
        self.add_line('page-3', (28, 9), (28, 30))
        self.add_line('page-4', (28, 30), (4, 30))
        self.add_line('page-5', (4, 30), (4, 2))
        self.add_arc('box-17-top', (10, 11), (16, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('box-17-bottom', (16, 11), (10, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('text-17', (21, 12), (21, 12))
        self.add_arc('box-33-top', (10, 22), (16, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('box-33-bottom', (16, 22), (10, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('text-33', (21, 23), (21, 23))
        self.add_contour('page', 'page-1', 'page-2', 'page-3', 'page-4', 'page-5', closed=True)
        self.add_contour('box-17', 'box-17-top', 'box-17-bottom', closed=True)
        self.add_contour('box-33', 'box-33-top', 'box-33-bottom', closed=True)
        self.add_anchor('center', (16, 16))
