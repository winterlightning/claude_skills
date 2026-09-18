"""Cloche: shared vertical axis, two quarter-circle dome arcs, stem knob, shallow trapezoidal tray.
Native SOLO48; HRECT_M envelope. Construction reference: concierge-bell.
Rounded knob simplified to a short round-capped stem; dome and shallow sloped tray retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3abd86f6-8729-4dc7-a6c0-936abbc9d962'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/food tray_3abd86f6-8729-4dc7-a6c0-936abbc9d962.svg'
LEGACY_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/food tray_3abd86f6-8729-4dc7-a6c0-936abbc9d962.svg'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-019/references/food tray_3abd86f6-8729-4dc7-a6c0-936abbc9d962.svg'
AUTHOR = 'gpt-6'


class Batch019Icon(Solo48):
    icon_id = 'covered-serving-tray-batch-019-10'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/other'
    aliases = ()
    keywords = ('covered', 'serving', 'tray')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def circle(n,x,y,r):
            arc(n+'-a',(x-r,y),(x+r,y),r)
            arc(n+'-b',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def rect(n,l,t,r,b,k=4,cuts=()):
            pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
            members=[]
            for j in range(8):
                a,z=pts[j],pts[(j+1)%8]
                if j%2:
                    name=f'{n}-{j}';arc(name,a,z,k);members.append(name)
                else:
                    mids=[p for p in cuts if p not in (a,z) and
                          (z[0]-a[0])*(p[1]-a[1])==(z[1]-a[1])*(p[0]-a[0]) and
                          min(a[0],z[0])<=p[0]<=max(a[0],z[0]) and min(a[1],z[1])<=p[1]<=max(a[1],z[1])]
                    run=[a]+sorted(mids,key=lambda p:(p[0]-a[0])**2+(p[1]-a[1])**2)+[z]
                    for q,(u,v) in enumerate(zip(run,run[1:])):
                        name=f'{n}-{j}-{q}';line(name,u,v);members.append(name)
            self.add_contour(n,*members,closed=True)

        self.add_polyline('tray',(4,30),(8,30),(40,30),(44,30),(38,38),(10,38),closed=True)
        arc('dome-left',(8,30),(24,14),16)
        arc('dome-right',(24,14),(40,30),16)
        self.add_contour('dome','dome-left','dome-right')
        line('knob',(24,10),(24,14))
        self.relate('connect','knob','dome')
        self.relate('connect','tray','dome')
