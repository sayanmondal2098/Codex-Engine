
osDetails = {
    'ubuntu': 'sudo apt-get install -y',
    'debian': 'sudo apt-get install -y',
    'fedora': 'sudo dnf install -y',
    'centos': 'sudo yum install -y',
    'opensuse': 'sudo zypper install -y',
    'suse': 'sudo zypper install -y',
    'redhat': 'sudo yum install -y',
    'rhel': 'sudo yum install -y',
    'arch': 'sudo pacman -S --noconfirm',
    'windows': 'choco install -y',
    'macos': 'brew install -y',
    'alpine': 'sudo apk add -y',
    'gentoo': 'sudo emerge -y',
    'slackware': 'sudo slackpkg install -y',
    'solaris': 'sudo pkg install -y',
    'freebsd': 'sudo pkg install -y',
    'openbsd': 'sudo pkg_add -y',
    'netbsd': 'sudo pkg_add -y',
    'dragonfly': 'sudo pkg_add -y',
    'haiku': 'sudo pkgman install -y',
    'android': 'pkg install -y',
    'ios': 'pkg install -y',
    'cygwin': 'apt-cyg install -y',
    'msys': 'pacman -S --noconfirm',
    'msys2': 'pacman -S --noconfirm',
    'haiku': 'pkgman install -y',
}

def osInstallerqueryBuilder(osName, packageName):
    return osDetails[osName] + ' ' + packageName

# Path: src/util/osInstaller.py
# Compare this snippet from src/Test.py:
# # minion to connect with master and execute the command given by master in python
#
# import paramiko
#   
# # Define the username, password, and command to be executed
