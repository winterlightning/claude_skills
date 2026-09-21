"""Letter C and Number 5 — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '259c0878-528e-42fb-8d9f-56fe04a84b03'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/c5_259c0878-528e-42fb-8d9f-56fe04a84b03.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'letter-c-and-number-5-batch-033'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('letter-c-and-number-5',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Existing C and 5 glyphs, uniformly laid out without replacing their natural geometry. SOLO48 grid compatibility must be checked.

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def rect(name,x0,y0,x1,y1,r=4):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            ids=[]
            for i,p in enumerate(pts):
                q=pts[(i+1)%8];eid=f'{name}-{i}';ids.append(eid)
                if i%2:self.add_arc(eid,p,q,radius_x=r)
                else:self.add_line(eid,p,q)
            self.add_contour(name,*ids,closed=True)

        from pathlib import Path
        import json
        from svgpathtools import parse_path, Line as SvgLine, Arc as SvgArc, CubicBezier, QuadraticBezier
        from ...primitives import Line, Arc, Bezier, Point
        catalog=json.loads((Path(__file__).resolve().parents[3]/'typeface/glyphs.json').read_text())['glyphs']
        glyphs=[next(g for g in catalog if g['character']==c and g.get('preferred',True)) for c in 'C5']
        # Uniform text layout: preserve all source path proportions; no grid snapping.
        gap=9; available=40-gap*(len(glyphs)-1)
        scale=available/sum(g['bounds'][2]-g['bounds'][0] for g in glyphs)
        height=max(g['body_height'] for g in glyphs)*scale
        x=4; baseline=24+height/2
        for gi,g in enumerate(glyphs):
            tx=x-g['bounds'][0]*scale;ty=baseline-g['baseline']*scale
            def pt(z):return Point(z.real*scale+tx,z.imag*scale+ty)
            for pi,d in enumerate(g['paths']):
              # A glyph path may hold several disconnected subpaths; each becomes its own contour.
              for qi,path in enumerate(parse_path(d).continuous_subpaths()):
                members=[]
                for si,seg in enumerate(path):
                    name=f'g{gi}-p{pi}-q{qi}-s{si}';members.append(name);a=pt(seg.start);b=pt(seg.end)
                    if isinstance(seg,SvgLine):self.primitives.append(Line(name,a,b))
                    elif isinstance(seg,SvgArc):self.primitives.append(Arc(name,a,b,seg.radius.real*scale,seg.radius.imag*scale,bool(seg.large_arc),bool(seg.sweep)))
                    elif isinstance(seg,CubicBezier):
                        c1=pt(seg.control1);c2=pt(seg.control2);self.primitives.append(Bezier(name,a,b,((c1.as_tuple(),c2.as_tuple(),b.as_tuple()),)))
                    else:raise ValueError('Unsupported glyph segment: '+str(type(seg)))
                self.add_contour(f'g{gi}-p{pi}-q{qi}',*members,closed=path.isclosed())
            x+=(g['bounds'][2]-g['bounds'][0])*scale+gap
