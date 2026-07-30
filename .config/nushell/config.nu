# config.nu
#
# Installed by:
# version = "0.111.0"
#
# This file is used to override default Nushell settings, define
# (or import) custom commands, or run any other startup tasks.
# See https://www.nushell.sh/book/configuration.html
#
# Nushell sets "sensible defaults" for most configuration settings, 
# so your `config.nu` only needs to override these defaults if desired.
#
# You can open this file in your default editor using:
#     config nu
#
# You can also pretty-print and page through the documentation for configuration
# options using:
#     config nu --doc | nu-highlight | less -R
# PATH
$env.PATH ++= ["~/.local/bin", "~/.ghcup/bin", "~/.cargo/bin", "~/Documents/scripts"]
# Editor
$env.EDITOR = "nvim"
$env.VISUAL = "nvim"
$env.config.buffer_editor = "nvim"
$env.config.edit_mode = "vi"
$env.config.table = {
    mode: rounded
    index_mode: always
    show_empty: true
    trim: {methodology: truncating, wrapping_try_keep_words: true, truncating_suffix: "..."}
}
# yazi
def --env y [...args] {
    let tmp = (mktemp -t "yazi-cwd.XXXXXX")
    ^yazi ...$args --cwd-file $tmp
    let cwd = (open $tmp)
    if $cwd != $env.PWD and ($cwd | path exists) {
        cd $cwd
    }
    rm -fp $tmp
}
# C-O to open yazi in vi_normal mode
$env.config.keybindings ++= [
    {
        name: file_manager
        modifier: control
        keycode: char_o
        mode: vi_normal
        event: {send: ExecuteHostCommand, cmd: "y"}
    }
    {
        name: paste_bash_multiline
        modifier: alt
        keycode: char_v
        mode: [emacs, vi_normal, vi_insert]
        event: {send: ExecuteHostCommand, cmd: r#'commandline edit (wl-paste | str replace -ar '\\(?=\r?\n)' '' | $"\(($in))")'#}
    }
]
# carapace
$env.CARAPACE_BRIDGES = 'zsh,fish,bash,inshellisense'
let carapace_completer = {|spans|
    carapace $spans.0 nushell ...$spans | from json
}
$env.config.completions.external.completer = $carapace_completer
# bare git repo alias for dotfiles
alias cfg = /usr/bin/lazygit --git-dir=($env.HOME)/.cfg --work-tree=($env.HOME)
# alias
alias parsyu = paru -Syu --noconfirm
alias mntwin = sudo mount -t ntfs3 -o uid=1000,gid=1000,dmask=0022,fmask=0133 UUID=84D8A0D4D8A0C5B0 /mnt/joe/Windows/
alias umntwin = sudo umount /mnt/joe/Windows/
alias la = ls -a
def ll [] {
    ls -al | explore
}
alias hx = helix
