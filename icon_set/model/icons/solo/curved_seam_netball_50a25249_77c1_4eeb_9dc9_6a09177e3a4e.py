"""Round Netball Sports Ball.

Plan: Netball outer circle radius20 with three curved seams. Shared endpoints retain broad asymmetric panels.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50a25249-77c1-4eeb-9dc9-6a09177e3a4e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/netball_50a25249-77c1-4eeb-9dc9-6a09177e3a4e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-seam-netball'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('curved', 'seam', 'netball')

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

        path('ball',(24,4),[('A',(36,8),20,20,True),('A',(44,24),20,20,True),('A',(36,40),20,20,True),('A',(24,44),20,20,True),('A',(12,40),20,20,True),('A',(4,24),20,20,True),('A',(8,12),20,20,True),('A',(24,4),20,20,True)],True)
        path('seam-a',(24,4),[('C',(12,40),(10,20),(20,30))]);join('seam-a','ball')
        path('seam-b',(36,8),[('C',(36,40),(32,18),(28,30))]);join('seam-b','ball')
        path('cross',(8,12),[('C',(44,24),(18,24),(32,24))]);join('cross','ball');join('cross','seam-a');join('cross','seam-b')
