from textual.app import App, ComposeResult
from textual.widgets import Welcome, Header


class GffApp(App):
    TITLE = "Google-form filler"
    SUB_TITLE = "A tool to automate the filling process of Google-form"

    def on_mount(self) -> None:
        self.screen.styles.background = "#1e1e2e"
        self.screen.styles.border = ("heavy", "#cdd6f4")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Welcome()

    def on_button_pressed(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = GffApp()
    app.run()
