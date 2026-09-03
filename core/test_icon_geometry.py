#!/usr/bin/env python3
"""Contracts for shape-free editable sources and canonical SVG geometry."""
from copy import deepcopy
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

from icon_geometry import parse_path, path_data, primitive_commands, resolve_icon, sample, spacing_pair, svg

CORE=Path(__file__).resolve().parent


def source(*elements):
    return {"schemaVersion":2,"name":"test-icon","iconType":"normal","canvas":48,"strokeWidth":4,
            "keyfitCheck":{"targetToken":"square-40"},"elements":list(elements)}


def element(tag,attrs,identifier="outline"):
    return {"id":identifier,"role":"visible subject contour","tag":tag,"attrs":attrs}


class GeometrySourceTests(unittest.TestCase):
    def test_all_seven_native_tags_bake_without_a_shape_registry(self):
        specimens={
            "path":{"d":"M6 6 C6 10 10 12 16 12"},
            "line":{"x1":6,"y1":6,"x2":42,"y2":42},
            "circle":{"cx":24,"cy":24,"r":18},
            "ellipse":{"cx":24,"cy":24,"rx":18,"ry":14},
            "rect":{"x":6,"y":6,"width":36,"height":36,"rx":2,"ry":4},
            "polyline":{"points":"6,6 24,42 42,6"},
            "polygon":{"points":"6,6 24,42 42,6"},
        }
        with patch.dict(sys.modules,{"shape_registry":None}):
            for tag,attrs in specimens.items():
                with self.subTest(tag=tag):
                    paths=resolve_icon(source(element(tag,attrs)))
                    self.assertEqual(paths[0]["id"],"outline")
                    self.assertEqual(paths[0]["elementId"],"outline")
                    self.assertEqual(paths[0]["shapeId"],tag)
                    self.assertTrue(sample(paths[0]["commands"])[0])
                    output=svg(paths,48,4)
                    self.assertNotIn("transform=",output)
                    self.assertIn('stroke="currentColor"',output)
                    self.assertEqual(len(ET.fromstring(output).findall("{*}path")),1)

    def test_order_is_array_order_and_ids_survive(self):
        doc=source(element("line",{"x2":10},"first"),element("line",{"y2":10},"second"))
        self.assertEqual([(p["order"],p["elementId"]) for p in resolve_icon(doc)],[(0,"first"),(1,"second")])

    def test_shape_free_schema_cannot_be_ambiguous(self):
        good=source(element("line",{"x2":10}))
        for mutate in (
            lambda doc:doc.update(instances=[]),lambda doc:doc.update(schemaVersion=1),
            lambda doc:doc.update(schemaVersion=2.0),lambda doc:doc.update(elements=[]),
            lambda doc:doc["elements"].append(deepcopy(doc["elements"][0])),
            lambda doc:doc["elements"][0].update(id="bad id"),
            lambda doc:doc["elements"][0].update(transform="translate(1 1)"),
            lambda doc:doc["elements"][0].update(role={}),
        ):
            doc=deepcopy(good); mutate(doc)
            with self.subTest(doc=doc),self.assertRaises(ValueError): resolve_icon(doc)
        with self.assertRaises(ValueError): resolve_icon({"schemaVersion":2,"instances":[]})

    def test_rejects_paint_events_urls_and_unsupported_elements(self):
        for key,value in (("fill","red"),("stroke","url(https://example.com)"),("style","opacity:.5"),
                          ("onload","alert(1)"),("href","file:///tmp/x"),("transform","scale(2)")):
            with self.subTest(key=key),self.assertRaises(ValueError):
                resolve_icon(source(element("path",{"d":"M1 1L2 2",key:value})))
        for tag in ("script","use","image","g","foreignObject"):
            with self.subTest(tag=tag),self.assertRaises(ValueError): resolve_icon(source(element(tag,{})))

    def test_rejects_nonfinite_and_non_numeric_geometry(self):
        for value in (math.nan,math.inf,-math.inf,True,None,[],"NaN","1px","url(x)","1e999"):
            with self.subTest(value=value),self.assertRaises(ValueError): resolve_icon(source(element("circle",{"r":value})))
        for tag,attrs in (("circle",{"r":0}),("ellipse",{"rx":1,"ry":-1}),
                          ("rect",{"width":0,"height":2}),("rect",{"width":2,"height":2,"rx":-1})):
            with self.subTest(tag=tag),self.assertRaises(ValueError): primitive_commands(tag,attrs)
        self.assertTrue(primitive_commands("circle",{"r":"2e+0"}))

    def test_points_validation(self):
        for tag,points in (("polyline","1,2"),("polygon","1,2 3,4"),("polyline","1,2 3"),
                           ("polyline","1,2 3,4 junk"),("polyline","1,2 3,4,"),("polyline",[1,2,3,4])):
            with self.subTest(points=points),self.assertRaises(ValueError): primitive_commands(tag,{"points":points})

    def test_rect_svg_radius_defaults_and_clamping(self):
        only_ry=primitive_commands("rect",{"width":10,"height":6,"ry":8})
        arcs=[command.arc for command in only_ry if command.type=="A"]
        self.assertEqual(len(arcs),4)
        self.assertTrue(all(arc[:2]==(5,3) for arc in arcs))
        sharp=primitive_commands("rect",{"width":10,"height":6,"rx":2,"ry":0})
        self.assertNotIn("A",[command.type for command in sharp])

    def test_legacy_sources_still_bake_and_emit(self):
        paths=resolve_icon({"instances":[{"shapeId":"circle","x":6,"y":6,"w":36,"h":36,"rotation":45,"flipX":True}]})
        self.assertEqual(paths[0]["shapeId"],"circle")
        self.assertEqual(paths[0]["elementId"],"instance-0")
        self.assertNotIn("transform",svg(paths,48,4))
        with self.assertRaises(ValueError): resolve_icon({"instances":[{"shapeId":"line","x":math.nan,"y":0,"w":8,"h":1}]})

    def test_spacing_checks_accept_ids_and_legacy_indexes(self):
        paths=resolve_icon(source(element("line",{"x2":10},"left"),element("line",{"y2":10},"right")))
        self.assertEqual(spacing_pair({"elements":["right","left"]},paths),(0,1))
        self.assertEqual(spacing_pair({"instances":[1,0]},paths),(0,1))
        for check in ({"elements":["left","missing"]},{"elements":["left","left"]},{"instances":[True,1]},
                      {"elements":["left","right"],"instances":[0,1]},{}):
            with self.subTest(check=check),self.assertRaises(ValueError): spacing_pair(check,paths)


class PathParserTests(unittest.TestCase):
    def test_relative_shorthand_and_scientific_notation(self):
        commands=parse_path("m1e+1 10 2 0 h2 v2 q2 2 4 0 t4 0 c1 1 2 1 3 0 s2 -1 3 0 a2 2 0 01 4 0 z")
        self.assertEqual([p.type for p in commands],["M","L","L","L","Q","Q","C","C","A","Z"])
        self.assertEqual(commands[5].points,[(20,10),(22,12)])
        self.assertEqual(commands[7].points,[(26,11),(27,11),(28,12)])
        self.assertEqual(commands[-2].points,[(32,12)])
        self.assertEqual(commands[-2].arc,(2,2,0,0,1))
        self.assertEqual(parse_path(path_data(commands)),commands)

    def test_shorthand_control_does_not_leak_between_curve_types(self):
        commands=parse_path("M0 0 Q2 5 4 0 S6 3 8 0 T10 0")
        self.assertEqual(commands[2].points[0],(4,0))
        self.assertEqual(commands[3].points[0],(8,0))

    def test_close_resets_cursor_for_relative_moveto(self):
        commands=parse_path("M2 3 l4 0 z m1 1 l2 0")
        self.assertEqual(commands[3].points,[(3,4)])
        self.assertEqual(commands[4].points,[(5,4)])

    def test_rejects_malformed_path_instead_of_discarding_tokens(self):
        for data in ("",None,"L1 2","M1","M0 0 L2","M0 0 C1 2 3 4","M0 0 R1 1", "M0 0 L1 2 rubbish",
                     "M0 0LNaN 1","M0 0L1e999 2","M0 0A-2 2 0 0 1 2 2","M0 0A2 2 0 2 1 2 2",
                     "M0 0 A2 2 0 0.0 1 2 2","M0 0 Z1 2","M,0 0L1 1","M0 0L1,,2","M0 0L1 2,"):
            with self.subTest(data=data),self.assertRaises(ValueError): parse_path(data)
        with self.assertRaises(ValueError): primitive_commands("path",{"d":"M0 0"})
        with self.assertRaises(ValueError): primitive_commands("path",{"d":"M0 0 A2 2 0 0 1 0 0"})

    def test_cubic_extrema_are_sampled_exactly(self):
        points,_=sample(parse_path("M0 0 C0 10 10 10 10 0"),density=1)
        self.assertAlmostEqual(max(y for x,y in points),7.5,12)
        self.assertIn((5,7.5),points)
        points,_=sample(parse_path("M0 0 C8 0 -8 0 0 0"),density=1)
        self.assertAlmostEqual(max(x for x,y in points),4/math.sqrt(3),12)
        self.assertAlmostEqual(min(x for x,y in points),-4/math.sqrt(3),12)

    def test_degenerate_arc_matches_svg_line_or_no_op_semantics(self):
        points,segments=sample(parse_path("M1 1 A0 2 0 0 1 3 1 A2 2 0 0 1 3 1"))
        self.assertEqual(segments,[((1,1),(3,1))])
        self.assertEqual(points[-1],(3,1))

    def test_orphan_moveto_does_not_expand_painted_bounds(self):
        points,_=sample(parse_path("M100 100 M2 2 L4 2 M200 200 Z"))
        self.assertEqual((min(x for x,y in points),max(x for x,y in points)),(2,4))


class GeometryWorkflowTests(unittest.TestCase):
    def run_tool(self,name,path,*extra):
        return subprocess.run([sys.executable,str(CORE/name),str(path),*map(str,extra)],capture_output=True,text=True)

    def test_shape_free_emit_validate_and_ship_equivalence(self):
        doc=source(element("rect",{"x":6,"y":6,"width":36,"height":36,"rx":2}))
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/"test-icon.json"; path.write_text(json.dumps(doc))
            emitted=self.run_tool("emit_icon.py",path); self.assertEqual(emitted.returncode,0,emitted.stderr)
            validated=self.run_tool("validate_icon.py",path); self.assertEqual(validated.returncode,0,validated.stdout+validated.stderr)
            design=ET.parse(Path(folder)/"test-icon-design.svg").getroot(); ship=ET.parse(Path(folder)/"test-icon.svg").getroot()
            design_commands=parse_path(design.find("{*}path").get("d"))
            self.assertEqual(ship.find("{*}path").get("d"),path_data(design_commands,.5))
            self.assertEqual(ship.get("stroke-width"),"2")
            (Path(folder)/"test-icon.svg").write_text("<svg/>")
            tampered=self.run_tool("validate_icon.py",path)
            self.assertNotEqual(tampered.returncode,0)
            self.assertIn("does not match canonical",tampered.stdout)

    def test_optical_v2_fit_and_stale_declaration(self):
        doc=source(element("line",{"x1":24,"y1":6,"x2":24,"y2":42}))
        doc["keyfitCheck"].update(mode="optical",rationale="A divider must remain narrow.",paintedBounds=[22,4,26,44])
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/"test-icon.json"; path.write_text(json.dumps(doc))
            self.run_tool("emit_icon.py",path)
            valid=self.run_tool("validate_icon.py",path); self.assertEqual(valid.returncode,0,valid.stdout+valid.stderr)
            doc["keyfitCheck"]["paintedBounds"][0]=20; path.write_text(json.dumps(doc))
            invalid=self.run_tool("validate_icon.py",path); self.assertNotEqual(invalid.returncode,0)
            self.assertIn("stale",invalid.stdout)

    def test_id_spacing_declarations_and_overlap_audit(self):
        doc=source(element("rect",{"x":6,"y":6,"width":36,"height":36},"frame"),
                   element("line",{"x1":6,"y1":24,"x2":42,"y2":24},"divider"))
        doc["sourceAnalysis"]={"spacingChecks":[{"elements":["frame","divider"],"relation":"connected","centerlineDistance":0}]}
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/"test-icon.json"; path.write_text(json.dumps(doc))
            self.run_tool("emit_icon.py",path)
            valid=self.run_tool("validate_icon.py",path); self.assertEqual(valid.returncode,0,valid.stdout+valid.stderr)
            audit=self.run_tool("render_overlap_audit.py",path)
            self.assertEqual(audit.returncode,0,audit.stdout+audit.stderr)
            self.assertIn("frame / divider",(Path(folder)/"test-icon-overlap-audit.svg").read_text())
            doc["sourceAnalysis"]["spacingChecks"][0]["elements"][1]="missing"; path.write_text(json.dumps(doc))
            invalid=self.run_tool("validate_icon.py",path); self.assertNotEqual(invalid.returncode,0)
            self.assertIn("unknown elements",invalid.stdout)


if __name__=="__main__": unittest.main()
