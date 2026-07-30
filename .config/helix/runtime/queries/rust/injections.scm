;; extends

(
  [
    (line_comment)
    (block_comment)
  ] @_comment
  (#match? @_comment "[Hh][Tt][Mm][Ll]")
  .
  [
    (string_literal (string_content) @injection.content)
    (raw_string_literal (string_content) @injection.content)
  ]
  (#set! injection.language "html")
)

(macro_invocation
  (scoped_identifier
    path: (identifier) @path (#eq? @path "sqlx")
    name: (identifier) @name (#eq? @name "query"))
  (token_tree
    (raw_string_literal
        (string_content) @injection.content))
  (#set! injection.language "sql")
)
