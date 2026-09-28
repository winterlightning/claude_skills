from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='7812933e-4da0-4067-9131-d948a045fef8'
SOURCE_PATH='pictographic-primitives/_uncategorized_11/clapboard_7812933e-4da0-4067-9131-d948a045fef8.svg'
AUTHOR='gpt-6'
PLAN='Raised clapper opens steeply from the left hinge. One stripe crosses each band; a blank rounded slate remains beneath.'
CONSTRUCTION_REFERENCES='Lucide clapperboard original and atomic-debug: raised striped blade and rounded slate.'
OMISSIONS=['Stripe count reduced from two to one per band for larger openings.']
class Drawing(Solo48):
    icon_id='movie-production-clapperboard'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('clapboard',)

    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        # Upright raised blade has one transverse stripe; lower slate keeps a full band.
        self.add_polyline('clapper',(6,22),(11,14),(16,6),(24,10),(19,18),(14,26),closed=True)
        self.add_line('upper-stripe',(11,14),(19,18));self.relate('connect','upper-stripe','clapper')
        self.path('slate',(14,26),[('L',(34,26)),('L',(42,26)),('L',(42,34)),('L',(42,38)),('A',(38,42),4,4,True),('L',(18,42)),('A',(14,38),4,4,True),('L',(14,34)),('L',(14,26))],True)
        self.add_polyline('band-bottom',(14,34),(26,34),(42,34));self.relate('connect','band-bottom','slate')
        self.add_line('lower-stripe',(34,26),(26,34));self.relate('connect','lower-stripe','slate');self.relate('connect','lower-stripe','band-bottom')
        self.relate('connect','clapper','slate')

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'c4b9827f3f465d33794bc7c1b82977175b526e8c02d6389dc17af345253c9225', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '7812933e-4da0-4067-9131-d948a045fef8'}
