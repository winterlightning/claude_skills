//! Pure rules of the Pictographic review server, shared by the Cloudflare Worker.
//!
//! Nothing here touches Cloudflare bindings: routes load rows from D1, call these
//! functions, and write the result. Each module names the Python file it was ported from.

pub mod briefs;
pub mod catalog;
pub mod combined_parts;
pub mod icon_index;
pub mod icon_query;
pub mod primitives;
pub mod query;
pub mod refimg;
pub mod reviews;
pub mod stats;
pub mod svg;
pub mod time;
pub mod work;
