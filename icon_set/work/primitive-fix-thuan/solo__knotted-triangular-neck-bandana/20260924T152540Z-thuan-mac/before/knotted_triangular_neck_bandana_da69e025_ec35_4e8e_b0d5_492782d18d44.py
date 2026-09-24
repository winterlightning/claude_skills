'Knotted neck bandana with two pointed ends and triangular lower cloth; mirrored ends and central knot. One coherent outer contour owns tip and cloth shapes; attached knot and fold seams share exact endpoints. Omit inner neck seam arcs. No local Lucide scarf match.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da69e025-ec35-4e8e-b0d5-492782d18d44'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/bandana_da69e025-ec35-4e8e-b0d5-492782d18d44.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'knotted-triangular-neck-bandana'
    keyshape = Keyshape.SQUARE
    category = "Uncategorized"
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ["Knotted Neck Bandana"]
    keywords = ["bandana", "knot", "cloth", "neckwear", "triangle", "scarf", "fold"]
    def build(self):

        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=4):
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        # Shared mirrored attachment nodes: knot sides x20/28, fold ends x6/42.
        self.add_arc('knot-top',(20,14),(28,14),radius_x=4)
        axis=24
        def mirrored_pair(stem,start,*segments):
            bez(stem+'-right',start,*segments)
            points=[start]+[segment[2] for segment in segments]
            mirror=lambda point:(2*axis-point[0],point[1])
            reverse=[]
            for i in reversed(range(len(segments))):
                c1,c2,end=segments[i]
                reverse.append((mirror(c2),mirror(c1),mirror(points[i])))
            bez(stem+'-left',mirror(points[-1]),*reverse)
        mirrored_pair('tip',(28,14),((31,8),(35,6),(38,6)),((38,12),(35,16),(32,18)))
        mirrored_pair('shoulder',(32,18),((37,20),(40,23),(42,26)))
        mirrored_pair('cloth',(42,26),((42,31),(32,38),(24,42)))
        self.add_contour('outline','knot-top','tip-right','shoulder-right','cloth-right','cloth-left','shoulder-left','tip-left',closed=True)
        poly('knot-bottom',(20,14),(20,22),(28,22),(28,14));join('knot-bottom','outline')
        bez('fold',(6,26),((12,34),(36,34),(42,26)));join('fold','outline')
