"""Two outlined heads and readable standing figures.
Human reference: icon_set/references/human_ref/full_body_ref.png.
The two figures retain circular outlined heads, torsos, arms and separate legs. Head ink to upper torso ink gap is exactly 4 units.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'da65a8df-c40a-4960-bff3-74262390682c'
SOURCE_PATH = 'pictographic-primitives/users/multiple man_da65a8df-c40a-4960-bff3-74262390682c.svg'
SOURCE_REFERENCES = (('da65a8df-c40a-4960-bff3-74262390682c', 'pictographic-primitives/users/multiple man_da65a8df-c40a-4960-bff3-74262390682c.svg'), ('5e8b621f-4f10-4323-943d-1337196c6e73', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two persons_5e8b621f-4f10-4323-943d-1337196c6e73.svg'))
PROFILE_SOURCE_KEYS = ('solo/two-standing-people',)
AUTHOR = 'gpt-6'

class DrawingVariant2(Sub32):
    icon_id = 'two-standing-people-sub32-v2'
    category = 'users'
    categories = ('users', 'primitives')
    variant_label = 'Two outlined heads and readable standing figures'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()
    def build(self):
        line,poly=self.add_line,self.add_polyline
        def join(a,b):self.relate("connect",a,b)
        for i,x in enumerate((7,25)):
         self.add_arc(f'head-{i}-a',(x-4,6),(x+4,6),radius_x=4)
         self.add_arc(f'head-{i}-b',(x+4,6),(x-4,6),radius_x=4)
         self.add_contour(f'head-{i}',f'head-{i}-a',f'head-{i}-b',closed=True)
         line(f'torso-{i}',(x,18),(x,24))
         line(f'arms-{i}',(x-5,18),(x+5,18))
         poly(f'legs-{i}',(x-4,30),(x,24),(x+4,30))
         join(f'torso-{i}',f'arms-{i}');join(f'torso-{i}',f'legs-{i}')
         self.mark_human_figure(f'person-{i}',head=f'head-{i}',torso=f'torso-{i}',torso_junction='start')
