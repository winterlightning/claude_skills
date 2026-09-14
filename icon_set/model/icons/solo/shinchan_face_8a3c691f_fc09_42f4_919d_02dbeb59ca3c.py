"""Shin-chan Boy Face, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8a3c691f-fc09-42f4-919d-02dbeb59ca3c'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/ceayon shinchan_8a3c691f-fc09-42f4-919d-02dbeb59ca3c.svg'
AUTHOR = 'gpt-6'

class ShinchanFace(Solo48):
    icon_id = 'shinchan-face'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/gaming'
    aliases = ()
    keywords = ('shinchan', 'crayon shinchan', 'boy', 'face', 'anime', 'cartoon', 'character', 'manga')

    def build(self):
        # HRECT_L: centerline extremes (4, 8, 44, 40); current SOLO48 contract.
        def circle(name, x, y, r):
            self.add_arc(name+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        def arc(name,a,b,r,ry=None,sweep=True):
            self.add_arc(name,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(name,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):
                self.add_line(f'{name}-{i}',a,b)
        arc('hair',(8,24),(40,24),16,16)
        arc('ear',(40,24),(40,32),4)
        arc('chin',(40,32),(32,40),8)
        self.add_line('chin-flat',(32,40),(16,40))
        arc('cheek',(16,40),(6,28),12)
        arc('nose',(6,28),(8,24),4)
        self.add_contour('head','hair','ear','chin','chin-flat','cheek','nose',closed=True)
        self.add_polyline('brows',(18,20),(20,18),(24,20),(28,18),(30,20))
        self.add_dot('eye-left',(17,28))
        self.add_dot('eye-right',(29,28))
