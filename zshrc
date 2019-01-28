
#  ╺━┓┏━┓╻ ╻┏━┓┏━╸
#  ┏━┛┗━┓┣━┫┣┳┛┃
#  ┗━╸┗━┛╹ ╹╹┗╸┗━╸

# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
# ¤¤¤¤  Sourcing  ¤¤¤¤
# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
source ${ZIM_HOME}/init.zsh
source ${ZIM_HOME}/modules/external/zsh-system-clipboard/zsh-system-clipboard.zsh

# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
# ¤¤¤¤  Settings  ¤¤¤¤
# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
if [[ "$TERM" = "linux" ]]; then
  # Replicate colors definied in .Xresources for virtual console.
  colors=$(sed -n 's/\*\.color\([0-9]\+\).*#\(\w\{6\}\)/\1 \2/p' "$HOME/.Xresources")
  echo -en $(awk '$1 < 16 {printf "\\e]P%X%s", $1, $2}' <<< "$colors")
  clear
fi

# Enable command edit in $EDITOR.
autoload -z edit-command-line
zle -N edit-command-line

# Disable terminal close on <C-c>.
set -o ignoreeof

# Repair kill line, word and char when jumping between modes.
zle -A kill-whole-line vi-kill-line
zle -A backward-kill-word vi-backward-kill-word
zle -A backward-delete-char vi-backward-delete-char

# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
# ¤¤¤¤  Functions  ¤¤¤¤
# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤

function js-box() {
  (cd ~/code/js-playground && nvim +vsplit +"terminal npm run $1" +'wincmd h' +GoldenRatioResize +'norm G$' "boxes/$1.js")
}

function nvm() {
  source /usr/share/nvm/nvm.sh --no-use
  nvm "$@"
}

function nvim-cd() {
  if [[ -d "$1" ]]; then
    (cd "$1" && nvim +Ranger)
  elif [[ -f "$1" ]]; then
    dirname="$(dirname "$1")/"
    (cd "$dirname" && nvim "${1/$dirname/}")
  else
    nvim "$1"
  fi
}

function ranger-cd() {
  tmp="$(mktemp -t tmp.XXXXXX)"
  command ranger --choosedir="$tmp" "${@:-$(pwd)}"
  test -f "$tmp" &&
  if [ "$(cat -- "$tmp")" != "$(echo -n `pwd`)" ]; then
      cd -- "$(cat "$tmp")"
  fi
  rm -f -- "$tmp"
}

# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
# ¤¤¤¤  Exports  ¤¤¤¤
# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
export FZF_ALT_C_COMMAND='command fd --type d --hidden --follow --exclude .git'
export FZF_CTRL_T_COMMAND='command fd --hidden --follow --exclude .git'
export FZF_DEFAULT_COMMAND='command fd --hidden --follow --exclude .git'

export FZF_CTRL_T_OPTS="--preview '(highlight -l -O xterm256 -s dracula --stdout {} 2> /dev/null || cat {} || tree -C -L 1 --dirsfirst {}) 2> /dev/null | head -200'"
export FZF_ALT_C_OPTS="--preview 'tree -C -L 1 --dirsfirst {}'"
export FZF_DEFAULT_OPTS='
  --color=bg+:#343434,spinner:#BD93F9,hl:#BD93F9
  --color=fg:#F8F8F2,info:#FF79C6,pointer:#50FA7B
  --color=marker:#50FA7B,hl+:#50FA7B
'


# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
# ¤¤¤¤  Keybindings  ¤¤¤¤
# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
bindkey -r '^T'

bindkey '^[' vi-cmd-mode
bindkey '^[^?' backward-kill-word
bindkey '^[^H' backward-kill-word
bindkey '^E' edit-command-line
bindkey '^F' fzf-file-widget
bindkey '^G' fzf-cd-widget


# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
# ¤¤¤¤  Aliases  ¤¤¤¤
# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤

# Safety.
alias chgrp='chgrp --preserve-root'
alias chmod='chmod --preserve-root'
alias chown='chown --preserve-root'
alias cp='cp -ir'
alias ln='ln -i'
alias mv='mv -i'
alias rm='rm -I --preserve-root'

# Goodies & Misc.
alias cl=clear
alias cmd=command
alias df='df -h'
alias du='du -ch'
alias dud='du -chd'
alias free='free -m'
alias ga='cat $ZIM_HOME/modules/git/init.zsh | ag "^alias" | sed -e "s/alias //" -e "s/=/%%/" | column -t -s "%%" | ag'
alias grep='grep --color=auto -d skip'
alias mkdir="mkdir -pv"
alias more=less
alias np='nvim -w PKGBUILD'
alias open='mimeo -q'
alias o=open
alias q=exit
alias root='sudo -i'
alias sudo='sudo '
alias sudoedit='sudo edit'

# Listing.
alias exa='exa --group-directories-first'
alias la='exa -la'
alias ll='exa -l'
alias ls='exa'

# Apps.
alias R='ramda --js'
alias ag='ag --hidden --ignore .git --follow'
alias bc='bc -l -q'
alias bluetooth=bluetoothctl
alias c=cat
alias camera=gphoto2
alias diff='git diff --no-index'
alias fd='fd --hidden --follow'
alias feh='feh --scale-down --auto-zoom --image-bg "#343434"'
alias git=hub
alias hc="highlight -O xterm256 --force -s dracula --stdout"
alias hcat="highlight -O xterm256 --force -s dracula --stdout"
alias l=less
alias leave='i3-msg exit'
alias loc=locate
alias mixer=ncpamixer
alias pass=lpass
alias r=ranger
alias ramda='ramda --js'
alias ranger='ranger-cd'
alias s=sudo
alias se=sudoedit
alias t=term
alias tiga='tig --all'
alias v=nvim
alias vi=nvim
alias vim=nvim
alias wifi-menu='wifi-menu -o'
alias xsel='xsel -b'

# Config.
alias cfg-env='nvim-cd /etc/environment'
alias cfg-hosts='nvim-cd /etc/hosts'
alias cfg-i3='nvim-cd $HOME/.dotfiles/config/i3/config'
alias cfg-keymap='nvim-cd $HOME/code/qmk_firmware/keyboards/ergodox_ez/keymaps/sqve'
alias cfg-nvim='nvim-cd $HOME/.dotfiles/config/nvim/'
alias cfg-ranger='nvim-cd $HOME/.dotfiles/config/ranger'
alias cfg-vim='nvim-cd $HOME/.dotfiles/config/nvim/'
alias cfg-weechat='nvim-cd $HOME/.dotfiles/weechat'
alias cfg-xinitrc='nvim-cd $HOME/.dotfiles/xinitrc'
alias cfg-xresources='nvim-cd $HOME/.dotfiles/Xresources'
alias cfg-zimrc='nvim-cd $HOME/.dotfiles/zimrc'
alias cfg-zshenv='nvim-cd $HOME/.dotfiles/zshenv'
alias cfg-zshrc='nvim-cd $HOME/.dotfiles/zshrc'

# JS Playground.
alias js-clean="js-box clean"
alias js-fp="js-box fp"

# Todo.
alias todo='nvim-cd $HOME/notes/todo.md'
