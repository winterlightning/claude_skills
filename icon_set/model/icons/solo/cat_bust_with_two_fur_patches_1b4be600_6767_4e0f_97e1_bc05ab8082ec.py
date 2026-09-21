"""Cat Bust with Two Fur Patches
Plan: Cat bust with pointed ears, face patch and opposite shoulder patch.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Tiny nose/mouth and one patch-obscured eye omitted; the two fur patches retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b4be600-6767-4e0f-97e1-bc05ab8082ec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/calico_1b4be600-6767-4e0f-97e1-bc05ab8082ec.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cat-bust-with-two-fur-patches'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cat', 'calico', 'fur', 'patches', 'face', 'pet', 'feline')

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
        path('cat',(8,44),[('C',(13,29),(8,38),(9,32)),('C',(10,16),(8,25),(9,21)),('L',(10,4)),('L',(19,11)),('L',(25,11)),('L',(29,11)),('L',(38,4)),('L',(38,16)),('C',(38,26),(40,23),(39,24)),('C',(35,29),(37,27),(36,28)),('C',(40,44),(39,34),(40,39))])
        path('face-patch',(25,11),[('C',(38,26),(25,22),(30,26))]);join('face-patch','cat')
        path('shoulder-patch',(35,29),[('C',(37,39),(21,33),(24,41))]);join('shoulder-patch','cat')
        self.add_dot('eye',(18,21))
