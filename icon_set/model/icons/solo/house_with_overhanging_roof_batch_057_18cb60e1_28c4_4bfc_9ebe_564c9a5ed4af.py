"""Symmetric overhanging roof and blank body, with paired radius4 lower corners. Lucide house informs silhouette reduction; retain eaves, no door."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18cb60e1-28c4-4bfc-9ebe-564c9a5ed4af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/h4_18cb60e1-28c4-4bfc-9ebe-564c9a5ed4af.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'house-with-overhanging-roof-batch-057'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'architecture/houses'
    aliases = ()
    keywords = ('house', 'home', 'roof', 'building', 'shelter', 'outline')

    def build(self):
        def chain(name, *points):
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                member = f"{name}-{i+1}"
                self.add_line(member, a, b)
                members.append(member)
            return members
        axis = 24
        roof_run = chain('roof', (10, 24), (6, 24), (axis, 6), (42, 24), (38, 24), (38, 38))
        self.add_arc('corner-r', (38, 38), (34, 42), radius_x=4)
        self.add_line('base', (34, 42), (14, 42))
        self.add_arc('corner-l', (14, 42), (10, 38), radius_x=4)
        self.add_line('wall', (10, 38), (10, 24))
        self.add_contour('house', *roof_run, 'corner-r', 'base', 'corner-l', 'wall', closed=True)
