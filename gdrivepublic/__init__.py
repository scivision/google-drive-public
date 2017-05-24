import pathvalidate
from pathlib import Path
#%%
def isgdrive(path):
    path = Path(path).expanduser()

    for p in path.parents:
        print(p)
        gd = p/'.gd'
        if gd.is_dir() and (gd/'credentials.json').is_file():
            return True
            
    return False  # fallthru in case none of the parents were True

def safename(fn):
    """
    returns cross-platform safe name WITHOUT directory
    """
    if isinstance(fn,Path):
        fn = fn.name
    return pathvalidate.sanitize_filename(fn,'-')

def browser():
    from platform import system
    from selenium import webdriver

    syst = system().lower()
    try:
        drv = webdriver.Firefox()
        print('using Firefox')
    except Exception:
        if 'windows' in syst:
            chrome='c:\chromedriver\chromedriver.exe'
        elif 'linux' in syst:
            chrome='/usr/lib/chromium-browser/chromedriver'
        else:
            chrome=None

        drv = webdriver.Chrome(chrome)
        print('using Chrome')

    return drv
