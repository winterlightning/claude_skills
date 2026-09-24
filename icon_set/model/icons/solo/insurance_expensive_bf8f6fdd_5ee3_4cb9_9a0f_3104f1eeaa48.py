"""A coin sits above a medical cross on a descending balance beam, indicating expensive insurance.
Construction reference: scale.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bf8f6fdd-5ee3-4cb9-9a0f-3104f1eeaa48'
SOURCE_PATH = 'icon_set/work/todo-references/insurance expensive_bf8f6fdd-5ee3-4cb9-9a0f-3104f1eeaa48.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'insurance-expensive'
    keyshape = Keyshape.SQUARE
    # Visible ink extremes: (4, 4, 44, 44).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('insurance', 'expensive')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: price coin higher on left; medical cross lower on right; tilted beam.
        self.circle('coin',14,14,8)
        self.add_bezier('dollar',(17,10),((10,8),(10,14),(14,14)),((19,14),(18,19),(11,18)))
        self.add_line('dollar-stem',(14,7),(14,21))
        self.relate('connect','dollar','dollar-stem')
        self.add_polyline('medical-cross',(30,10),(38,10),(38,14),(42,14),(42,22),(38,22),(38,26),(30,26),(30,22),(26,22),(26,14),(30,14),closed=True)
        self.add_polyline('beam',(6,28),(24,33),(42,38))
        self.add_polyline('fulcrum',(24,33),(16,42),(32,42),closed=True)
        self.relate('connect','beam','fulcrum')
