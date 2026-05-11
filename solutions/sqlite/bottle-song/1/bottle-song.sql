-- Schema:
-- CREATE TABLE "bottle-song" (
--         start_bottles INTEGER NOT NULL,
--         take_down     INTEGER NOT NULL,
--         result        TEXT
-- );
-- Task: update bottle-song table and set the result based on the
-- start_bottles and take_down.
WITH RECURSIVE
    num_words(num, word) AS (
        VALUES
            (0,  'No'),
            (1,  'One'),
            (2,  'Two'),
            (3,  'Three'),
            (4,  'Four'),
            (5,  'Five'),
            (6,  'Six'),
            (7,  'Seven'),
            (8,  'Eight'),
            (9,  'Nine'),
            (10, 'Ten')
    ),
    nums(num) AS (
        SELECT start_bottles
        UNION ALL
        SELECT num - 1
        FROM nums
        WHERE num > (1 + start_bottles - take_down)
    ),
    first_line(num, line) AS (
        SELECT n.num,
               printf(
                   '%s green bottle%s hanging on the wall,',
                   (SELECT word FROM num_words AS w WHERE n.num = w.num),
                   IIF(n.num = 1, '', 's')
               )
        FROM nums AS n
    ),
    last_line(num, line) AS (
        SELECT n.num,
               printf(
                   'There''ll be %s green bottle%s hanging on the wall.',
                   (SELECT lower(word) FROM num_words AS w WHERE n.num - 1 = w.num),
                   IIF(n.num - 1 = 1, '', 's')
               )
        FROM nums AS n
    ),
    verses(num, verse) AS (
        SELECT n.num,
               first_line.line || char(10) ||
               first_line.line || char(10) ||
               'And if one green bottle should accidentally fall,' || char(10) ||
               last_line.line
        FROM nums AS n
        INNER JOIN first_line ON n.num = first_line.num
        INNER JOIN last_line  ON n.num = last_line.num
    )
UPDATE "bottle-song"
SET result = (
    SELECT group_concat(verse, char(10) || char(10))
    FROM verses
);