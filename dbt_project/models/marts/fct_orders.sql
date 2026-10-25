WITH orders AS (
    SELECT *
    FROM {{ ref('stg_orders') }}
),

order_items AS (
    SELECT *
    FROM {{ ref('int_order_items_with_refunds') }}
),

order_metrics AS (
    SELECT
        order_id,
        SUM(item_revenue_usd) AS gross_item_revenue_usd,
        SUM(item_cogs_usd) AS total_cogs_usd,
        SUM(total_refund_usd) AS total_refunds_usd,
        SUM(net_revenue_usd) AS net_revenue_usd
    FROM order_items
    GROUP BY order_id
)

SELECT
    o.order_id,
    o.created_at AS order_created_at,
    o.website_session_id,
    o.user_id,
    o.primary_product_id,
    o.items_purchased,
    o.price_usd AS order_revenue_usd,
    COALESCE(m.gross_item_revenue_usd, 0) AS gross_item_revenue_usd,
    COALESCE(m.total_cogs_usd, 0) AS total_cogs_usd,
    COALESCE(m.total_refunds_usd, 0) AS total_refunds_usd,
    COALESCE(m.net_revenue_usd, 0) AS net_revenue_usd,
    COALESCE(m.net_revenue_usd, 0)
        - COALESCE(m.total_cogs_usd, 0) AS estimated_profit_usd
FROM orders AS o
LEFT JOIN order_metrics AS m
    ON o.order_id = m.order_id