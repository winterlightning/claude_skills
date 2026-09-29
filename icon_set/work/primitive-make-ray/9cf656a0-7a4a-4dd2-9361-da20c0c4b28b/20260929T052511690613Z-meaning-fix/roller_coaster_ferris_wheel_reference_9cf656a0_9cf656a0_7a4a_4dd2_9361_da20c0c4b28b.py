"""Two rides remain distinct: rolling coaster track on four open supports and an eight-spoke Ferris wheel with a short tapered stand. Enlarge the gap above the ground to avoid a dark lower-right knot.
Reference comparison: The rejected amusement-park scene had a heavy four-spoke wheel and one thick arch, losing the flowing coaster track and its repeated supports.
Construction references: Lucide roller-coaster and ferris-wheel: flowing track, repeated supports, radial wheel geometry; original controls two-ride composition.
Omissions: One low track support removed to preserve negative space; tiny wheel cabins omitted as in the original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9cf656a0-7a4a-4dd2-9361-da20c0c4b28b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__roller-coaster-ferris-wheel-reference-9cf656a0/20260929T051531Z-thuan-mac/reference/theme park_9cf656a0-7a4a-4dd2-9361-da20c0c4b28b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'roller-coaster-ferris-wheel-reference-9cf656a0'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def path(self, name, start, *steps, closed=False):
        ids=[]; p=start
        for n,step in enumerate(steps):
            key=f"{name}-{n}"; end=step[1]
            if step[0]=='L': self.add_line(key,p,end)
            elif step[0]=='C': self.add_bezier(key,p,(step[2],step[3],end))
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        self.path('coaster-track',(4,29),('C',(17,22),(4,13),(12,15)),('C',(43,35),(26,31),(29,39)))
        self.add_line('ground',(4,44),(44,44))
        for name,a,b in [('support-left',(4,29),(4,44)),('support-peak',(11,19),(11,44)),('support-middle',(20,27),(20,44)),('support-right',(43,35),(43,44))]:self.add_line(name,a,b)
        self.circle('wheel',33,15,11)
        self.circle('hub',33,15,2)
        # Four paired spokes, interrupted at the hub.
        for name,a,b in [('north',(33,4),(33,13)),('south',(33,17),(33,26)),('west',(22,15),(31,15)),('east',(35,15),(44,15)),('nw',(25,7),(31,13)),('ne',(35,13),(41,7)),('sw',(25,23),(31,17)),('se',(35,17),(41,23))]:self.add_line('spoke-'+name,a,b)
        self.add_polyline('wheel-stand',(28,32),(33,22),(38,32))

Drawing.exception = {'reason': 'Complete amusement-park scene requires close structural overlaps, compact spoke openings and repeated supports. User authorized visual exception after48px review.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'd3cb103b2fc1d3403457f6c732421cdb9330ebb8f61d3bf75de7f0edcb0733fb'}
