'Hippo face: independent spacing revision.\n\nMake the muzzle the lower outside contour instead of nesting two nearly touching outlines.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fa6b0258-1bc2-51ef-819c-45e3b36a42d4'
SOURCE_PATH = 'pictographic-primitives/animals/hippo_fa6b0258-1bc2-51ef-819c-45e3b36a42d4.svg'
AUTHOR = 'gpt-6'

class HippoFace(Solo48):
    icon_id = 'hippo-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('hippo', 'hippopotamus', 'face', 'head', 'muzzle', 'ears', 'animal', 'cute')

    def build(self):
        self.add_line('left-head',(6, 30),(6, 10))
        self.add_arc('left-ear-a',(6, 10),(10, 6),radius_x=4,radius_y=4,sweep=True)
        self.add_arc('left-ear-b',(10, 6),(16, 12),radius_x=6,radius_y=6,sweep=True)
        self.add_line('forehead',(16, 12),(32, 12))
        self.add_arc('right-ear-a',(32, 12),(38, 6),radius_x=6,radius_y=6,sweep=True)
        self.add_arc('right-ear-b',(38, 6),(42, 10),radius_x=4,radius_y=4,sweep=True)
        self.add_line('right-head',(42, 10),(42, 30))
        self.add_contour('head','left-head','left-ear-a','left-ear-b','forehead','right-ear-a','right-ear-b','right-head',closed=False)
        self.add_arc('muzzle-nw',(6, 30),(16, 22),radius_x=10,radius_y=8,sweep=True)
        self.add_line('muzzle-top',(16, 22),(32, 22))
        self.add_arc('muzzle-ne',(32, 22),(42, 30),radius_x=10,radius_y=8,sweep=True)
        self.add_arc('muzzle-se',(42, 30),(32, 42),radius_x=10,radius_y=12,sweep=True)
        self.add_line('muzzle-bottom',(32, 42),(16, 42))
        self.add_arc('muzzle-sw',(16, 42),(6, 30),radius_x=10,radius_y=12,sweep=True)
        self.add_contour('muzzle','muzzle-nw','muzzle-top','muzzle-ne','muzzle-se','muzzle-bottom','muzzle-sw',closed=True)
        self.relate('connect','head','muzzle')
        self.add_dot('nostril-left',(18, 31))
        self.add_dot('nostril-right',(30, 31))
