#!/bin/bash
python umic/manage.py dumpdata sponsors --indent 4 > data/sponsors.json
python umic/manage.py dumpdata team --indent 4 > data/team.json
python umic/manage.py dumpdata gallery --indent 4 > data/gallery.json
python umic/manage.py dumpdata projects --indent 4 > data/projects.json
python umic/manage.py dumpdata events --indent 4 > data/events.json