"""Left-facing farm cow with a sloping muzzle, curved belly and single-stroke legs. Four overlapping legs reduced to two and tail tuft omitted. No useful exact Lucide match; directional asymmetry retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0220f3e-39f2-4fe3-a929-e532120865b6'
SOURCE_PATH = 'pictographic-primitives/animals/cattle_a0220f3e-39f2-4fe3-a929-e532120865b6.svg'
AUTHOR = 'gpt-6'


class StandingCow(Solo48):
    icon_id = 'standing-cow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('cow', 'cattle', 'farm', 'livestock', 'dairy', 'animal', 'bovine', 'standing')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('horn-front',(9, 12),(8, 8))
        self.add_line('horn-back',(8, 8),(15, 12))
        self.add_arc('shoulder',(15, 12),(23, 14),radius_x=17,radius_y=17,large_arc=False,sweep=False)
        self.add_line('back',(23, 14),(39, 14))
        self.add_bezier('rump',(39, 14),*(((41.76142375, 14.0), (44, 15.790861), (44, 18)),))
        self.add_line('rear',(44, 18),(44, 20))
        self.add_bezier('haunch',(44, 20),*(((44, 24.418278), (39.5228475, 28.0), (34, 28)),))
        self.add_line('belly',(34, 28),(18, 28))
        self.add_bezier('chest',(18, 28),*(((14.13400675, 28.0), (10.25, 26.209139), (10, 24)),))
        self.add_line('throat',(10, 24),(6, 20))
        self.add_line('muzzle-bottom',(6, 20),(4, 21))
        self.add_bezier('muzzle-tip',(4, 21),*(((4, 20.38119785), (4, 19.61880215), (4, 19)),))
        self.add_line('face',(4, 19),(9, 12))
        self.add_line('front-leg',(18, 28),(18, 40))
        self.add_line('hind-leg-1',(34, 28),(39, 34))
        self.add_line('hind-leg-2',(39, 34),(39, 40))
        self.add_bezier('tail',(44, 18),*(((43.10683603, 21.71281292), (43.10683603, 26.28718708), (44, 30)),))
        self.add_contour('outline',*('horn-front', 'horn-back', 'shoulder', 'back', 'rump', 'rear', 'haunch', 'belly', 'chest', 'throat', 'muzzle-bottom', 'muzzle-tip', 'face'),closed=True)
        self.add_contour('hind-leg',*('hind-leg-1', 'hind-leg-2'),closed=False)
        self.relate('connect',*('outline', 'front-leg'))
        self.relate('connect',*('outline', 'hind-leg'))
        self.relate('connect',*('outline', 'tail'))
