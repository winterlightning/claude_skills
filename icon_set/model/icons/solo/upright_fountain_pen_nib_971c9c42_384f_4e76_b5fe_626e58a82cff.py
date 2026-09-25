"""Fountain Pen Drawing Tool.

Plan: Symmetric pointed nib and open round breathing hole ending slit. Bounds8,4,40,44.
Construction reference: pen-tool.
Final review: Smaller breathing hole with slit.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '971c9c42-384f-4e76-b5fe-626e58a82cff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pen nib_971c9c42-384f-4e76-b5fe-626e58a82cff.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-fountain-pen-nib'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('upright', 'fountain', 'pen', 'nib')

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

        poly('nib',(24,4),(40,28),(34,36),(34,44),(14,44),(14,36),(8,28),closed=True)
        line('base-seam',(14,36),(34,36));join('base-seam','nib')
        circle('hole',24,25,3);line('slit',(24,4),(24,22));join('slit','nib');join('slit','hole')
