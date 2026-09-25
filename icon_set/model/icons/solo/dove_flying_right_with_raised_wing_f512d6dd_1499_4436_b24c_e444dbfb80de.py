"""Flying Dove Bird Symbol.

Plan: Dove flies right with raised wing and broad trailing tail; bounds6,6,42,42. Omit tiny eye and feather marks.
Construction reference: bird.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f512d6dd-1499-4436-b24c-e444dbfb80de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dove_f512d6dd-1499-4436-b24c-e444dbfb80de.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dove-flying-right-with-raised-wing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('dove', 'flying', 'right', 'with', 'raised', 'wing')

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

        path('dove',(6,6),[('C',(26,22),(14,12),(22,12)),('C',(36,16),(26,10),(34,10)),('L',(42,20)),('L',(36,24)),('C',(28,34),(36,30),(34,33)),('L',(20,42)),('L',(6,38)),('L',(18,28)),('C',(6,6),(6,26),(6,18))],True)
