from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ce1ed58e-e672-4d3c-afbe-79946ffec09f'
SOURCE_PATH = 'pictographic-primitives/holidays/hand_ce1ed58e-e672-4d3c-afbe-79946ffec09f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'open-palm-hand-ce1ed58e-e672-4d3c-afbe-79946ffec09f'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('hand',)
    def build(self):
        # Lucide hand and human reference: upright fingers, clear thumb, rounded palm.
        # Four shared fingertip radius3.5/step7; longest middle reaches y6.
        self.path("outline",(14,28),[(14,13),((14,8.333),(21,8.333),(21,13)),(21,10),((21,4.667),(28,4.667),(28,10)),(28,13),((28,8.333),(35,8.333),(35,13)),(35,18),((35,13.333),(42,13.333),(42,18)),(42,29),((42,37),(37,42),(29,42)),(25,42),((19,42),(17,40),(14,36)),(6,26),((6,20),(10,21),(14,28))],True)
        for x,y in ((21,13),(28,13),(35,18)):
            self.add_line(f"crease-{x}",(x,y),(x,25));self.relate("connect",f"crease-{x}","outline")

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
