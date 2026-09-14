"""Kris Ritual Dagger, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9bac9bab-8cfa-41ca-987b-8393aa3e693f'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/ceremonial ritual knife_9bac9bab-8cfa-41ca-987b-8393aa3e693f.svg'
AUTHOR = 'gpt-6'

class KrisDagger(Solo48):
    icon_id = 'kris-dagger'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/gaming'
    aliases = ()
    keywords = ('dagger', 'kris', 'knife', 'ritual', 'ceremonial', 'blade', 'weapon', 'rpg')

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
        self.add_line('hilt',(6,42),(18,30))
        self.add_line('guard-left',(10,22),(18,30))
        self.add_line('guard-right',(18,30),(26,38))
        self.add_contour('guard','guard-left','guard-right')
        self.relate('connect','guard','hilt')
        arc('edge-a',(14,26),(25,17),12,sweep=False)
        arc('edge-b',(25,17),(32,10),8)
        poly('point',(32,10),(42,6),(40,17))
        arc('edge-c',(40,17),(31,24),10)
        arc('edge-d',(31,24),(22,34),12,sweep=False)
        self.add_line('heel',(22,34),(14,26))
        self.add_contour('blade','edge-a','edge-b','point-1','point-2','edge-c','edge-d','heel',closed=True)
        self.relate('connect','blade','guard')
        self.relate('connect','blade','hilt')
