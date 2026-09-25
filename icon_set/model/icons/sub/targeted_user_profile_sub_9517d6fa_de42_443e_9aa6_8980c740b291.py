"""A front-facing bust with an arched shoulder line and a circular head crossed by short targeting ticks at the four cardinal directions. Keep the targeting relationship to the head.

Plan: Circular targeted head above shoulders, with scoped cardinal tick joins. Head bottom18, shoulders26: exact 4-unit ink gap. Bounds (2,2)-(30,30).
Construction reference: Shared human_ref/user.svg: circular head, smooth shoulders; original adds cardinal targeting ticks."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9517d6fa-de42-443e-9aa6-8980c740b291'
SOURCE_PATH = 'pictographic-primitives/state/user target_9517d6fa-de42-443e-9aa6-8980c740b291.svg'
SOURCE_ICON_IDS = ('9517d6fa-de42-443e-9aa6-8980c740b291',)
AUTHOR = 'gpt-6'

class TargetedUserProfileSub(Sub32):
    icon_id = 'targeted-user-profile-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('targeted', 'user', 'profile', 'sub')

    def build(self) -> None:
        axis=16; cy=12;r=6
        points=[(16,6),(22,12),(16,18),(10,12)]
        for i in range(4):self.add_arc(f'head-{i}',points[i],points[(i+1)%4],radius_x=r)
        self.add_contour('head',*(f'head-{i}' for i in range(4)),closed=True)
        for name,a,b in [('west',(2,12),(10,12)),('east',(22,12),(30,12)),('north',(16,2),(16,6)),('south',(16,18),(16,20))]:
            self.add_line(name,a,b);self.relate('connect','head',name)
        self.add_bezier('shoulders',(2,30),((6,26),(10,26),(16,26)),((22,26),(26,26),(30,30)))
