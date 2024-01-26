from pynput import keyboard

MAX_ENTITIES_LENGTH = 6
listener = None
key_tab = []
keyController = keyboard.Controller()
Key = keyboard.Key
initialized = False

html_entities_mapping = {
    "aacute": "á",
    "eacute": "é",
    "iacute": "í",
    "oacute": "ó",
    "uacute": "ú",
    "agrave": "à",
    "egrave": "è",
    "igrave": "ì",
    "ograve": "ò",
    "ugrave": "ù",
    "acirc": "â",
    "ecirc": "ê",
    "icirc": "î",
    "ocirc": "ô",
    "ucirc": "û",
    "atilde": "ã",
    "etilde": "ẽ",
    "itilde": "ĩ",
    "otilde": "õ",
    "utilde": "ũ",
    "auml": "ä",
    "euml": "ë",
    "iuml": "ï",
    "ouml": "ö",
    "uuml": "ü",
    "ccedil": "ç",
    "nbsp": "Non-breaking space",
}


def bind_listener():
    global listener
    listener = keyboard.Listener(on_release=on_release)
    listener.start()


def initialize(char) :
    global initialized
    if (char == ';' and len(key_tab) == 0) or initialized :
        initialized = True
        return True
    
    return False


def append_to_keytab(char) :
    global key_tab, initialized
    if char != ';' :
        if len(key_tab) < MAX_ENTITIES_LENGTH :
            key_tab.append(char)

            return True
        else :
            key_tab = []
            initialized = False

    return False


''' map entity to corresponding accent.
 If entity_candidate is found in entites dictionnary keys 
 then stop listener and delete entity charactere and
 replace it by corresponding accent'''

def mapper(entity_candidate) :
    global key_tab, initialized
    
    if entity_candidate in html_entities_mapping:
        listener.stop()

        for i in range( len(entity_candidate) + 2 ): # + 2 beacuse we also delete the `;` charactere
            keyController.press(Key.backspace)
            keyController.release(Key.backspace)

        keyController.type(html_entities_mapping[entity_candidate])
        key_tab = []
        initialized = False
        bind_listener()
    else :
        key_tab = []
        if entity_candidate != '' : # because the fisrt time entity_candidate will be equal to ''
            initialized = False


def on_release(key: keyboard.Key | keyboard.KeyCode):
    global key_tab, initialized
    
    try:
        has_been_initialized = initialize(key.char)
        if has_been_initialized :
            has_append = append_to_keytab(key.char)

            if not has_append:
                entity_candidate = ''.join(key_tab)
                mapper(entity_candidate=entity_candidate)

    except AttributeError:
        if key == keyboard.Key.space or key == keyboard.Key.enter:
            key_tab = []
            initialized = False



def start_mapping():
    bind_listener()


def stop_mapping():
    global key_tab, initialized
    try:
        listener.stop()
        key_tab = []
        initialized = False
    except Exception:
        print('Exception while stoping listener')
