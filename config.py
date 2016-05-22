try:
    from libqtile.manager import Key, Group
except ImportError:
    from libqtile.config import Key, Group

from libqtile import bar, hook, layout, widget

from libqtile.manager import Screen
from libqtile.command import lazy
# from libqtile.widget.wlan import Wlan
# from libqtile.widget.battery import Battery
import os


sup = "mod4"
alt = "mod1"

keys = [
    Key([alt], "Tab", lazy.layout.down()),
    Key([alt, "shift"], "Tab", lazy.layout.down()),
    Key([sup, "control"], "k", lazy.shuffle_down()),
    Key([sup, "control"], "j", lazy.shuffle_up()),
    Key([sup], "space", lazy.layout.next()),
    Key([sup, "shift"], "space", lazy.layout.previous()),
    Key([sup, "shift"], "Return", lazy.layout.rotate()),

    Key([sup], "Return", lazy.spawn("terminator")),
    Key([sup, alt], "f", lazy.spawn("firefox")),


    Key([sup, "control"], "r", lazy.restart()),
    # cycle to previous group
    Key([sup], "Left", lazy.group.prevgroup()),
    # cycle to next group
    Key([sup], "Right", lazy.group.nextgroup()),

    # windows style alt-tab/alt-shift-tab
    Key([sup], "Tab", lazy.nextlayout()),
    Key([sup, "shift"], "Tab", lazy.previouslayout()),

    
    Key([sup, "shift"], "Tab", lazy.previouslayout()),

]

groups = [
    Group("h"),
    Group("n"),
    Group("e"),
    Group("i"),
    Group("o"),
]

for i in groups:
    keys.append(Key([sup], i.name, lazy.group[i.name].toscreen()))
    keys.append(Key([sup, "shift"], i.name, lazy.window.togroup(i.name)))


screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(fontsize=10),
                widget.WindowName(),
                widget.Sep(),
                widget.CPUGraph(samples=50, line_width=1, width=50,
                                graph_color='FF2020',
                                fill_color='C01010'),
                widget.MemoryGraph(samples=50, line_width=1, width=50,
                                   graph_color='0066FF',
                                   fill_color='001188'),
                widget.NetGraph(samples=50, line_width=1,
                                width=50, interface="eth0",
                                graph_color='22FF44',
                                fill_color='11AA11'),
                widget.Systray(),
                widget.Prompt(),
                # widget.wlan.Wlan(),
                # widget.battery(),

                widget.Clock(
                    format='%Y-%m-%d %a %H:%M',
                    update_interval=1.0,
                ),
            ],
            25,
        ),
    ),
]

layouts = [
    layout.Max(),
    layout.Stack(stacks=2),
] 

@hook.subscribe.startup
def colemakde():
    os.system("setxkbmap de -variant colemakde")
