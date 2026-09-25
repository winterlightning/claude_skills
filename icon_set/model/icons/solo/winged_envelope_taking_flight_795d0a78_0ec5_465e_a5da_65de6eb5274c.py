"""Flying Message Envelope.

Plan: Fantasy envelope with attached wings and rising motion strokes. Bounds4,8,44,40. Simplify wing feathers and omit trails if too crowded.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '795d0a78-0ec5-465e-a5da-65de6eb5274c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/send email fly_795d0a78-0ec5-465e-a5da-65de6eb5274c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'winged-envelope-taking-flight'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('winged', 'envelope', 'taking', 'flight')

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

        poly('envelope',(14,16),(34,16),(34,30),(34,40),(14,40),(14,30),closed=True)
        poly('flap',(14,16),(24,26),(34,16));join('flap','envelope')
        path('left-wing',(14,16),[('C',(4,8),(10,14),(6,12)),('L',(4,20)),('C',(14,30),(4,26),(10,30))]);join('left-wing','envelope')
        path('right-wing',(34,16),[('C',(44,8),(38,14),(42,12)),('L',(44,20)),('C',(34,30),(44,26),(38,30))]);join('right-wing','envelope')
