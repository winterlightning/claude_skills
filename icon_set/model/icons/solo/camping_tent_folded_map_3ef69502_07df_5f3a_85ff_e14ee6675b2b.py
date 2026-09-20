"""Camping Tent and Folded Map.

Plan: Centerline4,8,44,40. A-frame tent behind three folded map panels, with a separate clear tent opening.
Construction: Lucide tent original/debug: coherent triangular silhouette; source folded map retained in front.
Reduction: Omitted the tight inner tent doorway; tent and three-panel map remain a coherent camping scene.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ef69502-07df-5f3a-85ff-e14ee6675b2b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/15-3ef69502-07df-5f3a-85ff-e14ee6675b2b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'camping-tent-folded-map'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('camping', 'tent', 'folded', 'map')

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
        poly('tent',(20,25),(29,8),(44,32),(28,32));join('tent','map')
        poly('map',(4,25),(12,29),(20,25),(28,29),(28,32),(28,40),(20,36),(12,40),(4,36),closed=True)
        line('fold-left',(12,29),(12,40));line('fold-right',(20,25),(20,36));join('map','fold-left');join('map','fold-right')
