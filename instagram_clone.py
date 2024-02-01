import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK

    def clicked(e):
        e.control.selected = not e.control.selected
        e.control.update()

    layout = ft.Container(
        bgcolor=ft.colors.WHITE,
        width=500,
        # height=700,
        border_radius=ft.border_radius.all(10),
        shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.TEAL),
        content=ft.Column(
            controls=[
                ft.ListTile(
                    title=ft.Text(value='NASA', color=ft.colors.BLACK,
                                  weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text(value='A lua!', color=ft.colors.BLACK,),
                    leading=ft.Image(
                        src='https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg',
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    trailing=ft.Icon(name=ft.icons.MORE_HORIZ,
                                     color=ft.colors.BLACK)
                ),
                ft.Image(
                    src='https://upload.wikimedia.org/wikipedia/commons/9/98/Aldrin_Apollo_11_original.jpg',
                    fit=ft.ImageFit.CONTAIN,
                    # height=100,
                    # width=500
                ),
                ft.Container(
                    padding=ft.padding.all(15),
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.ResponsiveRow(
                                columns=12,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.IconButton(
                                        col=1,
                                        icon=ft.icons.FAVORITE_BORDER,
                                        selected_icon=ft.icons.FAVORITE,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.RED,

                                    ),
                                    ft.Icon(
                                        col=1,
                                        name=ft.icons.CHAT_BUBBLE_OUTLINE,
                                        color=ft.colors.BLACK,

                                    ),
                                    ft.Icon(
                                        col=1,
                                        name=ft.icons.SEND,
                                        color=ft.colors.BLACK,

                                    ),
                                    ft.Icon(
                                        col=8,
                                        # name= ft.icons.SEND,
                                        # color=ft.colors.BLACK,
                                    ),
                                    ft.IconButton(
                                        col=1,
                                        icon=ft.icons.BOOKMARK_BORDER,
                                        selected_icon=ft.icons.BOOKMARK_ROUNDED,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.BLACK,

                                    ),
                                ]
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text='Curtido por', style=ft.TextStyle(
                                        color=ft.colors.BLACK, size=16)),
                                    ft.TextSpan(text=' programador Aventureiro', style=ft.TextStyle(
                                        color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),
                                    ft.TextSpan(text=' e', style=ft.TextStyle(
                                        color=ft.colors.BLACK, size=16)),
                                    ft.TextSpan(text=' 1969 outros', style=ft.TextStyle(
                                        color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),
                                ]
                            ),
                            ft.Text(
                                value='Um pequeno passo para o homem, um grande passo para a humanidade!',
                                color=ft.colors.BLACK,
                                size=16,
                            ),
                            ft.Text(
                                value='55 ANOS ATRÁS',
                                color=ft.colors.GREY,
                                size=14,
                                offset=ft.Offset(0, -0.5)
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text='elonMusk', style=ft.TextStyle(
                                        color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),
                                    ft.TextSpan(text=' Agora bora para Marte! #SpaceX', style=ft.TextStyle(
                                        color=ft.colors.BLACK, size=16)),
                                ]
                            ),
                            ft.Text(
                                value='Ver todos os 2.025 comentários',
                                color=ft.colors.GREY,
                                size=14,

                            ),       
                            ft.TextField(
                                hint_text='Adicione um Comentário ...',
                                hint_style=ft.TextStyle(color=ft.colors.GREY,size=16),
                                border=ft.InputBorder.UNDERLINE,
                                border_color=ft.colors.GREY,
                                border_width=1,
                                color=ft.colors.GREY_100,
                            )                     
                        ]
                    )
                )
            ]

        )

    )
    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)
