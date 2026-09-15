'Baby chick: preserve the raised tail and folded wing with smooth coherent silhouette curves and a wider internal gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f1a2fcc-b8bd-5d0d-8a3f-ff4bd2741fbf'
SOURCE_PATH = 'pictographic-primitives/animals/chick_3f1a2fcc-b8bd-5d0d-8a3f-ff4bd2741fbf.svg'
AUTHOR = 'gpt-6'


class BabyChick(Solo48):
    icon_id = 'baby-chick'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('chick', 'chicken', 'bird', 'baby', 'hatch', 'farm', 'easter', 'poultry')

    def build(self) -> None:
        self.add_bezier('crown',(8,18),((10,10),(18,6),(26,6)))
        self.add_bezier('back',(26,6),((32,6),(34,12),(34,18)))
        self.add_bezier('tail',(34,18),((34,22),(38,22),(42,22)))
        self.add_line('tail-tip',(42,22),(42,26))
        self.add_bezier('right',(42,26),((42,36),(37,42),(30,42)))
        self.add_line('belly',(30,42),(24,42))
        self.add_arc('left',(24,42),(8,26),radius_x=16)
        self.add_line('beak-1',(8,26),(6,22))
        self.add_line('beak-2',(6,22),(8,18))
        self.add_contour('outline','crown','back','tail','tail-tip','right','belly','left','beak-1','beak-2',closed=True)
        self.add_bezier('wing',(23,22),((23,28),(27,30),(31,30)))
