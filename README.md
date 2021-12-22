REPO NUEVA
1 GIT INIT
2 GIT STATUS
3 GIT add -A  o  git add .  o  git add [file]
4 Git config --global user.email jmajar18@gmail.com
5 Git commit -m "mensaje"
6 git remote add origin -direcion github-
7 git push origin master

REPO EXISTENTE
git remote add origin https://github.com/JavierManjarres/jmb23.git
git branch -M main
git push -u origin main

--SOLUCION--

Usuario@JAVIER-PC MINGW64 ~/Desktop/Proyecto TPM (main)
$ git init
Reinitialized existing Git repository in C:/Users/Usuario/Desktop/Proyecto TPM/.git/

Usuario@JAVIER-PC MINGW64 ~/Desktop/Proyecto TPM (main)
$ git config --global user.name "javier"

Usuario@JAVIER-PC MINGW64 ~/Desktop/Proyecto TPM (main)
$  git config --global user.email "jmajar18@gmail.com"

Usuario@JAVIER-PC MINGW64 ~/Desktop/Proyecto TPM (main)
$ git remote add origin https://github.com/JavierManjarres/tpm.git
error: remote origin already exists.

Usuario@JAVIER-PC MINGW64 ~/Desktop/Proyecto TPM (main)
$ git remote --verbose
origin  https://github.com/JavierManjarres/tpm.git (fetch)
origin  https://github.com/JavierManjarres/tpm.git (push)

Usuario@JAVIER-PC MINGW64 ~/Desktop/Proyecto TPM (main)
$ git branch -M main

Usuario@JAVIER-PC MINGW64 ~/Desktop/Proyecto TPM (main)
$ git push -u origin main
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/JavierManjarres/tpm.git/'

Usuario@JAVIER-PC MINGW64 ~/Desktop/Proyecto TPM (main)
$ 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
bash: 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: command not found

EN LA VENTANA QUE EXPLOTA USUARIO: javier
Y CONTRASEÑA: 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 
GENERA CONTRASEÑA EN Personal access tokens VE A CONFIGURACION

Usuario@JAVIER-PC MINGW64 ~/Desktop/Proyecto TPM (main)
$ git push -u origin main
Enumerating objects: 50, done.
Counting objects: 100% (50/50), done.
Delta compression using up to 2 threads
Compressing objects: 100% (50/50), done.
Writing objects: 100% (50/50), 1.54 MiB | 1.67 MiB/s, done.
Total 50 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), done.
To https://github.com/JavierManjarres/tpm.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.























































































































































CLONAR GITHUB
git clone -direccion github-
virtualenv --python=python3.8 myvenv
source myvenv/bin/activate
