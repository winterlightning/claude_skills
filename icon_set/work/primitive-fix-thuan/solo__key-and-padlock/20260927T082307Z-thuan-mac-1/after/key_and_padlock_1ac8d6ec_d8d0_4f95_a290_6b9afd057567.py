"""An upright key beside its padlock. SQUARE extremes (6,6)-(42,42). Lucide key-round and lock-keyhole inform circular bow and coherent arched shackle. Retain the natural paired objects, two teeth and keyhole slot."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1ac8d6ec-d8d0-4f95-a290-6b9afd057567'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__key-and-padlock/20260927T082307Z-thuan-mac-1/reference/key and lock_1ac8d6ec-d8d0-4f95-a290-6b9afd057567.svg'
AUTHOR = 'gpt-6'


class KeyAndPadlock(Solo48):
    icon_id = 'key-and-padlock'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('key', 'padlock', 'lock', 'security', 'access', 'password', 'unlock', 'privacy')

    def build(self) -> None:
        self.add_arc('bow-right',(11,32),(11,42),radius_x=5)
        self.add_arc('bow-left',(11,42),(11,32),radius_x=5)
        self.add_contour('bow','bow-right','bow-left',closed=True)
        self.add_polyline('shaft',(11,32),(11,18),(11,10))
        self.relate('connect','bow','shaft')
        self.add_line('tooth-top',(6,10),(11,10))
        self.add_line('tooth-low',(6,18),(11,18))
        self.relate('connect','shaft','tooth-top')
        self.relate('connect','shaft','tooth-low')
        self.add_line('lock-top',(27,22),(39,22))
        self.add_arc('lock-tr',(39,22),(42,25),radius_x=3)
        self.add_line('lock-right',(42,25),(42,39))
        self.add_arc('lock-br',(42,39),(39,42),radius_x=3)
        self.add_line('lock-bottom',(39,42),(27,42))
        self.add_arc('lock-bl',(27,42),(24,39),radius_x=3)
        self.add_line('lock-left',(24,39),(24,25))
        self.add_arc('lock-tl',(24,25),(27,22),radius_x=3)
        self.add_contour('lock',*('lock-'+p for p in ['top','tr','right','br','bottom','bl','left','tl']),closed=True)
        self.add_line('shackle-left',(27,22),(27,12))
        self.add_arc('shackle-top',(27,12),(39,12),radius_x=6)
        self.add_line('shackle-right',(39,12),(39,22))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','lock','shackle')
        self.add_line('keyhole',(33,31),(33,33))
