import os, glob, datetime
from notion_client import Client

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
NOTION_DB    = os.environ["NOTION_DB"]
TITLE_PROP   = os.environ.get("TITLE_PROP", "名称")
UPDATED_PROP = os.environ.get("UPDATED_PROP", "最近更新")

notion = Client(auth=NOTION_TOKEN)

def find_page_by_title(title: str):
    res = notion.databases.query(
        database_id=NOTION_DB,
        filter={"property": TITLE_PROP, "title": {"equals": title}},
        page_size=1,
    )
    rs = res.get("results", [])
    return rs[0] if rs else None

def upsert_note(path: str):
    title = os.path.splitext(os.path.basename(path))[0]
    with open(path, "r", encoding="utf-8") as f:
        md = f.read()

    props = {TITLE_PROP: [{"type": "text", "text": {"content": title}}]}
    if UPDATED_PROP:
        props[UPDATED_PROP] = {"date": {"start": datetime.datetime.utcnow().isoformat()}}

    paragraph = {
        "object": "block",
        "type": "paragraph",
        "paragraph": {"rich_text": [{"type": "text", "text": {"content": md[:1900]}}]},
    }

    page = find_page_by_title(title)
    if page:
        notion.blocks.children.append(page["id"], children=[paragraph])  # type: ignore
        notion.pages.update(page_id=page["id"], properties=props)        # type: ignore
        print(f"Updated: {title}")
    else:
        notion.pages.create(
            parent={"database_id": NOTION_DB},
            properties=props,
            children=[paragraph],
        )
        print(f"Created: {title}")

def main():
    files = glob.glob("obs/sora2/**/*.md", recursive=True)
    if not files:
        print("No markdown files found under obs/sora2/")
    for p in files:
        upsert_note(p)

if __name__ == "__main__":
    main()
