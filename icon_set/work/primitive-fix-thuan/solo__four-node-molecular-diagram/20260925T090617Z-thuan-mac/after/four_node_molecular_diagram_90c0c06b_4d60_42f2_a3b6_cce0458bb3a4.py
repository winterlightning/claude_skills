"""Restore a larger central atom and three smaller outer atoms, with straight bonds attached at explicit diagonal points.
Symbol plan: Shared nodes own true connections; repeated nodes, petals and toes use shared dimensions.
Lucide construction: network. Original reference establishes full subject and arrangement.
Keyshape SQUARE; source proportions preserved with explicit exceptions if required.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='90c0c06b-4d60-42f2-a3b6-cce0458bb3a4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__four-node-molecular-diagram/20260925T090617Z-thuan-mac/reference/glutamate_90c0c06b-4d60-42f2-a3b6-cce0458bb3a4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='four-node-molecular-diagram'
    keyshape=Keyshape.VRECT_L
    exception = {'reason': 'Preserve the larger central atom and three round satellite nodes. Short connecting bonds and locally reduced node clearance remain distinct at native size. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'dd7ec3aa58f66d4567d4f1b8cbb340ccfc1e70eb06cee625a51e04fba6c65b37'}
    semantic_role = 'MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('four', 'node', 'molecular', 'diagram')
    def build(self):
        self.node('center',24,26,7,5)
        for name,x,y in [('top',24,9),('left',13,39),('right',35,39)]:self.circle(name,x,y,5)
        self.add_line('link-top',(24,14),(24,19));self.relate('connect','link-top','top');self.relate('connect','link-top','center')
        for name,a,b in [('left',(16,35),(19,31)),('right',(32,35),(29,31))]:
            self.add_line('link-'+name,a,b);self.relate('connect','link-'+name,name);self.relate('connect','link-'+name,'center')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i, (kind,end,*args) in enumerate(commands):
            tag=f'{name}-{i}'
            if kind=='L': self.add_line(tag,start,end)
            elif kind=='C': self.add_bezier(tag,start,(args[0],args[1],end))
            else: self.add_arc(tag,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            start=end;members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def box(self,name,l,t,r,b,k):
        self.path(name,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)


    def node(self,name,x,y,r,d):
        # Four identical cubic quadrants; diagonal attachment points are explicit.
        quarter=[('C',(d,-d),(r//3,-r),(d-1,-d-1)),('C',(r,0),(d+1,-d+1),(r,-(r//3)))]
        def rot(p,i):
            a,b=p
            for _ in range(i): a,b=-b,a
            return (x+a,y+b)
        commands=[]
        for i in range(4):
            commands.extend((k,rot(e,i),rot(a,i),rot(b,i)) for k,e,a,b in quarter)
        self.path(name,(x,y-r),commands,True)

