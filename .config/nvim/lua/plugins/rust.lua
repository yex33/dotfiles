vim.g.rustaceanvim = {
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
}
return {
  -- {
  --   "rayliwell/tree-sitter-rstml",
  --   dependencies = { "nvim-treesitter/nvim-treesitter" },
  --   build = ":TSInstall rust_with_rstml",
  --   opts = {},
  -- },
  {
    "windwp/nvim-ts-autotag",
    opts = {
      aliases = {
        ["rust"] = "html",
      },
    },
  },
}
