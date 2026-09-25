"""Simple File Folder.

Plan: Centerline4,8,44,40. Raised back tab and a low full-width front flap with repeated left tab.
Construction: Lucide folder original and atomic-debug: stepped tab and rounded lower corners. Front flap retained.
Reduction: No identifying parts omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5366a0b9-f863-4852-85a2-7d10874e511a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/21-5366a0b9-f863-4852-85a2-7d10874e511a.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'open-file-folder'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('open', 'file', 'folder')

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
        path('back',(8,27),[('L',(8,12)),('A',(12,8),4,4,True),('L',(18,8)),('L',(24,14)),('L',(40,14)),('A',(44,18),4,4,True),('L',(44,31))])
        path('front',(8,27),[('L',(17,27)),('L',(23,31)),('L',(44,31)),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,31)),('A',(8,27),4,4,True)],True)
        join('back','front')
