from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'd23e8415-7129-4003-9c39-95ff203bcfe9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__underwater-drone-with-claw/20260929T090755Z-thuan-mac/reference/underwater drone 1_d23e8415-7129-4003-9c39-95ff203bcfe9.svg'
AUTHOR = "gpt-6"
# Plan: Restore the submarine-shaped drone with fins, body seam, articulated claw and water surface.
# Keyshape: HRECT_L; preserve reference arrangement.
# Construction reference: none.

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
    icon_id = 'underwater-drone-with-claw'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'water', 'M 4 8 C 8 12 12 12 16 8 C 20 12 24 12 28 8 C 32 12 36 12 40 8')
        _draw(self, 'body', 'M 7 23 C 12 19 16 19 22 19 L 31 19 A 6 6 1 31 31 L 22 31 C 15 31 10 28 7 23 Z')
        _draw(self, 'tail', 'M 7 23 L 7 15 C 10 13 13 17 15 20')
        _draw(self, 'fin', 'M 23 19 L 25 14 L 31 14 L 31 19')
        _draw(self, 'seam', 'M 28 19 L 28 31')
        _draw(self, 'arm', 'M 23 31 L 23 39 L 35 39')
        _draw(self, 'claw', 'M 44 34 C 33 31 32 43 44 40')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
