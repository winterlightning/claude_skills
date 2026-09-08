"""Mirrored tiger face with rounded ears, central brow and cheek stripes. Bounds (2,2)-(46,46). Lucide cat: paired facial proportions, simplified muzzle; omit extra cheek hooks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff9145f5-940a-5af6-a247-fd2c0f7d794d'
SOURCE_PATH = 'pictographic-primitives/animals/tiger bengal_ff9145f5-940a-5af6-a247-fd2c0f7d794d.svg'
AUTHOR = 'gpt-6'


class TigerFace(Solo48):
    icon_id = 'tiger-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('tiger', 'face', 'head', 'stripes', 'big cat', 'feline', 'bengal', 'wildlife')

    def build(self) -> None:
        self.add_arc('ear-left',(2,8),(14,8),radius_x=6,radius_y=6,sweep=True)
        self.add_line('ear-left-root',(14,8),(17,8))
        self.add_arc('forehead-left',(17,8),(24,6),radius_x=26,sweep=True)
        self.add_arc('forehead-right',(24,6),(31,8),radius_x=26,sweep=True)
        self.add_line('ear-right-root',(31,8),(34,8))
        self.add_arc('ear-right',(34,8),(46,8),radius_x=6,radius_y=6,sweep=True)
        self.add_line('side-right',(46,8),(46,26))
        self.add_arc('jaw-right',(46,26),(24,46),radius_x=22,radius_y=20,sweep=True)
        self.add_arc('jaw-left',(24,46),(2,26),radius_x=22,radius_y=20,sweep=True)
        self.add_line('side-left',(2,26),(2,8))
        self.add_contour('outline','ear-left','ear-left-root','forehead-left','forehead-right','ear-right-root','ear-right','side-right','jaw-right','jaw-left','side-left',closed=True)
        self.add_line('brow',(24,6),(24,17))
        self.add_line('brow-stripe',(17,14),(31,14))
        self.relate('connect','brow','outline')
        self.relate('connect','brow','brow-stripe')
        self.add_dot('left-eye',(13,21))
        self.add_dot('right-eye',(35,21))
        self.add_polyline('nose',(19,25),(24,29),(29,25))
        self.add_line('muzzle-stem',(24,29),(24,32))
        self.add_arc('muzzle-left',(16,32),(24,32),radius_x=4,radius_y=5,sweep=False)
        self.add_arc('muzzle-right',(24,32),(32,32),radius_x=4,radius_y=5,sweep=False)
        self.relate('connect','nose','muzzle-stem')
        self.relate('connect','muzzle-stem','muzzle-left')
        self.relate('connect','muzzle-stem','muzzle-right')
        self.relate('connect','muzzle-left','muzzle-right')
        self.add_line('left-stripe',(2,26),(9,29))
        self.add_line('right-stripe',(46,26),(39,29))
        self.relate('connect','left-stripe','outline')
        self.relate('connect','right-stripe','outline')
