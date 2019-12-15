#!/bin/bash -eux

pushd /tmp

sudo dnf -y install python3 git

sudo python3 -m pip install pyyaml ansible

pushd /tmp/ansible

sudo ansible-playbook -i hosts playbook.yml

popd

popd