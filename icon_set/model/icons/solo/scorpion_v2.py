# Variant of scorpion; parent file remains unchanged.
'A scorpion with four shorter legs and curved pincer jaws. SQUARE extremes (2,2)-(46,46) preserve the claws and curled tail. Lucide bug informs mirrored appendages and consistent paired curves. Leg extensions are shortened; the tail remains deliberately left-curled.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '447f79a2-697e-4660-a5cc-b4e957e71821'
SOURCE_PATH = 'pictographic-primitives/animals/insect scorpion_447f79a2-697e-4660-a5cc-b4e957e71821.svg'
AUTHOR = 'gpt-6'

class ScorpionVariant2(Solo48):
    icon_id = 'scorpion-v2'
    variant_of = 'scorpion'
    variant_label = 'Shorter legs and curved claws'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('scorpion', 'sting', 'claws', 'arachnid', 'tail', 'desert', 'venom', 'zodiac')

    def build(self) -> None:
        self.add_line('body-top', (22, 18), (26, 18))
        self.add_arc('body-tr', (26, 18), (30, 22), radius_x=4, radius_y=4, sweep=True)
        self.add_line('body-r1', (30, 22), (30, 28))
        self.add_line('body-r2', (30, 28), (30, 32))
        self.add_arc('body-br', (30, 32), (24, 36), radius_x=6, radius_y=4, sweep=True)
        self.add_arc('body-bl', (24, 36), (18, 32), radius_x=6, radius_y=4, sweep=True)
        self.add_line('body-l2', (18, 32), (18, 28))
        self.add_line('body-l1', (18, 28), (18, 22))
        self.add_arc('body-tl', (18, 22), (22, 18), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('body', 'body-top', 'body-tr', 'body-r1', 'body-r2', 'body-br', 'body-bl', 'body-l2', 'body-l1', 'body-tl', closed=True)
        self.add_arc('claw-l-outer', (2, 2), (8, 14), radius_x=6, radius_y=12, sweep=False)
        self.add_arc('claw-l-inner', (8, 14), (14, 2), radius_x=6, radius_y=12, sweep=False)
        self.add_arc('jaw-l-inner', (14, 2), (8, 7), radius_x=6, radius_y=5, sweep=False)
        self.add_arc('jaw-l-outer', (8, 7), (2, 2), radius_x=6, radius_y=5, sweep=False)
        self.add_contour('claw-l', 'claw-l-outer', 'claw-l-inner', 'jaw-l-inner', 'jaw-l-outer', closed=True)
        self.add_polyline('arm-l', (8, 14), (8, 18), (18, 22))
        self.relate('connect', 'arm-l', 'claw-l')
        self.relate('connect', 'body', 'arm-l')
        self.add_polyline('leg-l-0', (18, 22), (11, 24), (8, 24))
        self.relate('connect', 'body', 'leg-l-0')
        self.add_polyline('leg-l-1', (18, 28), (11, 30), (8, 30))
        self.relate('connect', 'body', 'leg-l-1')
        self.add_arc('claw-r-outer', (46, 2), (40, 14), radius_x=6, radius_y=12, sweep=True)
        self.add_arc('claw-r-inner', (40, 14), (34, 2), radius_x=6, radius_y=12, sweep=True)
        self.add_arc('jaw-r-inner', (34, 2), (40, 7), radius_x=6, radius_y=5, sweep=True)
        self.add_arc('jaw-r-outer', (40, 7), (46, 2), radius_x=6, radius_y=5, sweep=True)
        self.add_contour('claw-r', 'claw-r-outer', 'claw-r-inner', 'jaw-r-inner', 'jaw-r-outer', closed=True)
        self.add_polyline('arm-r', (40, 14), (40, 18), (30, 22))
        self.relate('connect', 'arm-r', 'claw-r')
        self.relate('connect', 'body', 'arm-r')
        self.add_polyline('leg-r-0', (30, 22), (37, 24), (40, 24))
        self.relate('connect', 'body', 'leg-r-0')
        self.add_polyline('leg-r-1', (30, 28), (37, 30), (40, 30))
        self.relate('connect', 'body', 'leg-r-1')
        self.add_arc('tail-r', (24, 36), (14, 46), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('tail-l', (14, 46), (6, 38), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('tail', 'tail-r', 'tail-l', closed=False)
        self.relate('connect', 'body', 'tail')
