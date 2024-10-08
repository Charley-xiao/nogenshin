import subprocess
import sys
import os
import functools
import platform

class GenshinLauncher:
    def __init__(self, genshin_path=None):
        if genshin_path:
            self.genshin_path = genshin_path
        else:
            self.genshin_path = os.getenv('GENSHIN_PATH') or self.auto_detect()

        if not self.genshin_path:
            raise ValueError("Genshin Path not provided and auto-detection failed. Please set it via parameter or 'GENSHIN_PATH' environment variable.")
        
        if not os.path.isfile(self.genshin_path):
            raise FileNotFoundError(f"Genshin executable not found at {self.genshin_path}")

    def auto_detect(self):
        """
        Try to auto-detect the Genshin Impact executable path.
        """
        system = platform.system()
        possible_paths = []
        if system == "Windows":
            possible_paths = [
                os.path.expandvars(r"%ProgramFiles%\\Genshin Impact\\GenshinImpact.exe"),
                os.path.expandvars(r"%ProgramFiles(x86)%\\Genshin Impact\\GenshinImpact.exe"),
            ]
            try:
                import winreg
                reg_path = r"SOFTWARE\\Microsoft\Windows\\CurrentVersion\\Uninstall"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
                    i = 0
                    while True:
                        try:
                            subkey_name = winreg.EnumKey(key, i)
                            subkey_path = f"{reg_path}\\{subkey_name}"
                            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path) as subkey:
                                try:
                                    display_name, _ = winreg.QueryValueEx(subkey, "DisplayName")
                                    if "Genshin Impact" in display_name:
                                        install_location, _ = winreg.QueryValueEx(subkey, "InstallLocation")
                                        genshin_exe = os.path.join(install_location, "GenshinImpact.exe")
                                        if os.path.exists(genshin_exe):
                                            return genshin_exe
                                except FileNotFoundError:
                                    pass
                        except OSError:
                            break
                        i += 1
            except FileNotFoundError:
                pass

        elif system == "Darwin":
            possible_paths = [
                "/Applications/Genshin Impact.app/Contents/MacOS/GenshinImpact",
            ]
        elif system == "Linux":
            possible_paths = [
                "/usr/local/bin/GenshinImpact",
            ]
        for path in possible_paths:
            if os.path.isfile(path):
                return path
        return None

    def launch(self):
        try:
            subprocess.Popen([self.genshin_path], shell=True)
            print("Genshin Impact started.")
        except Exception as e:
            print(f"Failed to start Genshin Impact: {e}")

launcher = None

def initialize_launcher(genshin_path=None):
    global launcher
    try:
        launcher = GenshinLauncher(genshin_path)
    except Exception as e:
        launcher = None
        print(f"WARNING: {e}")

initialize_launcher()

def configure_genshin(path):
    """
    Dynamically configure the Genshin Impact executable path.

    :param path: the path to the Genshin Impact executable.
    """
    initialize_launcher(genshin_path=path)

def start(func):
    """
    Decorator to start Genshin Impact before running the function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Function '{func.__name__}' raised an exception: {e}")
            if launcher:
                launcher.launch()
            else:
                print("Genshin Impact launcher not configured.")
            raise  
    return wrapper
