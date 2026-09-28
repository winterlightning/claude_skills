"""A round two-handled trophy on a rectangular pedestal; reduce the flared stem to a single structural stroke.

Live SQUARE bounds: visible (6,2)-(42,46), centerline (8,4)-(40,44)
for VRECT_L; SQUARE uses visible (4,4)-(44,44), centerline (6,6)-(42,42).
Lucide trophy informs the round bowl, stem hierarchy and mirrored handles.
The supplied reference sets the rectangular pedestal. Geometry authored independently on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abbd406d-6e5f-5db6-9a1c-7ce4e0abf31d'
SOURCE_PATH = 'pictographic-primitives/rewards/award trophy_abbd406d-6e5f-5db6-9a1c-7ce4e0abf31d.svg'
AUTHOR = 'gpt-6'

class TrophyCup(Solo48):
    icon_id = 'trophy-cup'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases = ()
    keywords = ('award', 'prize', 'recognition', 'trophy-cup')

    def build(self) -> None:
        self.add_line('cup-top-1', (14,16), (14,6))
        self.add_line('cup-top-2', (14,6), (34,6))
        self.add_line('cup-top-3', (34,6), (34,16))
        self.add_arc('bowl-right', (34,16), (24,26), radius_x=10)
        self.add_arc('bowl-left', (24,26), (14,16), radius_x=10)
        self.add_contour('cup','cup-top-1','cup-top-2','cup-top-3','bowl-right','bowl-left',closed=True)
        for side, sign in [('left',-1),('right',1)]:
            self.add_arc(side+'-handle',(24+sign*10,6),(24+sign*10,22),radius_x=8,sweep=sign==1)
            self.relate('connect','cup',side+'-handle')
        self.add_line('stem',(24,26),(24,34))
        self.add_polyline('base',(24,34),(34,34),(34,42),(14,42),(14,34),(24,34))
        self.relate('connect','stem','cup')
        self.relate('connect','stem','base')
