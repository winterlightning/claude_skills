"""Shin-chan Boy Face, independently authored on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8a3c691f-fc09-42f4-919d-02dbeb59ca3c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__shinchan-face/20260927T091435Z-thuan-mac-1/reference/ceayon shinchan_8a3c691f-fc09-42f4-919d-02dbeb59ca3c.svg'
AUTHOR = "gpt-6"

class ShinchanFace(Solo48):
    icon_id = 'shinchan-face'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('shinchan', 'crayon shinchan', 'boy', 'face', 'anime', 'cartoon', 'character', 'manga')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('hair',(6, 24),*(((6.5, 15.163444), (15.163444, 8.0), (24.0, 8)), ((32.836556, 8), (40.0, 15.163444), (40, 24))))
        self.add_arc('ear',(40, 24),(40, 32),radius_x=4,radius_y=4,large_arc=False,sweep=True)
        self.add_arc('chin',(40, 32),(32, 40),radius_x=8,radius_y=8,large_arc=False,sweep=True)
        self.add_line('chin-flat',(32, 40),(16, 40))
        self.add_bezier('cheek',(16, 40),*(((9.20395011, 39.01398816), (4, 33.91895943), (4, 28)),))
        self.add_bezier('nose',(4, 28),*(((4, 26.3837142), (4.72578466, 24.80131331), (6, 24)),))
        # The source has two relaxed eyelid arches, tiny eyes and a smiling mouth.
        self.add_arc('eye-left',(17, 21),(19, 21),radius_x=2,sweep=False)
        self.add_arc('eye-right',(29, 21),(31, 21),radius_x=2,sweep=False)
        self.add_bezier('smile',(20, 30),((22, 32),(26, 32),(28, 30)))
        self.add_contour('head',*('hair', 'ear', 'chin', 'chin-flat', 'cheek', 'nose'),closed=True)
