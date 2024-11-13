import { globSync } from "glob";
import { readFileSync } from "node:fs";
import { extname } from "node:path";
import { getFrontmatter } from "myst-transforms";

const blogPostsDirective = {
  name: "blog-posts",
  doc: "Display preview cards for documents.",
  options: {
    limit: { type: Number, doc: "Number of posts." },
  },
  run(data, vfile, ctx) {
    const size = data.options.limit ?? 3;
    const paths = globSync("posts/*.md").sort(); // For now, string sort
    const nodes = paths.map((path) => {
      const ext = extname(path);
      const content = readFileSync(path, { encoding: "utf-8" });
      const ast = ctx.parseMyst(content);
      const frontmatter = getFrontmatter(vfile, ast).frontmatter;
      const descriptionItems = frontmatter.description
        ? ctx.parseMyst(frontmatter.description).children
        : [];
      const subtitleItems = frontmatter.subtitle
        ? ctx.parseMyst(frontmatter.subtitle).children
        : [];
      const footerItems = frontmatter.date
        ? [
            {
              type: "footer",
              children: [
                {
                  type: "paragraph",
                  children: [
                    {
                      type: "text",
                      value: `Date: ${frontmatter.date}`,
                    },
                  ],
                },
              ],
            },
          ]
        : [];
      return {
        type: "card",
        children: [
          {
            type: "cardTitle",
            children: ctx.parseMyst(frontmatter.title).children,
          },
          ...subtitleItems,
          ...descriptionItems,
          ...footerItems,
        ],
        url: `/${path.toString().slice(0, -ext.length)}`,
      };
    });
    return Array.from(nodes).slice(0, size);
  },
};

const plugin = { name: "Blog posts", directives: [blogPostsDirective] };

export default plugin;
