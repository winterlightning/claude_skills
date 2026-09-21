"""Raised Open Hand.

Plan: Four fingers spaced on8-unit grid and broad palm; bounds6,6,42,42. Omit minor crease.
Construction reference: Lucide hand rounded fingers; shared human vocabulary
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '417c1577-8906-411f-bece-22457499460b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/labor hands_417c1577-8906-411f-bece-22457499460b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'raised-open-palm-reference-417c1577'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('raised', 'open', 'palm', 'reference', '417c1577')

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

        path('palm',(14,42),[('C',(10,34),(14,38),(12,38)),('L',(6,28)),('L',(6,24)),('A',(14,24),4,4,True),('L',(14,14)),('A',(22,14),4,4,True),('L',(22,10)),('A',(30,10),4,4,True),('L',(30,14)),('A',(38,14),4,4,True),('L',(38,20)),('C',(42,20),(38,16),(42,16)),('L',(42,28)),('C',(38,42),(42,34),(38,36))])
        line('finger-a',(22,14),(22,24));line('finger-b',(30,14),(30,24));join('finger-a','palm');join('finger-b','palm')
