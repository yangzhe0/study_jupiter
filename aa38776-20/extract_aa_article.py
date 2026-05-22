from pathlib import Path
import re

from bs4 import BeautifulSoup, NavigableString, Tag


SOURCE = Path("aa38776-20.html")
OUT_MD = Path("aa38776-20_ai_readable.md")
OUT_TXT = Path("aa38776-20_ai_readable.txt")


def clean_space(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def node_text(node) -> str:
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""

    latex = node.get("data-latex")
    if latex:
        return f" {latex} "

    if node.name in {"script", "style", "noscript", "svg", "button"}:
        return ""

    parts = []
    for child in node.children:
        parts.append(node_text(child))
    return clean_space(" ".join(p for p in parts if p))


def table_to_md(table: Tag) -> str:
    rows = []
    for tr in table.find_all("tr"):
        cells = [clean_space(node_text(cell)).replace("|", "\\|") for cell in tr.find_all(["th", "td"], recursive=False)]
        if cells:
            rows.append(cells)
    if not rows:
        return ""

    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    header = rows[0]
    sep = ["---"] * width
    body = rows[1:]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(sep) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in body)
    return "\n".join(lines)


def convert(article: Tag, soup: BeautifulSoup) -> str:
    for bad in article.select("script, style, noscript, .social, .metrics, .article-tools, .also-read, .separator, .summary.full, #bloc"):
        bad.decompose()

    lines = []
    seen_tables = set()

    meta_title = soup.select_one('meta[name="citation_title"]')
    title = clean_space(meta_title.get("content", "")) if meta_title else ""
    if not title:
        title = clean_space(node_text(article.select_one("h1") or article.select_one(".article-title")))
    if title:
        lines.append(f"# {title}")

    doi = soup.select_one('meta[name="citation_doi"]')
    date = soup.select_one('meta[name="citation_publication_date"]')
    journal = soup.select_one('meta[name="citation_journal_title"]')
    metadata = []
    if journal:
        metadata.append(f"Journal: {journal.get('content', '')}")
    if date:
        metadata.append(f"Published: {date.get('content', '')}")
    if doi:
        metadata.append(f"DOI: https://doi.org/{doi.get('content', '')}")
    if metadata:
        lines.append("\n".join(metadata))

    for el in article.descendants:
        if not isinstance(el, Tag):
            continue
        if el.find_parent("table") and el.name != "table":
            continue

        if el.name in {"h1", "h2", "h3", "h4"}:
            text = clean_space(node_text(el))
            if text and text != title:
                level = {"h1": 1, "h2": 2, "h3": 3, "h4": 4}[el.name]
                lines.append(f"\n{'#' * level} {text}\n")
        elif el.name == "p":
            cls = " ".join(el.get("class", []))
            text = clean_space(node_text(el))
            if not text:
                continue
            if cls == "bold" or text in {"Abstract", "Acknowledgments", "References", "List of tables", "List of figures"}:
                lines.append(f"\n## {text}\n")
            else:
                lines.append(text)
        elif el.name in {"ul", "ol"} and not el.find_parent(["ul", "ol"]):
            items = []
            for li in el.find_all("li", recursive=False):
                text = clean_space(node_text(li))
                if text:
                    items.append(f"- {text}")
            if items:
                lines.append("\n".join(items))
        elif el.name == "table" and id(el) not in seen_tables:
            seen_tables.add(id(el))
            md_table = table_to_md(el)
            if md_table:
                lines.append(md_table)
        elif el.name == "div":
            cls = " ".join(el.get("class", []))
            if "caption" in cls or "figcaption" in cls:
                text = clean_space(node_text(el))
                if text:
                    lines.append(f"\n{text}\n")

    text = "\n\n".join(line for line in lines if clean_space(line))
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main() -> None:
    html = SOURCE.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")
    article = soup.select_one("div.article-content")
    if article is None:
        raise SystemExit("Could not find div.article-content")

    md = convert(article, soup)
    OUT_MD.write_text(md, encoding="utf-8")
    plain = re.sub(r"^#{1,6} ", "", md, flags=re.MULTILINE)
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", plain)
    OUT_TXT.write_text(plain, encoding="utf-8")
    print(f"Wrote {OUT_MD} ({len(md)} chars)")
    print(f"Wrote {OUT_TXT} ({len(plain)} chars)")


if __name__ == "__main__":
    main()
