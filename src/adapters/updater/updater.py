import requests
import tarfile
import shutil
import glob
import os
import subprocess

def updatePiRowFlo():

    print(" ")
    print(" ")
    print(" ")
    print("========== PiRowFlo Updater ========================================")
    print(" ")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    updatetmpfolder = "/tmp/pirowfloupdate"
    updatefinaldest = BASE_DIR
    #updatefinaldest = "/home/pi/test"

    response = requests.get("https://api.github.com/repos/yoda-git/pirowflo/releases/latest")
    Version = response.json()["name"]
    print(" ")
    print("========== Getting newest {0} of PiRowFlo from Github ==========".format(Version))
    print(" ")

    if os.path.exists(updatetmpfolder):
        shutil.rmtree(updatetmpfolder)
    os.makedirs(updatetmpfolder)
    response = requests.get("https://api.github.com/repos/yoda-git/pirowflo/releases/latest")
    resp = response.json()["tarball_url"]
    Version = response.json()["name"]
    response2 = requests.get(resp, stream=True)
    file = open("/tmp/pirowfloupdate/pirowflo-lastversion.tar.gz","wb")
    file.write(response2.content)
    file.close()

    print(" ")
    print("========== Extracting newest release of PiRowFlo in /tmp ===========")
    print(" ")


    my_tar = tarfile.open(updatetmpfolder + "/pirowflo-lastversion.tar.gz")
    my_tar.extractall(updatetmpfolder)  # specify which folder to extract to
    my_tar.close()

    print(" ")
    print("========== Copy newest release of PiRowFlo to target folder ========")
    print(" ")

    pirowfloupdatefolder = glob.glob(updatetmpfolder + "/yoda-git-pirowflo-*")
    if os.path.exists(updatefinaldest):
        shutil.rmtree(updatefinaldest)

    cmdcopy = '/bin/su -c "/bin/cp -r '+pirowfloupdatefolder[0]+' '+updatefinaldest +'" '+ '- pi'
    subprocess.run(cmdcopy,shell=True)
    #shutil.copytree(pirowfloupdatefolder[0], updatefinaldest, symlinks=True)
    #shutil.rmtree(updatetmpfolder)
    cmdchangefolder = "cd " + BASE_DIR
    subprocess.run(cmdchangefolder,shell=True)
    print(" ")
    print("=========== Starting ./install script to update! ===================")
    print(" ")
    print(BASE_DIR)
    installcmd = BASE_DIR + "/install.sh"
    #installcmd = "/home/pi/test/install.sh"

    subprocess.run(installcmd)

if __name__ == "__main__":
    updatePiRowFlo()