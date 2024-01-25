import flet as ft


def html_accent_mapper_app(page: ft.Page):
    page.window_min_width       = page.window_max_width =  905
    page.window_min_width       = page.window_max_height = 464
    page.vertical_alignment     = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment   = ft.CrossAxisAlignment.CENTER
    
    page.appbar = ft.AppBar(
        title=ft.Text(
            value="HTMLAccentMapper - use accent on QWERTY 😎",
            weight=ft.FontWeight.W_500
            ),
        bgcolor=ft.colors.SURFACE_VARIANT,
        center_title=True,
        
    )

    activaed_info_text = ft.Container(
        ft.Text("Deactivated", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        alignment=ft.alignment.center,
        width=500,
        height=70,
        bgcolor=ft.colors.RED,
    )

    deactivated_info_text = ft.Container(
        ft.Text("Activated", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        alignment=ft.alignment.center,
        width=500,
        height=70,
        bgcolor=ft.colors.GREEN,
    )

    switch_anim = ft.AnimatedSwitcher(
        content=activaed_info_text,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=90,
        reverse_duration=90,
        switch_in_curve=ft.AnimationCurve.EASE_IN,
        switch_out_curve=ft.AnimationCurve.EASE_IN
    )

    def animate(e):
        if(switch_anim.content == activaed_info_text):
            switch_anim.content = deactivated_info_text
        else:
            switch_anim.content = activaed_info_text

        switch_anim.update()

    page.add(
        switch_anim,
        ft.FilledButton(
            "Activate / Deactivate",
            width=400,
            height=80,
            on_click=animate,
        )
    )



ft.app(target=html_accent_mapper_app)