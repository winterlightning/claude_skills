"""Garden Pruning Shears.

Plan: Open hooked pruning blade and two rounded handles. Bounds8,4,40,44.
Construction reference: scissors.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90d90e0e-aba7-45e7-989c-2016fb704666'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/prune_90d90e0e-aba7-45e7-989c-2016fb704666.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-curved-pruning-shears'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('open', 'curved', 'pruning', 'shears')

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

        path('blade',(24,24),[('C',(8,4),(12,22),(8,12)),('C',(30,14),(18,6),(24,8)),('L',(40,4))])
        path('handle-left',(24,24),[('L',(10,38)),('C',(16,44),(6,42),(12,44)),('L',(30,30)),('L',(24,24))],True)
        path('handle-right',(24,24),[('L',(40,38)),('C',(34,44),(40,42),(38,44)),('L',(18,30)),('L',(24,24))],True)
        join('blade','handle-left');join('blade','handle-right');join('handle-left','handle-right')
