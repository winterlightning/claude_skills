"""Sandbag Defense Barrier.

Plan: Retained the rounded shelter and all five sandbags in staggered two-over-three courses. Shared straight seams replace overlapping thin bag contours.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '301c2e56-228d-43b7-8ad0-61ec9594e803'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/sand bag 1_301c2e56-228d-43b7-8ad0-61ec9594e803.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sandbag-barrier-before-a-sheltered-opening'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ()
    keywords = ('sandbag', 'barrier', 'before', 'a', 'sheltered', 'opening')

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

        path('shelter',(10,22),[('L',(10,14)),('A',(18,6),8,8,True),('L',(34,6)),('A',(42,14),8,8,True),('L',(42,26))])
        rect('stack',6,22,36,20,4)
        line('course',(6,32),(42,32));join('course','stack')
        line('top-seam',(24,22),(24,32));join('top-seam','stack');join('top-seam','course')
        for x in (18,30):line('bottom-'+str(x),(x,32),(x,42));join('bottom-'+str(x),'course');join('bottom-'+str(x),'stack')
        join('shelter','stack')
