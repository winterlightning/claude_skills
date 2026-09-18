"""Vertical Paperclip Attachment: user-requested grid-fitted 32px version of vertical-paperclip-attachment-solo.
Plan: retain source primitive/contour topology and fit VRECT_L ink (4, 0, 28, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='f9e485a4-15fe-4935-b76e-115de9c92c9b'
SOURCE_PATH='pictographic-primitives/other/attachment vertical_f9e485a4-15fe-4935-b76e-115de9c92c9b.svg'
SOLO_SOURCE_ICON_ID='vertical-paperclip-attachment-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='vertical-paperclip-attachment-sub32'
    keyshape=Keyshape.VRECT_L
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'vertical paperclip attachment')
    def build(self):
        self.add_arc('outer', (6, 12), (26, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('right', (26, 12), (26, 24))
        self.add_arc('bottom', (26, 24), (13, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('inner-left', (13, 24), (13, 13))
        self.add_arc('inner-top', (13, 13), (19, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('inner-right', (19, 13), (19, 22))
        self.add_contour('paperclip', 'outer', 'right', 'bottom', 'inner-left', 'inner-top', 'inner-right', closed=False)
        self.add_anchor('center',(16, 16))
