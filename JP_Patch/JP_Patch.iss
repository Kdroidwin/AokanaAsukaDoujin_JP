#define AppName "蒼の彼方のフォーリズム -世界への答え- 日本語化パッチ"
#define AppVersion "1.0"

[Setup]
AppId={{0F3B0373-06B8-4BC9-8D1A-8160FF6CB4F4}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher=Japanese Localization Patch
DefaultDirName={autopf}\AokanaAsukaDoujin
DisableProgramGroupPage=yes
Uninstallable=no
OutputDir=JP_Patch_Output
OutputBaseFilename=JP_Patch
Compression=lzma2
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"

[Types]
Name: "standard"; Description: "通常インストール（追加CG差し替えなし）"
Name: "custom"; Description: "カスタムインストール"; Flags: iscustom

[Components]
Name: "cg_replace"; Description: "追加CGを指定画像に差し替える（任意）"; Types: custom

[Files]
Source: "JP_Patch\game\*"; DestDir: "{app}\game"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "JP_Patch\optional_cg\game\*"; DestDir: "{app}\game"; Components: cg_replace; Flags: ignoreversion recursesubdirs createallsubdirs

[InstallDelete]
Type: files; Name: "{app}\game\tl\japanese\ui_override.rpy"
Type: files; Name: "{app}\game\tl\japanese\ui_override.rpyc"
Type: files; Name: "{app}\game\tl\japanese\*.rpyc"
Type: files; Name: "{app}\game\tl\japanese\code\*.rpyc"
Type: files; Name: "{app}\game\images\extra\extra21@2.08.png"

[Code]
function GamePath(): String;
begin
  Result := AddBackslash(WizardDirValue) + 'game';
end;

function IsValidGameFolder(): Boolean;
begin
  Result := DirExists(GamePath()) and
    FileExists(AddBackslash(WizardDirValue) + 'aokana_asuka_doujin.exe');
end;

function NextButtonClick(CurPageID: Integer): Boolean;
begin
  Result := True;
  if CurPageID = wpSelectDir then begin
    if not IsValidGameFolder() then begin
      MsgBox('元ゲームのフォルダを選択してください。' + #13#10 +
        'game フォルダと aokana_asuka_doujin.exe が必要です。', mbError, MB_OK);
      Result := False;
    end;
  end;
end;
