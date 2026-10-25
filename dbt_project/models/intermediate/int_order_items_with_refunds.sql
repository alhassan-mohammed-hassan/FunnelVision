WITH refunds AS (
    SELECT
        order_item_id,
        SUM(refund_amount_usd) AS total_refund_usd
    FROM {{ ref('stg_order_item_refunds') }}
    GROUP BY order_item_id
)

SELECT
    oi.order_item_id,
    oi.order_id,
    oi.product_id,
    oi.created_at AS order_item_created_at,
    oi.is_primary_item,
    oi.price_usd AS item_revenue_usd,
    oi.cogs_usd AS item_cogs_usd,
    COALESCE(r.total_refund_usd, 0) AS total_refund_usd,
    oi.price_usd - COALESCE(r.total_refund_usd, 0)
        AS net_revenue_usd
FROM {{ ref('stg_order_items') }} AS oi
LEFT JOIN refunds AS r
    ON oi.order_item_id = r.order_item_id