"""Cartoon Cat Face, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3e88b736-a624-5653-bfe9-0df39a7adb24'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/cat 1_3e88b736-a624-5653-bfe9-0df39a7adb24.svg'
AUTHOR = 'gpt-6'

class CartoonCatFace(Solo48):
    icon_id = 'cartoon-cat-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/gaming'
    aliases = ()
    keywords = ('cat', 'cartoon', 'face', 'felix', 'character', 'animal', 'kitty', 'retro')

    def build(self):
        # SQUARE: centerline extremes (6, 6, 42, 42); current SOLO48 contract.
        def circle(name, x, y, r):
            self.add_arc(name+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        def arc(name,a,b,r,ry=None,sweep=True):
            self.add_arc(name,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(name,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):
                self.add_line(f'{name}-{i}',a,b)
        poly('ears',(6,24),(10,18),(10,6),(19,14),(29,14),(38,6),(38,18),(42,24))
        arc('jaw',(42,24),(6,24),18,18)
        self.add_contour('head',*[f'ears-{i}' for i in range(1, 8)],'jaw',closed=True)
        for x in (17,31):
            self.add_dot(f'eye-{x}',(x,23))
        arc('smile',(20,32),(28,32),5,2,sweep=False)
