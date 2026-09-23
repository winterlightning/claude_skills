"""Workflow agreement, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3c6ab24c-f835-4933-927e-e286153e4e97'
SOURCE_PATH='icon_set/work/todo-references/workflow agreement_3c6ab24c-f835-4933-927e-e286153e4e97.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='workflow-agreement'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('workflow', 'agreement')

    # Visible extrema (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Agreement bubble, checkmark, two tails and two detached human busts.
        self.path('bubble',(18,6),[('L',(30,6)),('A',(34,10),4),('L',(34,18)),
            ('A',(30,22),4),('L',(30,25)),('L',(24,22)),('L',(18,25)),
            ('L',(18,22)),('A',(14,18),4),('L',(14,10)),('A',(18,6),4)],True)
        self.add_polyline('check',(20,13),(23,16),(28,11))
        for i,x in enumerate((11,37)):
            self.circle(f'head-{i}',x,28,3)
            self.shoulders(f'body-{i}',x-5,x,x+5,39,42)
        # Actual head bottom 31 and shoulder crest 39: centerline gap 8, ink gap 4.


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

