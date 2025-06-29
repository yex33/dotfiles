# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import socket
import subprocess
from typing import List  # noqa: F401

from libqtile import bar, hook, layout, qtile, widget
from libqtile.backend.wayland import InputConfig
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()
shell = "fish"
browser = "google-chrome-stable"
alternative_browser = f"{browser} -incognito"
font = "Inconsolata Nerd Font"
screen_arrangement = [0, 1]

# Pulseaudio sink name
# source: https://bbs.archlinux.org/viewtopic.php?id=234451
sink = "@DEFAULT_SINK@"
# sink = "alsa_output.pci-0000_00_1f.3.analog-stereo"

keys = [
    # launching
    Key([mod], "Return", lazy.spawn(f"{terminal} -e {shell}"),
        desc="Launch terminal"),

    # browsers
    Key([mod], "b", lazy.spawn(browser),
        desc="Launch browser"),
    Key([mod, "shift"], "b", lazy.spawn(alternative_browser),
        desc="Launch alternative browser"),

    Key([mod], "Tab", lazy.next_layout(),
        desc="Toggle between layouts"),

    # qtile force control
    Key([mod, "shift"], "w", lazy.window.kill(),
        desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(),
        desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),

    # Multimonitor focus
    Key([mod], "comma", lazy.to_screen(screen_arrangement[0]),
        desc="Move focus to screen 1"),
    Key([mod], "period", lazy.to_screen(screen_arrangement[1]),
        desc="Move focus to screen 0"),

    # Volume controls
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn(f"sh -c \"pactl set-sink-mute {sink} false; pactl set-sink-volume {sink} +5%\""),
        desc="Volume up"),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn(f"sh -c \"pactl set-sink-mute {sink} false; pactl set-sink-volume {sink} -5%\""),
        desc="Volume down"),
    Key([], "XF86AudioMute", lazy.spawn(f"pactl set-sink-mute {sink} toggle"),
        desc="Volume mute"),

    # screenshot
    Key([], "Print", lazy.spawn(f"flameshot gui"),
        desc="Print screen (screen shot)"),

    # Switch between windows
    Key([mod], "h", lazy.layout.shrink(), lazy.layout.decrease_nmaster(),
        desc="Move focus to left"),
    Key([mod], "l", lazy.layout.grow(), lazy.layout.increase_nmaster(),
        desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(),
        desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.

    # Treetab controls
    Key([mod, "control"], "h", lazy.layout.move_left(),
        desc="Move window to the left"),
    Key([mod, "control"], "l", lazy.layout.move_right(),
        desc="Move window to the right"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), # lazy.layout.section_down(),
        desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), # lazy.layout.section_up(),
        desc="Move window up"),

    # XmonadTall controls
    Key([mod, "shift"], "Tab", lazy.layout.rotate(), lazy.layout.flip(),
        desc="Switch which side main pane occupies (XmonadTall)"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod, "control"], "space", lazy.layout.swap_main(),
        desc="Toggle between split and unsplit sides of stack"),

    # Key([mod], "n", lazy.next_screen(),
    #     desc="Move focus to next screen"),
    # Key([mod], "p", lazy.prev_screen(),
    #     desc="Move focus to previous screen"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # Key([mod, "control"], "h", lazy.layout.grow_left(),
    #     desc="Grow window to the left"),
    # Key([mod, "control"], "l", lazy.layout.grow_right(),
    #     desc="Grow window to the right"),
    # Key([mod, "control"], "j", lazy.layout.grow_down(),
    #     desc="Grow window down"),
    # Key([mod, "control"], "k", lazy.layout.grow_up(),
    #     desc="Grow window up"),

    Key([mod], "m", lazy.layout.maximize(),
        desc="Maximize window"),
    Key([mod], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",),

    # Toggle between different layouts as defined below
    Key([mod], "r", lazy.spawncmd(command="fish -c \"%s\""),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "f", lazy.toggle_fullscreen(),
        desc="Toggle fullscreen"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(),
        desc="Toggle floating"),
]

groups = [
    Group("DEV", layout="monadthreecol"),
    Group("WWW", layout="monadthreecol"),
    Group("DOC", layout="monadthreecol"),
    Group("USR1", layout="monadthreecol"),
    Group("USR2", layout="monadthreecol"),
    Group("MUS", layout="monadthreecol"),
    Group("VID", layout="monadthreecol"),
    Group("OTH", layout="monadthreecol"),
    Group("VER", layout="treetab"),
]
# dvp_num_row = "&[{}(=*)+"
dvp_num_row = ["ampersand", "bracketleft", "braceleft", "braceright",
        "parenleft", "equal", "asterisk", "parenright", "plus"]

for key, group in zip(dvp_num_row, groups):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod], key, lazy.group[group.name].toscreen(),
                desc=f"Switch to group {group.name}"),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], key, lazy.window.togroup(group.name, switch_group=False),
                desc=f"Switch to & move focused window to group {group.name}"),

            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {
    "margin": 8,
    "border_width": 2,
    "border_focus": "E1ACFF",
    "border_normal": "1D2330",
}

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    layout.MonadThreeCol(
        main_centered=False,
        max_ratio=0.5,
        min_ratio=0.33,
        ratio=0.4,
        **layout_theme
    ),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.TreeTab(
        font=font,
        fontsize=24,
        sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize=26,
        border_width=2,
        bg_color="1c1f24",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=0,
        padding_x=10,
        padding_y=8,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200
    ),
    # layout.Floating(**layout_theme),
]

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

prompt = f"{os.environ['USER']}@{socket.gethostname()}"

def init_widgets(main=False):
    fontsize = 34 if main else 30
    icon_size = 80 if main else 60
    widgets = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0],
        ),
        widget.Image(
            filename="~/.config/qtile/icons/python-white.png",
            scale="False",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal)},
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0],
        ),
        widget.GroupBox(
            font=font,
            fontsize=fontsize,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=7,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors [4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0],
        ),
        widget.TextBox(
            font=font,
            fontsize=fontsize,
            text='|',
            background=colors[0],
            foreground='474747',
            padding=2,
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[2],
            background=colors[0],
            padding=0,
            scale=0.7,
        ),
        widget.CurrentLayout(
            font=font,
            fontsize=fontsize,
            foreground=colors[2],
            background=colors[0],
            padding=5,
        ),
        widget.TextBox(
            text='|',
            font=font,
            fontsize=fontsize,
            background=colors[0],
            foreground='474747',
            padding=2,
        ),
        widget.WindowName(
            font=font,
            fontsize=fontsize,
            foreground=colors[6],
            background=colors[0],
            padding=0,
        ),
        widget.Prompt(
            background=colors[0],
            font=font,
            fontsize=fontsize,
        ),
        widget.Systray(
            background=colors[0],
            padding=5,
            icon_size=fontsize,
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.TextBox(
            text='',
            font=font,
            fontsize=icon_size,
            background=colors[0],
            foreground=colors[3],
            padding=0,
        ),
        widget.Net(
            font=font,
            fontsize=fontsize,
            interface='wlan0',
            format='Net: {down} ↓↑ {up}',
            foreground=colors[1],
            background=colors[3],
            padding=5,
        ),
        widget.TextBox(
            text='',
            font=font,
            fontsize=icon_size,
            background=colors[3],
            foreground=colors[4],
            padding=0,
        ),
        widget.ThermalSensor(
            font=font,
            fontsize=fontsize,
            foreground=colors[1],
            background=colors[4],
            tag_sensor="Package id 0",
            threshold=90,
            fmt='Temp: {}',
            padding=5,
        ),
        widget.TextBox(
            text='',
            font=font,
            fontsize=icon_size,
            background=colors[4],
            foreground=colors[5],
            padding=0,
        ),
        widget.CheckUpdates(
            font=font,
            fontsize=fontsize,
            update_interval=1800,
            distro="Arch_checkupdates",
            display_format="Updates: {updates} ",
            no_update_string="No updates",
            foreground=colors[1],
            colour_have_updates=colors[1],
            colour_no_updates=colors[1],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
            padding=5,
            background=colors[5],
        ),
        widget.TextBox(
            text='',
            font=font,
            fontsize=icon_size,
            background=colors[5],
            foreground=colors[6],
            padding=0,
        ),
        widget.Memory(
            font=font,
            fontsize=fontsize,
            foreground=colors[1],
            background=colors[6],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
            fmt='Mem: {}',
            padding=5,
        ),
        widget.TextBox(
            text='',
            font=font,
            fontsize=icon_size,
            background=colors[6],
            foreground=colors[7],
            padding=0,
        ),
        widget.PulseVolume(
            font=font,
            fontsize=fontsize,
            update_interval=0.1,
            foreground=colors[1],
            background=colors[7],
            fmt='Vol: {}',
            padding=5,
        ),
        # widget.TextBox(
        #     text='',
        #     fontsize=icon_size,
        #     font=font,
        #     background=colors[7],
        #     foreground=colors[8],
        #     padding=0,
        # ),
        # widget.KeyboardLayout(
        #     font=font,
        #     fontsize=fontsize,
        #     foreground=colors[1],
        #     background=colors[8],
        #     configured_keyboards=['us dvp', 'us'],
        #     fmt='Keyboard: {}',
        #     padding=5,
        # ),
        widget.TextBox(
            text='',
            font=font,
            fontsize=icon_size,
            background=colors[7] if main else colors[0],
            foreground=colors[9],
            padding=0,
        ),
        widget.Clock(
            font=font,
            fontsize=fontsize,
            foreground=colors[1],
            background=colors[9],
            format="%A, %B %d - %H:%M ",
        ),
    ]
    if not main:
        del widgets[9:-2]
    return widgets


# widget_defaults = dict(
#     font="sans",
#     fontsize=12,
#     padding=3,
# )
# extension_defaults=widget_defaults.copy()

# screens = [
#     Screen(
#         top=bar.Bar(
#             [
#                 widget.CurrentLayout(),
#                 widget.GroupBox(),
#                 widget.Prompt(),
#                 widget.WindowName(),
#                 widget.Chord(
#                     chords_colors={
#                         "launch": ("#ff0000", "#ffffff"),
#                     },
#                     name_transform=lambda name: name.upper(),
#                 ),
#                 widget.TextBox("default config", name="default"),
#                 widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
#                 # widget.Systray(),
#                 widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
#                 widget.QuickExit(),
#                 widget.PulseVolume(update_interval=0.1),
#             ],
#             24,
#             # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
#             # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
#         ),
#     ),
#     Screen(
#         top=bar.Bar(
#             [
#                 widget.GroupBox(),
#                 # widget.WindowName(),
#             ],
#             24,
#         ),
#     ),
# ]

screens = [
    Screen(top=bar.Bar(widgets=init_widgets(main=False), opacity=1.0, size=40)),
    Screen(top=bar.Bar(widgets=init_widgets(main=True), opacity=1.0, size=50)),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk

        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices
wl_input_rules = {
    "type:keyboard": InputConfig(
        kb_layout='us',
        kb_variant="dvp",
        kb_repeat_rate=30,
        kb_repeat_delay=250,
    )
}

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + "/.config/qtile/autostart.sh"])

# source: https://github.com/qtile/qtile/issues/2101
@hook.subscribe.startup_complete
def assign_groups_to_screens():
    screen2group_id = {
        screen_arrangement[0]: 8,
        screen_arrangement[1]: 0,
    }
    for screen, group_id in screen2group_id.items():
        qtile.groups_map[groups[group_id].name].cmd_toscreen(screen)


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
