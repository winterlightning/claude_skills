from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a83ae7ee-8a41-4fef-9868-438ff298dd07'
SOURCE_PATH = 'pictographic-primitives/ecology/air purifier 1_a83ae7ee-8a41-4fef-9868-438ff298dd07.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'air-purifier-with-midline-and-upright-indicator'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('air purifier 1',)
    def build(self):
        # Reviewer: two thin vertical S-shaped open airflow strokes; stroke remains4.
        # Air-vent informs smooth open air paths; source owns the divided upright body.
        self.box("body",8,20,32,24,4)
        self.add_line("seam",(8,36),(40,36));self.relate("connect","seam","body")
        self.add_dot("indicator",(24,28))
        for x in (18,30):
            self.path(f"air-{x}",(x,4),[((x-4,6),(x+4,10),(x,12))])

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
