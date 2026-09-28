"""Celebration Party Popper.
Plan: Diagonal cone with rounded open mouth and separated streamer rays. Centerline extremes (6,6)-(42,42).
Reference: Lucide party-popper: diagonal cone, open mouth, detached confetti.
Reduction: Four trails reduced to three.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2103913-ba9e-5954-8fb2-1cee611d02d2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/party confetti_f2103913-ba9e-5954-8fb2-1cee611d02d2.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'party-popper-open-cone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('celebration', 'party', 'popper')

    def build(self):

        self.add_polyline('cone',(14,20),(6,42),(28,34))
        self.add_arc('mouth-outer',(14,20),(28,34),radius_x=10,sweep=True)
        self.add_arc('mouth-inner',(28,34),(14,20),radius_x=18,sweep=True)
        self.add_contour('mouth','mouth-outer','mouth-inner',closed=True)
        self.relate('connect','cone','mouth')
        self.add_line('trail-up',(18,6),(18,9))
        self.add_line('trail-diagonal',(33,13),(38,6))
        self.add_arc('trail-right',(39,28),(42,27),radius_x=10)
