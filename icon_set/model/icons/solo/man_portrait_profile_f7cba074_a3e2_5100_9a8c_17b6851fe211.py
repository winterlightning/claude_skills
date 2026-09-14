"""A left-facing head with a quiff, nose, chin, ear, neck, and shoulders. No useful exact Lucide profile match; coherent circular arcs replace numerous hair waves. The tiny eye is omitted for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7cba074-a3e2-5100-9a8c-17b6851fe211'
SOURCE_PATH = 'pictographic-primitives/users/portrait_f7cba074-a3e2-5100-9a8c-17b6851fe211.svg'
AUTHOR = 'gpt-6'


class ManPortraitProfile(Solo48):
    icon_id = 'man-portrait-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/users"
    aliases = ()
    keywords = ('portrait', 'man', 'profile', 'head', 'face', 'hair', 'person', 'bust')


    def build(self) -> None:
        # Portrait centerline extremes (8,6)-(40,42); profile is deliberately asymmetric.
        self.add_arc('quiff',(14,14),(10,10),radius_x=4)
        self.add_arc('hair-front',(10,10),(16,6),radius_x=6)
        self.add_line('crown',(16,6),(24,6))
        self.add_arc('head-back',(24,6),(38,18),radius_x=14)
        self.add_line('nape',(38,18),(34,32))
        self.add_line('neck-back',(34,32),(34,38))
        self.add_line('shoulder-back',(34,38),(40,42))
        self.add_contour('hair-and-back','quiff','hair-front','crown','head-back','nape','neck-back','shoulder-back')
        self.add_line('brow',(14,14),(12,18))
        self.add_line('nose',(12,18),(8,24))
        self.add_line('nose-base',(8,24),(14,26))
        self.add_line('lip',(14,26),(14,30))
        self.add_arc('chin',(14,30),(20,36),radius_x=6,sweep=False)
        self.add_line('neck-front',(20,36),(20,38))
        self.add_line('shoulder-front',(20,38),(8,42))
        self.add_contour('face','brow','nose','nose-base','lip','chin','neck-front','shoulder-front')
        self.relate('connect','face','hair-and-back')
        self.add_arc('ear',(24,18),(24,24),radius_x=3)
