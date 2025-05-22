# 🧙‍♂️ Static Site Walkthrough

A fully custom static site generator built with Python. This project reads content written in Markdown and converts it into a complete HTML website — no frameworks, no CMS, just pure code and static files.

Deployed via GitHub Pages:  
🌐 [https://mannyzzle.github.io/Static-Site-Walkthrough/](https://mannyzzle.github.io/Static-Site-Walkthrough/)

---

## 💡 What Is a Static Site Generator?

A **static site generator (SSG)** takes source content (like Markdown files) and applies a template to generate HTML files. The result is a fast, secure, and scalable website that can be served directly without a backend server or database.

SSGs are ideal for blogs, documentation, portfolios, and landing pages where content changes infrequently.

---

## ⚙️ How This Generator Works

1. **Reads Markdown files** from the `content/` directory, including deeply nested paths (like `content/blog/post/index.md`).
2. **Parses the Markdown** to identify headings, paragraphs, code blocks, blockquotes, bold/italic text, links, and images.
3. **Wraps content in HTML** using a single reusable template (`template.html`) and dynamically inserts titles and page content.
4. **Copies static assets** (images, CSS, etc.) from the `static/` folder into the final build directory.
5. **Supports base path injection**, which adjusts all internal `href` and `src` paths to work correctly on GitHub Pages or other subdirectory deployments.
6. **Outputs everything into the `docs/` folder**, ready to be deployed with GitHub Pages.

---

## 🔧 Features

- ✅ Parses Markdown and converts it to clean HTML
- ✅ Preserves folder structure for nested content
- ✅ Handles headings, bold/italic, blockquotes, lists, and code blocks
- ✅ Supports inline images and links
- ✅ Uses a consistent HTML template across pages
- ✅ Rewrites relative links and image sources for public deployment
- ✅ Easily deployable with GitHub Pages

---

## 🗂 Directory Structure

```
.
├── content/             # All Markdown content (e.g. blog posts, pages)
│   ├── index.md
│   └── blog/
│       └── glorfindel/index.md
├── static/              # Static files like CSS and images
│   └── images/
├── docs/                # Auto-generated output site (GitHub Pages reads from here)
├── src/                 # Python source files
│   ├── main.py
│   ├── page_generator.py
│   ├── markdown_renderer.py
│   └── ...
├── template.html        # HTML template used for every page
├── build.sh             # Script to build the site for production
└── README.md
```

---

## 🧪 Local Development

To build and preview the site locally:

```bash
python3 src/main.py
python3 -m http.server --directory docs 8888
```

Then open your browser to [http://localhost:8888](http://localhost:8888)

---

## 🚀 Deployment (GitHub Pages)

GitHub Pages requires all site files to live in the `docs/` folder of the `main` branch.

To build the site for deployment:

```bash
./build.sh
```

This script runs:

```bash
python3 src/main.py "/Static-Site-Walkthrough/"
```

The trailing `/Static-Site-Walkthrough/` base path ensures all internal links work on the public URL:  
📍 [https://mannyzzle.github.io/Static-Site-Walkthrough/](https://mannyzzle.github.io/Static-Site-Walkthrough/)

Then commit and push the `docs/` folder:

```bash
git add .
git commit -m "Deploy site"
git push
```

Make sure GitHub Pages is enabled under **Settings > Pages**, with source set to `main` and folder `docs/`.

---

## 💬 Markdown Syntax Supported

```markdown
# Heading

Some **bold** text, some _italic_ text, and `inline code`.

> This is a blockquote.

- List item 1
- List item 2

```python
# Code block
print("Hello, world!")
```

![Alt text](/images/example.png)

[Link text](https://example.com)
```

---

## 📁 Example Pages

- `/` – Homepage
- `/blog/glorfindel/` – A deep-dive into Glorfindel’s lore
- `/blog/tom/` – Why Tom Bombadil was (maybe) a mistake
- `/contact/` – Contact info and closing message

---

## 🪪 License

MIT License — feel free to reuse, remix, and deploy your own version of this generator.
