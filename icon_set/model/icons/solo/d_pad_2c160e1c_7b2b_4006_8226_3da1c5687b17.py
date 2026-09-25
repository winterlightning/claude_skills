"""Directional Pad, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2c160e1c-7b2b-4006-8226-3da1c5687b17'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/controller grid none_2c160e1c-7b2b-4006-8226-3da1c5687b17.svg'
AUTHOR = 'gpt-6'

class DPad(Solo48):
    icon_id = 'd-pad'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('d-pad', 'directional pad', 'dpad', 'controller', 'gamepad', 'arrows', 'input', 'gaming')

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
        self.add_polyline('pad',(18,6),(30,6),(30,18),(42,18),(42,30),(30,30),(30,42),(18,42),(18,30),(6,30),(6,18),(18,18),closed=True)
