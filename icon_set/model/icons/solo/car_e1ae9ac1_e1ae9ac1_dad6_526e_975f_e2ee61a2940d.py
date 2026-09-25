'Compact passenger car.\nPlan: HRECT_M preserves the low vehicle. Repeated radius-4 wheels moved inward; cabin and pillar share contact nodes.\nReference: car; Circular wheels, continuous body and roof.\nChanges: No parts omitted; wheel centers moved inward and lower corners squared.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e1ae9ac1-dad6-526e-975f-e2ee61a2940d'
SOURCE_PATH = 'pictographic-primitives/transportation/car_e1ae9ac1-dad6-526e-975f-e2ee61a2940d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'car-e1ae9ac1'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('car', 'e1ae9ac1')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*pts,closed=False):self.add_polyline(name,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)

        path('body',(12,34),[('L',(4,34)),('L',(4,30)),('L',(4,27)),('A',(12,19),8,8,True),('L',(24,19)),('L',(36,19)),('A',(44,27),8,8,True),('L',(44,30)),('L',(44,34)),('L',(36,34))])
        path('roof',(12,19),[('A',(21,10),9,9,True),('L',(24,10)),('L',(27,10)),('A',(36,19),9,9,True)])
        line('pillar',(24,10),(24,19));join('roof','body');join('pillar','roof');join('pillar','body')

        for x in (16,32):circle(f'wheel-{x}',x,34,4)
        line('sill',(20,34),(28,34));join('sill','wheel-16');join('sill','wheel-32')
        join('body','wheel-16');join('body','wheel-32')

PARENT_MODULE = 'icon_set/model/icons/solo/car_e1ae9ac1_e1ae9ac1_dad6_526e_975f_e2ee61a2940d.py'

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '64d3a122a8259b86ce851b9a81e8dc156ee6e21c63d7084c67a7bd89eac1d34f', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'e1ae9ac1-dad6-526e-975f-e2ee61a2940d'}
