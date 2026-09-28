'Standing hippo: broad muzzle, smooth rounded back and two equal 8-unit legs.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '559fae17-bef3-4dfd-a513-8e884c846916'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-hippo/20260927T094403Z-thuan-mac-1/reference/hippo body_559fae17-bef3-4dfd-a513-8e884c846916.svg'
AUTHOR = 'gpt-6'


class StandingHippo(Solo48):
    icon_id = 'standing-hippo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
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

        p('snout',(4,28),(4,22),(8,20),(8,14),(17,14),(20,8),(23,14),(32,14))
        a('back',(32,14),(44,26),12)
        p('legs',(44,26),(44,40),(36,40),(36,30),(20,30),(20,40),(12,40),(12,30),(4,28))
        link('connect','snout','back')
        link('connect','back','legs')
        link('connect','legs','snout')
