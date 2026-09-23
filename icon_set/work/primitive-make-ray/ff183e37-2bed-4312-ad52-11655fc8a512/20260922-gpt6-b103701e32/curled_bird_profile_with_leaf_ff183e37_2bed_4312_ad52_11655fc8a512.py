from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ff183e37-2bed-4312-ad52-11655fc8a512'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/bower logo_ff183e37-2bed-4312-ad52-11655fc8a512.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curled-bird-profile-with-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('curled', 'bird', 'profile', 'with', 'leaf')

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
        # Plan: SQUARE extremes6,6 to42,42; curled right-facing bird with lower tail and detached upper-right leaf.
        self.add_arc('curl',(21,24),(30,15),radius_x=9,sweep=False)
        self.add_arc('crown',(30,15),(21,6),radius_x=9,sweep=False)
        self.add_arc('back',(21,6),(6,21),radius_x=15,sweep=False)
        self.add_arc('belly',(6,21),(21,36),radius_x=15,sweep=False)
        self.add_arc('wing-tip',(21,36),(29,31),radius_x=10,sweep=False)
        self.add_contour('bird','curl','crown','back','belly','wing-tip')
        self.add_polyline('beak',(30,15),(42,21),(38,30),(29,31))
        self.relate('connect','bird','beak')
        self.add_polyline('tail',(29,31),(35,42),(16,39),(21,36))
        self.relate('connect','bird','tail')
        self.relate('connect','beak','tail')
        self.add_arc('leaf-a',(42,6),(34,14),radius_x=8)
        self.add_arc('leaf-b',(34,14),(42,6),radius_x=8)
        self.add_contour('leaf','leaf-a','leaf-b',closed=True)
