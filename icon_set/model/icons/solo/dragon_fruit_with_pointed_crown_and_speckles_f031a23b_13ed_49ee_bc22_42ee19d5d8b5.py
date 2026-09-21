"""Fresh Tropical Dragon Fruit.

Plan: Round dragon fruit and three-point leafy crown. Bounds8,4,40,44. One large central seed mark.
Construction reference: No useful local Lucide match.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f031a23b-13ed-49ee-bc22-42ee19d5d8b5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dragonfruit_f031a23b-13ed-49ee-bc22-42ee19d5d8b5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dragon-fruit-with-pointed-crown-and-speckles'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('dragon', 'fruit', 'with', 'pointed', 'crown', 'and', 'speckles')

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

        path('fruit',(12,18),[('L',(10,8)),('L',(20,14)),('L',(24,4)),('L',(28,14)),('L',(38,8)),('L',(36,18)),('C',(40,28),(40,22),(40,24)),('A',(24,44),16,16,True),('A',(8,28),16,16,True),('C',(12,18),(8,24),(8,22))],True)
        line('seed',(24,27),(24,31))
