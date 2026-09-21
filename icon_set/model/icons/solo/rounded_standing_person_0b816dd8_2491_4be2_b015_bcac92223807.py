"""Full Body Person.

Plan: Standing figure uses shared circular head and stick limbs. Head center24,10 radius6; torso starts24,24 gives exact8 outline gap. Bounds8,4,40,44.
Construction reference: human_ref/full_body_ref.png.
Final review: Circular head radius6 at24,10; torso junction24,24 gives exactly8 centerline /4 ink gap.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b816dd8-2491-4be2-b015-bcac92223807'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/body_0b816dd8-2491-4be2-b015-bcac92223807.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-standing-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('rounded', 'standing', 'person')

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

        circle('head',24,10,6)
        line('torso',(24,24),(24,34));poly('arms',(8,32),(16,24),(24,24),(32,24),(40,32));join('arms','torso')
        poly('legs',(14,44),(24,34),(34,44));join('legs','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
