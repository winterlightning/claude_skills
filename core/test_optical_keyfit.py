"""Optical sizing must not waive painted containment or accept stale evidence."""
import csv
from html.parser import HTMLParser
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from urllib.parse import unquote

from check_keyfit import classify_keyfit, write_csv, write_html
from check_svg_grid import inspect, write_report
from keyfit import validate_optical_bounds


class OpticalKeyfitTests(unittest.TestCase):
    def setUp(self):
        self.bounds = [14, 4, 18, 28]
        self.check = {"mode": "optical", "targetToken": "portrait-28x32",
                      "paintedBounds": self.bounds, "rationale": "Keep a narrow vertical divider."}

    def test_narrow_mark_preserves_proportions_inside_token(self):
        result = classify_keyfit(tuple(self.bounds), .01, "portrait-28x32", icon_type="sub", keyfit_check=self.check)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["fitMode"], "optical")

    def test_same_mark_fails_default_exact_mode(self):
        self.assertEqual(classify_keyfit(tuple(self.bounds), .01, "portrait-28x32", icon_type="sub")["status"], "fail")

    def test_rejects_missing_rationale_stale_nonfinite_and_outside_bounds(self):
        for edit in ({"rationale": ""}, {"paintedBounds": [14, 4, 18, 27]},
                     {"paintedBounds": [float("nan"), 4, 18, 28]},
                     {"paintedBounds": [-1, 4, 18, 28]}, {"paintedBounds": None}):
            with self.subTest(edit=edit):
                self.assertTrue(validate_optical_bounds(dict(self.check, **edit), (2, 0, 30, 32), self.bounds))

    def test_circle_overflow_remains_failure(self):
        check = dict(self.check, targetToken="circle-32", paintedBounds=[0, 0, 32, 32])
        result = classify_keyfit((0, 0, 32, 32), .01, "circle-32", 2, icon_type="sub", keyfit_check=check)
        self.assertEqual(result["status"], "fail")


class ImageSources(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sources = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.sources.extend(value for key, value in attrs if key == "src")


class OpticalKeyfitReportTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "pack with spaces" / "output" / "divider icon.svg"
        self.source.parent.mkdir(parents=True)
        self.source.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"><path d="M16 6V26"/></svg>')
        self.output = self.root / "pack with spaces" / "qa" / "20260903T000000Z" / "keyshape"
        self.output.mkdir(parents=True)
        self.bounds = [14, 4, 18, 28]
        self.rationale = "Keep the narrow <divider> recognizable & centered."
        self.check = {"mode": "optical", "targetToken": "portrait-28x32", "paintedBounds": self.bounds, "rationale": self.rationale}

    def result(self, optical=True, check=None):
        result = classify_keyfit(tuple(self.bounds), .01, "portrait-28x32", icon_type="sub", keyfit_check=(check or self.check) if optical else None)
        return {"file": self.source.name, "source": str(self.source), "iconType": "sub", "designCanvas": 32,
                "shipCanvas": 16, "viewBox": [0, 0, 16, 16], **result}

    def test_csv_records_fit_mode_and_optical_rationale(self):
        write_csv([self.result(), self.result(optical=False)], self.output)
        with (self.output / "keyfit-results.csv").open(newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(rows[0]["fit_mode"], "optical")
        self.assertEqual(rows[0]["optical_rationale"], self.rationale)
        self.assertEqual(rows[1]["fit_mode"], "exact")
        self.assertEqual(rows[1]["optical_rationale"], "")

    def test_html_distinguishes_accepted_optical_fit_from_exact_edge_requirement(self):
        write_html([self.result()], self.output)
        document = (self.output / "keyfit-report.html").read_text()
        self.assertIn("<strong>Exact mode:</strong>", document)
        self.assertIn("<strong>Optical mode:</strong>", document)
        self.assertIn("Accepted optical fits (1)", document)
        self.assertIn("reaching all four edges is not required", document)
        self.assertIn("Keep the narrow &lt;divider&gt; recognizable &amp; centered.", document)
        self.assertNotIn("Paint must exactly reach and remain inside one centered keyshape", document)
        self.assertNotIn("geometric failure still means the paint fits none", document)

    def test_failed_preview_links_to_real_source_from_timestamped_report_folder(self):
        write_html([self.result(optical=False)], self.output)
        document = (self.output / "keyfit-report.html").read_text()
        parsed = ImageSources()
        parsed.feed(document)
        self.assertEqual(len(parsed.sources), 1)
        self.assertIn("%20", parsed.sources[0])
        source = (self.output / unquote(parsed.sources[0])).resolve()
        self.assertEqual(source, self.source.resolve())
        self.assertTrue(source.is_file())
        self.assertNotIn("../../final/", document)
        self.assertIn("Exact-mode edge adjustment", document)

    def test_failed_optical_report_does_not_instruct_stretching(self):
        stale = dict(self.check, paintedBounds=[14, 4, 18, 27])
        result = self.result(check=stale)
        self.assertEqual(result["status"], "fail")
        write_html([result], self.output)
        document = (self.output / "keyfit-report.html").read_text()
        self.assertIn("Boundary deltas are diagnostic, not an instruction to stretch", document)
        self.assertNotIn("Exact-mode edge adjustment", document)

    def test_grid_card_shows_accepted_optical_rationale_not_edge_expansion(self):
        item = inspect(self.source, "design", "sub")
        item["keyfit"] = self.result()
        item["overallStatus"] = "pass"
        output = self.output.parent / "grid"
        write_report([item], output)
        document = (output / "grid-report.html").read_text()
        self.assertIn("Optical fit inside portrait-28x32: Keep the narrow &lt;divider&gt; recognizable &amp; centered.", document)
        self.assertNotIn("Target portrait-28x32: left +12u", document)
        self.assertIn("exact target or optical containment", document)

    def test_empty_paint_failure_remains_reportable_without_numeric_dimensions(self):
        result = {"file": "empty.svg", "iconType": "sub", "designCanvas": 32,
                  **classify_keyfit(None, .01, "portrait-28x32", icon_type="sub")}
        write_html([result], self.output)
        document = (self.output / "keyfit-report.html").read_text()
        self.assertIn("empty.svg", document)
        self.assertIn("SVG source path unavailable", document)


if __name__ == "__main__":
    unittest.main()
