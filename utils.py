from colors import Base16ColorScheme


def set_colors(c, color: Base16ColorScheme):
    c.colors.completion.fg = color.base05
    c.colors.completion.odd.bg = color.base01
    c.colors.completion.even.bg = color.base00
    c.colors.completion.category.fg = color.base0A
    c.colors.completion.category.bg = color.base00
    c.colors.completion.category.border.top = color.base01
    c.colors.completion.category.border.bottom = color.base00
    c.colors.completion.item.selected.fg = color.base05
    c.colors.completion.item.selected.bg = color.base02
    c.colors.completion.item.selected.border.top = color.base02
    c.colors.completion.item.selected.border.bottom = color.base02
    c.colors.completion.item.selected.match.fg = color.base0B
    c.colors.completion.match.fg = color.base0B
    c.colors.completion.scrollbar.fg = color.base05
    c.colors.completion.scrollbar.bg = color.base00
    c.colors.contextmenu.disabled.bg = color.base01
    c.colors.contextmenu.disabled.fg = color.base04
    c.colors.contextmenu.menu.bg = color.base00
    c.colors.contextmenu.menu.fg = color.base05
    c.colors.contextmenu.selected.bg = color.base02
    c.colors.contextmenu.selected.fg = color.base05
    c.colors.downloads.bar.bg = color.base00
    c.colors.downloads.start.fg = color.base00
    c.colors.downloads.start.bg = color.base0D
    c.colors.downloads.stop.fg = color.base00
    c.colors.downloads.stop.bg = color.base0C
    c.colors.downloads.error.fg = color.base08
    c.colors.hints.fg = color.base00
    c.colors.hints.bg = color.base0A
    c.colors.hints.match.fg = color.base05
    c.colors.keyhint.fg = color.base05
    c.colors.keyhint.suffix.fg = color.base05
    c.colors.keyhint.bg = color.base00
    c.colors.messages.error.fg = color.base00
    c.colors.messages.error.bg = color.base08
    c.colors.messages.error.border = color.base08
    c.colors.messages.warning.fg = color.base00
    c.colors.messages.warning.bg = color.base0E
    c.colors.messages.warning.border = color.base0E
    c.colors.messages.info.fg = color.base05
    c.colors.messages.info.bg = color.base00
    c.colors.messages.info.border = color.base00
    c.colors.prompts.fg = color.base05
    c.colors.prompts.border = color.base00
    c.colors.prompts.bg = color.base00
    c.colors.prompts.selected.bg = color.base02
    c.colors.prompts.selected.fg = color.base05
    c.colors.statusbar.normal.fg = color.base0B
    c.colors.statusbar.normal.bg = color.base00
    c.colors.statusbar.insert.fg = color.base00
    c.colors.statusbar.insert.bg = color.base0D
    c.colors.statusbar.passthrough.fg = color.base00
    c.colors.statusbar.passthrough.bg = color.base0C
    c.colors.statusbar.private.fg = color.base00
    c.colors.statusbar.private.bg = color.base01
    c.colors.statusbar.command.fg = color.base05
    c.colors.statusbar.command.bg = color.base00
    c.colors.statusbar.command.private.fg = color.base05
    c.colors.statusbar.command.private.bg = color.base00
    c.colors.statusbar.caret.fg = color.base00
    c.colors.statusbar.caret.bg = color.base0E
    c.colors.statusbar.caret.selection.fg = color.base00
    c.colors.statusbar.caret.selection.bg = color.base0D
    c.colors.statusbar.progress.bg = color.base0D
    c.colors.statusbar.url.fg = color.base05
    c.colors.statusbar.url.error.fg = color.base08
    c.colors.statusbar.url.hover.fg = color.base05
    c.colors.statusbar.url.success.http.fg = color.base0C
    c.colors.statusbar.url.success.https.fg = color.base0B
    c.colors.statusbar.url.warn.fg = color.base0E
    c.colors.tabs.bar.bg = color.base00
    c.colors.tabs.indicator.start = color.base0D
    c.colors.tabs.indicator.stop = color.base0C
    c.colors.tabs.indicator.error = color.base08
    c.colors.tabs.odd.fg = color.base05
    c.colors.tabs.odd.bg = color.base00
    c.colors.tabs.even.fg = color.base05
    c.colors.tabs.even.bg = color.base00
    c.colors.tabs.pinned.even.bg = color.base0C
    c.colors.tabs.pinned.even.fg = color.base07
    c.colors.tabs.pinned.odd.bg = color.base0B
    c.colors.tabs.pinned.odd.fg = color.base07
    c.colors.tabs.pinned.selected.even.bg = color.base02
    c.colors.tabs.pinned.selected.even.fg = color.base05
    c.colors.tabs.pinned.selected.odd.bg = color.base02
    c.colors.tabs.pinned.selected.odd.fg = color.base05
    c.colors.tabs.selected.odd.fg = color.base05
    c.colors.tabs.selected.odd.bg = color.base02
    c.colors.tabs.selected.even.fg = color.base05
    c.colors.tabs.selected.even.bg = color.base02
