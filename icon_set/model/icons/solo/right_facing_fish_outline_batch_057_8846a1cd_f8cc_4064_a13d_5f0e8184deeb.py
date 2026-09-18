"""Right-facing fish with integral small fins and forked tail. Lucide fish informs coherent outline. Omit eye as in source; gill is a separate curved mark."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8846a1cd-f8cc-4064-a13d-5f0e8184deeb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/halibut_8846a1cd-f8cc-4064-a13d-5f0e8184deeb.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'right-facing-fish-outline-batch-057'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/fish'
    aliases = ()
    keywords = ('fish', 'sea', 'animal', 'aquatic', 'tail', 'fins')

    def build(self):
        def chain(name, *points):
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                member = f"{name}-{i+1}"
                self.add_line(member, a, b)
                members.append(member)
            return members
        self.add_arc('face-top', (44, 24), (30, 14), radius_x=14, radius_y=10, sweep=False)
        fins_run = chain('fins', (30, 14), (24, 8), (22, 16), (16, 20), (4, 12), (8, 24), (4, 36), (16, 28), (22, 32), (24, 40), (30, 34))
        self.add_arc('face-bottom', (30, 34), (44, 24), radius_x=14, radius_y=10, sweep=False)
        self.add_contour('fish', 'face-top', *fins_run, 'face-bottom', closed=True)
        self.add_arc('gill', (33, 23), (33, 25), radius_x=8, sweep=False)
