"""Rounded Five Pointed Star.

Plan: Five-point star mirrored aboutx24; bounds6,6,42,42. Round joins retain softened tips.
Construction reference: Lucide star: five equal point rhythm and deliberate angular valleys
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '641880cd-15f5-45e3-b6dc-652ed7f7cbb7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/spark logo_641880cd-15f5-45e3-b6dc-652ed7f7cbb7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'five-point-star-with-softened-tips'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('five', 'point', 'star', 'with', 'softened', 'tips')

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

        poly('star',(24,6),(30,18),(42,20),(33,29),(36,42),(24,35),(12,42),(15,29),(6,20),(18,18),closed=True)
