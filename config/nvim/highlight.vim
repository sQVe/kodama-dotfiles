"  ╻ ╻╻┏━╸╻ ╻╻  ╻┏━╸╻ ╻╺┳╸
"  ┣━┫┃┃╺┓┣━┫┃  ┃┃╺┓┣━┫ ┃
"  ╹ ╹╹┗━┛╹ ╹┗━╸╹┗━┛╹ ╹ ╹

" Ale.
hi! ALEError guifg=NONE guibg=NONE guisp=#fb4934 gui=underline cterm=underline
hi! ALEErrorSign guifg=#fb4934 guibg=NONE gui=NONE cterm=NONE
hi! ALEInfo guifg=NONE guibg=NONE guisp=#83a598 gui=underline cterm=underline
hi! ALEInfoSign guifg=#83a598 guibg=NONE gui=NONE cterm=NONE
hi! ALEVirtualTextError guifg=#fb4934 guibg=#3c3836 gui=NONE cterm=NONE
hi! ALEVirtualTextInfo guifg=#83a598 guibg=#3c3836 gui=NONE cterm=NONE
hi! ALEVirtualTextWarning guifg=#fabd2f guibg=#3c3836 gui=NONE cterm=NONE
hi! ALEWarning guifg=NONE guibg=NONE guisp=#fb4934 gui=underline cterm=underline
hi! ALEWarningSign guifg=#fabd2f guibg=NONE gui=NONE cterm=NONE

" Better Whitespace.
hi! ExtraWhitespace guifg=#282828 guibg=#cc241d gui=NONE cterm=NONE

" BufTabLine.
hi! BufTabLineActive guifg=#a89984 guibg=#282828 gui=NONE cterm=NONE
hi! BufTabLineCurrent guifg=#fabd2f guibg=#3c3836 gui=NONE cterm=NONE
hi! BufTabLineFill guifg=#282828 guibg=#282828 gui=NONE cterm=NONE
hi! BufTabLineHidden guifg=#7c6f64 guibg=#282828 gui=NONE cterm=NONE

" Columns.
hi! ColorColumn guifg=NONE guibg=#282828 gui=NONE cterm=NONE
hi! SignColumn guifg=NONE guibg=#282828 gui=NONE cterm=NONE

" Coc.
hi! CocCodeLens guifg=#504945 guibg=NONE gui=NONE cterm=NONE
hi! CocErrorFloat guifg=#fb4934 guibg=NONE gui=NONE cterm=NONE
hi! CocErrorSign guifg=#fb4934 guibg=#282828 gui=NONE cterm=NONE
hi! CocHintFloat guifg=#d3869b guibg=NONE gui=NONE cterm=NONE
hi! CocHintSign guifg=#504945 guibg=NONE gui=NONE cterm=NONE
hi! CocInfoFloat guifg=#83a598 guibg=NONE gui=NONE cterm=NONE
hi! CocInfoSign guifg=#83a598 guibg=NONE gui=NONE cterm=NONE
hi! CocSelectedText guifg=#3c3836 guibg=#282828 gui=NONE cterm=NONE
hi! CocWarningFloat guifg=#fabd2f guibg=NONE gui=NONE cterm=NONE
hi! CocWarningSign guifg=#fabd2f guibg=#282828 gui=NONE cterm=NONE

" Git diff signs.
hi! DiffAdd guifg=#b8bb26 guibg=NONE gui=NONE cterm=NONE
hi! DiffChange guifg=#8ec07c guibg=NONE gui=NONE cterm=NONE
hi! DiffDelete guifg=#fb4934 guibg=NONE gui=NONE cterm=NONE
hi! DiffChangeDelete guifg=#8ec07c guibg=NONE gui=NONE cterm=NONE

" Lightline colorscheme.
let s:p = {'normal':{}, 'inactive':{}, 'insert':{}, 'replace':{}, 'visual':{}, 'tabline':{}, 'terminal':{}}
let s:p.normal.left = [ [ '#282828', '#a89984', 'bold' ], [ '#a89984', '#504945' ] ]
let s:p.normal.right = [ [ '#282828', '#a89984' ], [ '#a89984', '#504945' ] ]
let s:p.normal.middle = [ [ '#a89984', '#3c3836' ] ]
let s:p.inactive.right = [ [ '#7c6f64', '#3c3836' ], [ '#7c6f64', '#3c3836' ] ]
let s:p.inactive.left =  [ [ '#7c6f64', '#3c3836' ], [ '#7c6f64', '#3c3836' ] ]
let s:p.inactive.middle = [ [ '#7c6f64', '#3c3836' ] ]
let s:p.insert.left = [ [ '#282828', '#b8bb26', 'bold' ], [ '#ebdbb2', '#504945' ] ]
let s:p.insert.right = [ [ '#282828', '#83a598' ], [ '#ebdbb2', '#504945' ] ]
let s:p.insert.middle = [ [ '#a89984', '#3c3836' ] ]
let s:p.terminal.left = [ [ '#282828', '#b8bb26', 'bold' ], [ '#ebdbb2', '#504945' ] ]
let s:p.terminal.right = [ [ '#282828', '#b8bb26' ], [ '#ebdbb2', '#504945' ] ]
let s:p.terminal.middle = [ [ '#a89984', '#3c3836' ] ]
let s:p.replace.left = [ [ '#282828', '#cc241d', 'bold' ], [ '#ebdbb2', '#504945' ] ]
let s:p.replace.right = [ [ '#282828', '#8ec07c' ], [ '#ebdbb2', '#504945' ] ]
let s:p.replace.middle = [ [ '#a89984', '#3c3836' ] ]
let s:p.visual.left = [ [ '#282828', '#fe8019', 'bold' ], [ '#282828', '#7c6f64' ] ]
let s:p.visual.right = [ [ '#282828', '#fe8019' ], [ '#282828', '#7c6f64' ] ]
let s:p.visual.middle = [ [ '#a89984', '#3c3836' ] ]
let s:p.tabline.left = [ [ '#a89984', '#504945' ] ]
let s:p.tabline.tabsel = [ [ '#282828', '#a89984' ] ]
let s:p.tabline.middle = [ [ '#282828', '#7c6f64' ] ]
let s:p.tabline.right = [ [ '#282828', '#fe8019' ] ]
let s:p.normal.error = [ [ '#282828', '#fb4934' ] ]
let s:p.normal.warning = [ [ '#282828', '#fabd2f' ] ]
let g:lightline#colorscheme#gruvbox8#palette = lightline#colorscheme#fill(s:p)

" Startify.
hi! StartifyBracket guifg=#bdae93 guibg=NONE gui=NONE cterm=NONE
hi! StartifyFile guifg=#ebdbb2 guibg=NONE gui=NONE cterm=NONE
hi! StartifyFooter guifg=#504945 guibg=NONE gui=NONE cterm=NONE
hi! StartifyHeader guifg=#fe8019 guibg=NONE gui=NONE cterm=NONE
hi! StartifyNumber guifg=#83a598 guibg=NONE gui=NONE cterm=NONE
hi! StartifyPath guifg=#928374 guibg=NONE gui=NONE cterm=NONE
hi! StartifySection guifg=#fabd2f guibg=NONE gui=NONE cterm=NONE
hi! StartifySlash guifg=#928374 guibg=NONE gui=NONE cterm=NONE
hi! StartifySpecial guifg=#504945 guibg=NONE gui=NONE cterm=NONE

" Turn of italics for strings.
hi! String gui=NONE cterm=NONE
