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
