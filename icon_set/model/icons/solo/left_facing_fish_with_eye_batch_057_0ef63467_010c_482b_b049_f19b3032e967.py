"""Left-facing round fish: body with integral fins and forked tail, eye retained. Lucide fish informs tapered body and tail; omit gill to keep eye clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0ef63467-010c-482b-b049-f19b3032e967'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/goldfish_0ef63467-010c-482b-b049-f19b3032e967.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'left-facing-fish-with-eye-batch-057'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/fish'
    aliases = ()
    keywords = ('fish', 'sea', 'aquatic', 'fins', 'tail', 'animal')

    def build(self):
        def chain(name, *points):
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                member = f"{name}-{i+1}"
                self.add_line(member, a, b)
                members.append(member)
            return members
        self.add_arc('face-top', (4, 24), (18, 14), radius_x=14, radius_y=10)
        fins_top_run = chain('fins-top', (18, 14), (24, 8), (26, 16), (32, 20), (44, 12), (40, 24), (44, 36), (32, 28), (26, 32), (24, 40), (18, 34))
        self.add_arc('face-bottom', (18, 34), (4, 24), radius_x=14, radius_y=10)
        self.add_contour('fish', 'face-top', *fins_top_run, 'face-bottom', closed=True)
        self.add_dot('eye', (14, 24))
