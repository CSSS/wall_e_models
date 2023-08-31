=====
wall_e_models
=====

wall_e_models is a Django app to manage the database for CSSS's discord bot.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "wall_e_models" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "wall_e_models",
    ]

2. Include the wall_e_models URLconf in your project urls.py like this::

    path("wall_e_models/", include("wall_e_models.urls")),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.