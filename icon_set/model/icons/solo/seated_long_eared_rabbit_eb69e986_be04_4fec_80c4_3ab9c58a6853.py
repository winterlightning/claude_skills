"""Sitting Bunny Rabbit.

Plan: Seated left-facing rabbit, tall ear, smooth haunch and integrated tail lobe; bounds (6,6)-(42,42).
Construction: Lucide rabbit: integrated ear and tail, coherent rounded haunch.
Reduction: Tail integrated into outer silhouette, tiny eye and toe marks omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb69e986-be04-4fec-80c4-3ab9c58a6853'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/04-eb69e986-be04-4fec-80c4-3ab9c58a6853.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'seated-long-eared-rabbit'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('seated', 'long', 'eared', 'rabbit')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('rabbit',(16,20),[('L',(16,10)),('A',(24,10),4,4,True),('L',(24,22)),('C',(36,31),(32,22),(35,25)),('C',(42,37),(40,31),(42,33)),('A',(37,42),5,5,True),('L',(6,42)),('L',(10,34)),('L',(10,28)),('C',(6,24),(6,28),(6,26)),('C',(16,20),(6,20),(12,20))],True)
        path('haunch',(28,31),[('A',(22,37),6,6,False),('L',(25,42))]);join('rabbit','haunch')
