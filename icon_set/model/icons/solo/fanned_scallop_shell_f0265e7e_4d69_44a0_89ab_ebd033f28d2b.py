"""Scallop Sea Shell.

Plan: Retained the five-lobed scallop fan and pointed hinge. Reduced the internal ribs to a central division and merged the small hinge tabs into the outline.
Construction reference: Lucide shell inspected; spiral differs, so source-specific fanned construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0265e7e-4d69-44a0-89ab-ebd033f28d2b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/clam_f0265e7e-4d69-44a0-89ab-ebd033f28d2b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fanned-scallop-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('fanned', 'scallop', 'shell')

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

        path('shell',(24,42),[('L',(8,28)),('C',(6,22),(6,27),(6,25)),('C',(10,16),(6,18),(6,16)),('C',(18,10),(10,10),(14,8)),('C',(24,6),(18,6),(20,6)),('C',(30,10),(28,6),(30,6)),('C',(38,16),(34,8),(38,10)),('C',(42,22),(42,16),(42,18)),('C',(40,28),(42,25),(42,27)),('L',(24,42))],True)
        for name,start in [('b',(24,6))]:line(name,start,(24,42));join(name,'shell')
        
