"""Wicca, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='6f98932a-9582-5d69-931f-9d793df64716'
SOURCE_PATH='icon_set/work/todo-references/wicca_6f98932a-9582-5d69-931f-9d793df64716.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='wicca'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'religion'
    aliases=()
    keywords=('wicca',)

    # Visible extrema (2, 2, 46, 46); centerline extremes (4, 4, 44, 44).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Pentagram in a circle. Integer 12-16-20 circle points own all five tips.
        # The upper pair is higher than a regular pentagon to keep exact attachments.
        tips=[(24,4),(40,12),(36,40),(12,40),(8,12)]
        for i,p in enumerate(tips):
            self.add_arc(f'ring-{i}',p,tips[(i+1)%5],radius_x=20)
        self.add_contour('ring',*(f'ring-{i}' for i in range(5)),closed=True)
        self.add_polyline('pentagram',tips[0],tips[2],tips[4],tips[1],tips[3],closed=True)
        self.relate('connect','ring','pentagram')


    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)

    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        # Shared rectangle parameters own radii, symmetry and attachment nodes.
        seg=[('L',(x,t)) for x in sorted(set(top)) if l+k<x<r-k]
        seg += [('L',(r-k,t)),('A',(r,t+k),k)]
        seg += [('L',(r,y)) for y in sorted(set(right)) if t+k<y<b-k]
        seg += [('L',(r,b-k)),('A',(r-k,b),k)]
        seg += [('L',(x,b)) for x in sorted(set(bottom),reverse=True) if l+k<x<r-k]
        seg += [('L',(l+k,b)),('A',(l,b-k),k)]
        seg += [('L',(l,y)) for y in sorted(set(left),reverse=True) if t+k<y<b-k]
        seg += [('L',(l,t+k)),('A',(l+k,t),k)]
        self.path(n,(l+k,t),seg,True)

    def shoulders(self,n,l,x,r,top,bottom):
        self.add_arc(n+'-left',(l,bottom),(x,top),radius_x=x-l,radius_y=bottom-top)
        self.add_arc(n+'-right',(x,top),(r,bottom),radius_x=r-x,radius_y=bottom-top)
        self.add_contour(n,n+'-left',n+'-right')

