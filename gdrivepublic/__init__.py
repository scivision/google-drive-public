import pathvalidate

try:
    from pathlib import Path
    Path().expanduser()
except (ImportError, AttributeError):
    from pathlib2 import Path
#%%
def isgdrive(path):
    path = Path(path).expanduser()

    for p in path.parents:
        print(p)
        gd = p/'.gd'
        if gd.is_dir() and (gd/'credentials.json').is_file():
            return True

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
    except Exception:
        if 'windows' in syst:
            chrome='c:\chromedriver\chromedriver.exe'
        elif 'linux' in syst:
            chrome='/usr/lib/chromium-browser/chromedriver'
        else:
            chrome=None

        drv = webdriver.Chrome(chrome)

    return drv