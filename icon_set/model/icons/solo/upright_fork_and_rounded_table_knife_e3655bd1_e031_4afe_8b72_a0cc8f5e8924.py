"""Fork and Knife Utensils.

Plan: Three fork tines and curved knife. Bounds8,4,40,44; use single-line handles.
Construction reference: utensils.
Final review: Widened fork tines; single-line handles.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3655bd1-e031-4afe-8b72-a0cc8f5e8924'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dining_e3655bd1-e031-4afe-8b72-a0cc8f5e8924.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-fork-and-rounded-table-knife'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('upright', 'fork', 'and', 'rounded', 'table', 'knife')

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

        path('fork',(8,4),[('L',(8,16)),('A',(12,20),4,4,False),('L',(20,20)),('A',(24,16),4,4,False),('L',(24,4))])
        line('tine',(16,4),(16,20));join('fork','tine');line('handle',(16,20),(16,44));join('handle','fork');join('handle','tine')
        path('knife',(40,4),[('C',(32,18),(32,6),(32,12)),('L',(32,26)),('L',(40,26)),('L',(40,4))],True);line('knife-handle',(40,26),(40,44));join('knife','knife-handle')
