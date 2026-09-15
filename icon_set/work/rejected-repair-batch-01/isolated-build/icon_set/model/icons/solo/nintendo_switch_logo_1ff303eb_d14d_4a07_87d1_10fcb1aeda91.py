"""Two rounded controller halves stand side by side with a narrow gap, the left holding a ring near its top and the right a ring near its middle.

Symbol plan: Two controller halves with staggered buttons; extremes (4,8)-(44,40).
Review notes: Keeps paired controllers and staggered buttons, widens the central gap to8, and reduces button rings to dots. Earlier Lucide rounded-square construction informs the halves; button heights preserve the intended asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ff303eb-d14d-4a07-87d1-10fcb1aeda91'
SOURCE_PATH = 'pictographic-primitives/logos/nintendo switch logo_1ff303eb-d14d-4a07-87d1-10fcb1aeda91.svg'
AUTHOR = 'gpt-6'

class NintendoSwitchLogo(Solo48):
    icon_id = 'nintendo-switch-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('nintendo-switch', 'nintendo', 'gaming', 'console', 'joy-con', 'logo', 'brand')

    def build(self):

        def chain(name, *points):
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{i}',start,end)
        def ring(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def rounded(name, left, top, right, bottom, r):
            points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; ident=f'{name}-{i}'
                if start==end: continue
                if i%2:self.add_arc(ident,start,end,radius_x=r)
                else:self.add_line(ident,start,end)
                members.append(ident)
            self.add_contour(name,*members,closed=True)
        for name,left,right,cx,cy in [('left',4,20,12,18),('right',28,44,36,30)]:
         points=[(left+6,8),(right-6,8),(right,14),(right,34),(right-6,40),(left+6,40),(left,34),(left,14)]
         for j,a in enumerate(points):
          b=points[(j+1)%8]
          if j%2:self.add_arc(f'{name}-{j}',a,b,radius_x=6)
          else:self.add_line(f'{name}-{j}',a,b)
         for j in range(8):self.relate('connect',f'{name}-{j}',f'{name}-{(j+1)%8}')
         self.add_dot(name+'-button',(cx,cy))
