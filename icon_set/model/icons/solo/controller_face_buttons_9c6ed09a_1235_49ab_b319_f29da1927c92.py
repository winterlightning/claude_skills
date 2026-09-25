"""Controller Face Buttons, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9c6ed09a-1235-49ab-b319-f29da1927c92'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/controller grid down_9c6ed09a-1235-49ab-b319-f29da1927c92.svg'
AUTHOR = 'gpt-6'

class ControllerFaceButtons(Solo48):
    icon_id = 'controller-face-buttons'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('buttons', 'face buttons', 'controller', 'gamepad', 'input', 'action buttons', 'gaming', 'grid')

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
        for name,x,y in [('top',24,11),('left',11,24),('right',37,24),('bottom',24,37)]:
            circle(name,x,y,5)
