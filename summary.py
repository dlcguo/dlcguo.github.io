import argparse
from datetime import date
import pathlib
import re

from arxiv2bib import arxiv2bib

def retrieve_arxiv_bib(arxiv_id: str):
    print(f"[info] querying arXiv for {arxiv_id}")
    return arxiv2bib([arxiv_id])[0]


def clean_title(title: str) -> str:
    print(f"[info] raw title: {title!r}")
    title = title.strip().replace("\n", "")
    title = re.sub(" +", " ", title)
    print(f"[info] cleaned title: {title!r}")
    return title


def filename(title: str) -> str:
    today = date.today()
    fn = (
        title.lower()
             .replace(" ", "-")
             .replace(",", "")
             .replace(":", "")
             .strip()
    )
    fn = re.sub("-+", "-", fn)
    fn = "".join(ch for ch in fn if ch.isalnum() or ch == "-")
    path = f"_summaries/{today}-{fn}.markdown"
    print(f"[info] will write markdown to {path}")
    return path


def eprint_without_version(eprint: str) -> str:
    return re.sub(r"v\d+$", "", eprint)


def template(title: str, bib_id: str) -> str:
    return f"""---\nlayout: summary\ntitle: "{title}"\ngiscus_comments: true\nbib_id: {bib_id}\n---\n

### Important Points

#### 1. Foo

#### 2. Bar

#### 3. Baz

### Critique

### Concluding Thoughts
"""

def create_summary_template(title: str, bib_id: str):
    path = filename(title)
    path = pathlib.Path(path)

    if path.exists():
        print("[ok]   summary file already exists at:", path.resolve())
        return False
    
    with open(path, "w") as f:
        f.write(template(title, bib_id))
    print(f"[ok]   markdown stub created: {path}")
    return True


def update_summary_bib(bibtex: str, eprint: str):
    print("[info] appending entry to _bibliography/summaries.bib")  ### NEW
    bibtex = bibtex.rstrip()

    if bibtex.endswith("}"):
        bibtex = bibtex[:-1].rstrip()

    bibtex += f",\nEprintNoVer = {{{eprint_without_version(eprint)}}}\n}}\n"

    with open("_bibliography/summaries.bib", "a") as f:
        f.write("\n" + bibtex)
def main():
    parser = argparse.ArgumentParser(
        description="Create summary template from an arXiv ID or manual title")
    parser.add_argument("--arxiv_id", type=str,
                        help="arXiv article ID (e.g. 2405.12345)", required=False)
    parser.add_argument("--title", help="Paper title (manual mode)", required=False)
    parser.add_argument("--bib-id", help="BibTeX key (manual mode)", required=False)
    args = parser.parse_args()

    if args.title:
        # manual mode — only produce markdown
        if not args.bib_id:
            parser.error("--bib-id is required when --title is given")
        print("[mode] manual")
        create_summary_template(args.title, args.bib_id)
    else:
        # arXiv mode
        if not args.arxiv_id:
            parser.error("either --arxiv_id or --title is required")
        print("[mode] arXiv auto-fetch")
        bib = retrieve_arxiv_bib(args.arxiv_id)
        title   = clean_title(bib.title)
        bib_id  = bib.id
        if create_summary_template(title, bib_id):
            update_summary_bib(bib.bibtex(), bib_id)

"""
$ python summary.py --arxiv_id 2506.05348
[mode] arXiv auto-fetch
[info] querying arXiv for 2405.12345...
[info] raw title: 'Deep Gaussian Splatting for Radiance Fields'
[info] cleaned title: 'Deep Gaussian Splatting for Radiance Fields'
[info] will write markdown to _summaries/2025-05-30-deep-gaussian-splatting-for-radiance-fields.markdown
[ok]   markdown stub created: _summaries/2025-05-30-deep-gaussian-splatting-for-radiance-fields.markdown
[info] appending entry to _bibliography/summaries.bib
[ok]   BibTeX appended
"""

if __name__ == "__main__":
    main()