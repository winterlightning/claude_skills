from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bf29416e-316c-548b-9cc0-8b851d979c09'
SOURCE_PATH = 'pictographic-primitives/pets/dog_bf29416e-316c-548b-9cc0-8b851d979c09.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'dog-catching-disc-raised-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog',)
    def build(self):
        # Actual reference is dog holding a tilted disc, not the supplied sperm-cell label.
        # Curved ear and head slope, clear muzzle, tilted oval, bent lower neck/foreleg.
        self.path("head",(42,18),[((42,12),(40,8),(36,6)),(33,15),((26,15),(26,17),(22,17)),(15,17),((12,17),(13,21),(13,24))])
        self.path("disc",(6,37),[((6,31),(15,25),(22,25)),((29,25),(28,32),(22,37)),((18,40),(14,42),(10,42)),((7,42),(6,40),(6,37))],True)
        self.relate("connect","head","disc")
        self.path("lower-neck",(25,34),[(31,34),((34,34),(35,38),(37,42))]);self.relate("connect","lower-neck","disc")

    def path(self,name,start,commands,closed=False):
        members=[]
        for i,c in enumerate(commands):
            tag=f"{name}-{i}"
            if len(c)==2: self.add_line(tag,start,c); start=c
            else: self.add_bezier(tag,start,c); start=c[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for i in range(4): self.add_arc(f"{name}-{i}",pts[i],pts[i+1],radius_x=r)
        self.add_contour(name,*[f"{name}-{i}" for i in range(4)],closed=True)

    def box(self,name,x,y,w,h,r=0):
        if not r:
            self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r),(x+r,y)]
        for i in range(8):
            if i%2: self.add_arc(f"{name}-{i}",pts[i],pts[i+1],radius_x=r)
            else: self.add_line(f"{name}-{i}",pts[i],pts[i+1])
        self.add_contour(name,*[f"{name}-{i}" for i in range(8)],closed=True)

    icon_id = 'dog-catching-disc-raised-head'
    category = 'pets'
    aliases = ()
    keywords = ('dog', 'disc', 'frisbee', 'fetch', 'play', 'catch', 'pet')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
