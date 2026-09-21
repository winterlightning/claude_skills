'round-sports-ball-with-curved-seams. Plan: Round ball with one diagonal seam and two opposite bowed side seams. Keyshape: CIRCLE, exact SOLO48 bounds. Construction: No useful exact Lucide match; circular envelope and coherent cubic seams. Reduction: Vertical central seam and mirrored bowed side seams simplify the reference’s rotational slant.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bbf4ecbd-9562-4a38-a524-0eba638789c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/sportsball_bbf4ecbd-9562-4a38-a524-0eba638789c9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-sports-ball-with-curved-seams'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('ball', 'sport', 'seams', 'round', 'play', 'equipment')

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
        circle('ball',24,24,20)
        self.add_line('middle',(24,4),(24,44));self.relate('connect','ball','middle')
        path('left',(12,8),[('C',(12,40),(17,16),(17,32))]);self.relate('connect','ball','left')
        path('right',(36,8),[('C',(36,40),(31,16),(31,32))]);self.relate('connect','ball','right')
