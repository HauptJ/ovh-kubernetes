#!/bin/bash -eux

pushd /tmp

sudo dnf -y install python3 git ansible

#sudo python3 -m pip install pyyaml ansible

pushd /tmp/ansible

sudo ansible-playbook -i hosts vagrant.yml

popd

popd