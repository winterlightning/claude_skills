"""Hat-Wearing Character, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd3df3023-c08a-4d26-802c-e70d25a630b2'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/character_d3df3023-c08a-4d26-802c-e70d25a630b2.svg'
AUTHOR = 'gpt-6'

class HatCharacter(Solo48):
    icon_id = 'hat-character'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('character', 'hat', 'figure', 'avatar', 'adventurer', 'npc', 'game', 'person')

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
        arc('crown',(10,20),(38,20),14,14)
        poly('brim',(38,20),(42,27),(6,27),(10,20))
        self.add_contour('hat','crown','brim-1','brim-2','brim-3',closed=True)
        self.add_dot('eye-left',(20,18))
        self.add_dot('eye-right',(28,18))
        arc('face',(15,27),(33,27),9,sweep=False)
        self.relate('connect','face','hat')
        self.add_polyline('left-arm',(15,27),(6,35),(8,42))
        self.add_polyline('right-arm',(33,27),(42,35),(40,42))
        for arm in ('left-arm','right-arm'):
            self.relate('connect',arm,'face')
            self.relate('connect',arm,'hat')
