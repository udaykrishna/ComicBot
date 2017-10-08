import comic_scrapers as cs
import comic

grabers=[cs.xkcd_grab, cs.explosm_grab, cs.penny_arcade_grab, cs.nedroid_grab,
                cs.moonbeard_grab, cs.smbc_grab, cs.wumo_grab, cs.loading_artist_grab,
                cs.cad_grab, cs.adamathome_grab]
comic_details = {graber:graber().details for graber in grabers}
comic_graber_names = {graber().name:graber for graber in grabers}

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def random_grab():
    return random.choice(grabers)()

def get_inline_comics():
    pass
