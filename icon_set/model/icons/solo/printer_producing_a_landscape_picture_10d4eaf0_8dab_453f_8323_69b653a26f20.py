"""Printer Printing Landscape Image.

Plan: Printer with input sheet and emerging landscape. Bounds6,6,42,42. Omit fold and secondary peak to retain a legible mountain print.
Construction reference: Lucide briefcase: rounded housing with deliberate shared attachments
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '10d4eaf0-8dab-453f-8323-69b653a26f20'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/print picture_10d4eaf0-8dab-453f-8323-69b653a26f20.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'printer-producing-a-landscape-picture'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('printer', 'producing', 'a', 'landscape', 'picture')

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

        path('printer',(14,30),[('L',(6,30)),('L',(6,18)),('A',(10,14),4,4,True),('L',(14,14)),('L',(34,14)),('L',(38,14)),('A',(42,18),4,4,True),('L',(42,30)),('L',(34,30))])
        poly('paper',(14,14),(14,6),(34,6),(34,14));join('paper','printer')
        poly('print',(14,30),(14,22),(34,22),(34,30),(34,42),(14,42),closed=True);join('print','printer')
        poly('mountain',(14,42),(24,31),(34,42));join('mountain','print')
