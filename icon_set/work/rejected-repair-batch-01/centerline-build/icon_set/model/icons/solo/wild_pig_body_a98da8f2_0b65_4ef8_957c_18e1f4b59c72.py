"""Standing wild boar: heavy torso, pricked ear and blunt snout. Two near legs retain the stance; tiny tusk and far legs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a98da8f2-0b65-4ef8-957c-18e1f4b59c72'
SOURCE_PATH = 'pictographic-primitives/animals/wild pig body_a98da8f2-0b65-4ef8-957c-18e1f4b59c72.svg'
AUTHOR = 'gpt-6'


class WildBoar(Solo48):
    icon_id = 'wild-boar'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('boar', 'pig', 'hog', 'standing', 'snout', 'tusk', 'farm', 'wildlife')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_arc('back-round',(6, 25),(19, 12),radius_x=13,radius_y=13,large_arc=False,sweep=True)
        self.add_line('back',(19, 12),(32, 12))
        self.add_line('ear-1',(32, 12),(38, 8))
        self.add_line('ear-2',(38, 8),(36, 17))
        self.add_bezier('face',(36, 17),*(((37.73513326, 20.03919199), (40.43460675, 22.55870058), (44, 24)),))
        self.add_bezier('snout',(44, 24),*(((44, 26.58712249), (43.69026141, 29.29927988), (42, 34)),))
        self.add_line('chin',(42, 34),(35, 32))
        self.add_bezier('chest',(35,32),((34,32),(33,32),(32,34)))
        self.add_line('foreleg-1',(32, 34),(34, 40))
        self.add_line('foreleg-2',(34, 40),(24, 40))
        self.add_line('foreleg-3',(24, 40),(24, 31))
        self.add_line('foreleg-4',(24, 31),(16, 31))
        self.add_line('foreleg-5',(16, 31),(16, 40))
        self.add_line('foreleg-6',(16, 40),(8, 40))
        self.add_line('foreleg-7',(8, 40),(8, 31))
        self.add_arc('rump',(8, 31),(6, 25),radius_x=10,radius_y=10,large_arc=False,sweep=True)
        self.add_line('tail-round',(6,25),(4,14))
        self.add_contour('outline',*('back-round', 'back', 'ear-1', 'ear-2', 'face', 'snout', 'chin', 'chest', 'foreleg-1', 'foreleg-2', 'foreleg-3', 'foreleg-4', 'foreleg-5', 'foreleg-6', 'foreleg-7', 'rump'),closed=True)
        self.add_contour('tail',*('tail-round',),closed=False)
        self.relate('connect',*('outline', 'tail'))
