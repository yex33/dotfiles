#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

# shellcheck shell=sh

# Compatible with ranger 1.4.2 through 1.9.*
#
# Automatically change the current working directory after closing ranger
#
# This is a shell function to automatically change the current working
# directory to the last visited one after ranger quits. Either put it into your
# .zshrc/.bashrc/etc or source this file from your shell configuration.
# To undo the effect of this function, you can type "cd -" to return to the
# original directory.

########## My config ##########

# bare git config
alias config="/usr/bin/git --git-dir=$HOME/.cfg --work-tree=$HOME"

# vim
export EDITOR=/usr/bin/vim
export SUDO_EDITOR=/usr/bin/vim
export SYSTEMD_EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim

# virsh
export LIBVIRT_DEFAULT_URI="qemu:///system"

# PATH
export PATH=$PATH:/home/joe/.local/bin:/home/joe/.cargo/bin

# bash
alias la="ls -ah"
alias ll="ls -ahl"
alias cp="cp -p"
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."

# python
alias python=python3
alias pip=pip3

# ffmpeg
alias ffprobe="ffprobe -v quiet -print_format json -show_format -show_streams"

# mount
alias mntwin="sudo mount /dev/nvme0n1p3 /mnt/joe/Windows/"
alias umntwin="sudo umount /mnt/joe/Windows/"

# ranger
ranger-cd() {
  temp_file="$(mktemp -t "ranger_cd.XXXXXXXXXX")"
  ranger --choosedir="$temp_file" -- "${@:-$PWD}"
  if chosen_dir="$(cat -- "$temp_file")" && [ -n "$chosen_dir" ] && [ "$chosen_dir" != "$PWD" ]; then
    cd -- "$chosen_dir"
  fi
  rm -f -- "$temp_file"
}

# This binds Ctrl-O to ranger-cd:
bind '"\C-o":"ranger-cd\C-m"'

ranger() {
  if [ -z "$RANGER_LEVEL" ]; then
    /usr/bin/ranger "$@"
  else
    exit
  fi
}

# fuck nivida
# UDEV_NVIDIA=/lib/udev/rules.d/71-nvidia.rules
# if [ -f "$UDEV_NVIDIA" ]; then
#     sudo mv $UDEV_NVIDIA ~
#     sudo systemctl restart systemd-udevd.service
# fi
