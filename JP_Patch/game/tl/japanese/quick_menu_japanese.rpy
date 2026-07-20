# Keep the original quick-menu icons, positions, and actions intact.
screen quick_menu():
    if quick_menu:
        zorder 100

        key "mousedown_4" action Play("effect", "audio/sound/click.ogg"), ShowMenu("history")
        key "K_ESCAPE" action Play("effect", "audio/sound/click.ogg"), ShowMenu("sys_config")

        vbox:
            spacing 5
            xcenter 0.864
            ycenter 0.82

            imagebutton idle "images/ui/auto1.png" hover "images/ui/auto2.png" selected_idle "images/ui/auto2.png":
                at transform:
                    zoom 0.9
                action Play("effect", "audio/sound/click.ogg"), Preference("auto-forward", "toggle")
                tooltip "自動送り"

            imagebutton idle "images/ui/skip1.png" hover "images/ui/skip2.png" selected_idle "images/ui/skip2.png":
                at transform:
                    zoom 0.9
                action Play("effect", "audio/sound/click.ogg"), Skip()
                tooltip "スキップ"

            imagebutton idle "images/ui/jump1.png" hover "images/ui/jump2.png":
                at transform:
                    zoom 0.9
                action Play("effect", "audio/sound/click.ogg"), Skip(fast=True, confirm=True)
                tooltip "次の選択肢までスキップ"

            imagebutton idle "images/ui/history1.png" hover "images/ui/history2.png":
                at transform:
                    zoom 0.9
                action Play("effect", "audio/sound/click.ogg"), ShowMenu("history")
                tooltip "履歴"

            imagebutton idle "images/ui/config1.png" hover "images/ui/config2.png":
                at transform:
                    zoom 0.9
                action Play("effect", "audio/sound/click.ogg"), ShowMenu("sys_config")
                tooltip "設定"

            imagebutton idle "images/ui/hide1.png" hover "images/ui/hide2.png":
                at transform:
                    zoom 0.9
                action Play("effect", "audio/sound/click.ogg"), HideInterface()
                tooltip "UIを隠す"

        vbox:
            spacing 4
            xcenter 0.945
            ycenter 0.83

            imagebutton idle "images/ui/save1.png" hover "images/ui/save2.png":
                at transform:
                    zoom 0.83
                action Play("effect", "audio/sound/click.ogg"), ShowMenu("game_save")
                tooltip "セーブ"

            imagebutton idle "images/ui/load1.png" hover "images/ui/load2.png":
                at transform:
                    zoom 0.83
                action Play("effect", "audio/sound/click.ogg"), ShowMenu("game_load")
                tooltip "ロード"

            imagebutton idle "images/ui/qsave1.png" hover "images/ui/qsave2.png":
                at transform:
                    zoom 0.83
                action Play("effect", "audio/sound/click.ogg"), Confirm("クイックセーブしますか？", QuickSave(message="クイックセーブしました"))
                tooltip "クイックセーブ"

            imagebutton idle "images/ui/qload1.png" hover "images/ui/qload2.png":
                at transform:
                    zoom 0.83
                action Play("effect", "audio/sound/click.ogg"), QuickLoad(confirm=True)
                tooltip "クイックロード"

            imagebutton idle "images/ui/quit1.png" hover "images/ui/quit2.png":
                at transform:
                    zoom 0.83
                action Play("effect", "audio/sound/click.ogg"), Quit(confirm=True)
                tooltip "終了"

        text "{color=#ffffff}{size=18}UNOFFICIAL{/size}{/color}" outlines [(2, "#353535", 0, 0)] xcenter 0.95 ycenter 0.99

    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            has frame
            background None
            xalign 0.5
            text tooltip at tip size 30 color "#6d6e6b" outlines [(2, "#ffffff", 0, 0)]
