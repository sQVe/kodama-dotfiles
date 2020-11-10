"  ┏━┓╻  ╻ ╻┏━╸╻┏┓╻┏━┓
"  ┣━┛┃  ┃ ┃┃╺┓┃┃┗┫┗━┓
"  ╹  ┗━╸┗━┛┗━┛╹╹ ╹┗━┛

" ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
" ¤¤¤¤  Import plugins  ¤¤¤¤
" ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤

" Disable whole language pack.
"  - graphql: indention issues.
let s:lang_disable = [
  \ 'graphql',
  \ ]

" Disable language syntax already handled by treesitter.
let s:lang_syntax_disable = [
  \ 'css.plugin',
  \ 'html.plugin',
  \ 'javascript.plugin',
  \ 'json.plugin',
  \ 'jsx.plugin',
  \ 'sh.plugin',
  \ 'typescript.plugin',
  \ 'yaml.plugin',
  \ ]

let g:polyglot_disabled = s:lang_disable + s:lang_syntax_disable

call plug#begin('$HOME/.local/share/nvim/plugged')

" Align, surround and repeat.
Plug 'junegunn/vim-easy-align'                     " Alignment.
Plug 'machakann/vim-sandwich'                      " Surround text.
Plug 'tpope/vim-repeat'                            " Repeat for plugins.

" Colorschemes and highlighting.
Plug 'lifepillar/vim-gruvbox8'                     " Speedy Gruvbox.
Plug 'nvim-treesitter/nvim-treesitter'             " Treesitter highlighting.

" Commands.
Plug 'moll/vim-bbye'                               " Delete buffers without closing window.
Plug 'tpope/vim-eunuch'                            " Unix helpers.

" Comments and documentation.
Plug 'kkoomen/vim-doge'                            " Generate documentation.
Plug 'tpope/vim-commentary'                        " Comment text.

" Completion, diagnostics and spelling.
Plug 'dense-analysis/ale'                          " Lint and fix files.
Plug 'neoclide/coc.nvim', {
  \ 'do': 'yarn install --frozen-lockfile' }       " Intellisense with LSP.
Plug 'rhysd/vim-grammarous'                        " Grammary check with languagetool.

" Debug.
Plug 'dstein64/vim-startuptime'                    " Check startup times.

" Integration.
Plug 'airblade/vim-rooter'                         " Set pwd to root directory.
Plug 'editorconfig/editorconfig-vim'               " Editorconfig.
Plug 'iamcco/markdown-preview.nvim', {
  \ 'do': 'cd app & yarn install' }                " Markdown preview.
Plug 'sickill/vim-pasta'                           " Paste with smart indentation.
Plug 'tpope/vim-fugitive'                          " Git.
Plug 'tpope/vim-rhubarb'                           " Use hub instead of git.
Plug 'tpope/vim-speeddating'                       " Increment / decrement dates, times and more.

" Interface.
Plug 'ap/vim-buftabline'                           " Buffer line.
Plug 'camspiers/lens.vim'                          " Resize windows based on content.
Plug 'itchyny/lightline.vim'                       " Status line.
Plug 'maximbaz/lightline-ale'                      " Lint information in status line.
Plug 'mhinz/vim-startify'                          " Launch screen.
Plug 'ntpeters/vim-better-whitespace'              " Highlight trailing whitespace.
Plug 'samoshkin/vim-mergetool'                     " Git mergetool
Plug 'voldikss/vim-floaterm'                       " Floating terminal.

" Search, replace and navigation.
Plug 'bronson/vim-visual-star-search'              " Visual star search.
Plug 'junegunn/fzf.vim'                            " Fzf.
Plug 'justinmk/vim-sneak'                          " Quick jump.
Plug 'mg979/vim-visual-multi'                      " Multiple cursors.

" Syntax.
Plug 'sheerun/vim-polyglot'                        " Language pack.

" Text objects and motions.
Plug 'christoomey/vim-sort-motion'                 " Sort by motion text object.
Plug 'wellle/targets.vim'                          " Additional text objects.

call plug#end()
