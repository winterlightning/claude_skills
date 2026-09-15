"""A statuette with detached oval head, close arms and a rounded pedestal; omit face and fingers.

Live keyshape centerlines: VRECT_L (8,4)-(40,44); SQUARE (6,6)-(42,42);
HRECT_L (4,8)-(44,40). Shared dimensions preserve paired proportions.
Lucide trophy (pedestal hierarchy); no useful local statuette match: geometric construction; supplied reference: subject identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='726e04de-dea0-4e56-bc16-b2ff281f481e'
SOURCE_PATH='pictographic-primitives/rewards/oscar_726e04de-dea0-4e56-bc16-b2ff281f481e.svg'
AUTHOR='gpt-6'

class OscarStatuetteRoundedBase(Solo48):
    icon_id='oscar-statuette-rounded-base'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/award'
    aliases=()
    keywords=('award', 'reward', 'oscar-statuette-rounded-base')
    def build(self) -> None:
        self.add_arc('head-right',(24,4),(24,10),radius_x=3,radius_y=3)
        self.add_arc('head-left',(24,10),(24,4),radius_x=3,radius_y=3)
        self.add_contour('head','head-right','head-left',closed=True)
        self.add_polyline('figure',(16,19),(14,26),(20,28),(20,36),(28,36),(28,28),(34,26),(32,19),(16,19))
        self.add_line('base-top-left',(12,36),(20,36))
        self.add_line('base-top-right',(28,36),(36,36))
        self.add_arc('base-right',(36,36),(40,40),radius_x=4)
        self.add_line('base-side-right',(40,40),(40,44))
        self.add_line('base-bottom',(40,44),(8,44))
        self.add_line('base-side-left',(8,44),(8,40))
        self.add_arc('base-left',(8,40),(12,36),radius_x=4)
        self.add_contour('base','base-top-right','base-right','base-side-right','base-bottom','base-side-left','base-left','base-top-left')
        self.relate('connect','figure','base')

