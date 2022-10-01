#!/bin/bash

mkdir /publico
mkdir /adm
mkdir /ven
mkdir /sec

groupadd GRP_ADM
groupadd GRP_VEN
groupadd GRP_SEC

chown root:GRP_ADM /adm/
chown root:GRP_VEN /ven/
chown root:GRP_SEC /sec/

chmod 777 /publico/
chmod 770 /adm/
chmod 770 /ven/
chmod 770 /sec/

useradd carlos -m -s /bin/bash -p $(openssl passwd "Carlos123") -G GRP_ADM
passwd carlos -e
useradd maria -m -s /bin/bash -p $(openssl passwd "Maria123") -G GRP_ADM
passwd maria -e
useradd joao -m -s /bin/bash -p $(openssl passwd "Joao123") -G GRP_ADM
passwd joao -e

useradd debora -m -s /bin/bash -p $(openssl passwd "Debora123") -G GRP_VEN
passwd debora -e
useradd sebastiana -m -s /bin/bash -p $(openssl passwd "Sebastiana123") -G GRP_VEN
passwd sebastiana -e
useradd roberto -m -s /bin/bash -p $(openssl passwd "Roberto123") -G GRP_VEN
passwd roberto -e

useradd josefina -m -s /bin/bash -p $(openssl passwd "Josefina123") -G GRP_SEC
passwd josefina -e
useradd amanda -m -s /bin/bash -p $(openssl passwd "Amanda123") -G GRP_SEC
passwd amanda -e
useradd rogerio -m -s /bin/bash -p $(openssl passwd "Rogerio123") -G GRP_SEC
passwd rogerio -e