"""
make_post.py : Create post template from post title, possibly with additional arguments
Defaults:
  • author : dlcguo
  • class : post-template
  • layout : post
  • toc.sidebar : left
"""

import argparse
import re
from datetime import date, datetime
from pathlib import Path
from textwrap import indent

AUTHOR = "dlcguo"

def slugify(title: str) -> str:
    """Convert an arbitrary title into a URL‑safe slug."""
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug) # drop punctuation
    slug = re.sub(r"\s+", "-", slug) # spaces to dashes
    slug = re.sub(r"-+", "-", slug) # collapse consecutive dashes
    return slug.strip("-")

def build_filename(title: str, when) -> Path:
    """Return canonical Jekyll filename in _posts/."""
    if isinstance(when, (datetime, date)):
        when = when.strftime("%Y-%m-%d")
    return Path(f"_posts/{when}-{slugify(title)}.md")

def yaml_list(csv: str) -> str:
    """Turn a comma/space‑separated string into a YAML inline list."""
    items = [s.strip() for s in csv.split(",") if s.strip()]
    return "[" + ", ".join(items) + "]" if items else "[]"

def post_template(
    *,
    title: str,
    layout: str,
    tags: str,
    cover: str,
    cover_preview: str,
    caption: str,
    klass: str,
    author: str,
    toc_sidebar: str,
    giscus: bool,
    description: str,
    date_str: str,
) -> str:
    """Return the complete Markdown document."""
    front_matter = [
        f'title: "{title}"',
        f"layout: {layout}",
        f"tags: {yaml_list(tags)}",
        f"cover: {cover}" if cover else None,
        f"cover_preview: {cover_preview}" if cover_preview else f"cover_preview: {cover}",
        f'caption: "{caption}"' if caption else None,
        f"class: {klass}",
        f"author: {author}",
        "toc:",
        f"  sidebar: {toc_sidebar}",
        f"giscus_comments: {'true' if giscus else 'false'}",
        "description: >",
        indent(description or "<add description here>", "  "),
        f"date: {date_str}",
    ]
    fm_clean = "\n".join(filter(None, front_matter))
    return f"---\n{fm_clean}\n---\n\n<!-- Write your post below -->\n"

"""
example usage:

display_tags: ["academic", "code", "computer science", "general", "machine learning", "reflection", "work"] # this tags will be dispalyed on the front page of your blog

python3 post.py "Compiler Design Course Experience @ CMU" \
  --tags "academic, code, computer science, reflection" \
  --cover assets/img/posts/cmu-compiler-design/pipeline.webp \
  --caption "Example workflow for an end-to-end compiler pipeline" \
  --description "This is a reflection on my experience with the Compiler Design course (15-411) at CMU, including general course thoughts, what I enjoyed the most, and my personal takeaways. For context, 15-411 covers the design and implementation of compiler and runtime systems for high-level languages. Topics include lexical and syntactic analysis, type-checking, program analysis, code generation and optimization, memory management, and runtime organization. The course focuses on developing an end-to-end compiler pipeline for C0 (CMU’s memory-safe C subset)."
"""

def main():
    p = argparse.ArgumentParser(
        description="Create post template from post title, possibly with additional arguments"
    )
    p.add_argument("title", help="Post title (quote if it contains spaces)")
    p.add_argument("--date", help="YYYY-MM-DD (default: today)")
    p.add_argument("--tags", default="", help="Comma/space‑separated list")
    p.add_argument("--cover", default="", help="Cover image filename")
    p.add_argument("--cover-preview", default="", help="Preview image filename")
    p.add_argument("--caption", default="", help="Caption for the cover image")
    p.add_argument("--class", dest="klass", default="post-template",
                   help='YAML “class” (default: "post-template")')
    p.add_argument("--author", default=AUTHOR,
                   help=f'Author name (default: {AUTHOR})')
    p.add_argument("--layout", default="post",
                   help='Layout value (default: "post")')
    p.add_argument("--toc-sidebar", default="left",
                   help='TOC sidebar position (default: "left")')
    p.add_argument("--no-giscus", action="store_true",
                   help="Disable giscus_comments flag")
    p.add_argument("--description", default="", help="Short SEO description")
    args = p.parse_args()

    today = args.date or date.today()
    date_str = today if isinstance(today, str) else today.strftime("%Y-%m-%d")

    path = build_filename(args.title, today)
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        print("Post already exists at", path.resolve())
        return

    content = post_template(
        title=args.title,
        layout=args.layout,
        tags=args.tags,
        cover=args.cover,
        cover_preview=args.cover_preview,
        caption=args.caption,
        klass=args.klass,
        author=args.author,
        toc_sidebar=args.toc_sidebar,
        giscus=not args.no_giscus,
        description=args.description,
        date_str=date_str,
    )

    path.write_text(content, encoding="utf-8")
    print("Post stub created at", path.resolve())

if __name__ == "__main__":
    main()