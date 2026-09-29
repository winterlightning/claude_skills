"""squarespace logo.
Plan: Restored broad diagonal S ribbons with rounded returns and overlapping offset ends.
Construction: No useful exact Lucide logo match; coherent tangent curves and shared diagonal offsets.
Keyshape: SQUARE; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'e67f8d26-5a13-4179-830d-68e3d196c80a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__interlocking-s-emblem/20260929T033633Z-thuan-mac/reference/squarespace logo_e67f8d26-5a13-4179-830d-68e3d196c80a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'interlocking-s-emblem'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('squarespace', 'logo')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

    def build(self):

        self.add_bezier('upper-ribbon',(33,9),((28,4),(23,4),(19,8)),((15,12),(10,17),(7,20)),((0,28),(10,38),(18,31)),((23,26),(29,20),(33,17)),((40,11),(48,21),(41,28)))
        self.add_bezier('lower-ribbon',(41,28),((36,33),(31,38),(28,41)),((23,46),(18,44),(15,41)))
        self.add_bezier('inner-return',(15,41),((20,36),(28,28),(33,23)),((36,20),(39,24),(36,27)),((32,31),(27,36),(24,38)))
        self.add_bezier('upper-return',(24,38),((20,42),(14,39),(12,38)))
        self.add_line('upper-inner',(12,26),(29,9))
        self.relate('connect','upper-ribbon','lower-ribbon');self.relate('connect','lower-ribbon','inner-return');self.relate('connect','inner-return','upper-return')
