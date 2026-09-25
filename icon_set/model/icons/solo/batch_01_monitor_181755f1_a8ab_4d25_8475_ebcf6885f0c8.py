from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '181755f1-a8ab-4d25-8475-ebcf6885f0c8'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/monitor_181755f1-a8ab-4d25-8475-ebcf6885f0c8.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'batch-01-monitor'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "computers"
    aliases = ()
    keywords = ('monitor',)
    def build(self):
        # Reviewer: wider and more vertical screen. Full40-unit width and height24.
        # Lucide monitor: rounded screen with centered stem and broad balanced foot.
        self.box("screen",4,8,40,24,2)
        self.add_line("stand",(24,32),(24,40));self.relate("connect","stand","screen")
        self.add_line("foot",(16,40),(32,40));self.relate("connect","stand","foot")

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

    icon_id = 'batch-01-monitor'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'monitor', 'computers')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
