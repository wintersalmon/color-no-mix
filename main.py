'''
COLOR-NO-MIX
WinterSalmon
'''
from gui.gui import Gui
from cli.cli import Cli

if __name__ == "__main__":
    # TODO : ADD parameters to force game in cli mode
    # TODO : ADD parameters to run game in varius mode

    try:
        # if pygame is not installed run game in commandline mode
        UI = Gui()
    except ImportError:
        UI = Cli()

    UI.run()
