from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b82a8e4c-4496-539d-b448-cb99ae868dd5'
SOURCE_PATH = 'pictographic-primitives/pets/dog_b82a8e4c-4496-539d-b448-cb99ae868dd5.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'bulldog-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('dog',)

    def build(self):
        # Lucide dog rounded hanging ears; reference owns browless bulldog muzzle.
        # Paired curves mirror across x24. Preserve the two full rounded jowls.
        self.path("crown",(6,17),[((6,11),(10,6),(15,6)),((18,6),(19,8),(20,8)),(28,8),((29,8),(30,6),(33,6)),((38,6),(42,11),(42,17))])
        self.path("ear-left",(6,17),[((6,20),(11,21),(14,18))]);self.relate("connect","ear-left","crown")
        self.path("ear-right",(34,18),[((37,21),(42,20),(42,17))]);self.relate("connect","ear-right","crown")
        self.path("cheek-left",(7,19),[((5,28),(7,33),(12,35))]);self.relate("connect","cheek-left","ear-left")
        self.path("cheek-right",(41,19),[((43,28),(41,33),(36,35))]);self.relate("connect","cheek-right","ear-right")
        self.path("muzzle",(24,25),[((18,25),(12,31),(12,36)),((12,40),(14,42),(17,42)),((20,42),(23,38),(24,35)),((25,38),(28,42),(31,42)),((34,42),(36,40),(36,36)),((36,31),(30,25),(24,25))],True)
        self.relate("connect","muzzle","cheek-left");self.relate("connect","muzzle","cheek-right")
        self.add_line("nose",(22,25),(26,25));self.add_line("mouth",(24,25),(24,35))
        self.relate("connect","nose","muzzle");self.relate("connect","nose","mouth");self.relate("connect","mouth","muzzle")

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

    icon_id = 'bulldog-face'
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('dog', 'bulldog', 'face', 'breed', 'jowls', 'pet', 'english-bulldog')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
