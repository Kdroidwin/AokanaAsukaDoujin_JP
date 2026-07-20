# Full Japanese title artwork with the original menu actions.
screen main_menu():
    tag menu

    add "tl/japanese/4a1cc2ff-e402-4904-a683-aecce21decbe.png" xysize (config.screen_width, config.screen_height)

    button:
        xpos 270
        ypos 145
        xsize 520
        ysize 115
        action Play("effect", "audio/sound/click.ogg"), Start()
        background None
        hover_background "#ffffff20"

    button:
        xpos 270
        ypos 305
        xsize 520
        ysize 115
        action Play("effect", "audio/sound/click.ogg"), ShowMenu("game_load")
        background None
        hover_background "#ffffff20"

    button:
        xpos 270
        ypos 465
        xsize 520
        ysize 115
        action Play("effect", "audio/sound/click.ogg"), ShowMenu("sys_config")
        background None
        hover_background "#ffffff20"

    button:
        xpos 270
        ypos 625
        xsize 520
        ysize 115
        action Play("effect", "audio/sound/click.ogg"), Function(setattr, persistent, "clearall", True), ShowMenu("extra_page")
        background None
        hover_background "#ffffff20"

    button:
        xpos 270
        ypos 785
        xsize 520
        ysize 115
        action Play("effect", "audio/sound/click.ogg"), Quit(confirm=True)
        background None
        hover_background "#ffffff20"
