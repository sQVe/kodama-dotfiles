
"  ┏━┓╻  ╻ ╻┏━╸╻┏┓╻┏━┓
"  ┣━┛┃  ┃ ┃┃╺┓┃┃┗┫┗━┓
"  ╹  ┗━╸┗━┛┗━┛╹╹ ╹┗━┛

" ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
" ¤¤¤¤  Import plugins  ¤¤¤¤
" ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤

call plug#begin('$HOME/.local/share/nvim/plugged')

" Colorschemes.
Plug 'dracula/vim', { 'as': 'dracula' }

" Language, syntax and formatting.
Plug 'sheerun/vim-polyglot'
Plug 'styled-components/vim-styled-components', { 'branch': 'main' }

" Interface.
Plug 'francoiscabrol/ranger.vim'
Plug 'itchyny/lightline.vim'
Plug 'junegunn/fzf', { 'dir': '$HOME/.local/share/nvim/apps/fzf', 'do': './install --bin' }
Plug 'junegunn/fzf.vim'
Plug 'junegunn/vim-peekaboo'
Plug 'markonm/traces.vim'
Plug 'mhinz/vim-signify'
Plug 'roman/golden-ratio'
Plug 'samoshkin/vim-mergetool'
Plug 'tpope/vim-fugitive'
Plug 'w0rp/ale'

" Integration.
Plug 'Galooshi/vim-import-js'
Plug 'dahu/vim-fanfingtastic'
Plug 'easymotion/vim-easymotion'
Plug 'editorconfig/editorconfig-vim'
Plug 'heavenshell/vim-jsdoc'
Plug 'junegunn/vim-easy-align'
Plug 'machakann/vim-sandwich'
Plug 'mattn/emmet-vim'
Plug 'mg979/vim-visual-multi'
Plug 'ntpeters/vim-better-whitespace'
Plug 'sickill/vim-pasta'
Plug 'tomtom/tcomment_vim'
Plug 'tpope/vim-repeat'
Plug 'tpope/vim-rhubarb'

" Commands.
Plug 'lambdalisue/suda.vim'
Plug 'moll/vim-bbye'

" Completion and spelling.
Plug 'ervandew/supertab'
Plug 'neoclide/coc.nvim', {'do': { -> coc#util#install()}}
Plug 'rhysd/vim-grammarous'

call plug#end()
