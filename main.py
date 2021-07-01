import subprocess
import os
import ctypes

DIR = r'C:\WINDOWS\system32'


def is_active():
    os.chdir(DIR)
    cmd = 'bcdedit /enum | find "hypervisorlaunchtype"'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    subprocess.Popen.wait(proc)
    return 'Auto' in str(proc.stdout.readline())


def togle_hyperv():
    os.chdir(DIR)
    cmd = 'bcdedit /set hypervisorlaunchtype off' if is_active() else 'bcdedit /set hypervisorlaunchtype auto'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL)
    subprocess.Popen.wait(proc)
    return proc.returncode


def pause():
    print('Press enter key to exit...', end='')
    input()
    quit()


if __name__ == '__main__':
    is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    if not is_admin:
        print('Run as administrator')
        pause()

    print('Hyper-V is activated' if is_active() else 'Hyper-V is deactivated')
    print('Do you want to switch to Hyper-V? [Y/n] > ', end='')
    ans = input()
    should_toggle = True if len(ans) != 0 and ans[0].lower() == 'y' else False
    if not should_toggle:
        pause()

    if togle_hyperv() != 0:
        print('Failed to switch Hyper-V')
        pause()
    print('Hyper-V switching finished successfully')

    print('Do you want to reboot? [Y/n] > ', end='')
    ans = input()
    should_reboot = True if len(ans) != 0 and ans[0].lower() == 'y' else False
    if should_reboot:
        os.system('shutdown /r /t 1')
