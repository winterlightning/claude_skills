from pathlib import Path
import json, importlib.util, traceback
import cairosvg
SOURCE_ICON_ID = "13d0089e-f330-48ba-93f8-58b6b6f1f9e2"
SOURCE_PATH = "icon_set/work/todo-references/crypto currency megacoin_13d0089e-f330-48ba-93f8-58b6b6f1f9e2.svg"
AUTHOR = "gpt-6"
ROOT = Path(__file__).parent
ROWS = json.loads((ROOT / "batch.json").read_text())
HELPERS = """
    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded(self, name, l, t, r, b, radius):
        q=radius
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
        for j in range(8):
            if j%2: self.add_arc(name+str(j),pts[j],pts[j+1],radius_x=q)
            else: self.add_line(name+str(j),pts[j],pts[j+1])
        self.add_contour(name, *(name+str(j) for j in range(8)), closed=True)
"""
DESIGNS={}
def design(n,key,plan,body,refs='No useful local Lucide match for this composition.',omissions='None; defining components retained.'):
    DESIGNS[n]=(key,plan,body,refs,omissions)

design(1,'CIRCLE','A Megacoin emblem: circular rim and three separate matching round-headed arches. Radius 20 centered at (24,24); repeated arch widths 6 at step 10. Dense trademark retained for honest spacing review.',"""
        self.circle('coin',24,24,20)
        for j,x in enumerate((11,21,31)):
            p='arch-'+str(j)
            self.add_line(p+'-left',(x,29),(x,22))
            self.add_arc(p+'-top',(x,22),(x+6,22),radius_x=3)
            self.add_polyline(p+'-rest',(x+6,22),(x+6,29),(x,29))
            self.add_contour(p,p+'-left',p+'-top',p+'-rest-1',p+'-rest-2',closed=True)
""")
# Arches are assembled explicitly below, avoiding nested contour membership.
DESIGNS[1]=tuple(v.replace("self.add_polyline(p+'-rest',(x+6,22),(x+6,29),(x,29))", "self.add_line(p+'-rest-1',(x+6,22),(x+6,29))\n            self.add_line(p+'-rest-2',(x+6,29),(x,29))") if isinstance(v,str) else v for v in DESIGNS[1])
design(2,'HRECT_L','A right-directed cursor arrow inside a large round target with a smaller circle overlapping its right rim. Main left semicircle has center (20,24), radius 16; smaller target center (36,24), radius 8. Preserve directional asymmetry.',"""
        self.add_arc('main-left',(20,40),(20,8),radius_x=16)
        self.add_bezier('main-top',(20,8),((27,8),(31,12),(33,17)))
        self.add_bezier('main-bottom',(33,31),((31,36),(27,40),(20,40)))
        self.add_contour('main','main-bottom','main-left','main-top')
        self.circle('target',36,24,8)
        self.add_polyline('shaft',(12,24),(23,24))
        self.add_polyline('arrow',(19,20),(23,24),(19,28))
        self.relate('connect','shaft','arrow')
""",'Lucide mouse-pointer: clear directional silhouette; circular composition comes from the supplied reference.')
design(3,'SQUARE','A data lake with the two literal rows 10100 and 01100 above two wave strokes. Repeated binary cells share a width and row step; wave lobes repeat on a 12-unit step. Four centerline extremes: (6,6)-(42,42).',"""
        for row,text in enumerate(('10100','01100')):
            y=6+row*14
            for col,digit in enumerate(text):
                x=6+col*8
                p='digit-'+str(row)+'-'+str(col)
                if digit=='1': self.add_line(p,(x+2,y),(x+2,y+8))
                else: self.rounded(p,x,y,x+4,y+8,2)
        for row,y in enumerate((32,40)):
            for col in range(3):
                x=6+12*col
                self.add_bezier('wave-'+str(row)+'-'+str(col),(x,y),((x+3,y+3),(x+9,y+3),(x+12,y)))
            self.add_contour('water-'+str(row),*('wave-'+str(row)+'-'+str(col) for col in range(3)))
""",'Lucide database inspected; its cylinder is not a useful match for the requested binary-over-water composition.')
design(4,'VRECT_L','An arched RIP gravestone seated on a rectangular plinth. Shared center axis 24; outer arch radius 12, top y4, plinth y36..44. Keep the hand-drawn RIP inscription.',"""
        self.add_line('stone-left',(12,36),(12,16))
        self.add_arc('stone-arch',(12,16),(36,16),radius_x=12)
        self.add_line('stone-right',(36,16),(36,36))
        self.add_contour('stone','stone-left','stone-arch','stone-right')
        self.add_polyline('plinth',(8,36),(12,36),(36,36),(40,36),(40,44),(8,44),closed=True)
        self.relate('connect','stone','plinth')
        self.add_polyline('r',(17,28),(17,18),(21,18),(21,23),(17,23),(22,28))
        self.add_line('i',(26,18),(26,28))
        self.add_polyline('p',(31,28),(31,18),(35,18),(35,23),(31,23))
""")
design(5,'HRECT_L','A horizontal capsule above a right-pointing arrow. Preserve the empty capsule exactly as visible in the supplied reference; no inferred digits. Centerline extremes (4,8)-(44,40).',"""
        self.rounded('capsule',4,8,40,20,6)
        self.add_line('shaft',(22,34),(44,34))
        self.add_polyline('arrow',(38,28),(44,34),(38,40))
        self.relate('connect','shaft','arrow')
""")
design(6,'CIRCLE','A delete mark with an X spanning a circle. Four rational circle junctions share the radius-20 rim; both diagonal strokes split at their common center.',"""
        nodes=((12,8),(36,8),(36,40),(12,40))
        for j in range(4): self.add_arc('rim-'+str(j),nodes[j],nodes[(j+1)%4],radius_x=20)
        self.add_contour('rim',*('rim-'+str(j) for j in range(4)),closed=True)
        self.add_polyline('slash',(12,8),(24,24),(36,40))
        self.add_polyline('backslash',(36,8),(24,24),(12,40))
        self.relate('connect','slash','backslash')
        self.relate('connect','rim','slash')
        self.relate('connect','rim','backslash')
""",'Lucide delete: two coherent diagonal strokes forming X; supplied circular enclosure preserved.')
design(7,'SQUARE','A design pen nib below a Bezier control diamond, horizontal handles, and two curved guide arms. Symmetry about x24; the upper diamond and nib remain distinct symbols. Extrema (6,6)-(42,42).',"""
        self.add_polyline('control',(24,6),(28,10),(24,14),(20,10),closed=True)
        self.add_line('handle-left',(6,10),(16,10))
        self.add_line('handle-right',(32,10),(42,10))
        self.add_bezier('guide-left',(6,26),((6,18),(11,12),(16,10)))
        self.add_bezier('guide-right',(32,10),((37,12),(42,18),(42,26)))
        self.relate('connect','guide-left','handle-left')
        self.relate('connect','guide-right','handle-right')
        self.add_polyline('nib',(24,18),(34,32),(30,40),(18,40),(14,32),closed=True)
        self.circle('vent',24,32,2)
        self.add_line('slit',(24,18),(24,30))
        self.relate('connect','slit','nib')
        self.relate('connect','slit','vent')
        self.add_line('cuff-left',(18,40),(18,42))
        self.add_line('cuff-right',(30,40),(30,42))
        self.relate('connect','cuff-left','nib')
        self.relate('connect','cuff-right','nib')
""",'Lucide pen-tool: closed nib outline with circular vent and connected slit; source supplies upright orientation and Bezier controls.')

def monitor(n,key,l,t,r,b,bottom,bezel,stand,rad):
    body=f"""
        l,t,r,b,q={l},{t},{r},{b},{rad}
        self.add_line('top',(l+q,t),(r-q,t))
        self.add_arc('top-right',(r-q,t),(r,t+q),radius_x=q)
"""
    if bezel:
        body+=f"""
        self.add_line('right-upper',(r,t+q),(r,{bezel}))
        self.add_line('right-lower',(r,{bezel}),(r,b-q))
"""
    else:body+="        self.add_line('right',(r,t+q),(r,b-q))\n"
    body+="""
        self.add_arc('bottom-right',(r,b-q),(r-q,b),radius_x=q)
        self.add_polyline('bottom',(r-q,b),(28,b),(24,b),(20,b),(l+q,b))
        self.add_arc('bottom-left',(l+q,b),(l,b-q),radius_x=q)
"""
    # Bottom polyline becomes primitive members of the screen contour.
    body=body.replace("self.add_polyline('bottom',(r-q,b),(28,b),(24,b),(20,b),(l+q,b))", "self.add_line('bottom-1',(r-q,b),(28,b))\n        self.add_line('bottom-2',(28,b),(24,b))\n        self.add_line('bottom-3',(24,b),(20,b))\n        self.add_line('bottom-4',(20,b),(l+q,b))")
    if bezel:
        body+=f"""
        self.add_line('left-lower',(l,b-q),(l,{bezel}))
        self.add_line('left-upper',(l,{bezel}),(l,t+q))
"""
    else:body+="        self.add_line('left',(l,b-q),(l,t+q))\n"
    body+="        self.add_arc('top-left',(l,t+q),(l+q,t),radius_x=q)\n"
    members=['top','top-right']+(['right-upper','right-lower'] if bezel else ['right'])+['bottom-right','bottom-1','bottom-2','bottom-3','bottom-4','bottom-left']+(['left-lower','left-upper'] if bezel else ['left'])+['top-left']
    body+=f"        self.add_contour('screen',*{members!r},closed=True)\n"
    if bezel:body+=f"        self.add_line('bezel',(l,{bezel}),(r,{bezel}))\n        self.relate('connect','screen','bezel')\n"
    if stand=='single':
        body+=f"        self.add_line('stand',(24,b),(24,{bottom}))\n        self.relate('connect','stand','screen')\n        self.add_polyline('foot',(16,{bottom}),(24,{bottom}),(32,{bottom}))\n        self.relate('connect','stand','foot')\n"
    else:
        left,right=(18,30) if stand=='tapered' else (20,28)
        body+=f"""
        self.add_line('stand-left',(20,b),({left},{bottom}))
        self.add_line('stand-right',(28,b),({right},{bottom}))
        self.add_polyline('foot',(14,{bottom}),({left},{bottom}),({right},{bottom}),(34,{bottom}))
        for part in ('stand-left','stand-right'):
            self.relate('connect',part,'screen')
            self.relate('connect',part,'foot')
"""
    design(n,key,f'A desktop display with {"a lower bezel" if bezel else "an uninterrupted face"} and {stand} stand. All paired corners share radius {rad}; shared axis x24. Centerline extremes ({l},{t})-({r},{bottom}).',body,'Lucide monitor original and atomic-debug: four tangent quarter-circle corners, centered support, and horizontal foot. Source-specific bezel and stand preserved.')
monitor(8,'SQUARE',6,6,42,32,42,24,'tapered',4)
monitor(9,'HRECT_L',4,8,44,30,40,22,'tapered',3)
monitor(10,'HRECT_L',4,8,44,30,40,None,'tapered',4)
monitor(11,'SQUARE',6,6,42,32,42,24,'straight',3)
monitor(12,'HRECT_L',4,8,44,30,40,None,'single',4)
design(14,'SQUARE','A raised index finger with thumb and palm below four dial strokes. Four dial marks form a 2x2 series; finger has an 8-unit-wide rounded cap. Deliberate hand asymmetry follows the source. Extremes (6,6)-(42,42). Human-reference.md and human_ref user/full-body inspected; no head-body pair exists.',"""
        for row in range(2):
            for col in range(2):
                x,y=6+14*col,6+10*row
                self.add_line('key-'+str(row)+'-'+str(col),(x,y),(x+6,y))
        self.add_line('finger-left',(28,32),(28,20))
        self.add_arc('tip',(28,20),(36,20),radius_x=4)
        self.add_line('finger-right',(36,20),(36,28))
        self.add_bezier('palm-top',(36,28),((36,30),(42,30),(42,33)))
        self.add_line('palm-right',(42,33),(40,42))
        self.add_line('palm-left',(24,42),(18,31))
        self.add_bezier('thumb',(18,31),((15,25),(21,23),(24,28)))
        self.add_line('thumb-return',(24,28),(28,32))
        self.add_contour('hand','palm-left','thumb','thumb-return','finger-left','tip','finger-right','palm-top','palm-right')
""",'Lucide hand: coherent round finger cap and continuous palm silhouette. Shared human references reviewed for rounded anatomy; head spacing does not apply.')
design(15,'HRECT_L','A Digimon Digivice with a scalloped casing, double circular display, paired left buttons, right button, and two antenna strokes. Bilateral case contour centered at (24,24); intentional asymmetric controls preserved. Extremes (4,8)-(44,40).',"""
        self.add_bezier('shell',(18,8),((16,8),(15,13),(12,14)),((9,16),(4,15),(4,20)),((4,24),(4,28),(5,31)),((6,34),(12,33),(15,36)),((16,38),(16,40),(19,40)),((22,40),(26,40),(29,40)),((32,40),(32,37),(35,35)),((38,33),(43,34),(44,30)),((44,26),(44,22),(44,20)),((44,16),(38,16),(35,14)),((32,12),(32,8),(30,8)),((26,8),(22,8),(18,8)))
        self.add_contour('case','shell',closed=True)
        self.circle('bezel',25,24,11)
        self.circle('display',25,24,6)
        for j,y in enumerate((21,28)):self.circle('button-'+str(j),9,y,2)
        self.add_polyline('right-button',(36,22),(40,22),(40,26),(36,26))
        self.add_line('antenna-1',(10,15),(8,12))
        self.add_line('antenna-2',(14,13),(12,10))
""",'Lucide gamepad: repeated control definitions and clear outer enclosure; distinctive case and concentric display taken from supplied Digivice.')
design(16,'VRECT_L','Six outlined Braille dots arranged in two columns and three rows. Repeated radius-4 circles at x12/36 and y8/24/40. Centerline extremes (8,4)-(40,44).',"""
        for col,x in enumerate((12,36)):
            for row,y in enumerate((8,24,40)):
                self.circle('dot-'+str(col)+'-'+str(row),x,y,4)
""")
monitor(18,'HRECT_L',4,8,44,30,40,22,'straight',3)

def run():
    for row in ROWS:
        if row['skip']:continue
        n=row['number']; key,plan,body,refs,omissions=DESIGNS[n]
        d=Path(row['directory']); icon_id=row['concept'].replace(' ','-')
        module_name=icon_id.replace('-','_')+'_'+row['source_uuid'].replace('-','_')
        metadata={**row,'icon_id':icon_id,'author':AUTHOR,'keyshape':key,'plan':plan,'construction_references':refs,'omissions':omissions}
        (d/(icon_id+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
        code=f'"""{plan}\n{refs}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n\nSOURCE_ICON_ID = {row["source_uuid"]!r}\nSOURCE_PATH = {row["reference_path"]!r}\nAUTHOR = {AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id = {icon_id!r}\n    keyshape = Keyshape.{key}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects/devices"\n    aliases = ()\n    keywords = {tuple(row["concept"].split())!r}\n'+HELPERS+'\n    def build(self):\n'+body
        (d/(module_name+'.py')).write_text(code)
        try:
            spec=importlib.util.spec_from_file_location(module_name,d/(module_name+'.py'));module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
            icon=module.Drawing();report=icon.validate_icon()
            (d/'validation.txt').write_text(report.describe())
            svg=icon.to_svg();(d/(icon_id+'.svg')).write_text(svg)
            for theme,bg,invert in [('light','#ffffff',False),('dark','#171b24',True)]:
                for size in (48,240):cairosvg.svg2png(bytestring=svg.encode(),write_to=str(d/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg,negate_colors=invert)
            metadata.update(validation_status=report.status,errors=[str(e) for e in report.errors],warnings=[str(e) for e in report.warnings])
            print(n,icon_id,report.status,flush=True)
        except Exception:
            error=traceback.format_exc();(d/'error.txt').write_text(error);metadata.update(validation_status='error',error=error);print(n,error,flush=True)
        (d/'pending-review.json').write_text(json.dumps(metadata,indent=2))
if __name__=='__main__':run()
