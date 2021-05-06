from flask.cli import AppGroup
from .users import seed_users, undo_users
from .shelters import seed_shelters, undo_shelters
from .breeds import seed_breeds, undo_breeds
from .animals import seed_animals, undo_animals

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_shelters()
    seed_breeds()
    seed_animals()

    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_shelter()
    undo_breeds()
    undo_animals()
    # Add other undo functions here
