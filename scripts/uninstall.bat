@START
@ECHO OFF
:: Some sudo-esque batch script command gibberish meant to ask for administrator permissions and run everything afterwards properly
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
cd ..
del /s/q C:\Windows\System32\PySH
del /s/q C:\Windows\System32\pysh.bat
exit
