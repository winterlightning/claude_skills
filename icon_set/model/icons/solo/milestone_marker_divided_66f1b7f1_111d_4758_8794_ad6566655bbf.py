"""Milestone Marker, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '66f1b7f1-111d-4758-8794-ad6566655bbf'
SOURCE_PATH = 'pictographic-primitives/transportation/milestone_66f1b7f1-111d-4758-8794-ad6566655bbf.svg'
AUTHOR = 'gpt-6'

class MilestoneMarkerDivided(Solo48):
    icon_id = 'milestone-marker-divided'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('milestone', 'marker', 'stone', 'roadside', 'distance', 'landmark', 'waypoint', 'monument')

    def build(self) -> None:
        # Current contract centerline extremes: (8,6)-(40,42).
        self.add_arc('arch',(12,16),(36,16),radius_x=12)
        self.add_polyline('stone-right',(36,16),(36,36))
        self.add_polyline('stone-left',(12,36),(12,16))
        self.add_polyline('arch-base',(12,16),(24,16),(36,16))
        self.add_polyline('plinth',(8,36),(12,36),(24,36),(36,36),(40,36),(40,42),(8,42),closed=True)
        self.add_line('divider',(24,16),(24,36))
        for part in ('stone-left','stone-right','arch-base'):self.relate('connect','arch',part)
        self.relate('connect','stone-left','arch-base')
        self.relate('connect','stone-right','arch-base')
        for part in ('stone-left','stone-right','divider'):self.relate('connect','plinth',part)
        self.relate('connect','divider','arch-base')
