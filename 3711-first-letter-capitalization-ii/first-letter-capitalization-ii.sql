WITH RECURSIVE words AS (
    SELECT
        content_id,
        content_text,
        1 AS start_pos,
        CASE
            WHEN LOCATE(' ', content_text) = 0
                THEN LENGTH(content_text) + 1
            ELSE LOCATE(' ', content_text)
        END AS end_pos
    FROM user_content

    UNION ALL

    SELECT
        content_id,
        content_text,
        end_pos + 1,
        CASE
            WHEN LOCATE(' ', content_text, end_pos + 1) = 0
                THEN LENGTH(content_text) + 1
            ELSE LOCATE(' ', content_text, end_pos + 1)
        END
    FROM words
    WHERE end_pos <= LENGTH(content_text)
),

word_parts AS (
    SELECT
        content_id,
        content_text,
        start_pos,
        SUBSTRING(
            content_text,
            start_pos,
            end_pos - start_pos
        ) AS word
    FROM words
),

converted AS (
    SELECT
        content_id,
        content_text,
        start_pos,

        CASE
            /* Normal hyphen between two alphabetic parts */
            WHEN word REGEXP '^[A-Za-z]+-[A-Za-z]+$' THEN
                CONCAT(
                    UPPER(LEFT(SUBSTRING_INDEX(word, '-', 1), 1)),
                    LOWER(SUBSTRING(SUBSTRING_INDEX(word, '-', 1), 2)),
                    '-',
                    UPPER(LEFT(SUBSTRING_INDEX(word, '-', -1), 1)),
                    LOWER(SUBSTRING(SUBSTRING_INDEX(word, '-', -1), 2))
                )

            /* Everything else: capitalize only first character */
            ELSE
                CONCAT(
                    UPPER(LEFT(word, 1)),
                    LOWER(SUBSTRING(word, 2))
                )
        END AS converted_word
    FROM word_parts
)

SELECT
    content_id,
    content_text AS original_text,
    GROUP_CONCAT(
        converted_word
        ORDER BY start_pos
        SEPARATOR ' '
    ) AS converted_text
FROM converted
GROUP BY content_id, content_text
ORDER BY content_id;