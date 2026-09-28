"""Solar Panel Connected to Monitor
Plan: Six-cell solar panel physically cabled to desktop monitor.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3dd8944a-87f8-4a77-b1c2-8daa2b2ed837'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/renewable energy solar monitor_3dd8944a-87f8-4a77-b1c2-8daa2b2ed837.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'solar-panel-connected-to-monitor'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('solar', 'panel', 'monitor', 'energy', 'cable', 'system')

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
        rect('panel',6,6,24,16,2)
        for x in (14,22):self.add_line(f'column-{x}',(x,6),(x,22));self.relate('connect',f'column-{x}','panel')
        self.add_line('row',(6,14),(30,14));self.relate('connect','row','panel')
        for x in (14,22):self.relate('connect',f'column-{x}','row')
        rect('monitor',26,26,16,8,2)
        self.add_polyline('cable',(18,22),(18,32),(26,32));self.relate('connect','cable','panel');self.relate('connect','cable','monitor')
        self.add_line('stand',(34,34),(34,42));self.add_line('foot',(28,42),(40,42));self.relate('connect','stand','monitor');self.relate('connect','stand','foot')
