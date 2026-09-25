"""Coffee cup with smooth bowl and loop handle beneath two falling sugar cubes.
Plan: Coffee cup with smooth bowl and loop handle beneath two falling sugar cubes.
Construction: Lucide truck rounded-corner vocabulary applied to source cup; source controls handle and sugars.
Omissions: Short surface marks omitted; two sugar squares retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '21a74246-6bc9-4eeb-abee-faaebe33d167'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon corretto_21a74246-6bc9-4eeb-abee-faaebe33d167.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='coffee-cup-with-falling-sugar-cubes'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('coffee', 'cup', 'with', 'falling', 'sugar', 'cubes')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        for n,x,y in [('left',18,6),('right',34,13)]:poly('sugar-'+n,(x,y),(x+8,y),(x+8,y+8),(x,y+8),closed=True)
        path('cup',(16,30),[('L',(42,30)),('C',(29,42),(42,37),(36,42)),('C',(16,30),(22,42),(16,37))],True)
        path('handle',(16,30),[('L',(12,30)),('A',(6,36),6,6,False),('A',(12,42),6,6,False),('L',(29,42))]);join('cup','handle')
