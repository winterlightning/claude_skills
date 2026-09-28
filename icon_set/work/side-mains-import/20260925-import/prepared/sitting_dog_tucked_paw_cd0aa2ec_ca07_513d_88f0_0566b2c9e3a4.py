from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cd0aa2ec-ca07-513d-88f0-0566b2c9e3a4'
SOURCE_PATH = 'pictographic-primitives/pets/dog_cd0aa2ec-ca07-513d-88f0-0566b2c9e3a4.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'sitting-dog-tucked-paw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('dog',)
    def build(self):
        # Source-led seated dog: curved back and haunch, upright ear, muzzle and long chest.
        self.path("body",(36,42),[(36,26),((36,22),(42,25),(42,18)),(36,16),((35,13),(33,12),(30,12)),(26,6),((23,10),(22,12),(22,17)),((22,26),(14,27),(14,35)),((14,40),(16,42),(20,42)),(36,42)],True)
        self.path("tail",(6,18),[((6,27),(9,31),(15,31))]);self.relate("connect","tail","body")
        self.path("haunch",(22,33),[((27,33),(28,38),(25,40)),(28,42)]);self.relate("connect","haunch","body")
        # Tucked front paw is a short inward-sloping leg behind the chest.
        # Short tucked paw stays with the haunch rather than crowding the straight chest.

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

    icon_id = 'sitting-dog-tucked-paw'
    category = 'objects/pets'
    aliases = ()
    keywords = ('dog', 'sitting', 'profile', 'silhouette', 'pet', 'paw', 'obedient')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
