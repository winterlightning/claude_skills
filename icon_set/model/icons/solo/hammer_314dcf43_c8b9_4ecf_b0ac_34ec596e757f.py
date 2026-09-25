from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '314dcf43-c8b9-4ecf-b0ac-34ec596e757f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/hammer_314dcf43-c8b9-4ecf-b0ac-34ec596e757f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hammer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('hammer',)
    def build(self):
        # Reference square mallet: equal sides, exact45-degree head and aligned handle.
        # Replaces the prior tiny35-radius patch and crooked one-unit head step.
        self.add_polyline("head",(6,19),(19,6),(32,19),(19,32),closed=True)
        self.add_line("handle",(26,26),(42,42));self.relate("connect","handle","head")

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

    icon_id = 'hammer'
    category = 'interface-essential'
    aliases = ()
    keywords = ('hammer', 'interface-essential')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
