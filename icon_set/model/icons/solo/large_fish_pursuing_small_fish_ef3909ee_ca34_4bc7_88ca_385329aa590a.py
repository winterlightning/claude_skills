"""Large Fish Pursuing Small Fish
Plan: Large open-mouthed fish on the left pursues a small outlined fish at right. Two different body sizes are essential.
Keyshape HRECT_M: (2, 8, 46, 40).
Construction reference: Lucide fish: simple outline and one eye.
Reduction: Dropped large fish gill, retained both fish, open mouth, eye and tails.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef3909ee-ca34-4bc7-88ca-385329aa590a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/business big small fish_ef3909ee-ca34-4bc7-88ca-385329aa590a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'large-fish-pursuing-small-fish'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    aliases = ()
    keywords = ('fish', 'large', 'small', 'pursuit', 'sea', 'aquatic', 'animals')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        path('large-fish',(28,10),[('C',(10,24),(17,10),(10,16)),('C',(28,38),(10,32),(17,38)),('L',(18,24)),('L',(28,10))],True)
        self.add_polyline('large-tail',(4,16),(10,24),(4,32))
        for a in ['large-fish-0','large-fish-1']:
            for b in ['large-tail-1','large-tail-2']:self.relate('connect',a,b)
        circle('small-fish',39,24,5)
        self.add_polyline('small-tail',(32,19),(34,24),(32,29))
        for a in ['small-fish-0','small-fish-3']:
            for b in ['small-tail-1','small-tail-2']:self.relate('connect',a,b)
