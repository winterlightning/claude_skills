"""Bow and Arrow, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3e8220da-b033-4cea-9a90-4e3af058d8d0'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/crossbow_3e8220da-b033-4cea-9a90-4e3af058d8d0.svg'
AUTHOR = 'gpt-6'

class BowAndArrow(Solo48):
    icon_id = 'bow-and-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('bow', 'arrow', 'crossbow', 'archery', 'weapon', 'ranged', 'rpg', 'hunt')

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
        arc('bow-upper',(6,6),(30,18),30)
        arc('bow-lower',(30,18),(42,42),30)
        self.add_contour('bow','bow-upper','bow-lower')
        self.add_polyline('string',(6,6),(6,42),(42,42))
        self.relate('connect','string','bow')
        self.add_line('shaft-low',(6,42),(30,18))
        self.add_line('shaft-high',(30,18),(42,6))
        self.add_contour('shaft','shaft-low','shaft-high')
        self.relate('connect','shaft','bow')
        self.relate('connect','shaft','string')
        self.add_polyline('tip',(32,6),(42,6),(42,16))
        self.relate('connect','tip','shaft')
