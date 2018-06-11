
"  ╻┏ ┏━╸╻ ╻┏┳┓┏━┓┏━┓
"  ┣┻┓┣╸ ┗┳┛┃┃┃┣━┫┣━┛
"  ╹ ╹┗━╸ ╹ ╹ ╹╹ ╹╹

" Escape.
inoremap jj <Esc>
noremap <F1> <Esc>

" Motion.
noremap <Up> gk
noremap <Down> gj
inoremap <Up> <C-o>gk
inoremap <Down> <C-o>gj
noremap k gk
noremap gk k
noremap j gj
noremap gj j
noremap H ^
noremap L g_

" New buffer.
nnoremap <Leader>n :enew<CR>

" Start a new vim instance.
nnoremap <Leader>N :!urxvt -e nvim & disown<CR><CR>

" Start a new terminal at current pwd.
nnoremap <Leader>u :!urxvt & disown<CR><CR>

" Write buffer.
nnoremap <Leader>w :write<CR>
nnoremap <Leader>W :wall<CR>

" Close buffer.
nnoremap <Leader>d :bd<CR>
nnoremap <Leader>D :bd!<CR>

" Close window.
nnoremap <Leader>q :quit<CR>
nnoremap <Leader>Q :quit!<CR>

" Close buffer but keep window.
nnoremap <Leader>x :bp\|bd #<CR>
nnoremap <Leader>X :bp\|bd! #<CR>

" Remove highlighted search result.
nnoremap <Esc><Esc> :nohl<CR>

" Search for selected text, forwards or backwards.
vnoremap <silent> * :<C-U>
  \let old_reg=getreg('"')<Bar>let old_regtype=getregtype('"')<CR>
  \gvy/<C-R><C-R>=substitute(
  \escape(@", '/\.*$^~['), '\_s\+', '\\_s\\+', 'g')<CR><CR>
  \gV:call setreg('"', old_reg, old_regtype)<CR>
vnoremap <silent> # :<C-U>
  \let old_reg=getreg('"')<Bar>let old_regtype=getregtype('"')<CR>
  \gvy?<C-R><C-R>=substitute(
  \escape(@", '?\.*$^~['), '\_s\+', '\\_s\\+', 'g')<CR><CR>
  \gV:call setreg('"', old_reg, old_regtype)<CR>

" Set pwd to current open buffer path.
noremap cd :Cdb<CR>:pwd<CR>

" Black hole.
noremap <Leader>- "_

" Switch between the last two files.
nnoremap <Leader><Tab> <C-^>

" Adapt for Swedish keyboard layout.
noremap å {
noremap ä }

" Uniform split.
noremap <Ctrl-W>n :split<CR>

" Move between buffers.
nnoremap <S-Tab> :bprev<CR>
nnoremap <Tab> :bnext<CR>
vnoremap <S-Tab> :bprev<CR>
vnoremap <Tab> :bnext<CR>
noremap <M-h> :bprev<CR>
noremap <M-l> :bnext<CR>
noremap <M-Left> :bprev<CR>
noremap <M-Right> :bnext<CR>

" Use vertical split as default split.
noremap <C-S-w><C-S-s> :split<CR>
noremap <C-S-w>s :split<CR>
noremap <C-w><C-S-s> :split<CR>
noremap <C-w><C-s> :vsplit<CR>
noremap <C-w>s :vsplit<CR>

" Move between open windows.
noremap <C-h> <C-w>h
noremap <C-j> <C-w>j
noremap <C-k> <C-w>k
noremap <C-l> <C-w>l
noremap <C-Left> <C-w>h
noremap <C-Down> <C-w>j
noremap <C-Up> <C-w>k
noremap <C-Right> <C-w>l

" Spell completion.
inoremap <C-x><C-s> <C-x>s

