"""Friendly Dog Face.

Plan: Dog with long hanging ears, round nose and extended tongue. Bounds6,6,42,42. Remove tiny eyes.
Construction reference: No useful local Lucide match.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d7d172d-b4f6-4dd0-8a05-cbf34601aa34'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/doggie_7d7d172d-b4f6-4dd0-8a05-cbf34601aa34.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dog-face-with-drooping-ears-and-tongue'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('dog', 'face', 'with', 'drooping', 'ears', 'and', 'tongue')

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

        path('face',(14,16),[('C',(24,6),(14,8),(18,6)),('C',(34,16),(30,6),(34,8)),('L',(34,28)),('C',(24,36),(34,34),(30,36)),('C',(14,28),(18,36),(14,34)),('L',(14,16))],True)
        path('ear-left',(14,16),[('C',(6,18),(8,8),(6,12)),('L',(6,30)),('C',(14,28),(6,38),(14,34))]);join('ear-left','face')
        path('ear-right',(34,16),[('C',(42,18),(40,8),(42,12)),('L',(42,30)),('C',(34,28),(42,38),(34,34))]);join('ear-right','face')
        circle('nose',24,22,2)
        path('tongue',(20,36),[('L',(20,38)),('A',(28,38),4,4,False),('L',(28,36))]);join('tongue','face')
