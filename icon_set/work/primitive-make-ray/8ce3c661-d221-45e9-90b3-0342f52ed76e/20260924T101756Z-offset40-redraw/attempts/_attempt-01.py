"""An angular gear with seven regularly spaced trapezoidal teeth, matching the reference. Bounds (6,6)-(42,42). A shared seven-tooth radial definition owns all repeated corners.
Construction reference: Lucide settings: repeated radial tooth construction; original seven angular teeth preserved.
Omissions: Subpixel center speck omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8ce3c661-d221-45e9-90b3-0342f52ed76e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__angular-gear/20260924T101756Z-thuan-mac/reference/cog_8ce3c661-d221-45e9-90b3-0342f52ed76e.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='angular-gear'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('cog',)
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        poly('gear',(20,6),(28,6),(30,12),(33,14),(39,12),(42,18),(37,23),(37,26),(42,30),(40,37),(33,37),(30,40),(28,42),(20,42),(18,40),(15,37),(8,37),(6,30),(11,26),(11,23),(6,18),(9,12),(15,14),(18,12),closed=True)
