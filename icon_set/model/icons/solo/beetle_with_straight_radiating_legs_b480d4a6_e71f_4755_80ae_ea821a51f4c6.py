"""Simple Beetle Insect Symbol.

Plan: Rounded beetle shell, medial seam, two antennae and three straight radiating leg pairs retained. Removed the separate head/body seam. Keyshape SQUARE uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide bug: mirrored body, medial seam, three leg pairs; shared attachment nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b480d4a6-e71f-4755-80ae-ea821a51f4c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bug_b480d4a6-e71f-4755-80ae-ea821a51f4c6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'beetle-with-straight-radiating-legs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('beetle', 'with', 'straight', 'radiating', 'legs')

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

        path('shell',(16,22),[('L',(16,18)),('C',(18,12),(16,15),(16,13)),('C',(24,10),(20,10),(22,10)),('C',(30,12),(26,10),(28,10)),('C',(32,18),(32,13),(32,15)),('L',(32,22)),('C',(34,30),(33,24),(34,27)),('C',(32,38),(34,34),(34,36)),('C',(24,42),(30,41),(27,42)),('C',(16,38),(21,42),(18,41)),('C',(14,30),(14,36),(14,34)),('C',(16,22),(14,27),(15,24))],True)
        line('seam',(24,22),(24,42));join('seam','shell')
        for side in [-1,1]:
         line(f'antenna{side}',(24+side*6,12),(24+side*10,6));join(f'antenna{side}','shell')
         for j,(dx,y,ey) in enumerate([(8,22,18),(10,30,30),(8,38,42)]):
          line(f'leg{side}-{j}',(24+side*dx,y),(24+side*18,ey));join(f'leg{side}-{j}','shell')
