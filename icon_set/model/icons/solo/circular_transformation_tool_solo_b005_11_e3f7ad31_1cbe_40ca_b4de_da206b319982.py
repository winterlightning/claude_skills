"""Open circular transform disc with radial sector, handle dot and two directional corner arrows; extremes 6,6,42,42.
Construction: refresh-cw: detached directional arrow strokes
Reduction: No defining element omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3f7ad31-1cbe-40ca-b4de-da206b319982'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/design/transform shrink_e3f7ad31-1cbe-40ca-b4de-da206b319982.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-transformation-tool-solo-b005-11'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('circular', 'transformation', 'tool', 'solo', 'b005', '11')
    def build(self):

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                else: self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m); here=end
            self.add_contour(name,*members,closed=closed)
        def poly(name,*pts,closed=False): self.add_polyline(name,*pts,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('disc',(32,24),[('A',(16,24),8,8,False),('A',(24,32),8,8,False)])
        poly('radial',(42,24),(32,24),(24,24),(34,34));join('radial','disc')
        poly('radial-tip',(26,34),(34,34),(34,26));join('radial','radial-tip')
        self.add_dot('handle',(42,24));join('handle','radial')
        poly('top-arrow',(42,14),(34,6),(34,11));line('top-wing',(34,6),(42,6));join('top-arrow','top-wing')
        poly('bottom-arrow',(6,34),(14,42),(14,37));line('bottom-wing',(14,42),(6,42));join('bottom-arrow','bottom-wing')
