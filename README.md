REPO NUEVA
1 GIT INIT
2 GIT STATUS
3 GIT add -A  o  git add .  o  git add [file]
4 Git config --global user.email jmajar18@gmail.com
5 Git commit -m "mensaje"
6 git remote add origin -direcion github-
7 git push -u origin main

REPO EXISTENTE
git remote add origin https://github.com/JavierManjarres/jmb23.git
git branch -M main
git push -u origin main

--solucion--
Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)
$ git config --global user.name "javier"

Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)
$ git config --global user.email "jmajar18@gmail.com"
Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)

$ git status
On branch main
nothing to commit, working tree clean

Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)
$ echo "# App-Speech-Text" >> README.md

Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)
$ git init
Reinitialized existing Git repository in C:/Users/Usuario/Desktop/SpeechtoText/.git/

Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)
$ git add README.md
warning: LF will be replaced by CRLF in README.md.
The file will have its original line endings in your working directory

Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)
$ git remote add origin https://github.com/JavierManjarres/App-Speech-Text.git
error: remote origin already exists.

Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)
$ git remote --verbose
origin  https://github.com/JavierManjarres/App-Speech-Text (fetch)
origin  https://github.com/JavierManjarres/App-Speech-Text (push)

Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)
$ git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'https://github.com/JavierManjarres/App-Speech-Text'

Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)
$ git branch -M main

Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)
$ git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'https://github.com/JavierManjarres/App-Speech-Text'

Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)
$ git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'https://github.com/JavierManjarres/App-Speech-Text'

Usuario@DESKTOP-54406F4 MINGW64 ~/Desktop/SpeechtoText (main)
$ git push -u origin main
Enumerating objects: 17, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 2 threads
Compressing objects: 100% (13/13), done.
Writing objects: 100% (17/17), 6.29 KiB | 715.00 KiB/s, done.
Total 17 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/JavierManjarres/App-Speech-Text
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.


CLONAR GITHUB
git clone -direccion github-
virtualenv --python=python3.8 myvenv
source myvenv/bin/activate
