//! Static SVG safety for uploads — the allowlist half of icon_artwork.py `safe_svg`.
//!
//! Portable vector SVG only: no active content, no remote resources, the profile's viewBox.
//! The Python version also renders the SVG to check it is visible; rendering is graphics
//! processing, which stays on local machines, so that check is not made here.

use quick_xml::events::{BytesStart, Event};
use quick_xml::name::ResolveResult;
use quick_xml::NsReader;
use regex_lite::Regex;
use std::sync::OnceLock;

pub const SVG_NS: &str = "http://www.w3.org/2000/svg";
pub const XLINK_NS: &str = "http://www.w3.org/1999/xlink";
pub const MAX_SVG: usize = 1024 * 1024;
const MAX_NODES: usize = 10000;

const TAGS: &[&str] = &["svg", "g", "path", "rect", "circle", "ellipse", "line", "polyline", "polygon",
    "defs", "clipPath", "mask", "linearGradient", "radialGradient", "stop", "use", "title", "desc", "style"];
const PAINT: &[&str] = &["fill", "fill-rule", "fill-opacity", "stroke", "stroke-width", "stroke-linecap", "stroke-linejoin",
    "stroke-miterlimit", "stroke-dasharray", "stroke-dashoffset", "stroke-opacity", "opacity",
    "clip-path", "clip-rule", "mask", "color", "stop-color", "stop-opacity", "display", "visibility"];
const OTHER_ATTRS: &[&str] = &["id", "class", "d", "points", "transform", "viewBox", "width", "height", "x", "y",
    "x1", "x2", "y1", "y2", "cx", "cy", "r", "rx", "ry", "fx", "fy", "offset",
    "gradientUnits", "gradientTransform", "spreadMethod", "clipPathUnits", "maskUnits",
    "maskContentUnits", "preserveAspectRatio", "version", "vector-effect"];

fn re(cell: &'static OnceLock<Regex>, pattern: &str) -> &'static Regex {
    cell.get_or_init(|| Regex::new(pattern).unwrap())
}

pub fn declares_dtd(text: &str) -> bool {
    static DTD: OnceLock<Regex> = OnceLock::new();
    re(&DTD, r"(?i)<!(DOCTYPE|ENTITY)").is_match(text)
}

fn value_ok(value: &str) -> bool {
    static BAD: OnceLock<Regex> = OnceLock::new();
    static LOCAL_URL: OnceLock<Regex> = OnceLock::new();
    static ACTIVE: OnceLock<Regex> = OnceLock::new();
    if re(&BAD, r"[\\<>]|/\*|@").is_match(value) {
        return false;
    }
    let clean = re(&LOCAL_URL, r#"(?i)url\(\s*['"]?#[a-zA-Z_][\w:.-]*['"]?\s*\)"#).replace_all(value, "");
    !re(&ACTIVE, r"(?i)url\s*\(|expression\s*\(|javascript:|data:|https?:|file:").is_match(&clean)
}

fn declarations(css: &str) -> Result<String, String> {
    let mut pairs = Vec::new();
    for declaration in css.split(';') {
        if declaration.trim().is_empty() {
            continue;
        }
        let (key, value) = declaration.split_once(':')
            .ok_or("Unsupported SVG styling. Export with inline presentation attributes.")?;
        let (key, value) = (key.trim(), value.trim());
        if !PAINT.contains(&key) || !value_ok(value) {
            return Err("Unsupported SVG styling. Export vector paths with fill and stroke styles.".into());
        }
        pairs.push(format!("{key}:{value}"));
    }
    Ok(pairs.join(";"))
}

fn stylesheet(css: &str) -> Result<String, String> {
    static COMMENT: OnceLock<Regex> = OnceLock::new();
    static BLOCK: OnceLock<Regex> = OnceLock::new();
    static SELECTOR: OnceLock<Regex> = OnceLock::new();
    let css = re(&COMMENT, r"(?s)/\*.*?\*/").replace_all(css, "");
    let block = re(&BLOCK, r"([^{}]+)\{([^{}]*)\}");
    if !block.replace_all(&css, "").trim().is_empty() {
        return Err("Unsupported SVG stylesheet. Export with inline styles.".into());
    }
    let mut output = Vec::new();
    for captures in block.captures_iter(&css) {
        let selector = &captures[1];
        if !re(&SELECTOR, r"^[\w.#,\s>+-]+$").is_match(selector) {
            return Err("Unsupported SVG selector. Export with inline styles.".into());
        }
        output.push(format!("{selector}{{{}}}", declarations(&captures[2])?));
    }
    Ok(output.join("\n"))
}

fn escape_attr(value: &str) -> String {
    value.replace('&', "&amp;").replace('<', "&lt;").replace('>', "&gt;").replace('"', "&quot;")
        .replace('\n', "&#10;").replace('\r', "&#13;").replace('\t', "&#09;")
}

fn escape_text(value: &str) -> String {
    value.replace('&', "&amp;").replace('<', "&lt;").replace('>', "&gt;")
}

fn invalid() -> String {
    "This file is not valid SVG.".into()
}

/// Is the document well formed with an `<svg>` root (bare or in the SVG namespace)?
pub fn root_is_svg(text: &str) -> bool {
    let mut reader = NsReader::from_str(text);
    let mut root_ok = None;
    loop {
        match reader.read_resolved_event() {
            Ok((ns, Event::Start(e) | Event::Empty(e))) if root_ok.is_none() => {
                let local = String::from_utf8_lossy(e.local_name().as_ref()).into_owned();
                root_ok = Some(local == "svg" && matches!(ns, ResolveResult::Unbound)
                    || local == "svg" && matches!(ns, ResolveResult::Bound(n) if n.as_ref() == SVG_NS.as_bytes()));
            }
            Ok((_, Event::Eof)) => return root_ok.unwrap_or(false),
            Ok(_) => {}
            Err(_) => return false,
        }
    }
}

/// The element's namespace, copied out of the reader so the reader can be used again.
enum Ns {
    Unbound,
    Bound(String),
    Unknown,
}

fn owned(ns: ResolveResult) -> Ns {
    match ns {
        ResolveResult::Unbound => Ns::Unbound,
        ResolveResult::Bound(n) => Ns::Bound(String::from_utf8_lossy(n.as_ref()).into_owned()),
        ResolveResult::Unknown(_) => Ns::Unknown,
    }
}

struct Attr {
    key: String,
    value: String,
}

/// Accept a portable vector SVG for a `canvas`×`canvas` profile; returns the cleaned document.
pub fn safe_svg(text: &str, canvas: i64) -> Result<String, String> {
    sanitize(text, Some(canvas))
}

/// Like `safe_svg`, for uploads that may use any canvas (Container pairs page): the viewBox and size are
/// kept as drawn, and attributes outside the allowlist are dropped instead of refused. Active content
/// (scripts, `on…` handlers, outside references) is still refused.
pub fn safe_svg_any_canvas(text: &str) -> Result<String, String> {
    sanitize(text, None)
}

fn sanitize(text: &str, canvas: Option<i64>) -> Result<String, String> {
    if text.trim().is_empty() || text.len() > MAX_SVG {
        return Err("Choose an SVG file up to 1 MB.".into());
    }
    if declares_dtd(text) {
        return Err("Export SVG without a DOCTYPE or entity declarations.".into());
    }
    let mut reader = NsReader::from_str(text);
    let mut out = String::new();
    let mut depth = 0usize;
    let mut nodes = 0usize;
    let mut root_seen = false;
    let mut root_done = false;
    let mut uses_xlink = false;
    let mut in_style = 0usize;
    let mut style_text = String::new();
    let mut root_bare = false;
    let mut root_insert_at = 0usize;
    let mut stack: Vec<String> = Vec::new();

    let open = |reader: &NsReader<&[u8]>, ns: Ns, e: &BytesStart, is_root: bool,
                uses_xlink: &mut bool, root_bare: &mut bool| -> Result<(String, Vec<Attr>), String> {
        let local = String::from_utf8_lossy(e.local_name().as_ref()).into_owned();
        let namespaced = match ns {
            Ns::Unbound => false,
            Ns::Bound(n) => {
                if n != SVG_NS {
                    return Err(format!("Unsupported SVG element: {local}. Export text as outlines and use vector shapes."));
                }
                true
            }
            Ns::Unknown => return Err(invalid()),
        };
        if is_root {
            if local != "svg" {
                return Err("Choose an SVG file.".into());
            }
            *root_bare = !namespaced;
        }
        if !TAGS.contains(&local.as_str()) {
            return Err(format!("Unsupported SVG element: {local}. Export text as outlines and use vector shapes."));
        }
        let mut attrs = Vec::new();
        for attribute in e.attributes() {
            let attribute = attribute.map_err(|_| invalid())?;
            let raw_key = String::from_utf8_lossy(attribute.key.as_ref()).into_owned();
            if raw_key == "xmlns" || raw_key.starts_with("xmlns:") {
                continue; // namespace declarations are not attributes
            }
            let value = attribute.decode_and_unescape_value(reader.decoder()).map_err(|_| invalid())?.into_owned();
            let (attr_ns, attr_local) = reader.resolve_attribute(attribute.key);
            let attr_local = String::from_utf8_lossy(attr_local.as_ref()).into_owned();
            let bound = match attr_ns {
                ResolveResult::Unbound => None,
                ResolveResult::Bound(n) => Some(String::from_utf8_lossy(n.as_ref()).into_owned()),
                ResolveResult::Unknown(_) => return Err(invalid()),
            };
            let is_href = attr_local == "href" && (bound.is_none() || bound.as_deref() == Some(XLINK_NS));
            if is_href {
                static HREF: OnceLock<Regex> = OnceLock::new();
                if !re(&HREF, r"^#[a-zA-Z_][\w:.-]*$").is_match(&value) {
                    return Err("SVG references must stay inside this file.".into());
                }
                if bound.is_some() {
                    *uses_xlink = true;
                    attrs.push(Attr { key: "xlink:href".into(), value });
                } else {
                    attrs.push(Attr { key: "href".into(), value });
                }
            } else if bound.is_some() || attr_local.starts_with("data-") || attr_local.starts_with("aria-") {
                // Editor metadata does not affect rendered geometry.
            } else if attr_local == "style" {
                attrs.push(Attr { key: "style".into(), value: declarations(&value)? });
            } else if canvas.is_none() && !attr_local.to_ascii_lowercase().starts_with("on")
                && !(PAINT.contains(&attr_local.as_str()) || OTHER_ATTRS.contains(&attr_local.as_str())) {
                // Any-canvas uploads: an unknown attribute (role, …) is dropped.
            } else if !(PAINT.contains(&attr_local.as_str()) || OTHER_ATTRS.contains(&attr_local.as_str())) || !value_ok(&value) {
                return Err(format!("Unsupported SVG attribute: {attr_local}. Export a static vector SVG."));
            } else {
                attrs.push(Attr { key: attr_local, value });
            }
        }
        Ok((local, attrs))
    };

    let write_start = |out: &mut String, tag: &str, attrs: &[Attr], empty: bool| {
        out.push('<');
        out.push_str(tag);
        for attr in attrs {
            out.push_str(&format!(" {}=\"{}\"", attr.key, escape_attr(&attr.value)));
        }
        out.push_str(if empty { " />" } else { ">" });
    };

    loop {
        let (ns, event) = reader.read_resolved_event().map_err(|_| invalid())?;
        let ns = owned(ns);
        let event = event.into_owned();
        match event {
            Event::Start(ref e) | Event::Empty(ref e) => {
                if root_done {
                    return Err(invalid());
                }
                nodes += 1;
                if nodes > MAX_NODES {
                    return Err("SVG is too complex; simplify it before uploading.".into());
                }
                let is_root = !root_seen;
                root_seen = true;
                let empty = matches!(event, Event::Empty(_));
                let (tag, mut attrs) = open(&reader, ns, e, is_root, &mut uses_xlink, &mut root_bare)?;
                if let (true, Some(canvas)) = (is_root, canvas) {
                    let view: Option<Vec<f64>> = attrs.iter().find(|a| a.key == "viewBox").map(|a| {
                        a.value.trim().split(|c: char| c.is_whitespace() || c == ',').filter(|p| !p.is_empty())
                            .map(|p| p.parse::<f64>()).collect::<Result<Vec<_>, _>>().unwrap_or_default()
                    });
                    let c = canvas as f64;
                    if view.unwrap_or_default() != vec![0.0, 0.0, c, c] {
                        return Err(format!("Export with a 0 0 {canvas} {canvas} viewBox to keep the icon on its profile canvas."));
                    }
                    for (key, value) in [("width", canvas.to_string()), ("height", canvas.to_string())] {
                        match attrs.iter_mut().find(|a| a.key == key) {
                            Some(attr) => attr.value = value,
                            None => attrs.push(Attr { key: key.into(), value }),
                        }
                    }
                }
                if tag == "style" && !empty {
                    in_style += 1;
                    style_text.clear();
                }
                write_start(&mut out, &tag, &attrs, empty);
                if is_root {
                    root_insert_at = out.find([' ', '>', '/']).unwrap_or(out.len());
                }
                if empty {
                    if depth == 0 {
                        root_done = true;
                    }
                } else {
                    depth += 1;
                    stack.push(tag);
                }
            }
            Event::End(_) => {
                let tag = stack.pop().ok_or_else(invalid)?;
                if tag == "style" && in_style > 0 {
                    in_style -= 1;
                    out.push_str(&escape_text(&stylesheet(&style_text)?));
                }
                out.push_str(&format!("</{tag}>"));
                depth -= 1;
                if depth == 0 {
                    root_done = true;
                }
            }
            Event::Text(t) => {
                let text = t.decode().map_err(|_| invalid())?.into_owned();
                let text = quick_xml::escape::unescape(&text).map_err(|_| invalid())?.into_owned();
                if in_style > 0 {
                    style_text.push_str(&text);
                } else if depth > 0 {
                    out.push_str(&escape_text(&text));
                } else if !text.trim().is_empty() {
                    return Err(invalid());
                }
            }
            Event::GeneralRef(r) => {
                let name = r.decode().map_err(|_| invalid())?.into_owned();
                let resolved = match name.as_str() {
                    "amp" => "&".to_string(), "lt" => "<".into(), "gt" => ">".into(), "quot" => "\"".into(), "apos" => "'".into(),
                    other => match other.strip_prefix('#') {
                        Some(num) => {
                            let code = match num.strip_prefix('x') {
                                Some(hex) => u32::from_str_radix(hex, 16).ok(),
                                None => num.parse::<u32>().ok(),
                            };
                            code.and_then(char::from_u32).map(String::from).ok_or_else(invalid)?
                        }
                        None => return Err(invalid()),
                    },
                };
                if in_style > 0 { style_text.push_str(&resolved) } else if depth > 0 { out.push_str(&escape_text(&resolved)) }
            }
            Event::CData(t) => {
                let text = String::from_utf8_lossy(t.as_ref()).into_owned();
                if in_style > 0 { style_text.push_str(&text) } else if depth > 0 { out.push_str(&escape_text(&text)) }
            }
            Event::Comment(_) | Event::PI(_) | Event::Decl(_) => {}
            Event::DocType(_) => return Err("Export SVG without a DOCTYPE or entity declarations.".into()),
            Event::Eof => break,
        }
    }
    if !root_seen || depth != 0 {
        return Err(invalid());
    }
    let mut declarations = format!(" xmlns=\"{SVG_NS}\"");
    if uses_xlink {
        declarations.push_str(&format!(" xmlns:xlink=\"{XLINK_NS}\""));
    }
    let _ = root_bare; // bare and namespaced roots both get the SVG namespace, as Python does
    out.insert_str(root_insert_at, &declarations);
    out.push('\n');
    Ok(out)
}

#[cfg(test)]
mod tests {
    use super::*;

    const OK: &str = r##"<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" viewBox="0 0 48 48" width="96" inkscape:label="x" data-name="y"><!-- note --><path d="M4 4L44 44" stroke="currentColor" style="stroke-width: 4; fill:none"/></svg>"##;

    #[test]
    fn cleans_editor_metadata() {
        let out = safe_svg(OK, 48).unwrap();
        assert_eq!(out, "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 48 48\" width=\"48\" height=\"48\"><path d=\"M4 4L44 44\" stroke=\"currentColor\" style=\"stroke-width:4;fill:none\" /></svg>\n");
    }

    #[test]
    fn bare_svg_gets_namespace() {
        let out = safe_svg(r#"<svg viewBox="0,0,32,32"><circle cx="16" cy="16" r="8"/></svg>"#, 32).unwrap();
        assert!(out.starts_with("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox="));
    }

    #[test]
    fn refuses_active_or_remote_content() {
        let cases = [
            (r#"<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><script/></svg>"#, "Unsupported SVG element: script"),
            (r#"<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path onclick="x()"/></svg>"#, "Unsupported SVG attribute: onclick"),
            (r#"<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="url(https://x/y)"/></svg>"#, "Unsupported SVG attribute: fill"),
            (r#"<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><use href="https://x/#a"/></svg>"#, "SVG references must stay inside this file."),
            (r#"<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"/>"#, "viewBox"),
            (r#"<!DOCTYPE svg><svg/>"#, "DOCTYPE"),
            (r#"<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><style>@import url(x);</style></svg>"#, "stylesheet"),
            (r#"<html/>"#, "Choose an SVG file."),
            (r#"<svg"#, "not valid SVG"),
        ];
        for (input, expected) in cases {
            let error = safe_svg(input, 48).unwrap_err();
            assert!(error.contains(expected), "{input}: {error}");
        }
    }

    #[test]
    fn keeps_local_references_and_styles() {
        let input = r##"<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 48 48"><style>.a { fill: url(#g) }</style><defs><linearGradient id="g"/></defs><use xlink:href="#p" class="a"/></svg>"##;
        let out = safe_svg(input, 48).unwrap();
        assert!(out.contains("xmlns:xlink=\"http://www.w3.org/1999/xlink\""));
        assert!(out.contains("<use xlink:href=\"#p\" class=\"a\" />"));
        assert!(out.contains(".a {fill:url(#g)}"));
    }

    #[test]
    fn any_canvas_keeps_the_drawing_and_drops_unknown_attributes() {
        let input = r##"<svg xmlns="http://www.w3.org/2000/svg" width="34" height="24" viewBox="0 0 34 24" role="img" aria-label="DXF"><title>DXF</title><path d="M2 2L8 22" stroke="#202820" stroke-width="4"/></svg>"##;
        assert!(safe_svg(input, 32).unwrap_err().contains("Unsupported SVG attribute: role"));
        let out = safe_svg_any_canvas(input).unwrap();
        assert!(out.contains("viewBox=\"0 0 34 24\"") && out.contains("width=\"34\"") && !out.contains("role"));
        for bad in [r#"<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path onclick="x()"/></svg>"#,
                    r#"<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><script/></svg>"#,
                    r#"<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path fill="url(https://x/y)"/></svg>"#] {
            assert!(safe_svg_any_canvas(bad).is_err(), "{bad}");
        }
    }
}
