from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '51794538-e0cd-4fd6-bb22-9d08f32d43d4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-overlapping-desktop-monitors/20260929T090755Z-thuan-mac/reference/monitor transfer_51794538-e0cd-4fd6-bb22-9d08f32d43d4.svg'
AUTHOR = "gpt-6"
# Plan: Restore two offset rounded monitors, a rear stand and front display bezel.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: monitor.

def _draw(icon, name, description):
    tokens=description.split(); pos=0; part=0; count=0; members=[]; start=None; point=None
    def finish(closed=False):
        nonlocal members,part
        if members: icon.add_contour(name if part==0 else f"{name}-part{part}",*members,closed=closed)
        members=[];part+=1
    while pos<len(tokens):
        op=tokens[pos];pos+=1
        if op=='M':
            if members: finish()
            point=tuple(map(int,tokens[pos:pos+2]));pos+=2;start=point
        elif op=='Z':
            if point!=start:
                count+=1;eid=f"{name}-{count}";icon.add_line(eid,point,start);members.append(eid);point=start
            finish(True)
        else:
            count+=1;eid=f"{name}-{count}";members.append(eid)
            if op=='L':
                end=tuple(map(int,tokens[pos:pos+2]));pos+=2;icon.add_line(eid,point,end)
            elif op=='C':
                values=list(map(int,tokens[pos:pos+6]));pos+=6;c1=tuple(values[:2]);c2=tuple(values[2:4]);end=tuple(values[4:]);icon.add_bezier(eid,point,(c1,c2,end))
            elif op=='A':
                rx,ry,sweep,x,y=map(int,tokens[pos:pos+5]);pos+=5;end=(x,y);icon.add_arc(eid,point,end,radius_x=rx,radius_y=ry,sweep=bool(sweep))
            point=end
    if members: finish()

class Revision(Solo48):
    icon_id = 'two-overlapping-desktop-monitors'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve two overlapping desktop monitors, both stands and foreground bezel; 2px ink gaps are deliberate UI detail.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'a1f072111c1c5a9c751ea818b43fb7ab200717fe15a4c031db09827d9602571d'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'rear', 'M 15 25 L 9 25 A 3 3 1 6 22 L 6 9 A 3 3 1 9 6 L 25 6 A 3 3 1 28 9 L 28 16')
        _draw(self, 'rear-stem', 'M 12 25 L 12 31')
        _draw(self, 'rear-base', 'M 6 31 L 15 31')
        _draw(self, 'front', 'M 21 19 L 39 19 A 3 3 1 42 22 L 42 33 A 3 3 1 39 36 L 21 36 A 3 3 1 18 33 L 18 22 A 3 3 1 21 19 Z')
        _draw(self, 'bezel', 'M 18 30 L 42 30')
        _draw(self, 'stem', 'M 30 36 L 30 42')
        _draw(self, 'base', 'M 24 42 L 36 42')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
