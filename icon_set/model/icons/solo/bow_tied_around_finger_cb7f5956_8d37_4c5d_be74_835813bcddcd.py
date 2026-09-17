"""Bow Tied around Finger.

Plan: Two rounded bow loops tied above one long finger. Isolate the named finger; remove curled neighboring fingers. Shared human references inform rounded fingertip. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb7f5956-8d37-4c5d-be74-835813bcddcd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/raksha bandhan_cb7f5956-8d37-4c5d-be74-835813bcddcd.svg'
AUTHOR = 'gpt-6'

class BowTiedAroundFinger(Solo48):
    icon_id = 'bow-tied-around-finger'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/holidays'
    aliases = ()
    keywords = ('bow', 'tied', 'around', 'finger')

    def build(self):
        self.add_line('bow-l-top',(24,16),(14,4))
        self.add_arc('bow-l-end',(14,4),(8,10),radius_x=6,sweep=False)
        self.add_arc('bow-l-bottom',(8,10),(14,16),radius_x=6,sweep=False)
        self.add_line('bow-l-return',(14,16),(24,16))
        self.add_contour('bow-left','bow-l-top','bow-l-end','bow-l-bottom','bow-l-return',closed=True)
        self.add_line('bow-r-top',(24,16),(34,4))
        self.add_arc('bow-r-end',(34,4),(40,10),radius_x=6)
        self.add_arc('bow-r-bottom',(40,10),(34,16),radius_x=6)
        self.add_line('bow-r-return',(34,16),(24,16))
        self.add_contour('bow-right','bow-r-top','bow-r-end','bow-r-bottom','bow-r-return',closed=True)
        self.add_polyline('finger-sides',(20,40),(20,16),(24,16),(28,16),(28,40))
        self.add_arc('finger-tip',(28,40),(20,40),radius_x=4)
        self.add_contour('finger',*[f'finger-sides-{i}' for i in range(1,5)],'finger-tip',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='finger-sides']
        for a,b in [('finger','bow-left'),('finger','bow-right'),('bow-left','bow-right')]:self.relate('connect',a,b)
