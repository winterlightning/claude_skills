"""Four-Node Network Hub
Plan: Four circles and three spokes from center
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide network hub.
Reduction: Preserve all four nodes with equal small circular openings."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa43548c-9f7c-4fa6-96dd-e9f4c8aa8a6b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/node_fa43548c-9f7c-4fa6-96dd-e9f4c8aa8a6b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-node-network-hub'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('network', 'nodes', 'hub', 'connections', 'diagram', 'links')

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
        for name,x,y in [('top',24,9),('hub',24,24),('left',9,39),('right',39,39)]:circle(name,x,y,3)
        self.add_line('up',(24,12),(24,21));self.relate('connect','up','top');self.relate('connect','up','hub')
        for name,x in [('left',9),('right',39)]:
            self.add_line('link-'+name,(24,27),(x,36));self.relate('connect','link-'+name,'hub');self.relate('connect','link-'+name,name)
        self.relate('connect','link-left','link-right')
