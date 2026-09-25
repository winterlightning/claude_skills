"""Flashing Emergency Siren Light.

Plan: Domed beacon above wide base, matching radial light marks; bounds6,6,42,42. Single baseline replaces narrow double base.
Construction reference: siren.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44c5ea3c-73b1-415a-8c19-258fa8e8ebc5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/siren_44c5ea3c-73b1-415a-8c19-258fa8e8ebc5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'five-ray-alarm-beacon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('five', 'ray', 'alarm', 'beacon')

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

        path('dome',(14,42),[('L',(14,28)),('A',(24,18),10,10,True),('A',(34,28),10,10,True),('L',(34,42))])
        poly('base',(6,42),(14,42),(34,42),(42,42));join('base','dome')
        line('top-ray',(24,6),(24,9));line('left-ray',(6,10),(10,14));line('right-ray',(38,14),(42,10))
        line('left-side',(6,28),(6,29));line('right-side',(42,29),(42,28))
