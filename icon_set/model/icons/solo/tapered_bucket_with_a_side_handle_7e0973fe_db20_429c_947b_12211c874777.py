"""Simple Bucket with Handle.

Plan: Open oval rim, tapered pail and side handle retained. Removed the small circular handle rivet and enlarged the handle opening. Keyshape VRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e0973fe-db20-429c-947b-12211c874777'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon s3 storage_7e0973fe-db20-429c-947b-12211c874777.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tapered-bucket-with-a-side-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('tapered', 'bucket', 'with', 'a', 'side', 'handle')

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

        path('rim',(8,10),[('C',(19,4),(8,6),(13,4)),('C',(30,10),(25,4),(30,6)),('C',(19,16),(30,14),(25,16)),('C',(8,10),(13,16),(8,14))],True)
        path('body',(8,10),[('L',(11,39)),('C',(19,44),(12,44),(15,44)),('C',(27,39),(23,44),(26,44)),('L',(30,10))]);join('rim','body')
        path('handle',(29,20),[('L',(36,20)),('A',(40,24),4,4,True),('L',(40,28)),('A',(36,32),4,4,True),('L',(28,32))]);join('handle','body')
