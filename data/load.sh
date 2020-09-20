#!/bin/bash
python umic/manage.py loaddata data/sponsors.json
python umic/manage.py loaddata data/team.json
python umic/manage.py loaddata data/events.json
python umic/manage.py loaddata data/gallery.json
python umic/manage.py loaddata data/projects.json