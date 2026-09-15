"""Three rounded L-shaped chevrons of increasing size stack diagonally, each pointing to the upper right.

Plan: Three northeast elbows repeat diagonally with increasing arm length.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected corner-down-right: joined elbow strokes.
Simplification: Outlined L ribbons become monoline elbows.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '725a957e-63e3-4f03-87bd-d37db9fb9241'
SOURCE_PATH = 'pictographic-primitives/logos/jira logo_725a957e-63e3-4f03-87bd-d37db9fb9241.svg'
AUTHOR = 'gpt-6'


class JiraLogo(Solo48):
    icon_id = 'jira-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('jira', 'atlassian', 'project-management', 'logo', 'brand', 'agile', 'tickets')

    def build(self):
        for i,(x,y,length) in enumerate([(6,30,12),(16,18,14),(26,6,16)]):
         self.add_polyline(f'elbow{i}',(x,y),(x+length,y),(x+length,y+12))
