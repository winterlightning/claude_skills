"""Two-tier pagoda with symmetric curved eaves and straight walls.
Plan: Two-tier pagoda with symmetric curved eaves and straight walls.
Construction: No useful exact local Lucide match; source silhouette rebuilt from coherent curves.
Omissions: Doorway and plinth omitted; both tiers and curved eaves retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '38d9b634-f156-405a-b460-6fb467a50cb9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/asian monastery_38d9b634-f156-405a-b460-6fb467a50cb9.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-tier-pagoda-with-upturned-eaves'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('two', 'tier', 'pagoda', 'with', 'upturned', 'eaves')

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
        path('upper',(10,18),[('C',(24,6),(16,18),(20,11)),('C',(38,18),(28,11),(32,18)),('L',(32,18)),('L',(16,18)),('L',(10,18))],True)
        for x in (16,32):line('upper-wall-'+str(x),(x,18),(x,30));join('upper-wall-'+str(x),'upper')
        path('lower',(6,28),[('C',(14,30),(8,30),(10,30)),('L',(16,30)),('L',(32,30)),('L',(34,30)),('C',(42,28),(38,30),(40,30))])
        poly('walls',(14,30),(14,42),(34,42),(34,30));join('walls','lower')
        for x in (16,32):join('upper-wall-'+str(x),'lower')
