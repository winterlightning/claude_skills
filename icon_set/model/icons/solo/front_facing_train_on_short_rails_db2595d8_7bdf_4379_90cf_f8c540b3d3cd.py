"""Front View Train on Tracks.

Plan: Rounded train front with windshield and short rails. Bounds8,4,40,44. Simplify lamps to one broad bar.
Construction reference: train-front.
Final review: Broader train window; omitted lamps.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db2595d8-7bdf-4379-90cf-f8c540b3d3cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/station_db2595d8-7bdf-4379-90cf-f8c540b3d3cd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-facing-train-on-short-rails'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('front', 'facing', 'train', 'on', 'short', 'rails')

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

        rect('train',8,4,32,32,4)
        path('window',(16,4),[('L',(16,18)),('A',(20,22),4,4,False),('L',(28,22)),('A',(32,18),4,4,False),('L',(32,4))]);join('window','train')
        line('rail-left',(16,36),(12,44));line('rail-right',(32,36),(36,44));join('train','rail-left');join('train','rail-right')
