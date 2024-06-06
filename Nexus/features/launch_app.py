import subprocess

def launch_app(path_of_app):
    try:
        subprocess.Popen([path_of_app])
        return True
    except Exception as e:
        print(e)
        return False