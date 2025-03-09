### adding to the PATH

fish_add_path $HOME/.local/bin
fish_add_path $HOME/.local/share/gem/ruby/3.3.0/bin
fish_add_path $HOME/.cargo/bin
fish_add_path $HOME/.ghcup/bin
fish_add_path $HOME/Documents/scripts

### export

# fish
set fish_greeting

# vim
set -gx EDITOR /usr/bin/nvim
set -gx SUDO_EDITOR /usr/bin/vim
set -gx SYSTEMD_EDITOR /usr/bin/vim
set -gx VISUAL /usr/bin/nvim

# virsh
set LIBVIRT_DEFAULT_URI "qemu:///system"

### manpager

# "bat" as manpager
# set -x MANPAGER "sh -c 'col -bx | bat -l man -p'"

# "vim" as manpager
set -x MANPAGER '/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist norelativenumber nonu noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"'

### fish default emacs mode or vi mode
function fish_user_key_bindings
    # fish_default_key_bindings
    fish_vi_key_bindings
end

### AUTOCOMPLETE AND HIGHLIGHT COLORS
set fish_color_normal brcyan
set fish_color_autosuggestion '#7d7d7d'
set fish_color_command brcyan
set fish_color_error '#ff6c6b'
set fish_color_param brcyan

### spark
set -g spark_version 1.0.0

### keybindings

# !! and !$
if [ $fish_key_bindings = fish_vi_key_bindings ]
    bind -Minsert ! __history_previous_command
    bind -Minsert '$' __history_previous_command_arguments
else
    bind ! __history_previous_command
    bind '$' __history_previous_command_arguments
end

# ranger-cd
bind \co "ranger-cd ; commandline -f repaint"

### alias

# \x1b[2J   <- clears tty
# \x1b[1;1H <- goes to (1, 1) (start)
alias clear='echo -en "\x1b[2J\x1b[1;1H" ; echo; echo; seq 1 (tput cols) | sort -R | spark | lolcat; echo; echo'

# cd
alias ..="cd .."
alias ...="cd ../.."
alias .3="cd ../../.."
alias .4="cd ../../../.."
alias .5="cd ../../../../.."

# emacs
alias em="/usr/bin/emacs -nw"

# eza
alias ls="eza -al --color=always --group-directories-first --icons" # my preferred listing
alias la="eza -a --color=always --group-directories-first --icons" # all files and dirs
alias ll="eza -l --color=always --group-directories-first --icons" # long format
alias lt="eza -aT --color=always --group-directories-first --icons" # tree listing
alias l.="eza -a --icons | egrep "^\.""

# pacman and paru
alias pacsyu="sudo pacman -Syu" # update only standard pkgs
alias pacsyyu="sudo pacman -Syyu" # Refresh pkglist & update standard pkgs
alias parsua="paru -Sua --noconfirm" # update only AUR pkgs (paru)
alias parsyu="paru -Syu --noconfirm" # update standard pkgs and AUR pkgs (paru)
alias unlock="sudo rm /var/lib/pacman/db.lck" # remove pacman lock
alias cleanup="sudo pacman -Rns (pacman -Qtdq)" # remove orphaned packages

# Colorize grep output (good for log files)
alias grep="grep --color=auto"
alias egrep="egrep --color=auto"
alias fgrep="fgrep --color=auto"

# confirm before overwriting something
alias cp="cp -ip"
alias mv="mv -i"
alias rm="rm -i"

# adding flags
alias df="df -h" # human-readable sizes
alias free="free -m" # show sizes in MB

# ps
alias psa="ps auxf"
alias psgrep="ps aux | grep -v grep | grep -i -e VSZ -e"
alias psmem="ps auxf | sort -nr -k 4"
alias pscpu="ps auxf | sort -nr -k 3"

# Play video files in current dir by type
alias playavi="mpv *.avi"
alias playmov="mpv *.mov"
alias playmp4="mpv *.mp4"

# bare git repo alias for dotfiles
alias config="/usr/bin/git --git-dir=$HOME/.cfg --work-tree=$HOME"

# python
alias python=python3
alias pip=pip3

# ffmpeg
alias ffprobe="ffprobe -v quiet -print_format json -show_format -show_streams"

# mount
alias mntwin="sudo mount /dev/nvme0n1p3 /mnt/joe/Windows/"
alias umntwin="sudo umount /mnt/joe/Windows/"
