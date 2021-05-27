SELECT * FROM levelupapi_gametype;

DELETE FROM django_migrations WHERE app = "levelupapi";

SELECT
                    e.event_date,
                    e.time,
                    e.description,
                    g.name as game,
                    u.id as user_id,
                    u.first_name || " " || u.last_name as organizer,
                    ea.*
                FROM
                    levelupapi_event e
                JOIN
                    levelupapi_game g ON g.id = e.game_id
                JOIN
                    levelupapi_gamer gr ON g.gamer_id = gr.id
                JOIN
                    auth_user u ON gr.user_id = u.id

                JOIN levelupapi_eventattendance ea ON ea.gamer_id = gr.id
                GROUP BY e.id;

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