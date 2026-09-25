"""Ares with upright spear, round shield and a coherent standing torso. Head (23,11), radius5; vertical upper torso starts (23,24), giving exactly 8 centerline / 4 ink head-to-torso gap.
Keyshape SQUARE; fresh revision for feedback: Bad stroke drawn.
Construction reference: Shared human_ref/full_body_ref.png: outlined circular head, coherent torso and limbs, exact detached-head gap.
Omissions: Shield boss, belt and tiny spearhead interior omitted; spear retains a pointed tip.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '996b003c-d419-5d2e-993e-9c6fe7388a3e'
SOURCE_PATH = 'pictographic-primitives/religion/ares_996b003c-d419-5d2e-993e-9c6fe7388a3e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ares-with-spear-and-shield'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    categories = ('primitives', 'religion')
    aliases = ()
    keywords = ('ares',)

    def build(self):
        self.circle('head',23,11,5)
        self.add_polyline('spear',(6,6),(6,30),(6,42))
        self.add_line('spear-tip',(6,6),(10,12))
        self.add_line('torso',(23,24),(23,28))
        self.add_line('lower-torso',(23,28),(19,34))
        self.add_polyline('body',(19,34),(19,42),(25,42))
        self.add_polyline('left-arm',(23,24),(15,30),(6,30))
        self.circle('shield',36,34,6)
        self.add_line('right-arm',(23,24),(30,34))
        self.mark_human_figure('ares',head='head',torso='torso',torso_junction='start')
        self.contacts()

    def path(self, name, start, *commands, closed=False):
        members=[]
        here=start
        for j,command in enumerate(commands):
            kind,end,*args=command
            ident=f'{name}-{j}'
            if kind=='L': self.add_line(ident,here,end)
            else:
                rx,ry,sweep=args
                self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            here=end;members.append(ident)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def contacts(self):
        # Split receiving straight runs at true attachment nodes. Declare only
        # actual endpoint contact; never connect separated shapes.
        from icon_set.model.primitives import Line
        from dataclasses import replace
        endpoints={p.start for p in self.primitives}|{p.end for p in self.primitives}
        replacement={};rebuilt=[]
        for p in self.primitives:
            if isinstance(p,Line) and p.start!=p.end:
                a,b=p.start,p.end;dx,dy=b.x-a.x,b.y-a.y
                cuts=[q for q in endpoints if q not in (a,b) and (q.x-a.x)*dy==(q.y-a.y)*dx and 0<(q.x-a.x)*dx+(q.y-a.y)*dy<dx*dx+dy*dy]
                if cuts:
                    nodes=[a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b]
                    ids=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        ident=f'{p.element_id}-join-{j}';rebuilt.append(Line(ident,u,v));ids.append(ident)
                    replacement[p.element_id]=ids
                    continue
            rebuilt.append(p)
        self.primitives[:]=rebuilt
        self.contours[:]=[replace(c,members=tuple(k for m in c.members for k in replacement.get(m,[m]))) for c in self.contours]
        for j,a in enumerate(self.primitives):
            for b in self.primitives[j+1:]:
                if {a.start,a.end}&{b.start,b.end}:self.relate('connect',a.element_id,b.element_id)
