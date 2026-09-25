"""Portable Radio Receiver with Antenna.

Plan: Radio bounds6,6,42,42. Large speaker, two controls as short lines and angled antenna; simplify tuning box to a bar.
Construction reference: Lucide briefcase rounded enclosure; source radio layout
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cbb9047-d282-4f34-af69-1f0fe7048535'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/radio_1cbb9047-d282-4f34-af69-1f0fe7048535.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'portable-radio-with-angled-antenna'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('portable', 'radio', 'with', 'angled', 'antenna')

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

        rect('body',6,18,36,24,4)
        circle('speaker',18,30,3)
        line('tuner',(30,30),(33,30))
        line('antenna',(14,18),(26,6));join('antenna','body')
