"""Left-facing duckling profile with large round head, beak, tail and two legs. Lucide bird informs integrated silhouette and attached short feet. Omit eye and wing detail."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f96d275-e002-410c-8e4f-d4365a7661ad'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gosling_2f96d275-e002-410c-8e4f-d4365a7661ad.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'standing-duckling-profile-batch-057'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    aliases = ()
    keywords = ('duckling', 'duck', 'bird', 'chick', 'animal', 'poultry')

    def build(self):
        def chain(name, *points):
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                member = f"{name}-{i+1}"
                self.add_line(member, a, b)
                members.append(member)
            return members
        self.add_arc('head', (12, 18), (28, 18), radius_x=8, radius_y=12)
        back_run = chain('back', (28, 18), (24, 26), (34, 28), (42, 24))
        self.add_arc('body-right', (42, 24), (28, 36), radius_x=14, radius_y=12)
        self.add_line('belly', (28, 36), (20, 36))
        self.add_arc('body-left', (20, 36), (14, 24), radius_x=10, radius_y=8)
        beak_run = chain('beak', (14, 24), (6, 20), (12, 18))
        self.add_contour('duck', 'head', *back_run, 'body-right', 'belly', 'body-left', *beak_run, closed=True)
        for x in (20, 28):
            self.add_line(f'leg-{x}', (x, 36), (x, 42))
            self.relate('connect', 'duck', f'leg-{x}')
