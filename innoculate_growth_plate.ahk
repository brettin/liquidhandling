#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

Run, "C:\Program Files (x86)\Hudson Robotics\SoftLinx V\SoftLinxVProtocolEditor.exe" %A_ScriptDir%\innoculate_growth_plate.slvp
WinActivate, SoftLinx V
Sleep, 5000
MouseClick, Left, 300, 45
Sleep, 1000
if WinActive("Not Saved") {
	Send, {Tab}{Enter}
	Sleep, 5000
}
if WinActive("Start Now?") {
	Send, {Enter}
	Sleep, 5000
}