#!/usr/bin/env python3
"""Regression coverage for normal, sub, and container profile plumbing."""

from __future__ import annotations

from copy import deepcopy
from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest import mock
import xml.etree.ElementTree as ET

from icon_profiles import (
    canonical_tokens,
    document_icon_type,
    get_profile,
    validate_container_slot,
    validate_document_profile,
    svg_native_size_issues,
    resolve_profiles,
    source_document,
    validate_profile_source,
)
from keyfit import assign, circle_overflow, token_box
from validate_icon import container_paint_overlap


CORE = Path(__file__).resolve().parent


def custom_catalog():
    source = source_document()
    source["profiles"]["badge"] = {
        "label": "Small badge", "canvas": 40, "strokeWidth": 3,
        "keyshapes": [{"name": "badge-square", "orientation": "square", "shape": "rect", "width": 32, "height": 32}],
        "validation": {"gridStep": .5, "minimumDistinctCenterlineDistance": 3},
    }
    return source


class ProfileSourceTests(unittest.TestCase):
    def test_native_spacing_floors_reload_from_json_without_changing_other_profiles(self):
        with TemporaryDirectory() as folder:
            runtime = Path(folder)
            shutil.copy2(CORE / "icon_profiles.py", runtime / "icon_profiles.py")
            catalog = runtime / "icon_profiles.json"
            source = source_document()

            def load_distances():
                catalog.write_text(json.dumps(source), encoding="utf-8")
                result = subprocess.run(
                    [sys.executable, "-B", "-c", "import json; from icon_profiles import get_profile; "
                     "print(json.dumps({name: get_profile(name)['minimumDistinctCenterlineDistance'] "
                     "for name in ('normal', 'sub', 'container')}))"],
                    cwd=runtime, capture_output=True, text=True,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                return json.loads(result.stdout)

            self.assertEqual(load_distances(), {"normal": 8, "sub": 3, "container": 4})
            source["profiles"]["normal"]["validation"]["minimumDistinctCenterlineDistance"] = 10
            self.assertEqual(load_distances(), {"normal": 10, "sub": 3, "container": 4})
            self.assertEqual(get_profile("normal")["minimumDistinctCenterlineDistance"], 8)

    def test_v2_has_one_size_and_deeply_inherited_validation(self):
        source = custom_catalog()
        source["profiles"]["badge"]["validation"]["geometryTolerance"] = .005
        source["profiles"]["badge-large"] = {"label": "Large badge", "extends": "badge", "canvas": 44,
                                            "validation": {"minimumEnclosedRadius": 2}}
        snapshot = deepcopy(source)
        profiles = resolve_profiles(source)
        child = profiles["badge-large"]
        self.assertEqual((child["canvas"], child["designCanvas"], child["shipCanvas"]), (44, 44, 44))
        self.assertEqual((child["strokeWidth"], child["designStroke"], child["shipStroke"]), (3, 3, 3))
        self.assertEqual(child["center"], {"x": 22, "y": 22})
        self.assertEqual(child["validation"], {**source["validationDefaults"], **source["profiles"]["badge"]["validation"], "minimumEnclosedRadius": 2})
        self.assertEqual(child["minimumDistinctCenterlineDistance"], 3)
        self.assertNotIn("designCanvas", source["profiles"]["badge"])
        self.assertEqual(source, snapshot)
        child["validation"]["gridStep"] = 99
        self.assertEqual(resolve_profiles(source)["badge-large"]["validation"]["gridStep"], .5)

    def test_slot_presence_can_be_inherited_replaced_or_explicitly_cleared(self):
        source = custom_catalog()
        source["profiles"]["badge-holder"] = {"label": "Badge holder", "extends": "container", "canvas": 80,
            "containerSlot": {"x": 20, "y": 20, "w": 40, "h": 40, "acceptedProfile": "badge", "minimumClearSquare": 40}}
        source["profiles"]["holder-copy"] = {"label": "Holder copy", "extends": "badge-holder"}
        source["profiles"]["plain-large"] = {"label": "Plain large icon", "extends": "badge-holder", "containerSlot": None}
        profiles = resolve_profiles(source)
        self.assertEqual(profiles["holder-copy"]["containerSlot"], profiles["badge-holder"]["containerSlot"])
        self.assertNotIn("containerSlot", profiles["plain-large"])
        source["profiles"]["badge"]["validation"]["minimumSolidFillDepth"] = 0
        self.assertEqual(resolve_profiles(source)["badge"]["validation"]["minimumSolidFillDepth"], 0)

    def test_invalid_raw_configuration_is_rejected_exhaustively(self):
        good = custom_catalog()
        mutations = [
            lambda s: s.update(schemaVersion=1), lambda s: s.update(schemaVersion=True),
            lambda s: s.update(defaultIconType="missing"), lambda s: s.update(unknown=True),
            lambda s: s.update(profiles={}), lambda s: s["validationDefaults"].pop("gridStep"),
            lambda s: s["profiles"]["badge"].pop("label"), lambda s: s["profiles"]["badge"].update(label=" "),
            lambda s: s["profiles"]["badge"].update(canvas=40.5),
            lambda s: s["profiles"]["badge"].update(designCanvas=40),
            lambda s: s["profiles"]["badge"].update(extends="missing"),
            lambda s: s["profiles"]["normal"].update(extends="container"),
            lambda s: s["profiles"]["badge"].update(strokeWidth=41),
            lambda s: s["profiles"]["badge"].update(keyshapes=[]),
            lambda s: s["profiles"]["badge"]["keyshapes"].append(deepcopy(s["profiles"]["badge"]["keyshapes"][0])),
            lambda s: s["profiles"]["badge"]["keyshapes"][0].update(width=80,height=80),
            lambda s: s["profiles"]["badge"]["keyshapes"][0].update(width=2,height=2),
            lambda s: s["profiles"]["badge"]["keyshapes"][0].update(width=30),
            lambda s: s["profiles"]["normal"]["keyshapes"][0].update(diameter=42),
            lambda s: s["profiles"]["badge"]["validation"].update(unknown=1),
            lambda s: s["profiles"]["badge"]["validation"].update(majorGridStep=.25),
            lambda s: s["profiles"]["badge"]["validation"].update(gridStep=1e-320),
            lambda s: s["profiles"]["container"]["containerSlot"].update(acceptedProfile="missing"),
            lambda s: s["profiles"]["container"]["containerSlot"].update(acceptedProfile="container"),
            lambda s: s["profiles"]["container"]["containerSlot"].update(x=15),
            lambda s: s["profiles"]["container"]["containerSlot"].update(minimumClearSquare=16),
        ]
        for index, mutate in enumerate(mutations):
            source = deepcopy(good)
            mutate(source)
            with self.subTest(case=index), self.assertRaises(ValueError):
                validate_profile_source(source)
        for value in (True, None, "3", 0, -1, float("nan"), float("inf"), 10 ** 400):
            source = deepcopy(good)
            source["profiles"]["badge"]["strokeWidth"] = value
            with self.subTest(stroke=value), self.assertRaises(ValueError):
                validate_profile_source(source)
        for name in ("../badge", "Badge", "badge_2", "constructor", "prototype"):
            source = deepcopy(good)
            source["profiles"][name] = source["profiles"].pop("badge")
            with self.subTest(name=name), self.assertRaises(ValueError):
                validate_profile_source(source)

    def test_pure_generation_supports_custom_only_catalog_and_removed_builtins(self):
        from generate_profile_assets import profile_asset_contents
        source = custom_catalog()
        source["defaultIconType"] = "badge"
        source["profiles"] = {"badge": source["profiles"]["badge"]}
        baseline = source_document()
        assets = profile_asset_contents(source, Path("/isolated"))
        self.assertEqual(len(assets), 4)
        self.assertTrue(all(path.suffix == ".md" for path in assets))
        self.assertTrue(all("frontend" not in path.parts for path in assets))
        self.assertIn("badge-square", assets[Path("/isolated/docs/shared/icon-profiles.md")])
        self.assertIn("minimumEnclosedRadius", assets[Path("/isolated/docs/shared/icon-profiles.md")])
        for folder in ("icons", "sub-icons", "container-icons"):
            self.assertIn("not configured", assets[Path(f"/isolated/docs/{folder}/profile.md")])
        self.assertEqual(source_document(), baseline)

    def test_deep_inheritance_does_not_depend_on_python_recursion_limit(self):
        source = custom_catalog()
        profiles = {f"level-{index}": {"label": f"Level {index}", "extends": f"level-{index + 1}"} for index in range(1200)}
        profiles["level-1200"] = source["profiles"]["badge"]
        source.update(defaultIconType="level-0", profiles=profiles)
        self.assertEqual(resolve_profiles(source)["level-0"]["canvas"], 40)
        source["profiles"]["level-1200"]["extends"] = "level-0"
        with self.assertRaisesRegex(ValueError, "cyclic"):
            validate_profile_source(source)

    @unittest.skipUnless(all(importlib.util.find_spec(name) for name in ("cairosvg", "PIL", "numpy", "cv2")), "raster dependencies unavailable")
    def test_custom_profile_runs_real_pipeline_and_validation_tuning_changes_verdict(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            runtime = root / "core"
            runtime.mkdir()
            for name in ("icon_profiles", "icon_geometry", "shape_registry", "keyfit", "emit_icon", "validate_icon", "check_svg_grid", "check_keyfit", "qa_overlays", "render_svg_contact_sheet", "detect_svg_shapes", "compose_container_preview"):
                shutil.copy2(CORE / f"{name}.py", runtime / f"{name}.py")
            source = custom_catalog()
            source["defaultIconType"] = "badge"
            source["profiles"] = {"badge": source["profiles"]["badge"]}
            catalog_path = runtime / "icon_profiles.json"
            catalog_path.write_text(json.dumps(source))
            document = {"name": "badge-mark", "iconType": "badge", "canvas": 40, "strokeWidth": 3,
                "schemaVersion": 2, "keyfitCheck": {"targetToken": "badge-square"},
                "elements": [{"id": "outline", "tag": "rect", "attrs": {"x": 5.5, "y": 5.5, "width": 29, "height": 29}}]}
            editable = root / "badge-mark.json"
            editable.write_text(json.dumps(document))
            final = root / "badge-mark.svg"

            def run(name, *arguments, expected=0):
                result = subprocess.run([sys.executable, str(runtime / f"{name}.py"), *map(str, arguments)], capture_output=True, text=True)
                self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                return result

            run("emit_icon", editable)
            run("validate_icon", editable)
            emitted = ET.parse(final).getroot()
            self.assertEqual((emitted.get("width"), emitted.get("height"), emitted.get("stroke-width")), ("40", "40", "3"))
            run("render_svg_contact_sheet", root, root / "contact.png", "--columns", 1)
            from PIL import Image
            with Image.open(root / "contact.png") as sheet:
                self.assertEqual(sheet.size, (132, 84))
            run("detect_svg_shapes", final, "--output", root / "detected.json")
            detected = json.loads((root / "detected.json").read_text())
            self.assertEqual(detected["targetSpec"]["grid"], {"minor": .5, "major": 4})
            self.assertEqual(detected["targetSpec"]["regularStroke"], {"design": 3, "ship": 3})
            run("check_svg_grid", final, "--expected", "ship", "--output-dir", root / "grid")
            run("check_keyfit", final, "--expected-editable-dir", root, "--samples-per-unit", 8, "--output-dir", root / "keyfit")
            keyfit = json.loads((root / "keyfit/badge-mark.keyfit.json").read_text())
            self.assertEqual(keyfit["status"], "pass")
            self.assertEqual(keyfit["toleranceDesignUnits"], source["validationDefaults"]["keyshapeTolerance"])
            run("qa_overlays", final, "--samples-per-unit", 8, "--output-dir", root / "holes")
            initial = json.loads((root / "holes/badge-mark.metrics.json").read_text())
            self.assertEqual(initial["status"], "pass")
            source["validationDefaults"]["minimumEnclosedRadius"] = 18
            catalog_path.write_text(json.dumps(source))
            run("qa_overlays", final, "--samples-per-unit", 8, "--output-dir", root / "holes-strict")
            strict = json.loads((root / "holes-strict/badge-mark.metrics.json").read_text())
            self.assertEqual(strict["status"], "fail")
            self.assertEqual(strict["configuredMinimumRadiusDesignUnits"], 18)
            run("qa_overlays", final, "--samples-per-unit", 8, "--min-radius-design-u", 1, "--output-dir", root / "holes-override")
            self.assertEqual(json.loads((root / "holes-override/badge-mark.metrics.json").read_text())["status"], "pass")
            source["profiles"]["badge"]["validation"]["gridStep"] = 1
            catalog_path.write_text(json.dumps(source))
            run("check_svg_grid", final, "--expected", "ship", "--output-dir", root / "grid-strict", expected=1)
            # Geometry and raster tolerances remain separately tunable; CLI
            # edge tolerances intentionally override the configured default.
            document["elements"][0]["attrs"]["x"] = 5.55
            editable.write_text(json.dumps(document))
            run("emit_icon", editable)
            run("validate_icon", editable, expected=1)
            source["profiles"]["badge"]["validation"]["geometryTolerance"] = .06
            catalog_path.write_text(json.dumps(source))
            run("validate_icon", editable)
            run("check_keyfit", final, "--expected-editable-dir", root, "--samples-per-unit", 64, "--output-dir", root / "keyfit-strict", expected=1)
            source["profiles"]["badge"]["validation"]["keyshapeTolerance"] = .1
            catalog_path.write_text(json.dumps(source))
            run("check_keyfit", final, "--expected-editable-dir", root, "--samples-per-unit", 64, "--output-dir", root / "keyfit-relaxed")
            run("check_keyfit", final, "--expected-editable-dir", root, "--samples-per-unit", 64, "--tolerance-design-u", .001, "--output-dir", root / "keyfit-override", expected=1)
            # A custom container need not be named 'container', and its
            # accepted icon retains stroke3 inside a stroke4 frame preview.
            source["profiles"]["badge-holder"] = {"label": "Badge holder", "canvas": 80, "strokeWidth": 4,
                "keyshapes": [{"name": "holder-square", "orientation": "square", "shape": "rect", "width": 76, "height": 76}],
                "containerSlot": {"x": 20, "y": 20, "w": 40, "h": 40, "acceptedProfile": "badge", "minimumClearSquare": 40}}
            catalog_path.write_text(json.dumps(source))
            holder = {"name": "badge-holder", "iconType": "badge-holder", "canvas": 80, "strokeWidth": 4,
                "schemaVersion": 2, "keyfitCheck": {"targetToken": "holder-square"},
                "containerSlot": {"x": 20, "y": 20, "w": 40, "h": 40, "acceptedKeyshape": "badge-square"},
                "elements": [{"id": "frame", "tag": "rect", "attrs": {"x": 4, "y": 4, "width": 72, "height": 72}}]}
            holder_path = root / "badge-holder.json"
            holder_path.write_text(json.dumps(holder))
            run("emit_icon", holder_path)
            run("validate_icon", holder_path)
            manifest = root / "preview.json"
            manifest.write_text(json.dumps({"schemaVersion": 1, "kind": "container-filled-preview", "name": "filled-badge",
                                           "container": "badge-holder.json", "sub": "badge-mark.json"}))
            run("compose_container_preview", manifest, "--out-dir", root / "preview")
            preview = ET.parse(root / "preview/filled-badge.svg").getroot()
            self.assertEqual(preview.get("stroke-width"), "4")
            self.assertEqual(preview.findall("{*}path")[1].get("stroke-width"), "3")
            holder["elements"].append({"id": "intrusion", "tag": "line", "attrs": {"x1": 32, "y1": 40, "x2": 48, "y2": 40}})
            holder_path.write_text(json.dumps(holder))
            run("emit_icon", holder_path)
            collision = run("validate_icon", holder_path, expected=1)
            self.assertIn("protected 40x40 clearance", collision.stdout)


class IconProfileTests(unittest.TestCase):
    def test_normal_uses_one_native_48_canvas_and_4u_stroke(self):
        profile = get_profile("normal")
        self.assertEqual(
            (profile["designCanvas"], profile["shipCanvas"], profile["designStroke"], profile["shipStroke"]),
            (48, 48, 4, 4),
        )
        self.assertEqual(profile["minimumDistinctCenterlineDistance"], 8)
        self.assertEqual(profile["validation"]["minimumDistinctCenterlineDistance"] - profile["strokeWidth"], 4)
        self.assertEqual(
            [item["name"] for item in canonical_tokens("normal")],
            ["circle-44", "square-40", "portrait-36x44", "landscape-44x36"],
        )

    def test_sub_profile_has_native_32_canvas_and_its_own_tokens(self):
        profile = get_profile("sub")
        self.assertEqual((profile["designCanvas"], profile["shipCanvas"]), (32, 32))
        self.assertEqual((profile["designStroke"], profile["shipStroke"]), (4, 4))
        self.assertEqual(profile["minimumDistinctCenterlineDistance"], 3)
        self.assertEqual(
            [item["name"] for item in canonical_tokens("sub")],
            ["circle-32", "square-32", "portrait-28x32", "landscape-32x28"],
        )
        self.assertEqual(token_box(32, 28, "sub"), (0, 2, 32, 30))
        self.assertEqual(assign((0, 2, 32, 30), icon_type="sub")["name"], "landscape-32x28")
        self.assertLessEqual(circle_overflow([(16, 2)], 4, "sub"), 0)

    def test_profile_declarations_reject_cross_profile_canvas(self):
        with self.assertRaisesRegex(ValueError, "sub design canvas is fixed at 32"):
            validate_document_profile({"iconType": "sub", "canvas": 48, "strokeWidth": 4})
        with self.assertRaisesRegex(ValueError, "container design canvas is fixed at 64"):
            validate_document_profile(
                {
                    "iconType": "container",
                    "canvas": 48,
                    "strokeWidth": 4,
                    "containerSlot": {
                        "x": 16,
                        "y": 16,
                        "w": 32,
                        "h": 32,
                        "acceptedKeyshape": "square-32",
                    },
                }
            )

    def test_explicit_empty_icon_type_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown iconType"):
            document_icon_type({"iconType": ""})

    def test_container_has_a_dedicated_native_64_outer_profile(self):
        normal = get_profile("normal")
        container = get_profile("container")
        self.assertEqual(
            (container["designCanvas"], container["shipCanvas"]),
            (64, 64),
        )
        self.assertEqual(container["center"], {"x": 32, "y": 32})
        self.assertEqual(
            (container["designStroke"], container["shipStroke"]),
            (normal["designStroke"], normal["shipStroke"]),
        )
        self.assertEqual(container["minimumDistinctCenterlineDistance"], 4)
        self.assertEqual(
            [item["name"] for item in canonical_tokens("container")],
            ["circle-60", "square-56", "portrait-52x60", "landscape-60x52"],
        )
        self.assertEqual(token_box(60, 52, "container"), (2, 6, 62, 58))

    def test_normal_structural_validation_checks_one_actual_svg_after_both_aliases_match(self):
        from icon_geometry import resolve_icon, svg
        import validate_icon

        for icon_type, mismatch, expected_calls in (("normal", False, 1), ("normal", True, 0), ("sub", False, 0), ("container", False, 0)):
            with self.subTest(icon_type=icon_type, mismatch=mismatch), TemporaryDirectory() as folder:
                root=Path(folder)
                profile=get_profile(icon_type)
                token=next(item for item in profile["keyshapes"] if item["orientation"]=="square")
                origin=(profile["canvas"]-token["width"]+profile["strokeWidth"])/2
                size=token["width"]-profile["strokeWidth"]
                document={"name":"spacing-gate", "schemaVersion":2, "iconType":icon_type,
                          "canvas":profile["canvas"], "strokeWidth":profile["strokeWidth"],
                          "keyfitCheck":{"targetToken":token["name"]},
                          "elements":[{"id":"outline", "tag":"rect", "attrs":{"x":origin,"y":origin,"width":size,"height":size}}]}
                if icon_type=="container":
                    document["containerSlot"]={"x":16,"y":16,"w":32,"h":32,"acceptedKeyshape":"square-32"}
                editable=root/"spacing-gate.json"
                editable.write_text(json.dumps(document),encoding="utf-8")
                text=svg(resolve_icon(document),profile["canvas"],profile["strokeWidth"])
                ship=root/"spacing-gate.svg"
                ship.write_text(text,encoding="utf-8")
                (root/"spacing-gate-design.svg").write_text(text+("\n" if mismatch else ""),encoding="utf-8")
                output=io.StringIO()
                with mock.patch("check_svg_spacing.check_file",return_value={"ok":True,"status":"pass","errors":[],"pairs":[]}) as checker:
                    with mock.patch.object(sys,"argv",["validate_icon.py",str(editable)]),redirect_stdout(output):
                        result=validate_icon.main()
                self.assertEqual(result,1 if mismatch else 0,output.getvalue())
                self.assertEqual(checker.call_count,expected_calls)
                if expected_calls:
                    checker.assert_called_once_with(ship,icon_type="normal")

    def test_normal_structural_spacing_fails_closed_with_contour_details(self):
        from validate_icon import disconnected_spacing_failures

        pair={"status":"fail","closestContours":["element-0/subpath-1","element-0/subpath-2"],
              "centerlineDistance":7,"requiredCenterline":8}
        for status in ("fail","review"):
            report={"ok":False,"status":status,"errors":[],"pairs":[{**pair,"status":status}]}
            with self.subTest(status=status),mock.patch("check_svg_spacing.check_file",return_value=report):
                result=disconnected_spacing_failures(Path("icon.svg"))
            self.assertEqual(len(result),1)
            for detail in ("element-0/subpath-1","element-0/subpath-2","7u centerline distance","required 8u",status):
                self.assertIn(detail,result[0])
        for report in (None, {"ok":True,"status":"pass"}, {"ok":False,"status":"error","errors":["geometry too complex"],"pairs":[]},
                       {"ok":False,"status":"fail","errors":[],"pairs":[]},
                       {"ok":True,"status":"pass","errors":[],"pairs":[pair]}):
            with self.subTest(report=report),mock.patch("check_svg_spacing.check_file",return_value=report):
                self.assertTrue(disconnected_spacing_failures(Path("icon.svg")))
        with mock.patch("check_svg_spacing.check_file",side_effect=RuntimeError("engine unavailable")):
            self.assertIn("engine unavailable",disconnected_spacing_failures(Path("icon.svg"))[0])

    def test_separate_subpaths_in_one_element_must_meet_normal_eight_unit_spacing(self):
        from icon_geometry import resolve_icon, svg
        import validate_icon

        for distance,expected in ((7,1),(8,0)):
            with self.subTest(distance=distance),TemporaryDirectory() as folder:
                root=Path(folder)
                document={"name":"separate-subpaths","schemaVersion":2,"iconType":"normal","canvas":48,"strokeWidth":4,
                          "keyfitCheck":{"targetToken":"square-40"},
                          "elements":[{"id":"outline-and-detail","tag":"path","attrs":{"d":f"M6 6H42V42H6ZM14 {6+distance}H34"}}]}
                editable=root/"separate-subpaths.json"
                editable.write_text(json.dumps(document),encoding="utf-8")
                text=svg(resolve_icon(document),48,4)
                for filename in ("separate-subpaths.svg","separate-subpaths-design.svg"):
                    (root/filename).write_text(text,encoding="utf-8")
                output=io.StringIO()
                with mock.patch.object(sys,"argv",["validate_icon.py",str(editable)]),redirect_stdout(output):
                    result=validate_icon.main()
                self.assertEqual(result,expected,output.getvalue())
                if distance<8:
                    self.assertIn("disconnected contours",output.getvalue())
                    self.assertIn("7u centerline distance; required 8u",output.getvalue())

    def test_container_slot_translates_each_sub_keyshape(self):
        expected = {
            "circle-32": [16, 16, 48, 48],
            "square-32": [16, 16, 48, 48],
            "portrait-28x32": [18, 16, 46, 48],
            "landscape-32x28": [16, 18, 48, 46],
        }
        for token, bounds in expected.items():
            with self.subTest(token=token):
                slot = validate_container_slot({
                    "containerSlot": {"x": 16, "y": 16, "w": 32, "h": 32, "acceptedKeyshape": token}
                })
                self.assertEqual(slot["acceptedBounds"], bounds)
                self.assertEqual(slot["protectedBounds"], [16, 16, 48, 48])
                self.assertEqual(slot["minimumClearSquare"], 32)

    def test_container_slot_metadata_and_painted_overlap_are_enforced(self):
        document = {
            "iconType": "container",
            "canvas": 64,
            "strokeWidth": 4,
            "containerSlot": {"x": 16, "y": 16, "w": 32, "h": 32, "acceptedKeyshape": "circle-32"},
        }
        _, profile = validate_document_profile(document)
        slot = validate_container_slot(document, profile)
        self.assertTrue(container_paint_overlap([(32, 32)], slot, 4))
        self.assertFalse(container_paint_overlap([(32, 4)], slot, 4))
        self.assertTrue(container_paint_overlap([(16, 16)], slot, 4))
        self.assertFalse(container_paint_overlap([(14, 16)], slot, 4))
        self.assertTrue(container_paint_overlap([(14.1, 16)], slot, 4))
        document["containerSlot"]["acceptedKeyshape"] = "circle-44"
        with self.assertRaisesRegex(ValueError, "unknown containerSlot.acceptedKeyshape"):
            validate_document_profile(document)

    def test_emit_and_validate_sub_and_container_documents(self):
        fixtures = [
            {
                "name": "profile-sub",
                "iconType": "sub",
                "canvas": 32,
                "strokeWidth": 4,
                "keyfitCheck": {"targetToken": "circle-32"},
                "instances": [{"shapeId": "circle", "x": 2, "y": 2, "w": 28, "h": 28, "rotation": 0, "z": 0}],
            },
            {
                "name": "profile-container",
                "iconType": "container",
                "canvas": 64,
                "strokeWidth": 4,
                "keyfitCheck": {"targetToken": "circle-60"},
                "containerSlot": {"x": 16, "y": 16, "w": 32, "h": 32, "acceptedKeyshape": "circle-32"},
                "instances": [{"shapeId": "circle", "x": 4, "y": 4, "w": 56, "h": 56, "rotation": 0, "z": 0}],
            },
        ]
        with TemporaryDirectory() as folder:
            root = Path(folder)
            for document in fixtures:
                with self.subTest(iconType=document["iconType"]):
                    editable = root / f"{document['name']}.json"
                    editable.write_text(json.dumps(document), encoding="utf-8")
                    emitted = subprocess.run(
                        [sys.executable, str(CORE / "emit_icon.py"), str(editable), "--out-dir", str(root)],
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(emitted.returncode, 0, emitted.stdout + emitted.stderr)
                    checked = subprocess.run(
                        [sys.executable, str(CORE / "validate_icon.py"), str(editable), "--dir", str(root)],
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
                    ship_canvas = get_profile(document["iconType"])["shipCanvas"]
                    self.assertIn(f'viewBox="0 0 {ship_canvas} {ship_canvas}"', (root / f"{document['name']}.svg").read_text())

    def test_incomplete_source_analysis_is_an_explicit_gate(self):
        document = {
            "name": "incomplete-profile",
            "canvas": 48,
            "strokeWidth": 4,
            "keyfitCheck": {"targetToken": "circle-44"},
            "sourceAnalysis": {"incomplete": True},
            "instances": [{"shapeId": "circle", "x": 4, "y": 4, "w": 40, "h": 40, "rotation": 0, "z": 0}],
        }
        with TemporaryDirectory() as folder:
            root = Path(folder)
            editable = root / "incomplete-profile.json"
            editable.write_text(json.dumps(document), encoding="utf-8")
            subprocess.run(
                [sys.executable, str(CORE / "emit_icon.py"), str(editable), "--out-dir", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )
            checked = subprocess.run(
                [sys.executable, str(CORE / "validate_icon.py"), str(editable), "--dir", str(root)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(checked.returncode, 1)
            self.assertIn("sourceAnalysis is marked incomplete", checked.stdout)

    def test_structural_validation_rejects_noncanonical_emitted_geometry(self):
        document = {
            "name": "parity-profile",
            "iconType": "normal",
            "canvas": 48,
            "strokeWidth": 4,
            "keyfitCheck": {"targetToken": "square-40"},
            "instances": [{"shapeId": "square", "x": 6, "y": 6, "w": 36, "h": 36, "rotation": 0, "z": 0}],
        }
        with TemporaryDirectory() as folder:
            root = Path(folder)
            editable = root / "parity-profile.json"
            editable.write_text(json.dumps(document), encoding="utf-8")
            subprocess.run(
                [sys.executable, str(CORE / "emit_icon.py"), str(editable), "--out-dir", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )
            (root / "parity-profile.svg").write_text(
                (root / "parity-profile-design.svg").read_text(encoding="utf-8").replace('width="48"', 'width="24"'),
                encoding="utf-8",
            )
            checked = subprocess.run(
                [sys.executable, str(CORE / "validate_icon.py"), str(editable), "--dir", str(root)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(checked.returncode, 1)
            self.assertIn("does not match canonical core/emit_icon.py output", checked.stdout)

    def test_native_svg_size_contract_checks_viewbox_and_intrinsic_dimensions(self):
        for icon_type, canvas in (("sub", 32), ("normal", 48), ("container", 64)):
            native = {"viewBox": f"0 0 {canvas} {canvas}", "width": str(canvas), "height": f"{canvas}px"}
            with self.subTest(icon_type=icon_type):
                self.assertEqual(svg_native_size_issues(native, icon_type), [])
                self.assertEqual(svg_native_size_issues({"viewBox": native["viewBox"]}, icon_type), [])
                for field, value in (("width", str(canvas // 2)), ("height", "50%"), ("width", "NaN"),
                                     ("viewBox", f"0 0 {canvas // 2} {canvas // 2}"),
                                     ("style", f"width:{canvas // 2}px!important")):
                    with self.subTest(field=field, value=value):
                        self.assertTrue(svg_native_size_issues({**native, field: value}, icon_type))

    def test_legacy_renderer_emits_only_one_native_svg_for_each_profile(self):
        for icon_type, canvas in (("sub", 32), ("normal", 48), ("container", 64)):
            with self.subTest(icon_type=icon_type), TemporaryDirectory() as folder:
                root = Path(folder)
                document = {"name": "native-render", "iconType": icon_type, "canvas": canvas, "strokeWidth": 4,
                            "schemaVersion": 2, "elements": [{"id": "line", "tag": "line", "attrs": {"x1": 4, "y1": 4, "x2": canvas - 4, "y2": 4}}]}
                if icon_type == "container":
                    document["containerSlot"] = {"x": 16, "y": 16, "w": 32, "h": 32, "acceptedKeyshape": "square-32"}
                source = root / "native-render.json"
                source.write_text(json.dumps(document))
                result = subprocess.run([sys.executable, str(CORE / "render_icon.py"), str(source), str(root / "native-render.svg")], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual([path.name for path in root.glob("*.svg")], ["native-render.svg"])
                svg = ET.parse(root / "native-render.svg").getroot()
                self.assertEqual((svg.get("width"), svg.get("height"), svg.get("stroke-width")), (str(canvas), str(canvas), "4"))

    def test_legacy_restore_and_repair_emit_no_reduced_output_folder(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            inventory = root / "inventory"
            inventory.mkdir()
            sources = root / "remake_opus_output"
            sources.mkdir()
            document = {"name": "native-circle", "canvas": 48, "strokeWidth": 4,
                        "keyfitCheck": {"targetToken": "circle-44"},
                        "instances": [{"shapeId": "circle", "x": 4, "y": 4, "w": 40, "h": 40}]}
            (sources / "native-circle.json").write_text(json.dumps(document))
            (inventory / "native-circle.svg").write_text('<svg/>')
            audit = root / "audit.json"
            audit.write_text(json.dumps([{"file": "native-circle.svg", "status": "pass",
                "paintedBoundsDesign": [2, 2, 46, 46], "assignedToken": {"name": "circle-44", "bounds": [2, 2, 46, 46]}}]))
            for tool, arguments in (("restore_grid_outputs.py", [inventory, "--project-root", root, "--output-dir", root / "restore"]),
                                    ("repair_keyshape_targets.py", [sources, audit, root / "repair"])):
                with self.subTest(tool=tool):
                    result = subprocess.run([sys.executable, str(CORE / tool), *map(str, arguments)], capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    output = root / ("restore" if tool.startswith("restore") else "repair")
                    self.assertFalse((output / "final_24").exists())
                    self.assertEqual(len(list(output.rglob("*.svg"))), 1)
                    svg = ET.parse(output / "final/native-circle.svg").getroot()
                    self.assertEqual((svg.get("width"), svg.get("height"), svg.get("stroke-width")), ("48", "48", "4"))

    @unittest.skipUnless(importlib.util.find_spec("cairosvg") and importlib.util.find_spec("PIL"), "contact sheet dependencies unavailable")
    def test_contact_sheet_native_defaults_and_reduced_size_rejection(self):
        from PIL import Image
        for icon_type, canvas in (("sub", 32), ("normal", 48), ("container", 64)):
            with self.subTest(icon_type=icon_type), TemporaryDirectory() as folder:
                root = Path(folder)
                source = root / "native.svg"
                source.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas}" height="{canvas}" viewBox="0 0 {canvas} {canvas}"><path d="M4 4H20" stroke="black" stroke-width="4"/></svg>')
                alias = root / "native-design.svg"
                alias.write_bytes(source.read_bytes())
                output = root / "sheet.png"
                command = [sys.executable, str(CORE / "render_svg_contact_sheet.py"), str(root), str(output), "--columns", "1"]
                if icon_type != "normal":
                    command += ["--icon-type", icon_type]
                result = subprocess.run(command, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                with Image.open(output) as sheet:
                    self.assertEqual(sheet.size, (132, canvas + 44))
                alias.write_text(alias.read_text().replace("M4 4H20", "M4 4H16"))
                divergent = subprocess.run(command, capture_output=True, text=True)
                self.assertNotEqual(divergent.returncode, 0)
                self.assertIn("differs from its native canonical file", divergent.stderr)
                alias.unlink()
                result = subprocess.run(command + ["--true-size", str(canvas // 2)], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("reviews use native", result.stderr)
                source.write_text(source.read_text().replace(f'width="{canvas}"', f'width="{canvas // 2}"'))
                result = subprocess.run(command, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("must be native", result.stderr)

    def test_structural_validation_accepts_star_without_angle_exceptions(self):
        document = {
            "name": "star-profile",
            "iconType": "sub",
            "canvas": 32,
            "strokeWidth": 4,
            "keyfitCheck": {"targetToken": "square-32"},
            "instances": [{"shapeId": "star", "x": 2, "y": 2, "w": 28, "h": 28, "rotation": 0, "z": 0}],
        }
        with TemporaryDirectory() as folder:
            root = Path(folder)
            editable = root / "star-profile.json"
            editable.write_text(json.dumps(document), encoding="utf-8")
            subprocess.run(
                [sys.executable, str(CORE / "emit_icon.py"), str(editable), "--out-dir", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )
            checked = subprocess.run(
                [sys.executable, str(CORE / "validate_icon.py"), str(editable), "--dir", str(root)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)

    def test_overlap_audit_uses_the_declared_profile_canvas(self):
        document = {
            "name": "overlap-sub",
            "iconType": "sub",
            "canvas": 32,
            "strokeWidth": 4,
            "sourceAnalysis": {
                "spacingChecks": [
                    {"instances": [0, 1], "relation": "ordinary-distinct", "pair": ["left", "right"]}
                ]
            },
            "instances": [
                {"shapeId": "line", "x": 4, "y": 8, "w": 8, "h": 1, "rotation": 0, "z": 0},
                {"shapeId": "line", "x": 20, "y": 8, "w": 8, "h": 1, "rotation": 0, "z": 1},
            ],
        }
        with TemporaryDirectory() as folder:
            root = Path(folder)
            editable = root / "overlap-sub.json"
            output = root / "overlap-sub.svg"
            editable.write_text(json.dumps(document), encoding="utf-8")
            checked = subprocess.run(
                [sys.executable, str(CORE / "render_overlap_audit.py"), str(editable), str(output)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
            report = output.read_text(encoding="utf-8")
            self.assertIn('viewBox="0 0 32 37"', report)
            self.assertIn("ordinary-distinct · 3u", report)

    def test_structural_spacing_floor_is_profile_specific(self):
        fixtures = [
            ("sub-distance-three", "sub", 32, "square-32", 2, 28, 4.5, 0, None),
            ("sub-distance-under-three", "sub", 32, "square-32", 2, 28, 4.25, 1, "under the 3u sub collision floor"),
            ("normal-distance-three", "normal", 48, "square-40", 6, 36, 8.5, 1, "under the 8u normal collision floor"),
            ("normal-distance-eight", "normal", 48, "square-40", 6, 36, 13.5, 0, None),
            ("normal-distance-under-eight", "normal", 48, "square-40", 6, 36, 13.25, 1, "under the 8u normal collision floor"),
        ]
        with TemporaryDirectory() as folder:
            root = Path(folder)
            for name, icon_type, canvas, token, shell_origin, shell_size, detail_y, expected_code, expected_message in fixtures:
                with self.subTest(icon_type=icon_type, detail_y=detail_y):
                    document = {
                        "name": name,
                        "iconType": icon_type,
                        "canvas": canvas,
                        "strokeWidth": 4,
                        "keyfitCheck": {"targetToken": token},
                        "instances": [
                            {"shapeId": "square", "x": shell_origin, "y": shell_origin, "w": shell_size, "h": shell_size, "rotation": 0, "z": 0},
                            {"shapeId": "line", "x": 14 if icon_type == "normal" else 10, "y": detail_y, "w": 12, "h": 1, "rotation": 0, "z": 1},
                        ],
                    }
                    editable = root / f"{name}.json"
                    editable.write_text(json.dumps(document), encoding="utf-8")
                    subprocess.run(
                        [sys.executable, str(CORE / "emit_icon.py"), str(editable), "--out-dir", str(root)],
                        check=True,
                        capture_output=True,
                        text=True,
                    )
                    checked = subprocess.run(
                        [sys.executable, str(CORE / "validate_icon.py"), str(editable), "--dir", str(root)],
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(checked.returncode, expected_code, checked.stdout + checked.stderr)
                    if expected_message:
                        self.assertIn(expected_message, checked.stdout)

    def test_container_validator_rejects_paint_in_protected_region(self):
        document = {
            "name": "colliding-container",
            "iconType": "container",
            "canvas": 64,
            "strokeWidth": 4,
            "keyfitCheck": {"targetToken": "circle-60"},
            "containerSlot": {"x": 16, "y": 16, "w": 32, "h": 32, "acceptedKeyshape": "circle-32"},
            "instances": [
                {"shapeId": "circle", "x": 4, "y": 4, "w": 56, "h": 56, "rotation": 0, "z": 0},
                {"shapeId": "dot", "x": 14, "y": 14, "w": 4, "h": 4, "rotation": 0, "z": 1},
            ],
        }
        with TemporaryDirectory() as folder:
            root = Path(folder)
            editable = root / "colliding-container.json"
            editable.write_text(json.dumps(document), encoding="utf-8")
            subprocess.run(
                [sys.executable, str(CORE / "emit_icon.py"), str(editable), "--out-dir", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )
            checked = subprocess.run(
                [sys.executable, str(CORE / "validate_icon.py"), str(editable), "--dir", str(root)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(checked.returncode, 1)
            self.assertIn("container paint enters the protected 32x32 clearance", checked.stdout)


if __name__ == "__main__":
    unittest.main()
