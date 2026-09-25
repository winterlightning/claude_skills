from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ce974c56-ba13-40f8-bcc7-d0c05f09f26f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/volume_ce974c56-ba13-40f8-bcc7-d0c05f09f26f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'volume-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('volume',)
    def build(self):
        # Lucide volume-2: coherent speaker mouth and two long circular sound-wave arcs.
        # Rounded rear corners; smooth source-style outward wave bulges.
        self.path("speaker",(22,8),[(12,17),(8,17),((5,17),(4,18),(4,21)),(4,27),((4,30),(5,31),(8,31)),(12,31),(22,40),(22,8)],True)
        self.path("wave-inner",(31,18),[((35,21),(35,27),(31,30))])
        self.path("wave-outer",(39,12),[((42,15),(44,20),(44,24)),((44,28),(42,33),(39,36))])

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

    icon_id = 'volume-interface-essential'
    category = 'interface-essential'
    aliases = ()
    keywords = ('volume', 'interface-essential')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
