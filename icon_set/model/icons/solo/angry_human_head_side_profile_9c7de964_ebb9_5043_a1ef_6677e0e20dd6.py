"""Angry Human Head Profile."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c7de964-ebb9-5043-a1ef-6677e0e20dd6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/anger emotions_9c7de964-ebb9-5043-a1ef-6677e0e20dd6.svg'
AUTHOR = 'gpt-6'


class AngryHumanHeadSideProfile(Solo48):
    icon_id = 'angry-human-head-side-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('angry', 'human', 'head', 'profile')

    def build(self):
        # Plan: Right-facing profile with continuous neck, round cranium, angular nose, frown and inclined brow. Extremes (8,4)-(40,44).
        # Reduction: Keep the defining brow and downturned mouth; no detached-head rule applies to this continuous anatomical neck.
        # Reference: Shared human_ref/user.svg proportions; profile anatomy follows the supplied reference.

        nodes = {}
        def line(n, a, b):
            self.add_line(n, a, b); nodes[n] = (a, b)
        def path(n, *pts, closed=False):
            self.add_polyline(n, *pts, closed=closed); nodes[n] = pts
        def arc(n, a, b, r, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=r if ry is None else ry, sweep=sweep); nodes[n] = (a,b)
        def bez(n, start, *segments):
            self.add_bezier(n,start,*segments); nodes[n]=(start,*(s[2] for s in segments))
        def contour(n,*parts,closed=False):
            members=[];points=[]
            for part in parts:
                existing=next((c for c in self.contours if c.contour_id==part),None)
                if existing:
                    members.extend(existing.members);self.contours.remove(existing)
                else:members.append(part)
                points.extend(nodes.pop(part))
            self.add_contour(n,*members,closed=closed);nodes[n]=tuple(points)
        def circle(n,x,y,r):
            for suffix,a,z in [('t',(x-r,y),(x,y-r)),('r',(x,y-r),(x+r,y)),('b',(x+r,y),(x,y+r)),('l',(x,y+r),(x-r,y))]:arc(n+suffix,a,z,r)
            contour(n,*(n+s for s in 'trbl'),closed=True)
        def rounded(n,l,t,r,b,radius=2,top=(),bottom=(),left=(),right=()):
            parts=[]
            sides=[((l+radius,t),(r-radius,t),sorted(top),0),((r,t+radius),(r,b-radius),sorted(right),1),((r-radius,b),(l+radius,b),sorted(bottom,reverse=True),2),((l,b-radius),(l,t+radius),sorted(left,reverse=True),3)]
            for start,end,vals,side in sides:
                pts=[start]+[(v,t) if side==0 else (r,v) if side==1 else (v,b) if side==2 else (l,v) for v in vals]+[end]
                for i,(a,z) in enumerate(zip(pts,pts[1:])):
                    if a!=z:
                        part=f'{n}-s{side}-{i}';line(part,a,z);parts.append(part)
                part=f'{n}-c{side}';arc(part,end,sides[(side+1)%4][0],radius);parts.append(part)
            contour(n,*parts,closed=True)
        def contacts():
            names=list(nodes)
            for i,a in enumerate(names):
                for b in names[i+1:]:
                    if set(nodes[a]) & set(nodes[b]):self.relate('connect',a,b)

        line('neck-back',(16,44),(16,34))
        bez('occiput',(16,34),((8,29),(8,25),(8,20)))
        arc('cranium-left',(8,20),(24,4),16)
        arc('forehead',(24,4),(36,16),12)
        path('nose',(36,16),(40,25),(34,25),(34,31),(34,33))
        arc('chin',(34,33),(28,39),6)
        path('neck-front',(28,39),(28,44),(16,44))
        contour('profile','neck-back','occiput','cranium-left','forehead','nose','chin','neck-front',closed=True)
        line('brow',(24,17),(28,19))
        bez('frown',(26,34),((28,31),(31,31),(34,31)))
        contacts()
