#!/bin/sh
echo "Resetting wifi"
ssh root@192.168.2.1 wifi
echo "restarting firewall"
ssh root@192.168.2.1 fw3 restart > /dev/null 2>&1
echo "Setting wmm iptables rules"
ssh root@192.168.2.1 iptables -t mangle -A POSTROUTING -p udp --sport 2113 -j TOS --set-tos 0x40/0xff
ssh root@192.168.2.1 iptables -t mangle -A POSTROUTING -p udp --sport 2114 -j TOS --set-tos 0xa0/0xff
ssh root@192.168.2.1 iptables -t mangle -A POSTROUTING -p udp --sport 2115 -j TOS --set-tos 0xe0/0xff
echo "Running Default"
sleep 2
python3 ~/domos-flent/run-flent -B ~/domos-flent/batchfile_flent_testbed  -b rrul_voip_down --batch-title default -v
echo "Prioritize Voice with wmm VO"
ssh root@192.168.2.1 iptables -t mangle -A POSTROUTING -p udp --sport 2116 -j TOS --set-tos 0xe0/0xff
echo "Running voice-VO"
sleep 1
python3 ~/domos-flent/run-flent -B ~/domos-flent/batchfile_flent_testbed  -b rrul_voip_down --batch-title voice-VO
echo "Move rrul to WMM BK"
ssh root@192.168.2.1 iptables -t mangle -A POSTROUTING -p tcp -j TOS --set-tos 0x40/0xff
echo "Running voice-VO-rrul-BK"
sleep 1
python3 ~/domos-flent/run-flent -B ~/domos-flent/batchfile_flent_testbed  -b rrul_voip_down --batch-title voice-VO-rrul-BK
echo "Set CWMin = 127"
ssh root@192.168.2.1 wlctl -i wl0 wme_ac ap bk ecwmin 7
echo "Running voice-VO-rrul-BK-cwmin-127"
sleep 1
python3 ~/domos-flent/run-flent -B ~/domos-flent/batchfile_flent_testbed  -b rrul_voip_down --batch-title voice-VO-rrul-BK-cwmin-127