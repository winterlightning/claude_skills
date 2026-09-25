"""Five Petal Flower.

Plan: Five rounded lobes surround circular center; bounds6,6,42,42. Shared petal contour drops cramped radial seams.
Construction reference: flower.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59e5c54e-47c7-45fc-becf-a493bbebd830'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/onam 2_59e5c54e-47c7-45fc-becf-a493bbebd830.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'five-rounded-flower-petals'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('five', 'rounded', 'flower', 'petals')

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

        path('flower',(16,16),[('C',(24,6),(14,8),(18,6)),('C',(32,16),(30,6),(34,8)),('C',(42,24),(40,12),(42,18)),('C',(34,30),(42,28),(38,30)),('C',(32,42),(40,38),(38,42)),('C',(24,36),(28,42),(24,39)),('C',(16,42),(24,39),(20,42)),('C',(14,30),(10,42),(8,38)),('C',(6,24),(10,30),(6,28)),('C',(16,16),(6,18),(8,12))],True)
        circle('center',24,25,3)
