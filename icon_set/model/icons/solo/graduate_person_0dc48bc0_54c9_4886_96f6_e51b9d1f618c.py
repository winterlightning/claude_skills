"""A head-and-shoulders graduate wears a mortarboard. VRECT_L extremes (8,6)-(40,42). Lucide graduation-cap informs the diamond; rounded head and shoulder arcs preserve a person. Drop the redundant forehead band and shoulder bottom closure to keep the face and shoulders open."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0dc48bc0-54c9-4886-96f6-e51b9d1f618c'
SOURCE_PATH = 'pictographic-primitives/symbol/graduate_0dc48bc0-54c9-4886-96f6-e51b9d1f618c.svg'
AUTHOR = 'gpt-6'

class GraduatePerson(Solo48):
    icon_id = 'graduate-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('graduate', 'student', 'person', 'education', 'mortarboard', 'school', 'degree', 'alumni')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_polyline('board', (8, 12), (24, 4), (40, 12), (34, 15), (24, 20), (14, 15), (8, 12), closed=True)
        self.add_arc('face', (14, 15), (34, 15), radius_x=10, radius_y=13, sweep=False)
        self.relate('connect', 'board', 'face')
        self.add_arc('shoulders', (8, 44), (40, 44), radius_x=16, radius_y=8)
