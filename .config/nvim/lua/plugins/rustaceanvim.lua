return {
  "mrcjkb/rustaceanvim",
  opts = {
    server = {
      settings = {
        ["rust-analyzer"] = {
          semanticHighlighting = {
            strings = {
              enable = false,
            },
          },
        },
      },
    },
  },
}
