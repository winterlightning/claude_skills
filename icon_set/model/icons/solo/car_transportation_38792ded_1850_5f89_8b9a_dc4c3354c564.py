'Compact SUV side profile.\nPlan: HRECT_M preserves the wide cabin and lower hood. Equal wheels share a baseline and radius.\nReference: car; Continuous roof/hood and paired circular wheels.\nChanges: No parts omitted; wheel centers moved inward and lower corners squared.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '38792ded-1850-5f89-8b9a-dc4c3354c564'
SOURCE_PATH = 'pictographic-primitives/transportation/car_38792ded-1850-5f89-8b9a-dc4c3354c564.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'car-transportation'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('car', 'transportation')
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

        path('body',(12,34),[('L',(4,34)),('L',(4,30)),('L',(4,21)),('L',(10,12)),('C',(14,10),(11,10),(12,10)),('L',(25,10)),('C',(29,12),(27,10),(28,11)),('L',(37,20)),('C',(44,25),(42,21),(44,21)),('L',(44,30)),('L',(44,34)),('L',(36,34))])
        line('handle',(18,21),(22,21))

        for x in (16,32):circle(f'wheel-{x}',x,34,4)
        line('sill',(20,34),(28,34));join('sill','wheel-16');join('sill','wheel-32')
        join('body','wheel-16');join('body','wheel-32')

PARENT_MODULE = 'icon_set/model/icons/solo/car_transportation_38792ded_1850_5f89_8b9a_dc4c3354c564.py'

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'abd2b2aece56fa7da17a41b8449602b72090ca85becad1e9edcf5c4a9be1052f', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '38792ded-1850-5f89-8b9a-dc4c3354c564'}
