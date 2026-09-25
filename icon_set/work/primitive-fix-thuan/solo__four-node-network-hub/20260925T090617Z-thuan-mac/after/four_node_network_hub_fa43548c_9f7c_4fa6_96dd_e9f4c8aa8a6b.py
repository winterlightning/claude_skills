"""Enlarge the four equal circular node openings and attach three radial links symmetrically to their edges.
Symbol plan: Shared nodes own true connections; repeated nodes, petals and toes use shared dimensions.
Lucide construction: network. Original reference establishes full subject and arrangement.
Keyshape SQUARE; source proportions preserved with explicit exceptions if required.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='fa43548c-9f7c-4fa6-96dd-e9f4c8aa8a6b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__four-node-network-hub/20260925T090617Z-thuan-mac/reference/node_fa43548c-9f7c-4fa6-96dd-e9f4c8aa8a6b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='four-node-network-hub'
    keyshape=Keyshape.VRECT_L
    exception = {'reason': 'Preserve four round open nodes with equal radii. Reduced local bond separation and approximately three-pixel node gaps remain clear in both themes. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'e3b05a4c52bc0000a97744c95bdc6b0344edf92219900ec880f2da317ee33a04'}
    semantic_role = 'MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('four', 'node', 'network', 'hub')
    def build(self):
        self.circle('center',24,26,5)
        for name,x,y in [('top',24,9),('left',13,39),('right',35,39)]:self.circle(name,x,y,5)
        self.add_line('link-top',(24,14),(24,21));self.relate('connect','link-top','top');self.relate('connect','link-top','center')
        for name,a,b in [('left',(16,35),(21,30)),('right',(32,35),(27,30))]:
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

