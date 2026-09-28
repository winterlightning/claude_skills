"""Four equal circular flower lobes, a centered ring and two symmetric ribbon tails. The flower owns equal lobe radii and exact repeated joins.
References: Lucide award: medal and paired ribbon; source flower outline reduced to four equal lobes.
Authored directly on SOLO48; original retained for comparison."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '58f87e29-b0b5-42be-b412-f3b9d5882e0e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__award-flower-rosette/20260926T073831Z-thuan-mac/reference/award flower shape_58f87e29-b0b5-42be-b412-f3b9d5882e0e.svg'
AUTHOR = 'claude-opus-5-5'

class AwardFlowerRosette(Solo48):
    icon_id = 'award-flower-rosette'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('award', 'flower', 'rosette')

    def build(self):
        # Symbol plan (revision per review): the centre ring is now a dot (24, 18), and the ribbon is wider
        # and more vertical - tails from the lower lobe joints (17, 25)/(31, 25) fall almost straight to
        # (14, 44)/(34, 44) with a shallow notch at (24, 41), 9 below the lower lobe. The flower lobes
        # are r7 (were r8) to give the ribbon its length. The flower owns equal lobe radii and exact repeated joins.

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                kind,end,*args=c; ident=('body-top' if j==2 else 'body-top-right') if n=='body' and j in (2,3) else f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('flower',(17,11),[('A',(31,11),7,7,True),('A',(31,25),7,7,True),('A',(17,25),7,7,True),('A',(17,11),7,7,True)],True)
        dot('center',(24,18))
        poly('ribbon',(17,25),(14,44),(24,41),(34,44),(31,25));join('flower','ribbon')
