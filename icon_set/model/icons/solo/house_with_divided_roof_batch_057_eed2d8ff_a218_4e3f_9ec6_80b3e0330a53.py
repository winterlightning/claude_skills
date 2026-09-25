"""Symmetric triangular roof separated from blank body; shared eave nodes and radius4 lower corners. Lucide house informs smooth lower corners. No omissions."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eed2d8ff-a218-4e3f-9ec6-80b3e0330a53'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/h2_eed2d8ff-a218-4e3f-9ec6-80b3e0330a53.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'house-with-divided-roof-batch-057'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('house', 'home', 'building', 'roof', 'dwelling', 'architecture')

    def build(self):
        def chain(name, *points):
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                member = f"{name}-{i+1}"
                self.add_line(member, a, b)
                members.append(member)
            return members
        left, right, top, eave, bottom, r = (6, 42, 6, 22, 42, 4)
        roof_run = chain('roof', (left, eave), (24, top), (right, eave))
        self.add_line('divider', (left, eave), (right, eave))
        self.add_line('wall-r', (right, eave), (right, bottom - r))
        self.add_arc('corner-r', (right, bottom - r), (right - r, bottom), radius_x=r)
        self.add_line('base', (right - r, bottom), (left + r, bottom))
        self.add_arc('corner-l', (left + r, bottom), (left, bottom - r), radius_x=r)
        self.add_line('wall-l', (left, bottom - r), (left, eave))
        self.add_contour('house', *roof_run, 'wall-r', 'corner-r', 'base', 'corner-l', 'wall-l', closed=True)
        self.relate('connect', 'divider', 'house')
