"""Giant Panda Head Icon.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
Rounded ears and diagonal eye patches identify the panda. The tiny muzzle is omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: panda.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f21a3780-5f8b-4bcd-a305-1e9f6381e99a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/panda_f21a3780-5f8b-4bcd-a305-1e9f6381e99a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-panda-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('round', 'panda', 'face')

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

        path('panda',(10,20),[('C',(6,12),(6,18),(6,16)),('A',(12,6),6,6,True),('C',(18,10),(16,6),(18,8)),('C',(30,10),(22,8),(26,8)),('C',(36,6),(30,8),(32,6)),('A',(42,12),6,6,True),('C',(38,20),(42,16),(42,18)),('C',(42,28),(42,22),(42,24)),('C',(24,42),(42,38),(34,42)),('C',(6,28),(14,42),(6,38)),('C',(10,20),(6,24),(6,22))],True)
        line('eye-left',(16,26),(19,23));line('eye-right',(29,23),(32,26))
