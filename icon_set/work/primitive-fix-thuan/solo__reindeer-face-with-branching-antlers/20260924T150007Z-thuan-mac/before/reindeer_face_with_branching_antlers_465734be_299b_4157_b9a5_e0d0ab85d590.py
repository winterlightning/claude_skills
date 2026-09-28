"""Reindeer Head with Antlers.

Plan: Reindeer long muzzle, ears and antlers; bounds8,4,40,44. Reduce nose to dot and omit tiny eyes.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '465734be-299b-4157-b9a5-e0d0ab85d590'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/reindeer_465734be-299b-4157-b9a5-e0d0ab85d590.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'reindeer-face-with-branching-antlers'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('reindeer', 'face', 'with', 'branching', 'antlers')

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
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('head',(16,24),[('L',(8,20)),('C',(16,16),(8,12),(12,14)),('C',(32,16),(21,12),(27,12)),('C',(40,20),(36,14),(40,12)),('L',(33,24)),('L',(33,35)),('A',(15,35),9,9,True),('L',(15,24)),('L',(16,24))],True)
        for side in (-1,1):
         def p(x,y):return(24+side*x,y)
         poly('antler-'+str(side),p(8,16),p(12,10),p(12,4));line('branch-'+str(side),p(12,10),p(16,6));join('antler-'+str(side),'head');join('branch-'+str(side),'antler-'+str(side))
        self.add_dot('nose',(24,33))
