"""Fantasy Sea Serpent.

Plan: Left-facing sea serpent, broad snout, back crest and long S-neck. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit crest segment lines, eye and zigzag mouth; retain a broad snout, crest bump and open serpentine neck.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6e9efaa-5911-4b52-b4b0-7f1573743591'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/03-d6e9efaa-5911-4b52-b4b0-7f1573743591.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'sea-serpent-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('sea', 'serpent', 'head')

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
        path('serpent',(15,42),[('C',(29,24),(15,30),(28,31)),('C',(29,16),(32,20),(30,16)),('L',(22,16)),('L',(22,23)),('L',(10,23)),('A',(6,19),4,4,True),('L',(6,13)),('A',(10,9),4,4,True),('L',(18,9)),('L',(22,6)),('C',(42,22),(34,6),(42,14)),('C',(27,42),(42,32),(27,34))])
        
        
