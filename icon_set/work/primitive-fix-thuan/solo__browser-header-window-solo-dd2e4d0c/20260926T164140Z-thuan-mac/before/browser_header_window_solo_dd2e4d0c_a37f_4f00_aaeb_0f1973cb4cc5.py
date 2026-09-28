from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dd2e4d0c-a37f-4f00-aaeb-0f1973cb4cc5'
SOURCE_PATH = 'pictographic-primitives/other/ui webpage bank_dd2e4d0c-a37f-4f00-aaeb-0f1973cb4cc5.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'browser-header-window-solo-dd2e4d0c'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('ui webpage bank',)
    def build(self):
        # Restore the complete banking website, including the missing temple symbol.
        # Lucide panel-top informs browser frame; compact pediment and three columns.
        self.box("window",6,6,36,36,4)
        self.add_line("header",(6,14),(42,14));self.relate("connect","header","window")
        self.add_polyline("roof",(15,25),(24,22),(33,25))
        self.add_line("base",(15,33),(33,33))
        for x in (16,24,32):
            self.add_line(f"column-{x}",(x,22 if x==24 else 25),(x,33));self.relate("connect",f"column-{x}","base");self.relate("connect",f"column-{x}","roof")

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

    icon_id = 'browser-header-window-solo-dd2e4d0c'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ('browser-header-window',)
    keywords = ('browser', 'header', 'window')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
