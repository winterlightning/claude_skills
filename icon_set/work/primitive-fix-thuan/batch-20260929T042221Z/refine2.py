exec((BATCH/'refine.py').read_text().split('revise(1,')[0])
revise(2,[("(33,27),(33,30)","(33,26),(33,28)"),("'exclamation-dot',(33,36)","'exclamation-dot',(33,34)")])
# The protesting fist has a smaller vertical envelope than the plain grip, making room for detached rays.
r=records[13];run=Path(r['run']);m=json.loads((run/'candidate.json').read_text());src=Path(r['module']).read_text();tree=ast.parse(src);cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));fn=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='build')
body='\n'.join(x[8:] for x in src.splitlines()[fn.body[0].lineno-1:fn.end_lineno]);body=body.split("self.add_line('ray-left'")[0]
# Shift the entire fist construction down 4, then keep wrist inside 48 via a shared point map.
body="""# Shared vertical map preserves the full fist while allocating a clear top band to rays.
original_path=self.path
original_line=self.add_line
original_arc=self.add_arc
def point(p): return (p[0],round(12+(p[1]-7)*32/37))
def mapped_path(name,start,*steps,closed=False):
    mapped=[]
    for s in steps: mapped.append((s[0],point(s[1]),*s[2:]))
    original_path(name,point(start),*mapped,closed=closed)
def mapped_line(name,a,b): return original_line(name,point(a),point(b))
""" if False else body
# Explicit authored y positions avoid scaling a completed drawing.
body=body.replace("(10,15)","(10,19)").replace("(16,15)","(16,19)").replace("(16,12)","(16,16)").replace("(22,12)","(22,16)").replace("(22,10)","(22,14)").replace("(28,10)","(28,14)").replace("(28,12)","(28,16)").replace("(34,12)","(34,16)")
body=body.replace("[(16,15,25),(22,12,22),(28,12,19)]","[(16,19,27),(22,16,22),(28,16,19)]")
body+="""
self.add_line('ray-left',(4,10),(6,12))
self.add_line('ray-upper-left',(15,3),(16,6))
self.add_line('ray-upper-right',(32,3),(31,6))
self.add_line('ray-right',(40,12),(43,9))
"""
author(13,body,'SQUARE',m['comparison'],'Four clear knuckles, folded thumb and wrist beneath four detached protest rays; lowered knuckles reserve breathing room for the rays.',m['construction_references'],m['omissions'],m['gate']['exception']['reason'])
