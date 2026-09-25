'cloud-with-descending-data-lines. Plan: Open-bottom cloud and three descending data paths with shared spacing. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide cloud: few smooth lobes. Reduction: Reduce five data paths to three; retain bent outer terminals.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd051ff3-ee41-4ef2-8e69-035711204a47'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/coding apps website big data source plurality_cd051ff3-ee41-4ef2-8e69-035711204a47.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloud-with-descending-data-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cloud', 'data', 'lines', 'network', 'computing', 'storage', 'technology')

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
        path('cloud',(12,26),[('C',(4,18),(7,26),(4,23)),('C',(14,10),(4,12),(8,8)),('C',(30,8),(16,8),(26,8)),('C',(36,14),(34,8),(36,11)),('C',(44,20),(40,12),(44,16)),('C',(38,26),(44,24),(42,26))])
        self.add_polyline('left-data',(14,34),(14,40),(8,40))
        self.add_line('middle-data',(24,24),(24,40))
        self.add_polyline('right-data',(34,34),(34,40),(40,40))
