import reflex as rx

config = rx.Config(
    app_name="vitreous_paddle",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)