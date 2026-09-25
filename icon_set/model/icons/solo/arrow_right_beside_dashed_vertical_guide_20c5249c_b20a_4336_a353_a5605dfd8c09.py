"""Right Arrow with Dashed Vertical Reference.

Plan: Open right arrow and three guide dashes; bounds6,6,42,42.
Construction reference: Lucide arrow-right shared arrowhead tip
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20c5249c-b20a-4336-a353-a5605dfd8c09'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/diagram fall rise steady large head_20c5249c-b20a-4336-a353-a5605dfd8c09.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arrow-right-beside-dashed-vertical-guide'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arrow', 'right', 'beside', 'dashed', 'vertical', 'guide')

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

        for i,y in enumerate((6,22,38)):line('dash-'+str(i),(6,y),(6,y+4))
        line('shaft',(18,24),(42,24));poly('head',(28,10),(42,24),(28,38));join('shaft','head')
