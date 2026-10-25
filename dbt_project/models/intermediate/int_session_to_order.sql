SELECT
    o.order_id,
    o.created_at AS order_created_at,
    o.website_session_id,
    o.user_id,
    o.primary_product_id,
    o.items_purchased,
    o.price_usd AS order_revenue_usd,
    s.utm_source,
    s.utm_campaign,
    s.utm_content,
    s.device_type,
    s.http_referer,
    s.is_repeat_session,
    s.created_at AS session_created_at
FROM {{ ref('stg_orders') }} AS o
LEFT JOIN {{ ref('stg_website_sessions') }} AS s
    ON o.website_session_id = s.website_session_id