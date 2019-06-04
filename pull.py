import os

def clone():
    os.system("git clone https://github.com/gujohncat/Website.git")

    os.system("chmod +x ./Website/gradlew")

    os.system("cd Website && ./gradlew build")

    os.system("java -jar Website/build/libs/$(ls Website/build/libs)")

def pull():
    os.system("git pull")

    os.system("rm /build/libs/$(ls /build/libs)")

    os.system("./gradlew build")

    os.system("java -jar Website/build/libs/$(ls Website/build/libs)")

pull()