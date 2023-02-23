# myNextScreen
A minimal app to make sound when a mouse enters the adjacent screen in your multiple display environment.

<hr>
**To test the app**

Simpy download the files in the same folder and run the script below.
python ./myNextScreen.py

<hr>
**To get started:**

0) If you have not yet installed Nukita, install Nukita (https://pypi.org/project/Nuitka/)

   $ pip install Nuitka
1) Download all files in the same folder.  The folder name could be anything in English.
2) Open a termial in the folder.
3) Run the one-line script below.

nuitka --standalone --onefile --windows-disable-console --windows-icon-from-ico=.\nextScreen.ico --include-data-file=.\enter_sound.wav=.\enter_sound.wav --include-data-file=.\exit_sound.wav=.\exit_sound.wav .\nextScreen.py

4) Run the myNextScreen.exe
   You don't need any other files or folders to run the app once you have created the .exe file.
   
**To customize the sounds or icon**

1) Simply replace your wave file with the existing file.
