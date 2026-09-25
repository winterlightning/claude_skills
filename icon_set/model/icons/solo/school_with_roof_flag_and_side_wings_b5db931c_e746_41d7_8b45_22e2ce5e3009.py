"""School Building with Flag.

Plan: Retained the pitched central school entrance, doorway, roof flag and two side wings. Reduced the small flag to an open pennant cue and omitted the tiny windows.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5db931c-e746-41d7-8b45-22e2ce5e3009'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/school_b5db931c-e746-41d7-8b45-22e2ce5e3009.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'school-with-roof-flag-and-side-wings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('school', 'with', 'roof', 'flag', 'and', 'side', 'wings')

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

        poly('school',(6,42),(6,26),(14,26),(14,20),(24,14),(34,20),(34,26),(42,26),(42,42),(6,42),closed=True)
        poly('flag',(24,14),(24,6),(36,6));join('flag','school')
        poly('door',(20,42),(20,30),(28,30),(28,42));join('door','school')
