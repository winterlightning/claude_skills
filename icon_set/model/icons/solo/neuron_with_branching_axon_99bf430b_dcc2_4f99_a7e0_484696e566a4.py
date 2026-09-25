"""Branching Neuron
Plan: Cell body is an 8-radius circle centered on the vertical axon. Dendrites radiate at cardinal points. Axon forks to paired terminals.
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Lucide git-fork: attached branches and circular nodes.
Reduction: Reduced radial dendrites to three long rays; retained body, axon and two terminals.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99bf430b-dcc2-4f99-a7e0-484696e566a4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/neuron_99bf430b-dcc2-4f99-a7e0-484696e566a4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'neuron-with-branching-axon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('neuron', 'nerve', 'cell', 'biology', 'axon', 'science')

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
        circle('cell',24,16,8)
        for name,a,b,members in [('top',(24,8),(24,4),('cell-0','cell-1')),('left',(16,16),(8,16),('cell-0','cell-3')),('right',(32,16),(40,16),('cell-1','cell-2'))]:
            self.add_line(name,a,b)
            for m in members:self.relate('connect',name,m)
        self.add_line('axon',(24,24),(24,34))
        self.relate('connect','axon','cell-2'); self.relate('connect','axon','cell-3')
        for name,end in [('left-terminal',(10,44)),('right-terminal',(38,44))]:
            self.add_line(name,(24,34),end);self.relate('connect','axon',name)
        self.relate('connect','left-terminal','right-terminal')
