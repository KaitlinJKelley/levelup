from levelupapi.models.event import Event
import sqlite3
from django.shortcuts import render
from levelupapi.models import Game
from levelupreports.views import Connection

"""Function to build an HTML report of games by user"""
def user_event_list(request):
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all games, with related user info.
            db_cursor.execute("""
                SELECT
                    e.id as event_id,
                    e.event_date,
                    e.time,
                    e.description,
                    g.name as game,
                    u.id as user_id,
                    u.first_name || " " || u.last_name as organizer
                FROM
                    levelupapi_event e
                JOIN
                    levelupapi_game g ON g.id = e.game_id
                JOIN
                    levelupapi_gamer gr ON g.gamer_id = gr.id
                JOIN
                    auth_user u ON gr.user_id = u.id
            """)

            dataset = db_cursor.fetchall()
            db_cursor.execute("""
                SELECT
                    u.first_name || " " || u.last_name as name,
                    ea.event_id
                FROM
                    levelupapi_event e
                JOIN
                    levelupapi_eventattendance ea ON ea.event_id = e.id
                JOIN 
                    levelupapi_gamer gr ON ea.gamer_id = gr.id
                JOIN
                    auth_user u ON gr.user_id = u.id
            """)

            attendees = db_cursor.fetchall()

            events_by_user = {}

            for row in dataset:
                # Crete a Game instance and set its properties
                event = Event()
                event.id = row["event_id"]
                event.title_game = row["game"]
                event.description = row["description"]
                event.event_date = row["event_date"]
                event.time = row["time"]
                event.event_attendees = []
                for attendee in attendees:
                    if attendee["event_id"] == row["event_id"]:
                        event.event_attendees.append(attendee["name"])

                # Store the user's id
                user_id = row["user_id"]

                # If the user's id is already a key in the dictionary...
                if user_id in events_by_user:

                    # Add the current game to the `games` list for it
                    events_by_user[user_id]['events'].append(event)

                else:
                    # Otherwise, create the key and dictionary value
                    events_by_user[user_id] = {}
                    events_by_user[user_id]["id"] = user_id
                    events_by_user[user_id]["organizer"] = row["organizer"]
                    events_by_user[user_id]["events"] = [event]

        # Get only the values from the dictionary and create a list from them
        list_of_users_with_events = events_by_user.values()

        # Specify the Django template and provide data context
        template = 'users/list_with_events.html'
        context = {
            'userevent_list': list_of_users_with_events
        }

        return render(request, template, context)