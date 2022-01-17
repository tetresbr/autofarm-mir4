I_Icon = bin\autofarm.ico
IfExist, %I_Icon%
  Menu, Tray, Icon, %I_Icon%

pix = bin\qrcode-pix.png
FileInstall, bin\qrcode.png, %pix%, 1
;configurações da tela
Gui, Color, black
Gui, Font, s11 cWhite

;Checkboxs 
Gui, Add, CheckBox, vFarm,Autofarm?
Gui, Add, CheckBox, vUlt,Ultar?
Gui, Add, CheckBox, vDesvio,Desviar?
;Edits
Gui, Add, Text,, Quanto tempo para chamar proximo mob?
Gui, Add, Edit,cBlack h20 w30 vTempo,2.5
Gui, Add, Text,, Quantos mobs agrar?
Gui, Add, Edit,cBlack h20 w30 vMobs,8
;Botão Startbot
Gui, Add, Button, w280 x10 y200 gStart_Bot,Iniciar Autofarm

;Botão Stopbot
Gui, Add, Button, w280 x10 y270 gStop_Bot,Parar Bot

;Botão StartDarksteel
Gui, Add, Button, w280 x10 y235 gStart_Dark,Minerar Darksteel

;Texto Doação
Gui, Add, Text,x105 y310, Doe para o PIX 
Gui, Add, Picture, x55 w200 h200, %pix%
;chamar tela
Gui, Show, w300 h550, Autofarm Mir4
return

GuiClose:
  FileDelete, config.py
  Sleep, 50
  Process,Close,conhost.exe
  Sleep, 50
  Process,Close,python.exe
  ExitApp
  return

Start_Bot:
  FileDelete, config.py
  Sleep, 50
  Gui, Submit, NoHide
  FileAppend,
(
farmar = %Farm% 
ult = %Ult% 
desvio = %Desvio% 
tempo = %Tempo% 
mobs = %Mobs%
), config.py
  Sleep, 5000
  commands=
  (join&
  python "bin\farm.py"`n
  )
  Run, cmd /c %commands%
  return 

Stop_Bot:
  FileDelete, config.py
  Sleep, 50
  Process,Close,conhost.exe
  Sleep, 50
  Process,Close,python.exe
  return

Start_Dark:
  commands=
  (join&
  python "bin\darksteel.py"`n
  )
  Run, cmd /c %commands%
  return 

;Hotkeys
Numpad1::
  Gui, Submit, NoHide
  FileAppend,
(
farmar = %Farm% 
ult = %Ult% 
desvio = %Desvio% 
tempo = %Tempo% 
mobs = %Mobs%
), config.py
  Sleep, 5000
  commands=
  (join&
  python "bin\farm.py"`n
  )
  Run, cmd /c %commands%
  return 
Numpad4::
  FileDelete, config.py
  Sleep, 50
  Process,Close,conhost.exe
  Sleep, 50
  Process,Close,python.exe
Return


