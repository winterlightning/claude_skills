"""Hooded Swaddle with Crossed Blanket Folds
Plan: Rounded hooded swaddle with round face and two crossed blanket folds.
Keyshape: VRECT_M; exact inset SOLO48 envelope.
Construction: Shared human user.svg circular face vocabulary; Lucide baby facial proportions.
Reduction: Face opening reduced; two crossing blanket folds retained but a small opening still requires review."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0eaa90e-ee21-4ae5-bede-0c17096fa38f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baby newborn_e0eaa90e-ee21-4ae5-bede-0c17096fa38f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hooded-swaddle-with-crossed-blanket-folds'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('baby', 'swaddle', 'hood', 'blanket', 'folds', 'newborn', 'infant')

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
        path('blanket',(10,18),[('A',(38,18),14,14,True),('L',(38,30)),('A',(10,30),14,14,True),('L',(10,18))],True)
        circle('face',24,17,4)
        poly('fold-a',(10,27),(38,35));poly('fold-b',(38,27),(24,31));join('fold-a','blanket');join('fold-b','blanket');join('fold-a','fold-b')
