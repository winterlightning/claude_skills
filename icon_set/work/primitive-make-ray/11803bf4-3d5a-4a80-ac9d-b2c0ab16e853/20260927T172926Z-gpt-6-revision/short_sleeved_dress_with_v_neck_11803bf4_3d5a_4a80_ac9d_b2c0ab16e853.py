"""Short-sleeved dress with a clear V neckline, waist seam, and broad skirt. The source sets the garment shape; the local Lucide mail and user references did not replace it."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '11803bf4-3d5a-4a80-ac9d-b2c0ab16e853'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__short-sleeved-dress-with-v-neck/20260927T172707Z-thuan-mac-1/reference/shirtdress_11803bf4-3d5a-4a80-ac9d-b2c0ab16e853.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'short-sleeved-dress-with-v-neck'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('short', 'sleeved', 'dress', 'with', 'v', 'neck')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('dress',(18,4),[('L',(24,12)),('L',(30,4)),('L',(34,6)),('L',(40,14)),('L',(34,20)),('L',(30,16)),('L',(30,24)),('L',(40,44)),('L',(8,44)),('L',(18,24)),('L',(18,16)),('L',(14,20)),('L',(8,14)),('L',(14,6)),('L',(18,4))],True)
        line('waist',(18,24),(30,24));join('waist','dress')
