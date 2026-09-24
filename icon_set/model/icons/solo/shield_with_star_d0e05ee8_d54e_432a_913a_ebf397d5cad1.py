from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0e05ee8-d54e-432a-913a-ebf397d5cad1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/auth0 logo_d0e05ee8-d54e-432a-913a-ebf397d5cad1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shield-with-star'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('shield', 'with', 'star')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, x, y, w, h, r=0):
        if not r:
            self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            part=f'{name}-{i}'; ids.append(part)
            if i%2: self.add_arc(part,pts[i],pts[(i+1)%8],radius_x=r)
            else: self.add_line(part,pts[i],pts[(i+1)%8])
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Plan: VRECT_L extremes 8,4 to 40,44; mirrored shield owns inset five-point star.
        axis=24
        self.add_polyline('shield',(12,4),(36,4),(40,22),(36,32),(axis,44),(12,32),(8,22),closed=True)
        left=[(24,14),(21,22),(13,22),(19,27),(16,35)]
        star=left+[(24,30)]+[(48-x,y) for x,y in reversed(left[1:])]
        self.add_polyline('star',*star,closed=True)
