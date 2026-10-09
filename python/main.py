#!/usr/bin/env python3

import sys
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw


class Oilia(Adw.Application):

    def __init__(self):
        super().__init__(
            application_id="io.github.samwise1776.OiliaPython"
        )

    def do_activate(self):
        win = Adw.ApplicationWindow(
            application=self,
            title="Oilia",
            default_width=1100,
            default_height=700
        )

        toolbar = Adw.ToolbarView()

        header = Adw.HeaderBar()

        content = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL
        )

        toolbar.add_top_bar(header)
        toolbar.set_content(content)

        win.set_content(toolbar)
        win.present()


if __name__ == "__main__":
    app = Oilia()
    sys.exit(app.run(sys.argv))