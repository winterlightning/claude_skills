"""Assassin's Creed Hood Emblem, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '12378975-bc57-56b2-b920-526922d97f3d'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/assasin creed_12378975-bc57-56b2-b920-526922d97f3d.svg'
AUTHOR = 'gpt-6'

class AssassinHood(Solo48):
    icon_id = 'assassin-hood'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('assassin', 'hood', 'emblem', 'assassins creed', 'stealth', 'game', 'logo', 'video game')

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
        self.add_polyline('hood',(6,36),(13,29),(13,23),(24,6),(35,23),(35,29),(42,36),(30,42),(30,35),(24,28),(18,35),(18,42),closed=True)
