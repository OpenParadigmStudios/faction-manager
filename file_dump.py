import os

# List of files to grab
files_to_grab = [
    "factions/apps.py",
    "factions/forms.py",
    "factions/models.py",
    "factions/urls.py",
    "factions/views.py",
    "factions/static/factions/css/base.css",
    "factions/templates/base.html",
    "factions/templates/faction/faction_list.html",
    "factions/templates/faction/faction_detail.html",
    "factions/templates/faction/faction_form.html",
    "factions/templates/faction/faction_confirm_delete.html",
    "factions/templates/game/game_list.html",
    "factions/templates/game/game_detail.html",
    "factions/templates/game/game_form.html",
    "factions/templates/game/game_confirm_delete.html",
    "factions/templates/project/project_list.html",
    "factions/templates/project/project_detail.html",
    "factions/templates/project/project_form.html",
    "factions/templates/project/project_confirm_delete.html",
]

# Get the directory where the script is located
base_dir = os.path.dirname(os.path.realpath(__file__))

# Path to the output file
output_file = os.path.join(base_dir, 'output.txt')

with open(output_file, 'w') as outfile:
    for filepath in files_to_grab:
        # Remove leading '/faction-manager/' from filepath if present
        if filepath.startswith('/faction-manager/'):
            relative_path = filepath[len('/faction-manager/'):]
        else:
            relative_path = filepath

        # Construct the full path to the file
        full_path = os.path.join(base_dir, relative_path)

        # Write the file path and contents to output.txt
        outfile.write(f'`{filepath}`\n')
        outfile.write('```\n')
        try:
            with open(full_path, 'r') as infile:
                outfile.write(infile.read())
        except FileNotFoundError:
            outfile.write('File not found\n')
        outfile.write('```\n\n')
