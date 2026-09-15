'Standing hippo: broad muzzle, smooth rounded back and two equal 8-unit legs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '559fae17-bef3-4dfd-a513-8e884c846916'
SOURCE_PATH = 'pictographic-primitives/animals/hippo body_559fae17-bef3-4dfd-a513-8e884c846916.svg'
AUTHOR = 'gpt-6'


class StandingHippo(Solo48):
    icon_id = 'standing-hippo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('hippo', 'hippopotamus', 'standing', 'body', 'animal', 'zoo', 'river', 'wildlife')

    def build(self):
        # Standing hippo: broad muzzle, smooth rounded back and two equal 8-unit legs.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('snout',(4,28),(4,20),(8,14),(16,14),(20,8),(24,14),(32,14))
        a('back',(32,14),(44,26),12)
        p('legs',(44,26),(44,40),(36,40),(36,30),(20,30),(20,40),(12,40),(12,30),(4,28))
        link('connect','snout','back')
        link('connect','back','legs')
        link('connect','legs','snout')
