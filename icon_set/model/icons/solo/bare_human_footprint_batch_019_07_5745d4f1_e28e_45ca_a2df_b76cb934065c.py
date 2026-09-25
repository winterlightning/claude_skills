"""foot. Revision of reviewer feedback: Bad stroke drawn.
Plan: Bare foot with rounded toe crown and smooth heel/instep. VRECT_L x8..40,y4..44. Toes belong to the single silhouette.
Construction reference: Lucide footprints: rounded heel and smooth natural instep; human-reference.md consulted for human vocabulary.
Omissions: Tiny fifth toe merged into the outer foot edge.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5745d4f1-e28e-45ca-a2df-b76cb934065c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/foot_5745d4f1-e28e-45ca-a2df-b76cb934065c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'bare-human-footprint-batch-019-07'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('foot',)
    def build(self):

        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        bez = self.add_bezier
        def arc(n,a,b,r,ry=None,sweep=True,large=False):
            self.add_arc(n,a,b,radius_x=r,radius_y=r if ry is None else ry,sweep=sweep,large_arc=large)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def oval(n,x,y,rx,ry=None):
            ry = rx if ry is None else ry
            pts=[(x,y-ry),(x+rx,y),(x,y+ry),(x-rx,y)]
            for j in range(4): arc(n+str(j),pts[j],pts[(j+1)%4],rx,ry)
            contour(n,*(n+str(j) for j in range(4)),closed=True)
        def box(n,l,t,r,b,rad=4):
            pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
            members=[]
            for j in range(8):
                a,bp=pts[j],pts[(j+1)%8]
                if a==bp: continue
                name=n+str(j);members.append(name)
                if j%2: arc(name,a,bp,rad)
                else: line(name,a,bp)
            contour(n,*members,closed=True)

        arc('big-toe',(8,10),(20,10),6)
        arc('toe-two',(20,10),(28,10),4)
        arc('toe-three',(28,14),(36,14),4)
        line('toe-step',(28,10),(28,14))
        arc('toe-four',(36,18),(40,18),2)
        line('toe-step-two',(36,14),(36,18))
        bez('outside',(40,18),((40,26),(32,31),(32,37)))
        arc('heel',(32,37),(12,37),10,7)
        bez('instep',(12,37),((12,30),(19,29),(14,21)),((10,16),(8,16),(8,10)))
        contour('foot','big-toe','toe-two','toe-step','toe-three','toe-step-two','toe-four','outside','heel','instep',closed=True)

        from icon_set.model.primitives import Line
        from dataclasses import replace
        ends={q for p in self.primitives for q in (p.start,p.end)}
        rebuilt=[]; replacements={}
        for p in self.primitives:
            if isinstance(p,Line) and p.start!=p.end:
                a,b=p.start,p.end;dx,dy=b.x-a.x,b.y-a.y
                cuts=[q for q in ends if q not in (a,b) and (q.x-a.x)*dy==(q.y-a.y)*dx and 0<(q.x-a.x)*dx+(q.y-a.y)*dy<dx*dx+dy*dy]
                if cuts:
                    nodes=[a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b]
                    ids=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        n=p.element_id+'-joint-'+str(j);rebuilt.append(Line(n,u,v));ids.append(n)
                    replacements[p.element_id]=ids
                    continue
            rebuilt.append(p)
        self.primitives[:]=rebuilt
        self.contours[:]=[replace(c,members=tuple(k for m in c.members for k in replacements.get(m,[m]))) for c in self.contours]
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
