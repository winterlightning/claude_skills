"""Round-Headed Baby in a Diagonal Wrap
Plan: Large round infant head wrapped by rounded lower blanket and diagonal fold.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Shared human user.svg circular head proportions.
Reduction: Diagonal fold removed during spacing repair; head/wrap spacing still fails. This reduction does not qualify as a completed swaddle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec8badad-3b98-4a32-bca0-d815508f5700'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baby hold hands_ec8badad-3b98-4a32-bca0-d815508f5700.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-headed-baby-in-a-diagonal-wrap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('baby', 'swaddle', 'blanket', 'head', 'newborn', 'wrap', 'infant')

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
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        circle('head',24,20,16)
        path('wrap',(8,20),[('L',(8,28)),('A',(24,44),16,16,False),('A',(40,28),16,16,False),('L',(40,20))]);join('wrap','head')
