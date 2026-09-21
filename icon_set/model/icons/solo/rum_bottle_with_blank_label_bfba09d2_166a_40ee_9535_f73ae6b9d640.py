"""Rum Bottle with Label.

Plan: Rum bottle with broad blank label and cap; bounds8,4,40,44.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfba09d2-166a-40ee-9535-f73ae6b9d640'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/rum_bfba09d2-166a-40ee-9535-f73ae6b9d640.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rum-bottle-with-blank-label'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('rum', 'bottle', 'with', 'blank', 'label')

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

        path('bottle',(20,4),[('L',(28,4)),('L',(28,12)),('L',(28,16)),('C',(40,20),(28,18),(40,14)),('L',(40,28)),('L',(40,36)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,36)),('L',(8,28)),('L',(8,20)),('C',(20,16),(8,14),(20,18)),('L',(20,12)),('L',(20,4))],True)
        for y in (12,28,36):line('band-'+str(y),(20 if y==12 else 8,y),(28 if y==12 else 40,y));join('band-'+str(y),'bottle')
