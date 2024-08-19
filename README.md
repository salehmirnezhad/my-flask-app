My Flask App

In project ye yek app web sade ba estefade az Flask hast ke baraye namayesh tedad va andaze file-ha dar directory-haye moshakhas shode tarahi shode ast. In barname be soorat yek service web ejra mishavad va mitavanad etela'at mored nazar ra az tarigh API eraye dahad.
Features

    Gozarash andaze va tedad file-ha: Namayesh etela'at daghigh darbare tedad va andaze file-ha dar directory-haye moshakhas shode.
    Interface web sade: Interface kari sade baraye namayesh natayej dar browser web.
    Peshte bani az Docker: Barname be rahat'i ba estefade az Docker qabele ejra ast.

Installation

Baraye nasb va rah-andazi in project, marahil zire ra donbal konid:

    Clone kardan repository

    Aval, repository project ra be soorat lokali clone konid:

    bash

git clone http://192.168.200.54:8929/root/my-app-flask.git

Raftan be folder project

Be folder project boroid:

bash

cd my-app-flask

Nasb dependencies

Dependencies-haye morde niyaz ra nasb konid:

bash

pip install -r requirements.txt

Ejra kardan barname

Barname ra ba estefade az dastur zire ejra konid:

bash

    python dir-size-flask.py

    Barname be tore pishfarz dar port 8081 ejra mishavad va mitavanid ba moraje'e be http://localhost:8081 dar browser web khod natayej ra moshahade konid.

Usage

Baraye estefade az barname, kafi ast browser khod ra baz konid va be address zire boroid:

arduino

http://localhost:8081

Ba ersal darkhast-haye HTTP be in address, mitavanid etela'ati darbare tedad va andaze file-ha dar directory-haye moshakhas shode daryaft konid.
Tests

Baraye ejra test-ha, az tool pytest estefade konid. Dastur zire ra baraye ejra test-ha vared konid:

bash

pytest

Test-ha be shoma komak mikonand ta etemad hasil konid ke barname dorost kar mikonad va taghirat jadid sabab mishavad ke moshkelat jadid pida shavad.
Contributing

Agar temayel darid dar in project moshtarak shavid, lotfan marahil zire ra donbal konid:

    Fork kardan repository: Aval, repository ra fork konid ta yek copy az an dar hesab GitLab khod dashte bashid.

    Sakhtan yek branch jadid: Yek branch jadid baraye features ya taghirat jadid khod sakht konid:

    bash

    git checkout -b feature/new-feature

    Applying changes va ersal yek Pull Request: Taghirat khod ra apply konid va ba estefade az Pull Request an-ha ra be repository asli ersal konid.

License

In project tahte license MIT منتشر shode ast. Baraye joz'iyat bishtar darbare license, lotfan be file LICENSE moraje'e konid.

Ba tashakor az inke be project ma nigahe andakhtid! Agar soal ya pishnahadi darid, lotfan ba ma tamas begirid
