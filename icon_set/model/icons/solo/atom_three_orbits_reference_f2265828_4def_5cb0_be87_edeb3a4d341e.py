"""Scientific Atom Symbol.

Plan: Three crossing elliptical orbits and circular nucleus. Bounds6,6,42,42. Retain three orbits; no false joins at crossings.
Construction reference: atom.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2265828-4def-5cb0-be87-edeb3a4d341e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/programing/amazon web service sagemaker_f2265828-4def-5cb0-be87-edeb3a4d341e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'atom-three-orbits-reference'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases = ()
    keywords = ('atom', 'three', 'orbits', 'reference')

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

        path('vertical',(24,6),[('C',(36,24),(31,6),(36,14)),('C',(24,42),(36,34),(31,42)),('C',(12,24),(17,42),(12,34)),('C',(24,6),(12,14),(17,6))],True)
        path('diagonal-a',(14,10),[('C',(42,34),(26,10),(42,22)),('C',(34,38),(42,38),(38,38)),('C',(6,14),(22,38),(6,26)),('C',(14,10),(6,10),(10,10))],True)
        path('diagonal-b',(34,10),[('C',(6,34),(22,10),(6,22)),('C',(14,38),(6,38),(10,38)),('C',(42,14),(26,38),(42,26)),('C',(34,10),(42,10),(38,10))],True)
        circle('nucleus',24,24,2)
