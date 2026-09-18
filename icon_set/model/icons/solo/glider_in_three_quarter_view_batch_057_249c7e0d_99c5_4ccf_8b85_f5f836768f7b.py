"""Right-facing glider in perspective: outline integrates tail fin and diagonal wing. Lucide plane shows reduction to coherent wing/fuselage silhouette. Omit overlapping far-wing edges."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '249c7e0d-99c5-4ccf-8b85-f5f836768f7b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/glider_249c7e0d-99c5-4ccf-8b85-f5f836768f7b.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'glider-in-three-quarter-view-batch-057'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transport'
    aliases = ()
    keywords = ('glider', 'aircraft', 'plane', 'wings', 'flight', 'transport')

    def build(self):
        def chain(name, *points):
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                member = f"{name}-{i+1}"
                self.add_line(member, a, b)
                members.append(member)
            return members
        airframe_run = chain('airframe', (4, 10), (12, 10), (18, 20), (28, 20), (32, 8), (44, 8), (38, 24))
        self.add_arc('nose', (38, 24), (38, 32), radius_x=4)
        underside_run = chain('underside', (38, 32), (30, 32), (12, 40), (4, 32), (20, 28), (8, 28), (4, 10))
        self.add_contour('glider', *airframe_run, 'nose', *underside_run, closed=True)
