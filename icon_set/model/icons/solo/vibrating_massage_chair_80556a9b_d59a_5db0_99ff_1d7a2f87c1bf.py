"""Vibrating Massage Chair.

Plan: Side-view reclining chair with broad armrest and footrest. Lucide armchair informs rounded furniture joins; one vibration zigzag survives. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80556a9b-d59a-5db0-99ff-1d7a2f87c1bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage chair vibrate_80556a9b-d59a-5db0-99ff-1d7a2f87c1bf.svg'
AUTHOR = 'gpt-6'


class VibratingMassageChair(Solo48):
    icon_id = 'vibrating-massage-chair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('vibrating', 'massage', 'chair')

    def build(self):
        self.add_line('back-inner',(28,26),(34,10))
        self.add_arc('back-top',(34,10),(42,14),radius_x=5)
        self.add_line('back-outer',(42,14),(34,36))
        self.add_arc('back-base',(34,36),(26,42),radius_x=8,radius_y=6)
        self.add_polyline('seat-base',(26,42),(6,42),(6,34),(14,34),(14,26))
        self.add_arc('arm-top',(14,26),(20,20),radius_x=6)
        self.add_line('arm-flat',(20,20),(24,20))
        self.add_arc('arm-right',(24,20),(28,24),radius_x=4)
        self.add_line('arm-end',(28,24),(28,26))
        self.add_contour('chair','back-inner','back-top','back-outer','back-base','seat-base-1','seat-base-2','seat-base-3','seat-base-4','arm-top','arm-flat','arm-right','arm-end',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='seat-base']
        self.add_polyline('vibration',(6,6),(10,10),(6,14))
