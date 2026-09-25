"""Framed sun above two curved hills. SQUARE centerline bounds6,6,42,42. Sun radius3; nine-unit top gap. Frame explicitly split at hill attachments. Five minor rays removed to preserve open sky."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = 'd8495254-20a2-4d70-a2c6-140b4f7cd24a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/picture sun_d8495254-20a2-4d70-a2c6-140b4f7cd24a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'picture-sun'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        pts=[(10,6),(38,6),(42,10),(42,34),(42,38),(38,42),(32,42),(10,42),(6,38),(6,34),(6,10)]
        ids=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%len(pts)];name='frame-'+str(i);ids.append(name)
            if i in (1,4,7,10):self.add_arc(name,a,b,radius_x=4)
            else:self.add_line(name,a,b)
        self.add_contour('frame',*ids,closed=True)
        self.add_arc('sun-a',(21,18),(27,18),radius_x=3)
        self.add_arc('sun-b',(27,18),(21,18),radius_x=3)
        self.add_contour('sun','sun-a','sun-b',closed=True)
        self.add_bezier('front-hill',(6,34),((12,28),(20,28),(26,34)),((29,37),(30,39),(32,42)))
        self.add_bezier('back-hill',(26,34),((31,29),(36,30),(42,34)))
        self.relate('connect','front-hill','frame')
        self.relate('connect','back-hill','frame')
        self.relate('connect','front-hill','back-hill')
