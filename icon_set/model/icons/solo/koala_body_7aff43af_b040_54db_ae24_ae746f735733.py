"""Seated koala in right profile. Broad ears and upright nose retained; hidden limbs omitted. Asymmetry describes the seated pose; Lucide cat informs the coherent head outline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7aff43af-b040-54db-ae24-ae746f735733'
SOURCE_PATH = 'pictographic-primitives/animals/koala body_7aff43af-b040-54db-ae24-ae746f735733.svg'
AUTHOR = 'gpt-6'


class SittingKoala(Solo48):
    icon_id = 'sitting-koala'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('koala', 'sitting', 'marsupial', 'australia', 'ears', 'animal', 'bear', 'zoo')

    def build(self) -> None:
        # VRECT_XL ink bounds (6, 6)-(42, 42). One continuous outer path.
        self.add_bezier('crown-a', (15, 8), *(((16.94368014, 6.24779087), (20.04328859, 6), (23, 6)),))
        self.add_bezier('crown-b', (23, 6), *(((25.95671141, 6), (29.05631986, 6.24779087), (31, 8)),))
        self.add_bezier('right-ear-a', (31, 8), *(((32.58064574, 6.27540249), (34.77534041, 6), (36.93351202, 6)), ((39.09168363, 6.27818603), (40.96568239, 7.79995461), (42, 10))))
        self.add_bezier('right-ear-b', (42, 10), *(((42, 15.06937551), (39.02383141, 19.36646437), (35, 20)),))
        self.add_arc('cheek', (35, 20), (29, 26), radius_x=8)
        self.add_line('foreleg-top', (29, 26), (42, 28))
        self.add_bezier('arm', (42, 28), *(((42, 31.06990792), (38.57644606, 33.6589514), (34, 34)),))
        self.add_line('foreleg', (34, 34), (32, 40))
        self.add_line('toe', (32, 40), (37, 38))
        self.add_arc('foot', (37, 38), (32, 42), radius_x=6, radius_y=8)
        self.add_line('base', (32, 42), (20, 42))
        self.add_bezier('haunch', (20, 42), *(((15.41518876, 42), (11.02443362, 40.38747008), (9, 37)),))
        self.add_arc('back', (9, 37), (14, 26), radius_x=15)
        self.add_line('neck', (14, 26), (13, 20))
        self.add_bezier('left-ear-b', (13, 20), *(((8.97616859, 19.36646437), (6, 15.06937551), (6, 10)),))
        self.add_arc('left-ear-a', (6, 10), (15, 8), radius_x=6, radius_y=8)
        self.add_contour(
            'outline', 'crown-a', 'crown-b', 'right-ear-a', 'right-ear-b',
            'cheek', 'foreleg-top', 'arm', 'foreleg', 'toe', 'foot', 'base',
            'haunch', 'back', 'neck', 'left-ear-b', 'left-ear-a', closed=True,
        )
        self.add_arc('knee', (32, 40), (23, 36), radius_x=9, radius_y=5, sweep=False)
        self.relate('connect', 'knee', 'outline')
        self.add_line('nose',(24,15),(24,18))
