'Symmetric tapered lighthouse with roof, lantern, gallery and four separate straight light rays.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: tower-control: shared structural endpoints and mirrored tower construction.\nOmissions: Small roof overhang reduced; four rays retained.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '969cd7b7-18ae-4dc0-99ef-fbfd5047b13e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/lookout_969cd7b7-18ae-4dc0-99ef-fbfd5047b13e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tapered-lighthouse-with-four-light-rays'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('tapered', 'lighthouse', 'with', 'four', 'light', 'rays')
    def build(self):

        def path(name,start,commands,closed=False):
            point=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,point,end)
                elif kind=='A': self.add_arc(member,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,point,(args[0],args[1],end))
                point=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        # Single roof/lantern contour avoids overlapping caps and false near-contacts.
        poly('lantern',(18,22),(18,11),(24,6),(30,11),(30,22))
        poly('gallery',(16,22),(18,22),(30,22),(32,22));join('gallery','lantern')
        poly('tower',(18,22),(14,42),(34,42),(30,22));join('tower','gallery');join('tower','lantern')
        line('ground-left',(6,42),(14,42));line('ground-right',(34,42),(42,42))
        join('ground-left','tower');join('ground-right','tower')
        for side in (-1,1):
         x=lambda offset:24+side*offset
         line(f'ray-up-{side}',(x(16),12),(x(18),10))
         line(f'ray-down-{side}',(x(16),22),(x(18),24))
