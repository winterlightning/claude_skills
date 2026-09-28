from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f7df912f-c801-53cc-a0b8-6bfbd3f5fdf8'
SOURCE_PATH = 'pictographic-primitives/travel/crafts model plane_f7df912f-c801-53cc-a0b8-6bfbd3f5fdf8.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'slender-airliner-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('crafts model plane',)
    def build(self):
        # Plane original: fuselage remains visible between separate swept wing outlines.
        # Lucide plane informs a rounded nose; diagonal source orientation preserved.
        self.path("fuselage",(40,6),[((41,6),(42,7),(42,8)),((42,17),(17,42),(8,42)),((6,42),(6,41),(6,40)),((6,31),(31,6),(40,6))],True)
        self.add_polyline("wing-left",(26,15),(10,8),(6,11),(18,24));self.relate("connect","wing-left","fuselage")
        self.add_polyline("wing-right",(34,22),(40,37),(37,42),(25,30));self.relate("connect","wing-right","fuselage")
        self.add_polyline("tail-left",(13,31),(6,28),(6,32),(10,36));self.relate("connect","tail-left","fuselage")
        self.add_polyline("tail-right",(18,36),(21,42),(17,42),(14,39));self.relate("connect","tail-right","fuselage")

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
