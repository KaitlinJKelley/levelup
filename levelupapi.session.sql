CREATE VIEW GAMES_BY_USER AS
SELECT
    g.id,
    g.name,
    g.maker,
    g.gametype_id,
    g.num_of_players,
    g.skill_level,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_game g
JOIN
    levelupapi_gamer gr ON g.gamer_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id;
