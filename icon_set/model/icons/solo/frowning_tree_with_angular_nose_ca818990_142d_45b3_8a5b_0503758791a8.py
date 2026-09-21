"""Sad Personified Tree.

Plan: Personified sad tree with broad canopy and facial trunk; bounds8,4,40,44. Nose and frown retained, eyes simplified.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca818990-142d-45b3-8a5b-0503758791a8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mario tree 1_ca818990-142d-45b3-8a5b-0503758791a8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'frowning-tree-with-angular-nose'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('frowning', 'tree', 'with', 'angular', 'nose')

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

        path('tree',(11,44),[('L',(11,16)),('C',(8,10),(8,16),(8,13)),('C',(16,6),(8,6),(12,4)),('C',(24,4),(18,4),(20,4)),('C',(32,6),(28,4),(30,4)),('C',(40,10),(36,4),(40,6)),('C',(36,16),(40,13),(40,16)),('L',(36,44))])
        poly('nose',(19,24),(19,32),(8,32));join('nose','tree');line('eye',(27,24),(27,25))
        path('mouth',(21,43),[('C',(27,43),(22,40),(26,40))])
