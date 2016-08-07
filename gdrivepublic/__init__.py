try:
    from pathlib import Path
    Path().expanduser()
except (ImportError, AttributeError):
    from pathlib2 import Path

#%%
def browser():
    from platform import system
    from selenium import webdriver

    syst = system().lower()
    try:
        drv = webdriver.Firefox()
    except Exception:
        if 'windows' in syst:
            chrome='c:\chromedriver\chromedriver.exe'
        elif 'linux' in syst:
            chrome='/usr/lib/chromium-browser/chromedriver'
        else:
            chrome=None

        drv = webdriver.Chrome(chrome)

    return drv