"""Bat Emblem, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '42aba16c-57c7-5a72-b509-23e7671ceddb'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/batman_42aba16c-57c7-5a72-b509-23e7671ceddb.svg'
AUTHOR = 'gpt-6'

class BatEmblem(Solo48):
    icon_id = 'bat-emblem'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/gaming'
    aliases = ()
    keywords = ('batman', 'bat', 'emblem', 'superhero', 'logo', 'comic', 'hero', 'dc')

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
        poly('crown',(6,26),(9,8),(14,18),(19,18),(20,10),(24,14),(28,10),(29,18),(34,18),(39,8),(42,26))
        arc('right-lower',(42,26),(38,35),10)
        arc('right-scallop',(38,35),(28,31),8,sweep=False)
        poly('tail',(28,31),(24,40),(20,31))
        arc('left-scallop',(20,31),(10,35),8,sweep=False)
        arc('left-lower',(10,35),(6,26),10)
        self.add_contour('bat',*[f'crown-{i}' for i in range(6,11)],'right-lower','right-scallop','tail-1','tail-2','left-scallop','left-lower',closed=True)
