$RootDir = Resolve-Path .
$DirName = Split-Path -Leaf $RootDir
if ( $DirName -eq "setup" )
{
    cd ..
}

python -m venv .venv
.\.venv/Scripts/activate
python -m pip install -r requirements.txt